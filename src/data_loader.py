import yfinance as yf


def load_stock_data(ticker, start_date, end_date):

    try:
        data = yf.download(
            ticker,
            start=start_date,
            end=end_date
        )

        if data.empty:
            raise ValueError(
                f"No data found for {ticker}"
            )

        return data

    except Exception as e:
        print(f"Error loading {ticker}: {e}")
        return None
