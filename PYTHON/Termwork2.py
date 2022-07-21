def add(Courses):
    code,cname,fname,regs = input("Enter Code,Coursename,faculty,no_of_regs: ").split(',')
    regs = int(regs)
    if code in Courses:
        print("Duplicates are not allowed")
    else:
        Courses[code] = [cname,fname,regs]

def dispAll(Courses):
    if len(Courses) == 0:
        print("Courses dictionary is empty")
    else:
        for code,details in Courses.items():
            print(code,details[0],details[1],details[2])

def disp(Courses):
    ccode = input("Enter course code to display: ")
    if ccode in Courses:
        print(ccode, Courses[ccode])
    else:
        print("Course not present")
        
def highest(Courses):
    if len(Courses) == 0:
        print("Courses dictionary is empty")
        return
    max = 0
    for code,details in Courses.items():
        if details[2] > max:
            max = details[2]

    hCourses = []
    for code,details in Courses.items():
        if details[2] == max:
            hCourses.append([code,details])
    print("Course with highest registration:\n", hCourses)

def main():
    Courses = {}
    while True:
        opt = int(input("1: CourseAdd 2: DisplayCourse 3: DispAll 4: Highest 5:Exit \nEnter your optiion:"))

        if opt == 1:
            add(Courses)
        elif opt == 2:
            disp(Courses)
        elif opt == 3:
            dispAll(Courses)
        elif opt == 4:
            highest(Courses)
        elif opt == 5:
            exit()
        else:
            print("Invalid option")
            break
if __name__=='__main__':
  main()
