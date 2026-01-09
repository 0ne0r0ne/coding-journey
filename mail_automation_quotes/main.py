import datetime as dt
import random
import smtplib


current_date = dt.datetime.now()
current_day = current_date.weekday() # Monday is 0 and Sunday is 6 (friday is 4)


if current_day == 4:
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
  my_email = "369zeka@gmail.com"
  password = "ykzu dvff slsq fpqt"
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() 
    connection.login(user=my_email, password=password)

    connection.sendmail(
      from_addr=my_email, to_addrs="soysalnihat32@gmail.com", 
      msg=f"Subject:Friday Motivation\n\n{random.choice(all_quotes)}"
      )

