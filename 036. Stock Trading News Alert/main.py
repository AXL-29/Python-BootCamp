import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "EC5XGS83V10USF9G"
NEWS_API_KEY = "0afbbc1cb1124276b67efaddae81bd4f"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params, verify=False)
stock_response.raise_for_status()

stock_data = stock_response.json()
time_series = stock_data["Time Series (Daily)"]

daily_prices = [value for (key, value) in time_series.items()]
yesterday_close = float(daily_prices[0]["4. close"])
day_before_close = float(daily_prices[1]["4. close"])

difference = round(abs(yesterday_close - day_before_close), 2)
diff_percent = round((difference / float(yesterday_close)) * 100, 2)

if diff_percent > 0.20:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params, verify=False)
    news_response.raise_for_status

    news_article = news_response.json()["articles"]
    three_articles = news_article[:3]

    news = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    print(news)
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

