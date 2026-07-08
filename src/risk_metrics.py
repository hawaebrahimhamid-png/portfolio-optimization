import numpy as np


def calculate_var(returns, confidence=0.95):

    return returns.quantile(1-confidence)


def calculate_sharpe(returns):

    return (
        returns.mean()
        /
        returns.std()
    ) * np.sqrt(252)
