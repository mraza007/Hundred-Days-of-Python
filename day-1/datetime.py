from datetime import datetime,date

"""
Its a simple program that will tell you how many day are left in christmas
"""

today = date.today()
christmas = (2018,12,25)
days = (christmas - today).days
print("There are " + str(days) + "left")
