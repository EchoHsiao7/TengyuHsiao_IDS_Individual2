import pytest
from main import add


def test_add():
    """Test the add function"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


if __name__ == "__main__":
    pytest.main()
