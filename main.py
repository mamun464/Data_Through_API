import time

import requests
MY_LAT=23.796621
MY_LNG=90.432604
#------------------International Space Station Location------------------
def issOverHead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_longitude=data["iss_position"]["longitude"]
    iss_latitude=data["iss_position"]["latitude"]

    if(MY_LNG-5 <= float(iss_longitude) <= MY_LNG+5) and (MY_LAT-5 <= float(iss_latitude) <= MY_LAT+5):
        return True

from datetime import datetime as dt

def isNight():
    paramitter={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0,
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/json",params=paramitter)
    response.raise_for_status()
    data=response.json()
    sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

    today=dt.now().hour
    if (today >= int(sunset)) or (today <= int(sunrise)):
        return True

def sentMail(msg,to_mail="mamunurrashid.s.bd@gmail.com"):
    import smtplib
    email="your.ex.daddy8@gmail.com"
    password="lpgfzommjqmtjlda"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_mail, #"mamunurrashid.s.bd@gmail.com",
            msg=(f"Subject: Look Up ISS 🛰️\n\n {msg}").encode('utf-8')
        )
    print("Sent: "+to_mail)

while True:

    if issOverHead() and isNight():
        msg=("The ISS is above ☝️  you in the SKY!")
        sentMail(msg=msg)
    else:
        print("Not Right time now!")

    time.sleep(60)


