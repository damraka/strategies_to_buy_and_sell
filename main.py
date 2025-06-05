import pandas as pd
from strategies.mean_reversion_strategy import MeanReversionStrategy
from backtest_engine import BacktestEngine
from visuals.performance_plot import plot_performance
from metrics.performance_metrics import calculate_metrics
import matplotlib.pyplot as plt

def plot_gs_price_with_signals(df, signals):
    if 'Position' not in signals.columns:
        print("ERROR: 'Position' column not found in signals! Here are the columns:", signals.columns)
        return
    
    plt.figure(figsize=(14,7))
    plt.plot(df.index, df['Close'], label='GS Close Price', color='blue')
    plt.scatter(signals.index, df.loc[signals.index, 'Close'], 
                c=signals['Position'], cmap='coolwarm', label='Positions', marker='o')
    plt.title('Goldman Sachs Price & Strategy Positions')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def main():
    df = pd.read_csv('data/historical_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    mean_reversion = MeanReversionStrategy(df, window=20, threshold=0.02)
    signals = mean_reversion.generate_signals()
    signals = signals.to_frame(name='Position')  # <<< THIS IS THE GOLD

    backtester = BacktestEngine(df, mean_reversion)
    results = backtester.run_backtest()

    print(f"Cumulative Strategy Return: {results['Cumulative_Strategy_Returns'][-1]:.2%}")
    print(f"Cumulative Buy & Hold Return: {results['Cumulative_BuyHold_Returns'][-1]:.2%}")

    stats = calculate_metrics(results)
    print("\n===== DETAILED PERFORMANCE METRICS =====")
    for k, v in stats.items():
        print(f"{k}: {v:.2%}")

    plot_performance(results)

    plot_gs_price_with_signals(df, signals)

if __name__ == '__main__':
    main()
