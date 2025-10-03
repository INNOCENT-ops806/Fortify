import sys  # noqa: F401
import os  # noqa: F401
from src import password_generator
from src.main import get_unique_filename


def test_get_unique_filename(tmp_path):
    # Create a file named output.txt
    file1 = tmp_path / "output.txt"
    file1.write_text("test")
    # Should return output1.txt
    filename = get_unique_filename(str(file1))
    assert filename.endswith("output1.txt")

