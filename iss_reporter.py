import requests
from datetime import datetime
import smtplib
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mail_adress = "369zeka@gmail.com"
password = "ykzu dvff slsq fpqt"

longitude = 34.632328
latitude = 36.799696

parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0,   
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise = sunrise.split('T')[1].split(":")[0]
sunset = sunset.split('T')[1].split(":")[0]

time_now = datetime.now()
current_hour = time_now.hour

def iss_check():
    """check if ISS is overhead"""
    iss_response = requests.get("http://api.open-notify.org/iss-now.json") 
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if (latitude - 5) <= iss_latitude <= (latitude + 5) and (longitude - 5) <= iss_longitude <= longitude + 5:
        return True

def night_check():
    """check if it's night time"""
    if current_hour >= int(sunset) or current_hour <= int(sunrise):
        return True
    
def sent_email():
    """send email notification if ISS is overhead and it's night"""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=mail_adress, password=password)
        connection.sendmail(
            from_addr=mail_adress,
            to_addrs="mikailbaser55@gmail.com",
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
    

if iss_check() and night_check():
    sent_email()
    print("Email sent: ISS is overhead and it's night time.")
elif iss_check():
    print("ISS is overhead but it'S not night time.")
else:
    print("ISS is not overhead.")
   
    
