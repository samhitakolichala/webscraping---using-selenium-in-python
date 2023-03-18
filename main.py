
## importing libraries

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

##pip install webdriver

## options
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


## creating webdriver instance

wd=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

## get the main page

wd.get("https://www.wikipedia.org/")


## assertion statement

assert "Wikipedia" in wd.title

# print the entire html

#print(wd.page_source)

#fetching the element by ID
input_element=wd.find_element(by=By.ID,value="searchInput")

#sending keys

input_element.send_keys('ASD')

# fetch search button through the CSS class name

search=wd.find_element(by=By.CLASS_NAME,value="pure-button")

## click the search button

wd.execute_script("arguments[0].click()",search)

print(wd.page_source)

## switching the windows

window_after=wd.window_handles[0]
wd._switch_to.window(window_after)

## assertion statement

assert "ASD - Wikipedia" in wd.title

#printing the title

print("Successfully loaded the page ",wd.title)


# fetch search button through the link text

link_text=wd.find_element(By.LINK_TEXT,"Adaptive software development")

#clicking the link

wd.execute_script("arguments[0].click();",link_text)

# switching the window

window_after=wd.window_handles[0]
wd.switch_to.window(window_after)

## assertion statement

assert "Adaptive software development - Wikipedia" in wd.title

## printing the title

print("Successfully loaded the page ",wd.title)

## fetch all the elements with <p> tags

p_tags=wd.find_elements(by=By.TAG_NAME,value="p")

## printing the array with <p> tag elements

print("Number of tags found:",len(p_tags))
# extract text from all elements
text_lines=""

for p_tag in p_tags:
    text_lines=text_lines+p_tag.text

print(text_lines)

## match all the digits  occuring in squared brackets in the string and replace them with an empty string

pattern=r'\[[0-9]\]'
new_string=re.sub(pattern,'',text_lines)
print(new_string)


elems=wd.find_elements(by=By.CSS_SELECTOR,value=' p > a ')

# creating a dictionary

link_dict={}
for elem in elems:
    link_dict[elem.text]=elem.get_attribute('href')
print(link_dict)










