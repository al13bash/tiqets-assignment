import pandas as pd


class CsvWriter:
    def write(self, data, path="data/result.csv"):
        data.to_csv(path, index=False)
