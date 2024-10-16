from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def stock_price():
    if request.method == 'POST':
        stock_symbol = request.form['symbol'].upper()  # Stock symbol entered by the user
        stock_symbol += ".NS"  # Append '.NS' for NSE stocks
        
        try:
            stock = yf.Ticker(stock_symbol)
            stock_data = stock.history(period="1d")
            if not stock_data.empty:
                stock_price = stock_data['Close'][0]
                return render_template('stock_price.html', stock_price=stock_price, symbol=stock_symbol)
            else:
                return render_template('stock_price.html', error="Stock symbol not found.")
        except Exception as e:
            return render_template('stock_price.html', error="Error fetching stock data.")
    
    return render_template('stock_price.html')


if __name__ == '__main__':
    app.run(debug=True)
