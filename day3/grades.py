
def grades_file():
    try:
        fl = open("grades.txt", "w")
        fl.write("1,Python,85\n")
        fl.write("2,Python,90\n")
        fl.write("5,Python,88\n")
        fl.write("4,Python,90\n")
        fl.write("1,Math,90\n")
        fl.write("2,programming,78\n")
        fl.write("2,c++,88\n")
        fl.write("3,HTML,95\n")
        fl.write("3,CSS,70\n")
        fl.close()
        print("grades.txt created")

    except:
        print("error creating grades.txt")


def show_grades():
    try:
        fl = open("grades.txt", "r")
        print("Grades python:")
        for line in fl:
            parts = line.split(",")
            if parts[1] == "Python":
                print(" ID:", parts[0], ", Grade:", parts[2])
        fl.close()

    except:
        print("error reading file")


def student_grades(student_id):
    try:
        fl = open("grades.txt", "r")
        print("Grades:")
        for line in fl:
            parts = line.split(",")
            if parts[0] == student_id:
                print(parts[1], ":", parts[2])
        fl.close()

    except:
        print("error reading file")


def average():
    try:
        grades_dict = {}

        fl = open("grades.txt", "r")
        for line in fl:
            parts = line.split(",")
            student_id = parts[0]
            grade = int(parts[2])

            if student_id not in grades_dict:
                grades_dict[student_id] = []
            grades_dict[student_id].append(grade)
        fl.close()

        print("Average Grades:")
        for student_id in grades_dict:
            total = sum(grades_dict[student_id])
            average = total / len(grades_dict[student_id])
            print("ID:", student_id, ", average:", round(average, 2))

    except:
        print("error calculate average")