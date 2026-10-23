from document_processor.pdf_reader import extract_text_from_pdf
from document_processor.text_cleaner import clean_extracted_text

def main():
    pdf_path = "documents/sample.pdf"

    try:
        text = extract_text_from_pdf(pdf_path)
        text = clean_extracted_text(text)
        print("PDF text extracted successfully!\n")
        print(text[:2000])

        if len(text) > 2000:
            print("\n... Output truncated ...")

        print(f"\nTotal extracted characters: {len(text)}")

    except (FileNotFoundError, ValueError) as error:
        print(f"Could not process PDF: {error}")


if __name__ == "__main__":
    main()
