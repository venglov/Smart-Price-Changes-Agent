import logging
import pandas as pd
from prophet import Prophet
import warnings
from src.db.db_utils import db_utils

logger = logging.getLogger('prophet')
logger.setLevel(logging.ERROR)
logger = logging.getLogger('cmdstanpy')
logger.setLevel(logging.ERROR)
logger = logging.getLogger('stanpy')
logger.setLevel(logging.ERROR)
warnings.simplefilter(action='ignore')


async def forecast(protocol: str):
    transaction_table = db_utils.get_swaps()
    future_table = db_utils.get_future()
    swaps_row = await transaction_table.get_all_rows_by_criteria({'pool_contract': protocol})

    df = pd.DataFrame([t.__dict__ for t in swaps_row])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df.set_index('timestamp').resample('Min').mean().reset_index()

    if df['price'].count() < 2:
        return

    train = df.reset_index()[['timestamp', 'price']].rename({'timestamp': 'ds', 'price': 'y'},
                                                            axis='columns')

    m = Prophet(changepoint_range=1, changepoint_prior_scale=0.5, interval_width=0.99)
    m.fit(train)
    future = m.make_future_dataframe(periods=30, freq='Min')

    forecast_rows = m.predict(future)

    await future_table.delete_row_by_contract(protocol)
    for index, row in forecast_rows.iterrows():
        await future_table.paste_row(
            {'pool_contract': protocol, 'timestamp': int(row['ds'].timestamp()), 'price': row['yhat'],
             'price_lower': row['yhat_lower'], 'price_upper': row['yhat_upper']})
