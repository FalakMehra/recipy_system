import pymysql

def Connect():
    c=pymysql.connect( host="localhost",
                       user="root",
                       password="System@2023",
                       database="project_july"
    )
    return c

def verify(email):
    if '.' in email and '@' in email:
        return 'Valid'
    else:
        return 'Invalid'

def check(mobile):
    if len(mobile)==10:
        if mobile[0] in '6789':
            return 'Valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'