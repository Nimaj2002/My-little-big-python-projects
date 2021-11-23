import pandas
import smtplib
import datetime as dt
from random import randint

def send_wish(name, email, year):







now = dt.datetime.now()
day = now.day
month = now.month

all_receivers_data = pandas.read_csv("data.csv")

for row, column in all_receivers_data.iterrows():
    if column.day == day and column.month == month:
        print(column["name"])


