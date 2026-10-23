from unittest.mock import MagicMock, patch

from src.mysql_generator import fetch_employees


@patch("src.mysql_generator.mysql.connector.connect")
@patch("src.mysql_generator.load_config")
def test_fetch_employees_yields_rows(mock_load_config, mock_connect):
    mock_load_config.return_value = {
        "mysql": {
            "host": "localhost",
            "database": "employees",
            "user": "root",
        }
    }

    mock_cursor = MagicMock()
    mock_cursor.fetchmany.side_effect = [
        [(1, "Alice", "Smith"), (2, "Bob", "Jones")],
        [],
    ]

    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_connection

    with patch("src.mysql_generator.getpass", return_value="test-password"):
        result = list(fetch_employees(batch_size=2))

    assert result == [
        (1, "Alice", "Smith"),
        (2, "Bob", "Jones"),
    ]
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()
