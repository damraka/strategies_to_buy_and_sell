import matplotlib.pyplot as plt

def plot_performance(df):
    plt.figure(figsize=(14,7))
    plt.plot(df['Cumulative_Strategy_Returns'], label='Momentum Strategy Returns', linewidth=2)
    plt.plot(df['Cumulative_BuyHold_Returns'], label='Buy & Hold Returns', linewidth=2)
    plt.title('Quant Strategy Evaluator - Momentum vs Buy & Hold')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.show()

