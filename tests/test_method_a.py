from dataclasses import asdict

import pytest


@pytest.fixture
def document():
    from package.someclass import SomeClass
    class_instance = SomeClass()
    return class_instance


def test_method_a_one(document):
    result = asdict(document.method_a("a")[0])
    assert result["string"] == "a"


def test_method_a_two(document):
    result = asdict(document.method_a("b")[0])
    assert result["string"] == "b"
