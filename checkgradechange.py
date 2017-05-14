from login import *
from utility import *

u_tags = r5_soup.findAll('u')
string_u_tags = [str(item) for item in u_tags]

trimmed_u_tags = []
for item in string_u_tags:
     trimmed_u_tags.append(replace_characters(' ', '\'', '\n', r'<u>', r'</u>',string = item, replacement = ''))






