from login import *

def replace_characters(*args, string, replacement):
    string2 = string
    for arg in args:
        string2 = string2.replace(arg, replacement)

    return string2
    
date = time.strftime('%m/%d/%Y')#gets the current date in string format
day = ''

odd_rows = r3_soup.findAll('tr', class_='listrowodd')
even_rows = r3_soup.findAll('tr', class_='listroweven')

school_days = dict()

for i in range(0, len(odd_rows)):#parses html to get odd numbered school days
    encoded1 = odd_rows[i].findChildren()[0].contents[0].encode('utf-8')#encode the navigable string, so it can be converted
    string1 = str(encoded1)#convert navigable string to string
    trimmed1 = replace_characters('\/','\,','>','<',' ', '\'', r'\n', 'b', string = string1, replacement = '')

    encoded2 = odd_rows[i].findChildren()[1].contents[0].encode('utf-8')
    string2 = str(encoded2)
    trimmed2 = replace_characters(' ', '\'', r'\n', 'b', string = string2, replacement = '')
    
    school_days[trimmed2] = trimmed1
    
for i in range(0, len(even_rows)):#parses html to get even numbered school days
    index1 = 0
    index2 = 1

    if(len(even_rows[i].findChildren()[0].contents) == 3):
        index1 = 1
    encoded1 = even_rows[i].findChildren()[0].contents[index1].encode('utf-8')#the innerhtml of second element of even_row
    string1 = str(encoded1)
    trimmed1 = replace_characters(' ', r'<b>',r'</b>', '\'', r'\n', 'b', string = string1, replacement = '')

    if(str(even_rows[i].findChildren()[1]) == r'<b>F (1)</b>'):
         index2 = 2
        
    encoded2 = even_rows[i].findChildren()[index2].contents[0].encode('utf-8')
    string2 = str(encoded2)
    trimmed2 = replace_characters(' ', '\'', r'\n', 'b', string = string2, replacement = '')
    
    school_days[trimmed2] = trimmed1


school_days = dict((k,v) for k,v in school_days.items() if not k[0].isalpha())

##prints school days
##for key, value in school_days.items():
##    print(key, value)
    
if date in school_days.keys():#checks to see if today is a school day
    day = school_days[date]
else:
    day = 'No School Today'
    print(day)

if(len(day)==1):
    if day == 'M':
        print('Today is Monday')
    elif day =='T':
        print('Today is Tuesday')
    elif day == 'W':
        print('Today is Wednesday')
    elif day == 'R':
        print('Today is Thursday')
    elif day == 'F':
        print('Today is Friday')
    day = 'Lab day 0'
    print('Today is lab day 0')


if day != 'No School Today' and day != 'Lab day 0':#if its a school day and not lab day 
    day_num = day[2:3]
    day_name = day[0:1]
    if day_name == 'M':
        print('Today is Monday')
    elif day_name =='T':
        print('Today is Tuesday')
    elif day_name == 'W':
        print('Today is Wednesday')
    elif day_name == 'R':
        print('Today is Thursday')
    elif day_name == 'F':
        print('Today is Friday')
    print('Day ' + day_num)

if day != 'No School Today' and day != 'Lab day 0': #if there is school and it is not lab day 0
    odd_rows = r4_soup.findAll('tr', class_='listrowodd')
    even_rows = r4_soup.findAll('tr', class_='listroweven')
    
    science_periods = dict()
    other_periods = dict()
    
    for i in range(0, len(odd_rows)-1):#parses summary to determine science/gym period
        if len(odd_rows[i].findChildren()[3].contents[0]) == 2:
            science_periods[odd_rows[i].findChildren()[3].contents[0]] = odd_rows[i].findChildren()[1].contents[0]
        elif len(odd_rows[i].findChildren()[3].contents[0]) == 3:
            other_periods[odd_rows[i].findChildren()[3].contents[0]] = odd_rows[i].findChildren()[1].contents[0]
    
    for i in range(6,12):#parses summary to determine science/gym period
        if len(even_rows[i].findChildren()[3].contents[0]) == 2:
            science_periods[even_rows[i].findChildren()[3].contents[0]] = even_rows[i].findChildren()[1].contents[0]
        elif len(even_rows[i].findChildren()[3].contents[0]) == 3:
            other_periods[even_rows[i].findChildren()[3].contents[0]] = even_rows[i].findChildren()[1].contents[0]
    
    science_periods_key = science_periods.keys()
    for key in science_periods_key:#every key in science_period_keys is a set of lab days
         if day_num in key:
             print('You have lab today: ' + science_periods[key])#access dictionary using keys
         else:
             print('No lab today')
