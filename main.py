##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd
import os

# 1. Update the birthdays.csv
now=dt.datetime.now()
month=now.month
day=now.day

# 2. Check if today matches a birthday in the birthdays.csv
birthday_details=pd.read_csv("c:/Users/Electrobot/python_new/birthdaywisher/birthdays.csv")

for index,row in birthday_details.iterrows():
    if row["month"]==month and row["day"]==day:
        name=row['name']
        email=row['email']
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter=[]
for filename in os.listdir("c:/Users/Electrobot/python_new/birthdaywisher/letter_templates"):
    if filename.endswith(".txt"): 
         letter.append(filename)
    else:
        continue
with open (f"c:/Users/Electrobot/python_new/birthdaywisher/letter_templates/{random.choice(letter)}") as file:
    content=file.read()
content=content.replace("[NAME]",name)
content=content.replace("Filler","Tridib")
# 4. Send the letter generated in step 3 to that person's email address.
my_email="-----@gmail.com"
password=******

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=f"Subject: Happy Birthday\n\n{content}"
    )





