
import smtplib
import random
import datetime as dt
my_email="mohitthakur9901@gmail.com"
password="edzyqqkhpficrkia"
now=dt.datetime.now()
weekday=now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        data=file.readlines()
        quotes=random.choices(data)
    print(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(password=password,user=my_email,)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,msg=f"Subject:MONDAY_MOTIVATION\n\n{quotes}")

