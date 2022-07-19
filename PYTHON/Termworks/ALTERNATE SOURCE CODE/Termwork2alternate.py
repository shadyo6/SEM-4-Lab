def ReadSaveCourseData(SD):
    n=int(input("Enter no. of courses : "))
    for i in range(n):
        cCode=input("Enter course code : ")
        cInfo=[]
        cInfo.append(input("Enter course name : "))
        cInfo.append(input("Enter faculty name : "))
        cInfo.append(int(input("Enter no. of registrations : ")))
        SD[cCode] = cInfo
    return SD

def highReg(sd):
    maxReg = max(sd[key][2] for key in sd)
    valueList = list(sd.values())
    highestList = [x for x in valueList if maxReg in x]
    for i in range(len(highestList)):
        for j in range(len(highestList[i])):
            print(highestList[i][j])

def dispAssDetails(sd):
    try:
        cCode=input("Enter the course code : ")
        print("Course_code : ",cCode)
        print("Course_name : ",sd[cCode][0])
        print("Faculty_Name : ",sd[cCode][1])
        print("No. of registration : ",sd[cCode][2])
    except KeyError:
        print("Wrong key !!")


def dispAllDetails(sd):
    print()
    print("Course code\tCourse name\tFaculty name\tNo.of reg")
    for i in sd.keys():
        print(i,"\t     ",sd[i][0],"\t      ",sd[i][1],"\t      ",sd[i][2])
        
studDict = {}
studDict = ReadSaveCourseData(studDict)
print(studDict)
menuDict = {"1":highReg,"2":dispAssDetails,"3":dispAllDetails}

while 1:
    try:
        print("\n1: Course having highest registration\
             \n2: Display details of given course code\
            \n3: Display all course details\
            \n4: Exit")

        choice=input("Enter your choice :")
        if choice == "4":
            break

        menuDict[choice](studDict)

    except KeyError:
        print("Wrong key!! Try again")
