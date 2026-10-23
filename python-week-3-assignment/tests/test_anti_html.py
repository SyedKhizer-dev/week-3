from unittest.mock import Mock, patch

import pytest
import requests

from src.anti_html import remove_html_tags


@patch("src.anti_html.requests.get")
def test_remove_html_tags(mock_get):
    mock_response = Mock()
    mock_response.text = """
        <html>
            <body>
                <h1>Hello World</h1>
                <p>This is a test.</p>
            </body>
        </html>
    """
    mock_get.return_value = mock_response

    result = remove_html_tags("https://example.com")

    assert result == "Hello World This is a test."
    mock_get.assert_called_once_with("https://example.com", timeout=10)
    mock_response.raise_for_status.assert_called_once()


@patch("src.anti_html.requests.get")
def test_remove_html_tags_raises_on_http_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        remove_html_tags("https://example.com")
