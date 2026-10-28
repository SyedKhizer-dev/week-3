import configparser
import os
from unittest.mock import MagicMock, patch

from src.mysql_generator import fetch_employees


@patch("src.mysql_generator.mysql.connector.connect")
@patch("src.mysql_generator.load_config")
def test_fetch_employees_yields_rows(mock_load_config, mock_connect):
    config = configparser.ConfigParser()
    config.read_dict(
        {
            "mysql": {
                "host": "localhost",
                "port": "3306",
                "database": "employees",
                "user": "root",
            }
        }
    )
    mock_load_config.return_value = config

    mock_cursor = MagicMock()
    mock_cursor.fetchmany.side_effect = [
        [(1, "Alice", "Smith"), (2, "Bob", "Jones")],
        [],
    ]

    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_connection

    with patch.dict(os.environ, {"MYSQL_PASSWORD": "test-password"}):
        result = list(fetch_employees(batch_size=2))

    assert result == [
        (1, "Alice", "Smith"),
        (2, "Bob", "Jones"),
    ]

    mock_connect.assert_called_once_with(
        host="localhost",
        port=3306,
        database="employees",
        user="root",
        password="test-password",
    )

    mock_cursor.execute.assert_called_once_with(
        "SELECT emp_no, first_name, last_name FROM employees"
    )
    assert mock_cursor.fetchmany.call_count == 2
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()
