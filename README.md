# HTML Analyzer

HTML Analyzer is a command-line tool designed to analyze, optimize and parse HTML files. It provides various functionalities such as syntax checking, validation against standards, optimization, accessibility checks, SEO analysis, and text extraction from different file formats.

## Features

- **Syntax Checking**: Check the HTML syntax for errors.
- **Validation**: Validate HTML against W3C standards.
- **Optimization**: Optimize HTML by minifying and formatting.
- **Accessibility**: Check HTML for accessibility issues.
- **SEO Analysis**: Analyze HTML for SEO improvements.
- **Text Parsing**: Extract text content from various file formats.

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

3. Install djvulibre (required for DJVU file parsing, do not needed, if you don't need to parse DJVU):

   **Linux (Debian/Ubuntu)**:
   ```sh
   sudo apt-get install djvulibre-bin
   ```

   **macOS**:
   ```sh
   brew install djvulibre
   ```

   **Windows**:
   - Download DjVuLibre installer from [DjVuLibre Downloads](https://djvu.sourceforge.net/download.html)
   - Run the installer and follow the installation wizard
   - Add the installation directory to your system's PATH environment variable

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
- `--parse`: Extract text content from the file and save it as .txt.

### Supported File Formats for Parsing

The `--parse` option supports the following file formats:
- HTML (.html)
- PDF (.pdf)
- Word Documents (.doc, .docx)
- DJVU (.djvu)

## Tests

Run tests

```sh
pytest
```

Run tests with additional information

```sh
pytest -v
```

Save test results to file (`ctrl + alt + l` for Win or `command + option + l` for Mac to format file)

```sh
pytest --junitxml=report.xml
```

### Example Commands

Analysis of HTML:
```sh
python main.py example.html --syntax --validate --optimize --accessibility --seo --output results.json
```

Text extraction:
```sh
python main.py document.pdf --parse
python main.py document.docx --parse
python main.py document.djvu --parse
```

## Project Structure

- `main.py`: The main script to run the HTML Analyzer.
- `analyzer/`: Directory containing the analysis modules.
  - `syntax_checker.py`: Module for syntax checking.
  - `validator.py`: Module for HTML validation.
  - `optimizer.py`: Module for HTML optimization.
  - `accessibility.py`: Module for accessibility checks.
  - `seo_analyzer.py`: Module for SEO analysis.
- `parser/`: Directory containing parsing modules.
  - `html.py`: Module for HTML text extraction.
  - `pdf.py`: Module for PDF text extraction.
  - `doc.py`: Module for Word documents text extraction.
  - `djvu.py`: Module for DJVU text extraction.
