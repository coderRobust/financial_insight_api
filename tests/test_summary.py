from unittest.mock import patch
from app.genai import summarizer


@patch("app.genai.summarizer.generate_summary", return_value="Mocked summary for testing.")
def test_generate_summary(mock_summary):
    result = summarizer.generate_summary()
    assert isinstance(result, str)
    assert "Mocked" in result
