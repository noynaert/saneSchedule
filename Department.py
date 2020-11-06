from enum import Enum

class Department(Enum):
    ALL = 0
    BIO = 1
    BUS = 2
    CHE = 3
    COM = 4
    CSMP = 5
    CJLG = 6
    EDU = 7
    ET = 8
    FIN = 9
    HP = 10
    HON = 11
    MIL = 12
    NURS = 13
    PSY = 14
    SSH = 15

    def __str__(self):
        description = ''
        if(self.value == 1):
            description = "Biology"
        if(self.value == 2):
            description = "Business"
        if(self.value == 3):
            description = "Chemistry"
        if(self.value == 4):
            description = "Communication"
        if(self.value == 5):
            description = "Comp Science, Math & Physics"
        if(self.value == 6):
            description = "Crim Justice & Legal Studies"
        if(self.value == 7):
            description = "Education"
        if(self.value == 8):
            description = "Engineering Technology"
        if(self.value == 9):
            description = "Fine Arts"
        if(self.value == 10):
            description = "Health Professions"
        if(self.value == 11):
            description = "Honors Program"
        if(self.value == 12):
            description = "Military Science"
        if(self.value == 13):
            description = "Nursing"
        if(self.value == 14):
            description = "Psychology"
        if(self.value == 15):
            description = "Social Sciences & Humanities"

        return description