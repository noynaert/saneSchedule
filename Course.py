class Course: 

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
        self.course_enrollment = {}
        self.course_description = ''
        self.course_messages = []
        self.course_term = []
        self.course_dates = {}
    
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
