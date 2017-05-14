from login import *
from utility import *

def get_course_names():
     u_tags = gradebook_soup.findAll('u')
     string_u_tags = [str(item) for item in u_tags]

     trimmed_u_tags = []
     for item in string_u_tags:
          trimmed_u_tags.append(replace_characters(r'amp;','\'', '\n', r'<u>', r'</u>',string = item, replacement = ''))
          
     return trimmed_u_tags

def get_course_soups():
     soups = []
     request_list = []
     links = []
     course_datas = []
     category_tabs = gradebook_soup.findAll('span', class_='categorytab')

     for item in category_tabs:
          string = item.get('onclick')
          courseAndSection = string[string.index('\',\'')+3:string.index('\');')]
          link = 'https://parents.ebnet.org/genesis/parents?tab1=studentdata&tab2=gradebook&tab3=listassignments&studentid=' + studentid + '&action=form&dateRange=' + dateRange + '&date=' + dateof + '&courseAndSection=' + courseAndSection
          links.append(link)

          course_datas.append(
          {
          'tab1':'studentdata',
          'tab2':'gradebook',
          'tab3':'listassignments',
          'studentid':studentid,
          'action':'form',
          'dateRange':dateRange,
          'date':dateof,
          'courseAndSection':courseAndSection
          })

     for i in range (0, len(links)):
          request_list.append(session.post(links[i], cookies=login.cookies, data=course_datas[i]))
          
     for item in request_list:
          soups.append(BeautifulSoup(item.text, 'html5lib'))

     return soups

courses = get_course_soups()

def initialize_grades():
     

def check_grades():


def compare_grades():
     
     






















