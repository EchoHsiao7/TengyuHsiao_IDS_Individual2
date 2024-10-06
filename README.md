[![Python CI](https://github.com/EchoHsiao7/TengyuHsiao_IDS_Project5/actions/workflows/cicd.yml/badge.svg)](https://github.com/EchoHsiao7/TengyuHsiao_IDS_Project5/actions/workflows/cicd.yml)
# TengyuHsiao_IDS_project5
# CRUD Operations for Student Database

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations on a simple SQLite database containing student information. The database operations include the ability to add, update, delete, and query students in a SQLite database.

## Features

- Connect to an SQLite database
- Create a `student` table contains s_id, name, age if it doesn't exist
- Insert new student records
- Update existing student records
- Delete student records
- Query student records with two different queries:
  - Fetch all students
  - Fetch students equal specified age


## Example log for CRUD
- Inital Table: Empty

- insert_student(connection, "Echo", 24): (1, 'Echo', 24)

- query1(connection): (1, 'Echo', 24)

- update_age(connection, 1, 25): (1, 'Echo', 25)

- delete_user(connection, 1): Empty


## Test

In test_main.py, I perform several tests to make sure my CRUD as well as the 2 extra queries works for my database, the following is a screenshot of the successful tests 
![alt text](image.png)