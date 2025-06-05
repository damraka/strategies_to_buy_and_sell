import pandas as pd

class MomentumStrategy:
    def __init__(self, data):
        self.data = data.copy()
        self.data['SMA20'] = self.data['Close'].rolling(window=20).mean()
        self.data['Position'] = 0

    def generate_signals(self):
        self.data.loc[self.data['Close'] > self.data['SMA20'], 'Position'] = 1
        self.data.loc[self.data['Close'] <= self.data['SMA20'], 'Position'] = -1
        return self.data[['Position']]
        
        
