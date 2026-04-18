import numpy as np
import matplotlib.pyplot as plt

number_students = int(input("Enter how many students you want to enter: "))
students = []

for i in range(number_students):
    name = input("Enter student name: ")
    students.append(name)

number_subjects = int(input("Enter how many subjects: "))
subject = []

for i in range(number_subjects):
    sub = input("Enter subject name: ")
    subject.append(sub)

data = {}

for student in students:
    marks = []
    print("\nEnter marks for", student)

    for sub in subject:
        num = int(input(f"Enter marks in {sub}: "))
        marks.append(num)

    data[student] = marks

print("\n--- STATISTICS ---")

totals = []
clean_totals = []

for student, marks in data.items():
    arr = np.array(marks)

    print("\n", student)
    print("Marks:", arr)

    mean = np.mean(arr)
    std = np.std(arr)

    print("Mean:", mean)
    print("Std:", std)

    max_index = np.argmax(arr)
    min_index = np.argmin(arr)

    print("Max in", subject[max_index], "=", arr[max_index])
    print("Min in", subject[min_index], "=", arr[min_index])

    if std == 0:
        print("No outliers")
        clean = arr
    else:
        z = (arr - mean) / std
        out = arr[np.abs(z) > 1]
        ind = np.where(np.abs(z) > 1)[0]

        if len(out) == 0:
            print("No outliers")
            clean = arr
        else:
            print("Outliers:", out)
            print("Subjects:", [subject[i] for i in ind])

            clean = []
            for i in range(len(arr)):
                if abs(z[i]) <= 1:
                    clean.append(arr[i])

    totals.append(sum(arr))
    clean_totals.append(sum(clean))

colors = ["green" if t == max(clean_totals) else "blue" for t in clean_totals]

plt.bar(students, clean_totals, color=colors)
plt.title("Student Marks Comparison (Outliers Removed)")
plt.show()

all_marks = []

for student, marks in data.items():
    arr = np.array(marks)
    mean = np.mean(arr)
    std = np.std(arr)

    if std == 0:
        for m in arr:
            all_marks.append(m)
    else:
        z = (arr - mean) / std
        for i in range(len(arr)):
            if abs(z[i]) <= 1:
                all_marks.append(arr[i])

plt.hist(all_marks, bins=5)
plt.title("Marks Distribution (Without Outliers)")
plt.show()