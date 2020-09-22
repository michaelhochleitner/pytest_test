from dataclasses import dataclass


@dataclass
class Result:
    """Instances of this class are appended to the list in ResultContainer by SomeClass.method_a()."""
    string: str


def __init__(self, string):
    self.string = string

