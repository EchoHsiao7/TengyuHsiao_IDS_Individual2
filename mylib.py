"""
This module contains CRUD database operations.
"""

import csv
import os
from databricks import sql
from dotenv import load_dotenv


def load_student(dataset="data/student.csv"):
    payload = csv.reader(open(dataset, newline="", encoding="utf-8"), delimiter=",")
    next(payload)
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(
                """
                           CREATE TABLE IF NOT EXISTS echo_student (id INT, first_name STRING, 
                           last_name STRING, age INT , balance INT)
                           """
            )
            cursor.execute(
                """
                           SELECT * FROM echo_student
                           """
            )
            result = cursor.fetchall()
            if not result:
                stringsql = "INSERT INTO echo_student VALUES"
                for i in payload:
                    stringsql += "\n" + str(tuple(i)) + ","
                stringsql = stringsql[:-1] + ";"
                cursor.execute(stringsql)
            cursor.close()
            connection.close()
    return "success"


def load_transaction(dataset="data/transaction.csv"):
    payload = csv.reader(open(dataset, newline="", encoding="utf-8"), delimiter=",")
    next(payload)
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(
                """
                           CREATE TABLE IF NOT EXISTS  echo_transactions 
                           (transaction_id INT,student_id INT,amount DECIMAL(10, 2),transaction_type STRING,
                            transaction_date DATE);
                           """
            )

            cursor.execute(
                """
                           SELECT * FROM echo_transactions 
                           """
            )
            result = cursor.fetchall()
            if not result:
                stringsql = "INSERT INTO echo_transactions VALUES"
                for i in payload:
                    stringsql += "\n" + str(tuple(i)) + ","
                stringsql = stringsql[:-1] + ";"
                cursor.execute(stringsql)
            cursor.close()
            connection.close()
    return "success"


def query():
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                           SELECT s.id, s.first_name, s.last_name, COUNT(t.transaction_id) AS total_transactions,
                           SUM(CASE WHEN t.transaction_type = 'deposit' THEN t.amount ELSE 0 END) AS total_deposited
                           FROM echo_student s
                           LEFT JOIN 
                           echo_transactions t ON s.id = t.student_id
                           GROUP BY 
                           s.id, s.first_name, s.last_name
                           ORDER BY 
                           total_deposited DESC;
                           """
            )
            result = cursor.fetchall()
            for i in result:
                print(i)
    return "success"


if __name__ == "__main__":
    load_student()
    load_transaction()
    query()
