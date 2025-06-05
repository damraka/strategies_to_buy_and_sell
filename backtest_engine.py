import pandas as pd

class BacktestEngine:
    def __init__(self, data, strategy):
        self.data = data.copy()
        self.strategy = strategy
        self.results = None

    def run_backtest(self):
        signals = self.strategy.generate_signals()
        self.data['Position'] = signals if isinstance(signals, pd.Series) else signals['Position']
        self.data['Returns'] = self.data['Close'].pct_change()
        self.data['Strategy_Returns'] = self.data['Returns'] * self.data['Position'].shift(1)
        self.data['Cumulative_Strategy_Returns'] = (1 + self.data['Strategy_Returns']).cumprod() - 1
        self.data['Cumulative_BuyHold_Returns'] = (1 + self.data['Returns']).cumprod() - 1
        self.results = self.data
        return self.results

