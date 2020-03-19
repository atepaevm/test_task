from logger import get_logger
import pandas as pd


class Loader:
    """Dummy of DB connection"""
    def __init__(self):
        self.logger = get_logger(type(self).__name__)

    def load(self, df):
        # get list of dicts like {'date': ..., 'AMT_HOLD': ...}
        data = [row.to_dict() for _, row in df.iterrows()]
        for item in data:
            """insert in DB"""
            self.logger.info(item)
        self.logger.info("success")
        return


if __name__ == '__main__':
    df = pd.read_excel('export/stat.xlsx').set_index('Unnamed: 0')
    Loader().load(df)
