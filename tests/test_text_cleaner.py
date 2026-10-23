from document_processor.text_cleaner import clean_extracted_text


def test_removes_trailing_whitespace():
    text = "Question 1   \nOption A\t\nOption B"

    result = clean_extracted_text(text)

    assert result == "Question 1\nOption A\nOption B"


def test_collapses_excessive_blank_lines():
    text = "Page 1\n\n\n\nQuestion 1"

    result = clean_extracted_text(text)

    assert result == "Page 1\n\nQuestion 1"


def test_preserves_question_structure():
    text = (
        "--- Page 1 ---\n"
        "1) What is Yoga?\n"
        "a) Option A\n"
        "b) Option B"
    )

    result = clean_extracted_text(text)

    assert "1) What is Yoga?" in result
    assert "a) Option A" in result
    assert "b) Option B" in result
    assert "--- Page 1 ---" in result


def test_empty_or_whitespace_input_returns_empty_string():
    assert clean_extracted_text("") == ""
    assert clean_extracted_text("   \n  ") == ""
