from enum import Enum

class Subject(Enum):
    ALL = 0
    ACC = 1
    ALH = 2
    ACT = 3
    MAS = 4
    ART = 5
    BIO = 6
    CHE = 7
    CIN = 8
    CLS = 9
    COM = 10
    CSC = 11
    CET = 12
    CED = 13
    LAW = 14
    ESC = 15
    ECO = 16
    EDU = 17
    EET = 18
    EGT = 19
    ENG = 20
    ETC = 21
    ENT = 22
    FIN = 23
    GBA = 24
    GEO = 25
    HDA = 26
    HIF = 27
    HIS = 28
    HON = 29
    HUM = 30
    MIM = 31
    JOU = 32
    LDR = 33
    LAT = 34
    MGT = 35
    MET = 36
    MKT = 37
    MAT = 38
    MTE = 39
    MIL = 40
    MUS = 41
    NUR = 42
    PHL = 43
    PED = 44
    PTA = 45
    PHY = 46
    POL = 47
    PSC = 48
    PSY = 49
    RDG = 50
    RSM = 51
    REL = 52
    SWK = 53
    SOC = 54
    SPA = 55
    SFM = 56
    SCM = 57
    TSL = 58
    THR = 59
    UNV = 60
    
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