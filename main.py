import argparse
import json
from analyzer.syntax_checker import check_syntax
from analyzer.validator import validate_html
from analyzer.optimizer import optimize_html
from analyzer.accessibility import check_accessibility
from analyzer.seo_analyzer import analyze_seo
from parser.html import parse as parse_html
from parser.doc import parse as parse_doc
from parser.pdf import parse as parse_pdf
from parser.djvu import parse as parse_djvu


def main() -> None:
    """
    HTML Analyzer CLI entry point.

    Parses command line arguments and calls the respective functions to
    perform analysis, validation, optimization, accessibility checking,
    and SEO analysis on the given HTML file.

    Saves the results to a JSON file if the --output option is given.
    """

    parser = argparse.ArgumentParser(description="HTML Analyzer CLI")
    parser.add_argument(
        "file", type=str, help="Path to the HTML|DOC|DOCX|PDF|DJVU file to analyze or parse"
    )
    parser.add_argument(
        "--syntax", action="store_true",
                        help="Check HTML syntax"
    )
    parser.add_argument(
        "--validate", action="store_true", help="Validate HTML against standards"
    )
    parser.add_argument("--optimize", action="store_true",
                        help="Optimize HTML")
    parser.add_argument(
        "--optimize-output",
        type=str,
        help="Save optimized HTML to a file (requires --optimize)"
    )
    parser.add_argument(
        "--accessibility", action="store_true", help="Check accessibility"
    )
    parser.add_argument("--seo", action="store_true",
                        help="Perform SEO analysis")
    parser.add_argument(
        "--output", type=str,
                        help="Save results to a JSON file"
    )

    parser.add_argument("--parse", action="store_true",
                        help="Parse HTML|DOC|DOCX|PDF|DJVU and save as text")

    args = parser.parse_args()
    file: str = args.file

    if file.lower().endswith('.html'):
        process_analyzer(args)

    if args.parse:
        try:
            process_parse(file)
        except FileNotFoundError as e:
            print("File not found.")
        except PermissionError:
            print("Permission denied: Unable to access the file.")
        except UnicodeDecodeError:
            print("Unable to read the file: Invalid encoding.")
        except IOError as e:
            print(f"I/O error occurred: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def process_parse(file):
    text_filename = file.rsplit('.', 1)[0] + '.txt'

    if file.lower().endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        with open(text_filename, 'w', encoding='utf-8') as f:
            f.write(parse_html(html_content))

    elif file.lower().endswith(('.doc', '.docx')):
        print("Processing Word document...")
        with open(text_filename, 'w', encoding='utf-8') as f:
            f.write(parse_doc(file))

    elif file.lower().endswith('.pdf'):
        print("Processing PDF file...")
        with open(text_filename, 'w', encoding='utf-8') as f:
            f.write(parse_pdf(file))

    elif file.lower().endswith('.djvu'):
        print("Processing DJVU file...")
        parse_djvu(file, text_filename)
    else:
        raise ValueError(f"Unsupported file type: {file}")

    print(f"Parsed text saved to {text_filename}")


def process_analyzer(args: argparse.Namespace) -> None:

    with open(args.file, "r", encoding="utf-8") as f:
        html_content: str = f.read()

    results: dict[str, dict] = {}

    if args.syntax:
        results["syntax"] = check_syntax(html_content)
    if args.validate:
        results["validation"] = validate_html(html_content)
    if args.optimize:
        optimization_result: dict[str, str] = optimize_html(html_content)
        results["optimization"] = optimization_result

        if args.optimize_output:
            with open(args.optimize_output, "w", encoding="utf-8") as f:
                f.write(optimization_result["optimized_html"])
            print(f"Optimized HTML saved to {args.optimize_output}")

    if args.accessibility:
        results["accessibility"] = check_accessibility(html_content)
    if args.seo:
        results["seo"] = analyze_seo(html_content)

    json_results: str = json.dumps(results, indent=4, ensure_ascii=False)

    print(json_results)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_results)
        print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
