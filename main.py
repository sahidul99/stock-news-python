import requests
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = 'H6S76RMRZXBA6ZOS'
NEWS_API = '2989d645284a45bd8e40944be84c1bdc'




    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API
}
request = requests.get(STOCK_ENDPOINT, params).json()['Time Series (Daily)']
data = [value for (key, value) in request.items()]


yesterday_closing = float(data[0]['4. close'])

before_yesterday_closing = float(data[1]['4. close'])

diff = abs(yesterday_closing-before_yesterday_closing)
percent_diff = (diff/before_yesterday_closing)*100
if percent_diff > 5:
    # print('GET NEWS')
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    pass


params = {
        'q': COMPANY_NAME,
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API
    }
news = requests.get(NEWS_ENDPOINT, params).json()['articles'][:3]




    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


news_formated=[{'title':item['title'],'description':item['description']} for item in news]

#TODO 9. - Send each article as a separate message via Twilio.
for item in news_formated:
    print(item['title'])
    print(item['description'])



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

