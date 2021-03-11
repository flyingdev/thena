import os
import sqlite3 as sql
import pandas as pd
from django.conf import settings

from thena import celery_app
from .utills import resolve_table_name


def _get_connection():
    db_file_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    return sql.connect(db_file_path)


@celery_app.task
def persist_data(customer_id: int, uploaded_file_name: str) -> None:
    # TODO
    #    create table if not exist
    #    append data to that table
    #    check whether django connection works instead of sqlite3 directly
    #    refactor to use cursor instead of connection
    print('--------------')
    print(uploaded_file_name)
    events = pd.read_csv(uploaded_file_name)
    connection = _get_connection()
    table_name = resolve_table_name(customer_id)
    events.to_sql(table_name, connection, if_exists='append')
