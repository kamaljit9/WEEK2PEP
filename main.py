##question 6:
import student_utils
import json
students = []

for i in range(1, 4):
    print(f"\nStudent {i} :- ")  
    name = input("Name: ")

    try:
        m1 = float(input("Sub 1 Marks: "))
        m2 = float(input("Sub 2 Marks: "))
        m3 = float(input("Sub 3 Marks: "))

        for m in [m1, m2, m3]:
            if m < 0 or m > 100:
                raise ValueError("Marks b/w 0 and 100")

        # student_utils module ke functions sahi se call kiye
        avg = student_utils.calculate_avg(m1, m2, m3)
        grade = student_utils.get_grade(avg)

        students.append(
            {"name": name, "marks": [m1, m2, m3], "average": avg, "grade": grade}
        )

    except Exception as e:
        print(f"Error: {e}")
    

with open("report.txt","wt") as fh:
    for s in students:
        fh.write(f"Name: {s['name']} | Average: {s['average']:.2f} | Grade: {s['grade']}\n")
    
with open("students.json","wt") as fh:
    json.dump(students,fh,indent=4)

with open("students.json","rt") as fh:
    content=json.load(fh)

print(content)

print("\n=== Reading 'students.json' ===")
with open("students.json", "r") as json_file:
    print(json_file.read())

print("=== Reading 'report.txt' ===")
with open("report.txt", "r") as txt_file:
    lines = txt_file.readlines()
    for num, line in enumerate(lines, start=1):
        print(f"Line {num}: {line.strip()}")