from pathlib import Path
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    # Extract text from a text-based PDF file.
    path = Path(pdf_path)

    if not path.is_file():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The supplied file must have a .pdf extension.")

    reader = PdfReader(str(path))
    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""

        if page_text.strip():
            extracted_pages.append(
                f"--- Page {page_number} ---\n{page_text.strip()}"
            )

    if not extracted_pages:
        raise ValueError(
            "No extractable text was found. "
            "The PDF may be scanned or contain no readable text."
        )

    return "\n\n".join(extracted_pages)
