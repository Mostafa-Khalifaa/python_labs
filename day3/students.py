
def students_file():
    try:
        fl = open("students.txt", "w")
        fl.write("1,mostafa mohsen\n")
        fl.write("2,Ahmed Ali\n")
        fl.write("3,Sara Mohamed\n")
        fl.write("4,Omar Hassan\n")
        fl.write("5,khalid ahmed\n")
        fl.close()
        print("students.txt created")

    except:
        print("error creating students.txt")


def show_students():
    try:
        fl = open("students.txt", "r")
        print("Students:")
        for line in fl:
            parts = line.split(",")
            print(" ID:", parts[0], ", Name:", parts[1])
        fl.close()

    except:
        print(" error open students.txt")

def find_student(student_id):
    try:
        name = ""
        fl = open("students.txt", "r")
        for line in fl:
            parts = line.split(",")
            if parts[0] == student_id:
                name = parts[1]
        fl.close()
        return name

    except:
        print("error open file students.txt")