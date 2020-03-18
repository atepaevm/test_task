import os
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as bs
from logger import get_logger
import re

class Transformer:
    def __init__(self):
        self.logger = get_logger(type(self).__name__)
        self.df = pd.DataFrame()
        self.stat_df = pd.DataFrame(columns=['Date',
                                             'AMT_HOLD', 'AMT_SELL', 'AMT_BUY',
                                             'INS_HOLD', 'INS_SELL', 'INS_BUY'])

    def preprocess(self, soup, to_excel=True):

        table = soup.find("table", {"class": "scroll-table sort-table"})
        columns = [th.text for th in table.find_all('th')]
        data = []
        rows = table.find_all_next("tr")
        # skip header
        for tr in rows[1:]:
            td = tr.find_all('td')
            row = [tr.text for tr in td]
            # preprocessing
            # date
            row[0] = datetime.strptime(row[0], '%m/%d/%Y')
            # rating
            match = re.search(r'(\w)+$', row[3])
            row[3] = None if match is None else match.group(0)
            # price
            match = re.search(r'(\d)+\.(\d)+$', row[4])
            row[4] = None if match is None else float(match.group(0))
            data.append(row)
        self.df = pd.DataFrame(data, columns=columns)
        if to_excel:
            self.df.to_excel('export/data.xlsx')
        self.logger.info("success")

    def stat(self, to_excel=True):
        l = []
        for d in sorted(self.df['Date'].unique(), reverse=True):
            tmp_df = self.df[self.df['Date'] == d]
            buy_df = tmp_df[tmp_df['Rating'] == 'Buy']
            hold_df = tmp_df[tmp_df['Rating'] == 'Hold']
            sell_df = tmp_df[tmp_df['Rating'] == 'Sell']
            row = [
                d, hold_df['Price Target'].mean(),
                sell_df['Price Target'].mean(),
                buy_df['Price Target'].mean(),
                len(hold_df), len(sell_df), len(buy_df)
            ]
            l.append(row)
        self.stat_df = pd.DataFrame(l, columns=self.stat_df.columns)
        if to_excel:
            self.stat_df.to_excel('export/stat.xlsx')
        self.logger.info("success")
        return self.stat_df

    def transform(self, text=None):
        if text is None:
            path = sorted(os.listdir('data'),
                                 key=lambda path: os.path.getmtime('data/' + path))[0]
            try:
                with open('data/' + path, 'r') as f:
                    soup = bs(f.read(), 'html.parser')
            except FileNotFoundError as e:
                self.logger.exception(e)
        else:
            soup = bs(text, 'html.parser')
        self.preprocess(soup)
        ret = self.stat()
        self.logger.info("success")
        return ret


if __name__ == '__main__':
    most_recent = sorted(os.listdir('data'),
                         key=lambda path: os.path.getmtime('data/' + path))[0]
    t = Transformer()
    with open('data/' + most_recent, 'r') as f:
        print(t.transform(f.read()))

