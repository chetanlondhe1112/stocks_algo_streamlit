from functions.db_conn import sqlalchemy_connect
import os

sql=sqlalchemy_connect(username="chetan")
#print(sql)
tables_dict=sql.read_tables()
candle_tbl=sql.candle_stic_table
print(candle_tbl)
"""
db_tables=tables_dict["db_tables"]

customer_tbl=db_tables["customer_table"]
candle_stick_tbl=db_tables["candle_stick_log_table"]
entry_conditions=db_tables["entry_conditions"]



candle_data=sql.fetch_tables(candle_stick_tbl)
candle_data.index=candle_data["date"]
print(candle_data)
"""