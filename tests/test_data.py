from src.preprocessing import clean_data
import pandas as pd


def test_clean_data():

    df = pd.DataFrame({
        "Close":[1,None,3]
    })


    result = clean_data(df)


    assert result.isna().sum().sum()==0
