import pandas as pd

from thena import celery_app
from .utills import resolve_table_name, get_db_connection


@celery_app.task
def persist_data(customer_id: int, uploaded_file_name: str) -> None:
    events = pd.read_csv(uploaded_file_name)
    connection = get_db_connection()
    table_name = resolve_table_name(customer_id)
    events.to_sql(table_name, connection, if_exists='append')
