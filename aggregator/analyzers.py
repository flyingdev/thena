from abc import ABC
from enum import IntEnum


class AnalyzerType(IntEnum):
    TIME_DIFFERENCE = 10000
    TOTAL_ROWS = 10001


class AnalysisFactory:
    def __init__(self):
        self.analyzers = {}

    def register_analyzer(self, key, class_):
        self.analyzers[key] = class_

    def get_analyzer(self, key):
        if key not in self.analyzers.keys():
            raise NotImplementedError

        return self.analyzers[key]


analyzer_factory = AnalysisFactory()


class Analyzer(ABC):
    def __init(self, table_name):
        self.table_name = table_name

    def analyze(self):
        raise NotImplementedError


class TimeDifference(Analyzer):
    pass


analyzer_factory.register_analyzer(AnalyzerType.TIME_DIFFERENCE, TimeDifference)


class TotalRows(Analyzer):
    pass


analyzer_factory.register_analyzer(AnalyzerType.TOTAL_ROWS, TotalRows)
