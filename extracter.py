import requests
from logger import get_logger
from datetime import datetime


class Extracter:
    def __init__(self, url):
        self.logger = get_logger(type(self).__name__)
        self.url = url

    def extract(self, to_file=True):
        try:
            r = requests.get(self.url)
        except requests.exceptions.ConnectionError as e:
            self.logger.exception(e)
            return
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if to_file:
            with open('data/data_{}.html'.format(now), 'w',
                      encoding='utf-8') as f:
                f.write(r.text)
        self.logger.debug("success")
        return r.text


if __name__ == '__main__':
    url = 'https://www.marketbeat.com/stocks/NASDAQ/MSFT/price-target/?MostRecent=0'
    Extracter(url).extract()
