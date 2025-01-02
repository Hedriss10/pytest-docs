from datetime import datetime

import sys
from datetime import datetime

def generate_report_pytest(prefix, test_results, coverage_report):
    emoji_map = {
        "PASSED": "✅",
        "FAILED": "❌",
    }

    passed_tests = []
    failed_tests = []
    coverage_data = ""

    with open(coverage_report, "r") as f:
        coverage_data = f.read()

    for result in test_results.split(" | "):
        name, status = result.split(" - ")
        if status == "PASSED":
            passed_tests.append(name)
        elif status == "FAILED":
            failed_tests.append(name)

    report_title = f"## Test Report - `{prefix}`\n"
    report_results = (
        "--------------------------------------------------\n"
        "### :memo: Test results\n\n"
        f"**Total Tests**: {len(passed_tests) + len(failed_tests)}\n"
        f"**Passed**: {len(passed_tests)}\n"
        f"**Failed**: {len(failed_tests)}\n\n"
        "### Passed Tests ✅\n"
    )

    report_passed_tests = "\n".join([f"- {test}" for test in passed_tests])
    report_failed_tests = "\n### Failed Tests ❌\n" + "\n".join([f"- {test}" for test in failed_tests])

    report_coverage = "\n### :bar_chart: Coverage\n\n"
    report_coverage += coverage_data

    report_summary = (
        f"{report_results}\n"
        f"{report_passed_tests}\n"
        f"{report_failed_tests}\n"
        f"{report_coverage}\n"
        "--------------------------------------------------\n"
        "### :bar_chart: Test Summary\n\n"
        f"- **Passed Tests**: {len(passed_tests)} ✅\n"
        f"- **Failed Tests**: {len(failed_tests)} ❌\n"
    )

    footer = f"\n---\n_Report styled with ❤️ for `{prefix}` on {datetime.now().strftime('%d-%b-%Y at %H:%M:%S')}_\n"

    final_report = report_title + report_summary + footer

    with open("report.md", "w") as file:
        file.write(final_report)

if __name__ == "__main__":
    test_results = sys.argv[1]
    generate_report_pytest(test_results, "coverage_report.txt")

