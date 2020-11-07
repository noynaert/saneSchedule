from bs4 import BeautifulSoup
from Department import Department
from Subject import Subject
from CourseType import CourseType
from Course import Course
import requests
import json

class SoupHandler:

    course_number = ''
    department = Department.ALL
    subject = Subject.ALL
    display_closed = 'yes'
    course_type = CourseType.ALL
    base_url = ''
    semester = ''
    year = 0

    courses_list = []
    
    def __init__(self, semester, year):
        if(semester == "fall"):
            semester_code = 10
        if(semester == "spring"):
            semester_code = 20
        if(semester == "summer"):
            semester_code = 30  
        self.base_url = f"https://aps4.missouriwestern.edu/schedule/Default.asp?tck={year}{semester_code}"
        self.year = year
        self.semester = semester
        
    def setup_soup_handler(self, course_number, department, subject, display_closed, course_type):
        self.course_number = course_number
        self.display_closed = display_closed
        self.courses_list = []
        if(department != None):
            for dpt in Department:
                if dpt.name == department:
                    self.department = dpt

        if(subject != None):
            for sbj in Subject:
                if sbj.name == subject:
                    self.subject = sbj
        
        if(course_type != None):
            for crse_type in CourseType:
                if crse_type.name == course_type:
                    self.department = crse_type


    # Get the html 
    def send_request(self):
        post_data = dict(course_numbr=self.course_number, subject=self.subject.name, department=self.department.name, display_closed=self.display_closed, course_type=self.course_type.name)
        response = requests.post(self.base_url, data = post_data)
        return response.text

    def remove_field_name(self, expression, field_name):
        if(expression.startswith(field_name)):
            expression = expression.replace(field_name, '')
            expression = expression.strip()
        return expression

    def get_info_from_class(self, soup, class_name):

        course_idx = 0
        #Pull all the data from a specific class and fill the Course's instances
        for class_item in soup.find_all(class_= class_name):
            
            detail_cell_list = list(class_item.stripped_strings)

            additional_info_idx = 1 
            for detail in detail_cell_list:
                detail = detail.replace('\t', '')
                detail = detail.replace('\xa0', '')
                detail_in_list = detail.split(':')
                for piece_idx in range(0, len(detail_in_list)):
                    detail_in_list[piece_idx] = detail_in_list[piece_idx].strip()
                
                if(len(detail_in_list) == 2):
                    if(class_name == "course_enrollment"):
                        self.courses_list[course_idx].course_enrollment.update({detail_in_list[0]:detail_in_list[1]})
                    if(class_name == "course_messages"):
                        self.courses_list[course_idx].course_messages.append(dict({detail_in_list[0]:detail_in_list[1]}))
                    if(class_name == "course_term"):
                        self.courses_list[course_idx].course_term.append(dict({detail_in_list[0]:detail_in_list[1]}))
                    if(class_name == "course_dates"):
                        self.courses_list[course_idx].course_dates.update({detail_in_list[0]:detail_in_list[1]})
                else:
                    if(class_name == "course_enrollment"):
                        self.courses_list[course_idx].course_enrollment.update({f"Additional Info {additional_info_idx}": detail_in_list[0]})
                    if(class_name == "course_messages"):
                        self.courses_list[course_idx].course_messages.append(dict({f"Additional Info {additional_info_idx}": detail_in_list[0]}))
                    if(class_name == "course_term"):
                        self.courses_list[course_idx].course_term.append(detail_in_list[0])
                    if(class_name == "course_dates"):
                        self.courses_list[course_idx].course_dates.update({f"Additional Info {additional_info_idx}": detail_in_list[0]})
            
            course_idx +=1

    def proceed_scrapping(self):
        
        html_file = "post_request_file.html"

        #Create the html file to parse and get data
        html_file_to_parse = open(html_file, 'w+')
        #File that file with content from http post request
        file_content = self.send_request()
        html_file_to_parse.write(file_content)

        #Declare a beautifulsoup instance
        soup = BeautifulSoup(file_content,'lxml')

        #Create the two dimensional list to add the fields values
        list_row = soup.find_all('tr', class_='list_row')
        number_of_courses = len(list_row)
        
        fields_total_number = 17
        courses = [[0] * fields_total_number for i in range(number_of_courses)]

        #Use indexes for add data in the right place in our courses' list
        i,j=0,0
        #Pull all the list row values
        for tr_item in list_row:

            detailed_td_list = list(tr_item.stripped_strings)
            if len(detailed_td_list) == 9:
                detailed_td_list.insert(7, 'No Time') 
            for detail in detailed_td_list:
                courses[i][j] = detail
                j += 1

            i += 1
            j = 0

        #Declare then initialize list of instances of Course
        for crse_idx in range(number_of_courses):
            self.courses_list.append(Course(courses[crse_idx][0], courses[crse_idx][1], courses[crse_idx][2], courses[crse_idx][3], courses[crse_idx][4], courses[crse_idx][5], courses[crse_idx][6], courses[crse_idx][7], courses[crse_idx][8], courses[crse_idx][9]))

        self.get_info_from_class(soup, 'course_enrollment')
        self.get_info_from_class(soup, 'course_messages')
        self.get_info_from_class(soup, 'course_term')
        self.get_info_from_class(soup, 'course_dates')

        i=0
        #Pull all the list row values
        for detail_cell_item in soup.find_all('td', class_='detail_row'):
            detailed_td_list = list(detail_cell_item.stripped_strings)

            description = detailed_td_list[len(self.courses_list[i].course_enrollment)]
            description = description.replace('\t', '')
            description = description.replace('\xa0', '')
            description = description.strip()
            self.courses_list[i].course_description = description
            i +=1
    
        list_of_dictionaries = []
        for course_idx in range(0, len(self.courses_list)):
            list_of_dictionaries.append(self.courses_list[course_idx].__dict__)

        html_file_to_parse.close()
        return list_of_dictionaries