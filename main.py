"""
This module contains CRUD database operations.
"""

import sqlite3


def connect_db(db_file=".db"):
    connection = sqlite3.connect(db_file)
    return connection


def create_table(connection):
    sql = """
    CREATE TABLE IF NOT EXISTS student (
        s_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    """
    connection.execute(sql)
    connection.commit()


def insert_student(connection, name, age):
    sql = "INSERT INTO student (name, age) VALUES (?, ?);"
    connection.execute(sql, (name, age))
    connection.commit()


def update_age(connection, s_id, age):
    sql = "UPDATE student SET age = ? WHERE s_id = ?;"
    connection.execute(sql, (age, s_id))
    connection.commit()


def delete_user(connection, s_id):
    sql = "DELETE FROM student WHERE s_id = ?;"
    connection.execute(sql, (s_id,))
    connection.commit()


def query1(connection):
    sql = "SELECT * FROM student;"
    cursor = connection.execute(sql)
    return cursor.fetchall()


def query2(connection, age):
    sql = "SELECT * FROM student where age = ?;"
    cursor = connection.execute(sql, (age,))
    return cursor.fetchall()


if __name__ == "__main__":
    conn = connect_db()
