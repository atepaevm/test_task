from prefect import Flow, task
from extracter import Extracter
from transformer import Transformer
from loader import Loader

with Flow("ETL") as flow:
    url = 'https://www.marketbeat.com/stocks/NASDAQ/MSFT/price-target/?MostRecent=0'
    e = Extracter(url).extract()
    df = Transformer().transform(text=e)
    l = Loader().load(df)

flow.run()


