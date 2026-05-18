"""
validate_report.py — Post-generation validation for PRISM finalizer output

Detects truncation, missing sections, and missing v5 design system classes.
Returns structured result for the report-finalizer skill's Step 4.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

V5_REQUIRED_CLASSES = {
    "metric-card",
    "fact-badge",
    "est-badge",
    "out-badge",
}

V5_OPTIONAL_CLASSES = {
    "synergy-block",
    "bottleneck-block",
    "principle-block",
}

TRUNCATION_SIGNALS = [
    # Trailing partial words / cut sentences
    re.compile(r"[가-힣a-zA-Z]\s*$"),
    # Open block-level tags without close at end
    re.compile(r"<(div|section|table|p)[^>]*>(?:(?!</\1>).)*$", re.DOTALL),
]


@dataclass
class ValidationResult:
    passed: bool
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    v5_classes_present: list[str] = field(default_factory=list)
    missing_sections: list[str] = field(default_factory=list)
    truncation_detected: bool = False


def check_unbalanced_tags(html: str) -> list[str]:
    """Find tags that are opened but not closed."""
    issues = []
    for tag in ("div", "section", "table", "tr", "td", "p", "ul", "ol", "li"):
        opens = len(re.findall(rf"<{tag}[\s>]", html))
        closes = len(re.findall(rf"</{tag}>", html))
        if opens != closes:
            issues.append(f"<{tag}>: {opens} open, {closes} close (diff: {opens - closes})")
    return issues


def check_v5_classes(html: str) -> tuple[list[str], list[str]]:
    """Returns (present, missing_required)."""
    present = []
    for cls in V5_REQUIRED_CLASSES | V5_OPTIONAL_CLASSES:
        if re.search(rf'class="[^"]*\b{re.escape(cls)}\b[^"]*"', html):
            present.append(cls)
    missing_required = list(V5_REQUIRED_CLASSES - set(present))
    return present, missing_required


def check_truncation(html: str) -> bool:
    """Heuristic truncation detection."""
    stripped = html.rstrip()
    # Healthy report ends with closing tag
    if stripped.endswith(("</div>", "</section>", "</body>", "</html>")):
        return False
    # Trailing partial sentence
    last_500 = stripped[-500:]
    if re.search(r"[가-힣a-zA-Z],\s*$", last_500):
        return True
    if re.search(r"\b(and|or|the|the|및|또는|그리고)\s*$", last_500, re.IGNORECASE):
        return True
    # No closing tag at all in last 200 chars
    if "</" not in stripped[-200:]:
        return True
    return False


def check_sections_present(html: str, planned_section_ids: list[str]) -> list[str]:
    """Returns IDs of planned sections that are missing from output."""
    missing = []
    for sid in planned_section_ids:
        if not re.search(rf'id="{re.escape(sid)}"', html):
            missing.append(sid)
    return missing


def validate_report(
    html: str,
    planned_section_ids: list[str] | None = None,
) -> ValidationResult:
    """Run all checks. Returns a ValidationResult."""
    result = ValidationResult(passed=True)

    # 1. Tag balance
    tag_issues = check_unbalanced_tags(html)
    if tag_issues:
        result.issues.extend([f"Unbalanced tag: {i}" for i in tag_issues])
        result.passed = False

    # 2. V5 classes
    present, missing_required = check_v5_classes(html)
    result.v5_classes_present = present
    if missing_required:
        result.warnings.append(
            f"Missing required v5 classes: {', '.join(missing_required)}. "
            "Report may lack visual hierarchy."
        )

    # 3. Truncation
    if check_truncation(html):
        result.truncation_detected = True
        result.issues.append("Truncation signals detected at end of report")
        result.passed = False

    # 4. Section coverage
    if planned_section_ids:
        missing = check_sections_present(html, planned_section_ids)
        result.missing_sections = missing
        if missing:
            result.issues.append(f"Missing planned sections: {', '.join(missing)}")
            result.passed = False

    return result


def format_validation_report(result: ValidationResult) -> str:
    """Human-readable summary for logging."""
    lines = [
        "=" * 60,
        f"VALIDATION: {'PASSED' if result.passed else 'FAILED'}",
        "=" * 60,
    ]
    if result.issues:
        lines.append("\nIssues:")
        lines.extend(f"  ✕ {i}" for i in result.issues)
    if result.warnings:
        lines.append("\nWarnings:")
        lines.extend(f"  ⚠ {w}" for w in result.warnings)
    if result.v5_classes_present:
        lines.append(f"\nV5 classes used: {', '.join(result.v5_classes_present)}")
    if result.missing_sections:
        lines.append(f"\nMissing sections: {', '.join(result.missing_sections)}")
    if result.truncation_detected:
        lines.append("\n⚠ TRUNCATION SUSPECTED — recommend retry with higher max_tokens")
    return "\n".join(lines)


if __name__ == "__main__":
    # Smoke test
    good_html = '''
    <div id="sec-1" class="metric-card">
      <span class="fact-badge">FACT</span>
      <span class="est-badge">EST</span>
      <span class="out-badge">OUT</span>
    </div>
    '''
    truncated_html = '<div class="metric-card">The result is approximately,'
    print(format_validation_report(validate_report(good_html, ["sec-1"])))
    print()
    print(format_validation_report(validate_report(truncated_html, ["sec-1", "sec-2"])))
