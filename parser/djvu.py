import subprocess


def parse(djvu_path: str, output_file: str) -> None:
    """Extracts text from a DJVU file and saves it to a text file.

    This function uses the 'djvutxt' command-line tool to extract text content
    from a DJVU document and save it to a specified output file.

    Args:
        djvu_path (str): Path to the source DJVU file
        output_file (str): Path where the extracted text will be saved

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: If the djvutxt command fails to execute

    Example:
        >>> parse("document.djvu", "output.txt")
        Text has been extracted and saved to: output.txt
    """
    subprocess.run(['djvutxt', djvu_path, output_file], check=True)
    print(f"Text has been extracted and saved to: {output_file}")
