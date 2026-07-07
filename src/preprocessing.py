import pandas as pd


def clean_data(df):

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df = df.ffill()

    # Ensure Date index format
    df.index = pd.to_datetime(df.index)

    return df



def select_close_price(df):

    close = df[["Close"]]

    return close
