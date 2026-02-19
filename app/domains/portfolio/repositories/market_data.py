# app/domains/portfolio/repositories/market_data.py

import pandas as pd
from datetime import date
from typing import Tuple

class PortfolioRepository:
    def fetch_data(
        self,
        tickers: Tuple[str, ...],
        start_date: date | None,
        end_date: date | None,
        period: str | None,
    ) -> pd.DataFrame:
        raise NotImplementedError
