from package.result import Result
from package.resultcontainer import ResultContainer


class SomeClass:
    def __init__(self):
        self.result = ResultContainer([])

    def method_a(self, string):
        self.result.result_list.append(Result(string))
        return self.result.result_list
