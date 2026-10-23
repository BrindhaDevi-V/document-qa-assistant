import re


def clean_extracted_text(text: str) -> str:
    # Clean unnecessary whitespace without changing document wording.
    if not text or not text.strip():
        return ""

    # Normalize Windows and old-style line endings.
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing spaces and tabs from each line.
    text = re.sub(r"[ \t]+\n", "\n", text)

    # Collapse three or more consecutive newlines to two.
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
