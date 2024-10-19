from mylib import load_student, load_transaction, query


def test_load_student():
    t = load_student()
    assert t == "success"


def test_load_transaction():
    t = load_transaction()
    assert t == "success"


def test_query():
    t = query()
    assert t == "success"


if __name__ == "__main__":
    test_load_student()
    test_load_transaction()
    test_query()
