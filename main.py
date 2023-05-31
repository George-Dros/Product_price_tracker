import requests
from bs4 import BeautifulSoup
import smtplib

URL = "insert your amazon URL"
my_email = "your GMAIL"
password = "Your GMAIL API password"

headers = {
    "Accept-Language": "insert your accept-language from 'https://myhttpheader.com/' ",
    "User-Agent": "insert your user agent from 'https://myhttpheader.com/' "

}
response = requests.get(URL, headers=headers)
page = response.text
soup = BeautifulSoup(page, "html.parser")
data = soup.find(class_="a-offscreen")

price_str = data.getText()
price = float(price_str.replace("$", ""))

target_price = 100 # Insert your target price

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Price!!\n\nPrice has fallen bellow ${target_price}, to ${price}!!")
        connection.close()