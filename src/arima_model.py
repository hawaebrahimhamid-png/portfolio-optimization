from statsmodels.tsa.arima.model import ARIMA


def train_arima(train_data, order=(1,1,1)):

    model = ARIMA(
        train_data,
        order=order
    )

    model_fit = model.fit()

    return model_fit



def forecast_arima(model_fit, steps):

    forecast = model_fit.forecast(
        steps=steps
    )

    return forecast
