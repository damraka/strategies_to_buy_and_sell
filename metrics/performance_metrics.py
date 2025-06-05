import numpy as np

def calculate_metrics(df):
    returns = df['Strategy_Returns'].dropna()
    total_return = df['Cumulative_Strategy_Returns'][-1]
    
    days = len(returns)
    annualized_return = (1 + total_return) ** (252 / days) - 1
    
    annualized_vol = returns.std() * np.sqrt(252)
    
    sharpe_ratio = annualized_return / annualized_vol if annualized_vol != 0 else np.nan
    
    cumulative = (1 + returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = drawdown.min()
    
    metrics = {
        'Total Return': total_return,
        'Annualized Return': annualized_return,
        'Annualized Volatility': annualized_vol,
        'Sharpe Ratio': sharpe_ratio,
        'Max Drawdown': max_drawdown
    }
    
    return metrics
