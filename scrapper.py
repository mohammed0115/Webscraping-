import mechanize   
from bs4 import BeautifulSoup
import urllib
from  http import cookiejar 
import pandas as pd 
data = pd.read_csv(r"dataset\test.csv")


def scrap(firstname,lastname,email,phonenumber,password):
        cj = cookiejar.CookieJar()
        br = mechanize.Browser()
        br.set_cookiejar(cj)
        br.open("http://localhost/useraccounts/registration.php")

        br.select_form(nr=0)
        br.form['firstname'] = firstname
        br.form['lastname'] = lastname
        br.form['email'] = email
        br.form['phonenumber'] = phonenumber
        br.form['password'] = password
        br.submit()
        print ("inserted successfully....")
        
for j in range(len(data)):
    scrap(data.iloc[j][0],data.iloc[j][1],data.iloc[j][2]," ",str(data.iloc[j][4]))