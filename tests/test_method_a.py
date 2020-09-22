from dataclasses import asdict

from package.someclass import SomeClass


def test_method_a_one():
    class_instance = SomeClass()
    result = asdict(class_instance.method_a("a")[0])
    assert result["string"] == "a"


def test_method_a_two():
    class_instance = SomeClass()
    result = asdict(class_instance.method_a("b")[0])
    assert result["string"] == "b"
