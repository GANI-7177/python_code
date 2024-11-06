def grade(m): return "A+" if m >= 90 else "A" if m >= 80 else "B+" if m >= 70 else "B" if m >= 60 else "C" if m >= 50 else "D" if m >= 40 else "F"

for _ in range(int(input("Number of students: "))):
    name, marks = input("Name: "), float(input("Marks: "))
    print(f"{name} - Marks: {marks}, Grade: {grade(marks)}")
