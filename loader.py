from logger import get_logger
import pandas as pd


class Loader:
    def __init__(self):
        self.logger = get_logger(type(self).__name__)

    def load(self, df):
        for index, row in df.iterrows():
            item = {
                        row['Date']:
                            {
                                'AMT_HOLD': row['AMT_HOLD'],
                                'AMT_SELL': row['AMT_SELL'],
                                'AMT_BUY': row['AMT_BUY'],
                                'INS_HOLD': row['INS_HOLD'],
                                'INS_SELL': row['INS_SELL'],
                                'INS_BUY': row['INS_BUY'],
                            }
                    }
            print(item)
            self.logger.info(item)
        self.logger.info("success")
        return


if __name__ == '__main__':
    df = pd.read_excel('data/stat.xlsx').set_index('Unnamed: 0')
    l = Loader().load(df)
