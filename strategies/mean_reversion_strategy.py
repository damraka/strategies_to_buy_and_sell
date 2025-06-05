import pandas as pd

class MeanReversionStrategy:
    def __init__(self, data, window=20, threshold=0.02):
        self.data = data
        self.window = window
        self.threshold = threshold 

    def generate_signals(self):
        df = self.data.copy()
        df['MA'] = df['Close'].rolling(window=self.window).mean()
        df['Price_vs_MA'] = (df['Close'] - df['MA']) / df['MA']

        df['Signal'] = 0
        df.loc[df['Price_vs_MA'] < -self.threshold, 'Signal'] = 1
        df.loc[df['Price_vs_MA'] > self.threshold, 'Signal'] = -1

        df['Signal'] = df['Signal'].replace(to_replace=0, method='ffill').fillna(0)

        return df['Signal']

