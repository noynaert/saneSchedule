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

def remove_field_name(expression, field_name):
    if(expression.startswith(field_name)):
        expression = expression.replace(field_name, '')
        expression = expression.strip()
    return expression

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
        detail = remove_field_name(detail, 'Maximum Enrollment:')
        detail = remove_field_name(detail, 'Section Seats Available:')
        detail = remove_field_name(detail, 'ADDITIONAL FEE:')
        detail = remove_field_name(detail, 'Course Begins:')
        detail = remove_field_name(detail, 'Course Ends:')
        courses[i][j] = detail
        print(i, j, detail)
        j += 1

    i += 1
    j = 10
    print("\n")


field_names = ['CRN', 'Course', 'Sec', 'Type', 'Title', 'Hrs', 'Days', 'Times', 'Room', 'Instructor', 'Maximum Enrollment', 'Section Seats Available', 'Course Details', 'ADDITIONAL FEE', 'Special Note', 'Course Begins', 'Course Ends']
with open('data_csv.csv', 'w+', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = field_names)
    csv_writer.writeheader()

    #Write courses values in a csv file
    for row_idx in range(0, len(courses)):

        #Start by removing special char
        for column_idx in range(0, len(courses[row_idx])):
            field_value = courses[row_idx][column_idx].replace('\t', '')
            field_value = field_value.replace('\xa0', '')
            courses[row_idx][column_idx] = field_value
            
        csv_writer.writerow({field_names[0]:courses[row_idx][0], field_names[1]:courses[row_idx][1],field_names[2]:courses[row_idx][2],
                            field_names[3]:courses[row_idx][3], field_names[4]:courses[row_idx][4], field_names[5]:courses[row_idx][5],
                            field_names[6]:courses[row_idx][6], field_names[7]:courses[row_idx][7], field_names[8]:courses[row_idx][8],
                            field_names[9]:courses[row_idx][9], field_names[10]:courses[row_idx][10], field_names[11]:courses[row_idx][11],
                            field_names[12]:courses[row_idx][12],field_names[13]:courses[row_idx][13],field_names[14]:courses[row_idx][14],
                            field_names[15]:courses[row_idx][15],field_names[16]:courses[row_idx][16]})

csv_file.close()
html_file_to_parse.close()