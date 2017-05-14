import requests
import time
from bs4 import BeautifulSoup

url1 = 'https://parents.ebnet.org/genesis/parents?gohome=true'
url2 = 'https://parents.ebnet.org/genesis/j_security_check'
url3 = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=attendance&tab3=class&action=form&studentid=91453'#class
url4 = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=studentsummary&action=form&studentid=91453'#summary
url5 = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=91453&action=form'#gradebook


j_username = 'riying2009@yahoo.com'#input('enter email: ')
j_password = 'hill78hill78'#input('enter password: ')

data2 = {

    'j_username':j_username, #fill this out
    'j_password':j_password #fill this out
}
data3 = {
    'tab1':'studentdata',
    'tab2':'attendance',
    'tab3':'class',
    'action':'form',
    'studentid':'91453'#need to change student id accordingly 
}
data4 = {
    'tab1':'studentdata',
    'tab2':'studentsummary',
    'action':'form',
    'studentid':'91453'
}

data5 = {
    'tab1':'studentdata',
    'tab2':'gradebook',
    'tab3':'weeklysummary',
    'studentid':'91453',
    'action':'form'
}

#loads up all the html using requests library
session = requests.Session()

r1 = requests.get(url1)
r2 = session.post(url2, cookies=r1.cookies, data=data2)
r3 = session.post(url3, cookies=r2.cookies, data=data3)
r4 = session.post(url4, cookies=r2.cookies, data=data4)
r5 = session.post(url5, cookies=r2.cookies, data=data5)

#used to parse the html
r3_soup = BeautifulSoup(r3.text, 'html5lib')#class
r4_soup = BeautifulSoup(r4.text, 'html5lib')#summary
r5_soup = BeautifulSoup(r5.text, 'html5lib')#gradebook


