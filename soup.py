from bs4 import BeautifulSoup
import requests
import csv

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

#Create the two dimensional list to add the fields values
list_row = soup.find_all('tr', class_='list_row')
number_of_courses = len(list_row)
fields_total_number = 17
courses = [[0] * fields_total_number for i in range(number_of_courses)]

#Use indexes for add data in the right place in our courses list
i,j=0,0
#Pull all the list row values
for tr_item in list_row:

    detailed_td_list = list(tr_item.stripped_strings)
    if len(detailed_td_list) == 9:
        detailed_td_list.insert(7, 'No Time') 
    for detail in detailed_td_list:
        courses[i][j] = detail
        print(i,j,detail)
        j += 1

    i += 1
    j = 0
    print("\n")

#Initialize index for add detailed values data in the right place in our courses list
i,j=0,10
#Pull all the courses details values
for td_item in soup.find_all('td', class_='detail_cell'):
     
    detail_cell_list = list(td_item.stripped_strings)
    if len(detail_cell_list) == 8:
        detail_cell_list.remove('Full') 
    for detail in detail_cell_list:
        courses[i][j] = detail
        print(i, j, detail)
        j += 1

    i += 1
    j = 10
    print("\n")

with open('data_csv.csv', 'w+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    #Write courses values in a csv file
    for idx in range(1, len(courses)):
        csv_writer.writerow(courses[idx])

csv_file.close()
html_file_to_parse.close()