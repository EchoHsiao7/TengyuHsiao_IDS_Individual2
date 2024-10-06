import sqlite3
import pytest
from main import create_table, insert_student, update_age, delete_user, query1, query2

@pytest.fixture
def connection():
    conn = sqlite3.connect(':memory:')
    create_table(conn)  
    yield conn
    conn.close()

def test_create_table(connection):
    cursor = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student';")
    table = cursor.fetchone()
    assert table is not None 

def test_insert_student(connection):
    insert_student(connection, 'Echo', 24)
    students = query1(connection)
    assert len(students) == 1
    assert students[0][1] == 'Echo'
    assert students[0][2] == 24

def test_update_age(connection):
    insert_student(connection, 'Echo', 24)
    students = query1(connection)
    student_id = students[0][0]
    update_age(connection, student_id, 25)
    updated_students = query1(connection)
    assert updated_students[0][2] == 25  

def test_delete_user(connection):
    insert_student(connection, 'Echo', 22)
    students = query1(connection)
    student_id = students[0][0]
    delete_user(connection, student_id)
    students_after_delete = query1(connection)
    assert len(students_after_delete) == 0  

def test_query1(connection):
    insert_student(connection, 'Echo', 24)
    insert_student(connection, 'Hsiao', 25)
    students = query1(connection)
    assert len(students) == 2  

def test_query2(connection):
    insert_student(connection, 'Echo', 24)
    insert_student(connection, 'Hsiao', 25)
    result = query2(connection,25)
    assert len(result) == 1
    assert result[0][1] == 'Hsiao'  # Only Bob should be returned
