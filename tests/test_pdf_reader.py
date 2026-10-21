
from types import SimpleNamespace

import pytest

from document_processor import pdf_reader


def make_page(text):
    return SimpleNamespace(extract_text=lambda: text)


def test_extract_text_from_pdf_successfully(tmp_path, monkeypatch):
    pdf_file = tmp_path / "sample.pdf"
    pdf_file.touch()

    pages = [
        make_page("  First page content  "),
        make_page("   "),
        make_page("Second page content"),
    ]

    monkeypatch.setattr(
        pdf_reader,
        "PdfReader",
        lambda path: SimpleNamespace(pages=pages),
    )

    result = pdf_reader.extract_text_from_pdf(str(pdf_file))

    assert "--- Page 1 ---" in result
    assert "First page content" in result
    assert "--- Page 3 ---" in result
    assert "Second page content" in result
    assert "--- Page 2 ---" not in result


def test_missing_pdf_raises_file_not_found_error(tmp_path):
    missing_file = tmp_path / "missing.pdf"

    with pytest.raises(FileNotFoundError, match="PDF file not found"):
        pdf_reader.extract_text_from_pdf(str(missing_file))


def test_non_pdf_file_raises_value_error(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("Sample text", encoding="utf-8")

    with pytest.raises(ValueError, match="must have a .pdf extension"):
        pdf_reader.extract_text_from_pdf(str(text_file))


def test_pdf_without_extractable_text_raises_value_error(
    tmp_path, monkeypatch
):
    pdf_file = tmp_path / "empty.pdf"
    pdf_file.touch()

    monkeypatch.setattr(
        pdf_reader,
        "PdfReader",
        lambda path: SimpleNamespace(
            pages=[make_page(""), make_page("   ")]
        ),
    )

    with pytest.raises(ValueError, match="No extractable text was found"):
        pdf_reader.extract_text_from_pdf(str(pdf_file))
