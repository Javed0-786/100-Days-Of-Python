import requests
import smtplib
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

my_email = "altaf9120573582@gmail.com"
password = "swytbfqhyoodpblf"


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def get_news():
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "apiKey": "aa8794b12ede4c65a66a9a5d8238ef12",
        "q": COMPANY_NAME,
        "from": "2022-05-14",
        "sortBy": "published",
    }
    news_response = requests.get(
        url="https://newsapi.org/v2/everything?", params=news_params)
    # print(news_response.json())
    headlines = [news['title'].encode('utf-8')
                 for news in news_response.json()['articles']]

    descriptions = [(html.unescape((news['description']))).encode('utf-8')
                    for news in news_response.json()['articles']]
    print(descriptions)

    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    message = ""
    for i in range(3):
        message += f"Headline: {headlines[i]} \nDescription: {descriptions[i]}\n\n"
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="alam9120573582@gmail.com", msg=f"Subject: Tesla Update\n\n{message}")
    print(message)


alphaadvantage_api_key = "M0KZ7O0ZF4YU632B"
parameter = {
    "apikey": alphaadvantage_api_key,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
}


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(
    url="https://www.alphavantage.co/query?", params=parameter)
data = (response.json())['Time Series (Daily)']

dates = [list(data)[0],
         list(data)[1]]
# print(type(data))
# print(dates)
yesterday = float(data[dates[0]]["1. open"])
previousday = float(data[dates[1]]["4. close"])
percent = round(((yesterday - previousday) * 100 / yesterday), 2)
print(abs(percent))

if percent >= 5 or percent <= -5:
    print("Alert")
    get_news()
else:
    print("Relax")
    get_news()
