class Course:

    crn = -1
    course = ''
    sec = -1
    type = ''
    title = ''
    hours = -1
    days = ''
    times = ''
    room = ''
    instructor = ''
    course_seats = []
    course_description = ''
    course_messages = []
    course_term = []
    course_dates = []    

    def __init__(self, crn = -1, course = '', sec = -1, type = '', title = '', hours = -1, days = '', times = '', room = '', instructor = ''):
        self.crn = crn
        self.course = course
        self.sec = sec
        self.type = type
        self.title =title
        self.hours = hours
        self.days = days
        self.times = times
        self.room = room
        self.instructor = instructor
    
    def setup_course(self,crn, course, sec, type, title, hours, days, times, room, instructor):
        self.crn = crn
        self.course = course
        self.sec = sec
        self.type = type
        self.title =title
        self.hours = hours
        self.days = days
        self.times = times
        self.room = room
        self.instructor = instructor

    def convert_to_dictionary(self):
        result = {
            "CRN": self.crn,
            "Course": self.course,
            "Sec": self.sec,
            "Type": self.type,
            "Title": self.title,
            "Hrs": self.hours,
            "Days": self.days,
            "Times": self.times,
            "Room": self.room,
            "Instructor": self.instructor
        }

        return result
