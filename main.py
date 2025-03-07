import argparse
import json
from analyzer.syntax_checker import check_syntax
from analyzer.validator import validate_html
from analyzer.optimizer import optimize_html
from analyzer.accessibility import check_accessibility
from analyzer.seo_analyzer import analyze_seo


def main():
    parser = argparse.ArgumentParser(description="HTML Analyzer CLI")
    parser.add_argument("file", type=str, help="Path to the HTML file to analyze")
    parser.add_argument("--syntax", action="store_true", help="Check HTML syntax")
    parser.add_argument(
        "--validate", action="store_true", help="Validate HTML against standards"
    )
    parser.add_argument("--optimize", action="store_true", help="Optimize HTML")
    parser.add_argument(
        "--optimize-output", type=str, help="Save optimized HTML to a file"
    )
    parser.add_argument(
        "--accessibility", action="store_true", help="Check accessibility"
    )
    parser.add_argument("--seo", action="store_true", help="Perform SEO analysis")
    parser.add_argument("--output", type=str, help="Save results to a JSON file")

    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        html_content = f.read()

    results = {}

    if args.syntax:
        results["syntax"] = check_syntax(html_content)
    if args.validate:
        results["validation"] = validate_html(html_content)
    if args.optimize:
        optimization_result = optimize_html(html_content)
        results["optimization"] = optimization_result

        if args.optimize_output:
            with open(args.optimize_output, "w", encoding="utf-8") as f:
                f.write(optimization_result["optimized_html"])
            print(f"Optimized HTML saved to {args.optimize_output}")

    if args.accessibility:
        results["accessibility"] = check_accessibility(html_content)
    if args.seo:
        results["seo"] = analyze_seo(html_content)

    json_results = json.dumps(results, indent=4, ensure_ascii=False)

    print(json_results)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_results)
        print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
