import pykx as kx


class Strategy:
    def execute(self, csv_file_path):
        pass


class StrategyTrades(Strategy):
    def execute(self, csv_file_path):
        return kx.q.read.csv(csv_file_path,
                             [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])


class StrategyQuotes(Strategy):
    def execute(self, csv_file_path):
        return kx.q.read.csv(csv_file_path,
                             [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom, kx.FloatAtom, kx.LongAtom])