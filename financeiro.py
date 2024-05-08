import requests
import mplfinance as mpf

def obter_dados_acao(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    dados = response.json()
    return dados['Time Series (Daily)']

def plotar_candlestick(dados):
    prices = {date: {'open': float(values['1. open']),
                     'high': float(values['2. high']),
                     'low': float(values['3. low']),
                     'close': float(values['4. close'])}
              for date, values in dados.items()}
    
    df = mpf.make_marketcolors(up='g', down='r', edge='black'), mpf.make_mpf_style(base_mpf_style='nightclouds')
    
    mpf.plot(prices, type='candle', style='charles', volume=True, show_nontrading=True, title='Gráfico de Candlestick')

if __name__ == "__main__":
    symbol = 'AAPL'  # Símbolo da ação (Apple, neste caso)
    api_key = 'sua_api_key'  # Substitua 'sua_api_key' pela sua chave da API do Alpha Vantage
    
    dados_acao = obter_dados_acao(symbol, api_key)
    
    plotar_candlestick(dados_acao)
