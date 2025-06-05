# Strategy Backtester
Overview

This project is designed to provide a robust framework for evaluating trading strategies using historical market data. It leverages a mean reversion strategy as a demonstrative example to illustrate how systematic trading models can be tested, analyzed, and visualized with clarity and precision.

The backtesting engine supports signal generation, portfolio performance computation, and detailed metrics reporting to empower informed decision-making for traders and analysts.
Features

    Mean Reversion Strategy Implementation: Demonstrates a practical example of a classical trading strategy based on statistical price behavior.

    Backtesting Engine: Executes the strategy against historical price data, simulating trades and calculating returns.

    Performance Metrics: Computes key quantitative measures including cumulative returns, volatility, Sharpe ratio, and drawdowns for comprehensive evaluation.

    Visual Analytics: Generates clear and informative plots of strategy performance and asset price with trading signals for intuitive insight.

Installation

Ensure you have Python 3.7+ installed. It is recommended to use a virtual environment. Install dependencies via:

pip install -r requirements.txt  

Usage

Place your historical price data CSV in the data/ directory with columns including Date and Close. Execute the main script to run the backtest and view results:

python main.py  

The script outputs cumulative strategy returns, benchmark buy & hold returns, and detailed metrics to the console. Visualizations appear sequentially for focused review.
Project Structure

    strategies/ — Contains trading strategy implementations.

    backtest_engine.py — Core backtesting logic combining data and strategy signals.

    metrics/ — Functions to calculate quantitative performance statistics.

    visuals/ — Plotting utilities for strategy and price visualization.

    data/ — Historical price data input files.

    main.py — Entry point to run the complete backtesting workflow.

Contributing

Contributions are welcome. Please ensure code quality and testing standards are met before submitting pull requests.
License

This project is licensed under the MIT License.
