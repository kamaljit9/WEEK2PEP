def get_grade(avg,pass_mark=40):
    if avg<pass_mark:
        return "F"
    elif avg>=80:
        return "A"
    elif avg>=60<80:
        return "B"
    elif avg>=40<60:
        return "C"
def calculate_average(*marks):
    avg=sum(marks)/len(marks)
    return avg

#print(get_grade(calculate_average(30,40,60)))
