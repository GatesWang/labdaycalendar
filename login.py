import requests
import time
from bs4 import BeautifulSoup

homeurl = 'https://parents.ebnet.org/genesis/parents?gohome=true'
loginurl = 'https://parents.ebnet.org/genesis/j_security_check'

j_username = 'email'#input('enter email: ')
j_password = 'password'#input('enter password: ')

logindata = {
    'j_username':j_username, 
    'j_password':j_password
}

session = requests.Session()

home = requests.get(homeurl)
login = session.post(loginurl, cookies=home.cookies, data=logindata)
login_soup = BeautifulSoup(login.text, 'html5lib')#login


studentid = ''
dateRange = ''
dateof = ''

for item in login_soup.findAll('a'):
    if item.get('href').startswith('/genesis/parents?tab1'):
        string = item.get('href')
        studentid = string[string.index(r'studentid=')+10:string.index(r'&action')]
        dateRange = string[string.index(r'mpToView=')+9:]
        dateof = string[string.index(r'date=')+5:string.index(r'&mpToView')]

############################################################################################################
attendenceurl = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=attendance&tab3=class&action=form&studentid=' + studentid#class
summaryurl = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=studentsummary&action=form&studentid=' + studentid#summary
gradebookurl = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&studentid=' + studentid + '&action=form'#gradebook
courseurl = 'https://parents.ebnet.org/genesis/parents?'

attendencedata = {
    'tab1':'studentdata',
    'tab2':'attendance',
    'tab3':'class',
    'action':'form',
    'studentid':studentid
}
summarydata = {
    'tab1':'studentdata',
    'tab2':'studentsummary',
    'action':'form',
    'studentid':studentid
}

gradebookdata = {
    'tab1':'studentdata',
    'tab2':'gradebook',
    'tab3':'weeklysummary',
    'studentid':studentid,
    'action':'form'
}

attendence = session.post(attendenceurl, cookies=login.cookies, data=attendencedata)
summary = session.post(summaryurl, cookies=login.cookies, data=summarydata)
gradebook = session.post(gradebookurl, cookies=login.cookies, data=gradebookdata)

#used to parse the html
attendence_soup = BeautifulSoup(attendence.text, 'html5lib')#attendence
summary_soup = BeautifulSoup(summary.text, 'html5lib')#summary
gradebook_soup = BeautifulSoup(gradebook.text, 'html5lib')#gradebook



