from enum import Enum

class CourseType(Enum):
    ALL = 0
    GRADUATE = 1
    HONORS_ALL = 2
    HONORS_GS = 3
    WEEKEND = 4
    NIGHT = 5
    KC_NORTHLAND = 6
    PENN_VALLEY = 7
    STUDY_AWAY = 8
    OFF_SCHEDULE = 9
    WEEK8 = 10
    DISTANCE_ED = 11
    WINTER_SESSION = 12
    ONLINE_100 = 13
    ONLINE_70_99 = 14
    ONLINE_1_69 = 15
    ONLINE_8WEEK = 16

    def __str__(self):
        description = ''
        if(self.value == 1):
            description = "Graduate Level"
        if(self.value == 2):
            description = "All Honors"
        if(self.value == 3):
            description = "General Studies Honors"
        if(self.value == 4):
            description = "Weekend"
        if(self.value == 5):
            description = "Night (After 4:30pm)"
        if(self.value == 6):
            description = "KC Northland"
        if(self.value == 7):
            description = "Penn Valley Campus"
        if(self.value == 8):
            description = "Study Away"
        if(self.value == 9):
            description = "Off-Schedule"
        if(self.value == 10):
            description = "8-Week On Campus"
        if(self.value == 11):
            description = "Distance Education (all)"
        if(self.value == 12):
            description = "Winter Session"
        if(self.value == 13):
            description = "Online 100%"
        if(self.value == 14):
            description = "Online 70-99%"
        if(self.value == 15):
            description = "Online 1-69%"
        if(self.value == 16):
            description = "8-Week Online"
        
        return description