import sqlite3 as sql
from django.conf import settings


def resolve_table_name(customer_id: str) -> str:
    return f'customer_{customer_id}'


def get_db_connection():
    return sql.connect(settings.DB_FILE)
