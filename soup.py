from bs4 import BeautifulSoup
import requests

# Get the html 
def send_request(base_url, department):
    post_data = dict(course_numbr='', subject='ALL', department=department, display_closed='yes', course_type='all')
    response = requests.post(base_url, data = post_data)
    return response.text

def set_base_url(year, semester):
    if(semester == "fall"):
        semester_code = 10
    if(semester == "spring"):
        semester_code = 20
    if(semester == "summer"):
        semester_code = 30  
    
    return f"https://aps4.missouriwestern.edu/schedule/Default.asp?tck={year}{semester_code}"

base_url = set_base_url(2021, "fall")
html_file = "post_request_file.html"

#Create the html file to parse and get data
html_file_to_parse = open(html_file, 'w+')
#File that file with content from http post request
file_content = send_request(base_url, "HON")
html_file_to_parse.write(file_content)

#Declare a beautifulsoup instance
soup = BeautifulSoup(file_content,'lxml')

for tr_item in soup.find_all('tr', class_='list_row'):

    detailed_td_list = list(tr_item.stripped_strings)
    if len(detailed_td_list) == 9:
        detailed_td_list.insert(7, 'No Time') 
    for detail in detailed_td_list:
        print(detail)

    print("\n")

for td_item in soup.find_all('td', class_='detail_cell'):
     
    detail_cell_list = list(td_item.stripped_strings)
    if len(detail_cell_list) == 8:
        detail_cell_list.remove('Full') 
    for detail in detail_cell_list:
        print(detail)

    print("\n")

html_file_to_parse.close()