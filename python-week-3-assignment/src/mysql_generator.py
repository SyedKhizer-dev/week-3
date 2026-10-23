import configparser
import logging
import os
from collections.abc import Iterator
from getpass import getpass
from pathlib import Path
from typing import Any

import mysql.connector
from mysql.connector import Error

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def load_config() -> configparser.ConfigParser:
    """Load database settings from config/config.ini."""
    config_path = Path(__file__).resolve().parent.parent / "config" / "config.ini"
    config = configparser.ConfigParser()

    if not config.read(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    if not config.has_section("mysql"):
        raise ValueError("Missing [mysql] section in configuration.")

    return config


def fetch_employees(batch_size: int = 500) -> Iterator[tuple[Any, ...]]:
    """Yield employee rows incrementally from MySQL."""
    if batch_size < 1:
        raise ValueError("batch_size must be greater than zero.")

    config = load_config()
    password = os.environ.get("MYSQL_PASSWORD")

    if password is None:
        password = getpass("MySQL password: ")

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=config["mysql"]["host"],
            database=config["mysql"]["database"],
            user=config["mysql"]["user"],
            password=password,
        )

        cursor = connection.cursor(buffered=False)
        cursor.execute("SELECT emp_no, first_name, last_name FROM employees")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break

            yield from rows

    except Error:
        logger.exception("Failed to fetch employee records from MySQL.")
        raise
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    try:
        count = 0
        for employee in fetch_employees():
            print(employee)
            count += 1

        logger.info("Processed %d employee records.", count)
    except (Error, FileNotFoundError, ValueError) as exc:
        logger.error("Employee processing failed: %s", exc)
