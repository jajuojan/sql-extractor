import os


def get_test_data(filename) -> str:
    """
    Returns the data from a test data file.
    """
    fn = os.path.join("tests", "test_data", filename)
    return open(fn, "r").read()
