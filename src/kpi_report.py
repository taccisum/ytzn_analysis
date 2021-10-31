import pandas as pd
import numpy as np


class KpiReport:
    def __init__(self, csv_path):
        self.csv = None
        self.csv_path = csv_path

    def byname(self):
        csv = self.__read_csv()
        return csv.groupby('姓名').sum()

    def bycity(self):
        csv = self.__read_csv()
        return csv.groupby('所属大区').sum()

    def byarea(self):
        csv = self.__read_csv()
        return csv.groupby('负责业务单元').sum()

    def for_saler(self):
        csv = self.__read_csv()

        arr = []

        for name, group in csv.groupby('姓名'):
            arr.append([
                group['姓名'].iloc[0],
                group['入职日期'].iloc[0],
                group['今日新点开发'].sum(),
                group['今日网点资料整理'].sum(),
                group['今日出货'].sum()
            ])

        df = pd.DataFrame(arr, columns=['姓名', '入职日期', '新点开发', '网点资料整理', '出货'])
        return df

    def for_area(self):
        csv = self.__read_csv()

        arr = []

        for name, group in csv.groupby(['所属大区', '所属工作站']):
            arr.append([
                group['所属大区'].iloc[0],
                group['所属工作站'].iloc[0],
                group['今日新点开发'].sum(),
                group['今日网点资料整理'].sum(),
                group['今日出货'].sum()
            ])

        df = pd.DataFrame(arr, columns=['所属大区', '所属工作站', '新点开发', '网点资料整理', '出货'])
        return df

    def __read_csv(self):
        if self.csv is None:
            self.csv = pd.read_csv(self.csv_path)
        return self.csv


if __name__ == '__main__':
    r = KpiReport('data/1.csv')
    print(r.for_saler())
