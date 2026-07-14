#q3
#a.
def calculate_tax(*salaries):
    try:
        tax=list(map(lambda x:(x*10)/100,salaries))
        sum_t=sum(tax)
        return sum_t
    except TypeError:
        print("Enter valid numeric salary")
    except Exception as e:
        print(e)
total_tax=calculate_tax(2000,3000,1000)
print(total_tax)
