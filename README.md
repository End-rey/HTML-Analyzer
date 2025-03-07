# HTML Analyzer

HTML Analyzer is a command-line tool designed to analyze and optimize HTML files. It provides various functionalities such as syntax checking, validation against standards, optimization, accessibility checks, and SEO analysis.

## Features

- **Syntax Checking**: Check the HTML syntax for errors.
- **Validation**: Validate HTML against W3C standards.
- **Optimization**: Optimize HTML by minifying and formatting.
- **Accessibility**: Check HTML for accessibility issues.
- **SEO Analysis**: Analyze HTML for SEO improvements.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/End-rey/HTML-Analyzer.git
   cd html-analyzer
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the HTML Analyzer with the desired options:

```sh
python main.py <file> [options]
```

### Options

- `--syntax`: Check HTML syntax.
- `--validate`: Validate HTML against standards.
- `--optimize`: Optimize HTML.
- `--optimize-output <file>`: Save optimized HTML to a file.
- `--accessibility`: Check accessibility.
- `--seo`: Perform SEO analysis.
- `--output <file>`: Save results to a JSON file.

### Example

```sh
python main.py example.html --syntax --validate --optimize --accessibility --seo --output results.json
```

## Project Structure

- `main.py`: The main script to run the HTML Analyzer.
- `analyzer/`: Directory containing the analysis modules.
  - `syntax_checker.py`: Module for syntax checking.
  - `validator.py`: Module for HTML validation.
  - `optimizer.py`: Module for HTML optimization.
  - `accessibility.py`: Module for accessibility checks.
  - `seo_analyzer.py`: Module for SEO analysis.
