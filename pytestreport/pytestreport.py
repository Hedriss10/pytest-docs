import sys
from datetime import datetime

def add_emojis_to_report(test_results):
    emoji_map = {
        "PASSED": "✅",
        "FAILED": "❌",
    }

    passed_tests = []
    failed_tests = []

    # Processamento dos resultados de teste
    for result in test_results.split(" | "):
        name, status = result.split(" - ")
        if status == "PASSED":
            passed_tests.append(name)
        elif status == "FAILED":
            failed_tests.append(name)

    # Construção do relatório
    report_title = "## Test Report - `platform-bs-users`\n"
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

    report_summary = (
        f"{report_results}\n"
        f"{report_passed_tests}\n"
        f"{report_failed_tests}\n"
        "--------------------------------------------------\n"
        "### :bar_chart: Test Summary\n\n"
        f"- **Passed Tests**: {len(passed_tests)} ✅\n"
        f"- **Failed Tests**: {len(failed_tests)} ❌\n"
    )

    footer = f"\n---\n_Report styled with ❤️ for `platform-bs-users` on {datetime.now().strftime('%d-%b-%Y at %H:%M:%S')}_\n"

    final_report = report_title + report_summary + footer

    # Salvando o relatório gerado
    with open("report.md", "w") as file:
        file.write(final_report)

if __name__ == "__main__":
    # Recebe os resultados passados por subprocess
    test_results = sys.argv[1]
    add_emojis_to_report(test_results)
