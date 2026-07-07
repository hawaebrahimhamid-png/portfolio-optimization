from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


def build_lstm(window_size=60):

    model = Sequential()

    model.add(
        LSTM(
            units=50,
            return_sequences=True,
            input_shape=(window_size,1)
        )
    )

    model.add(
        Dropout(0.2)
    )

    model.add(
        LSTM(
            units=50
        )
    )

    model.add(
        Dropout(0.2)
    )

    model.add(
        Dense(1)
    )

    model.compile(
        optimizer="adam",
        loss="mean_squared_error"
    )

    return model
