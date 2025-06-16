import yfinance as yf

# Define your portfolio: {'TICKER': quantity}
portfolio = {
    'AAPL': 10,
    'GOOGL': 5,
    'MSFT': 8,
    'TSLA': 3
}

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    if not data.empty:
        return data['Close'].iloc[0]
    return 0.0

def calculate_portfolio_value(portfolio):
    total_value = 0.0
    print("📊 Current Portfolio Value:\n")
    for ticker, quantity in portfolio.items():
        price = get_stock_price(ticker)
        value = price * quantity
        print(f"{ticker}: {quantity} shares × ${price:.2f} = ${value:.2f}")
        total_value += value
    print(f"\n💰 Total Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    calculate_portfolio_value(portfolio)
