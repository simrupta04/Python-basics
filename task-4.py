n = int(input("Please enter the number of students records:"))
student_marks = {}
for _ in range(n):
        name, *line = input("Enter the names and marks obtained by a student::").split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input("enter the name of a student to find the average score:: ")
lis = student_marks.get(query_name)
sum = 0
for i in lis:
        sum = sum + i
print("The average of the marks obtained by "+query_name+  ":: %.2f"% (sum/3))