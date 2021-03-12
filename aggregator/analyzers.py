from abc import ABC
from enum import IntEnum

from .utills import get_db_connection


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
    def __init__(self, table_name):
        self.table_name = table_name

    def analyze(self):
        raise NotImplementedError


class TimeDifference(Analyzer):
    def analyze(self):
        raw_sql = """
        SELECT CAST (
            (
                JULIANDAY((
                    SELECT event_time
                    FROM "%s"
                    ORDER BY `index` DESC limit 1))
                -
                JULIANDAY((
                    SELECT event_time
                    FROM %s
                    ORDER BY `index` limit 1))
            ) * 24 * 60 As Integer
        );
        """ % (self.table_name, self.table_name)
        connection = get_db_connection()
        result = connection.execute(raw_sql).fetchone()[0]

        return result


analyzer_factory.register_analyzer(AnalyzerType.TIME_DIFFERENCE, TimeDifference)


class TotalRows(Analyzer):
    def analyze(self):
        raw_sql = 'SELECT COUNT(*) FROM "%s";' % (self.table_name, )
        connection = get_db_connection()
        result = connection.execute(raw_sql).fetchone()[0]

        return result


analyzer_factory.register_analyzer(AnalyzerType.TOTAL_ROWS, TotalRows)
