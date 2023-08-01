total_days = int(input("total number of working days"))
total_absent = int(input("number of days Absent"))
present = total_days - total_absent
percentage = (present/total_days)*100
if(percentage>75):
    print("you are able to sit in exams")
else:
    print("you are not able to sit in exams")