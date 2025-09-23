import csv

print("College Catalog Search - Credit To University Of Illinois Urbana Champaign")

courseInput = input("\nWhat course are you looking for?\n")
results = []

with open('course-catalog.csv') as csvFile:
    reader = csv.reader(csvFile)
    header = next(reader)
    
    courseIndex = header.index("Name")
    
    for row in reader:
        if courseInput.lower() in row[courseIndex].lower():
            results.append(row[courseIndex])

print("\nAll courses containing keyword \"" + courseInput + "\"")
count = 0

attempts0 = 100

if not results:
    print("No Results Found. Please consider a different keyword")
else:
    for result in results:
        print("[" + str(count + 1) + "] " + result)
        count += 1

selectionIndex = 0

attempts1 = 1000000

while attempts1 > 0:
    try:
        selectionIndex = int(input("Select: [1 - " + str(count) + "]"))
        course = results[selectionIndex - 1]
        attempts1 = attempts1 - 1000000 
    except (TypeError, IndexError):
        print("Please Enter A Valid Number")
        continue

description = ""
creditHours = 0
degreeAttributes = ""
enrollmentType = "" 
courseType = ""

with open('course-catalog.csv') as csvFile:
    reader = csv.reader(csvFile)
    header = next(reader)
    
    courseIndex = header.index("Name")
    descIndex = header.index("Description")
    hourIndex = header.index("Credit Hours")
    attributeIndex = header.index("Degree Attributes")
    enrollmentIndex = header.index("Enrollment Status")
    typeIndex = header.index("Type")
    
    for row in reader:
        if row[courseIndex] == course:
            description = row[descIndex]
            creditHours = row[hourIndex]
            degreeAttributes = row[attributeIndex]
            enrollmentType = row[enrollmentIndex]
            courseType = row[typeIndex]
        
print("\nWhat information would you like to know about the " + course + "?\n")

possibleArray = ["Course Description", "Hours Credited From Course", "The Degree This Course Is Attributed To", "The Enrollment Status Of The Course", "The Type Of The Course"]

count2 = 0

for poss in possibleArray:
    print("[" + str(count2 + 1) + "] " + poss)
    count2 += 1

attempts2 = 1000000

while attempts2 > 0:
    try:
        selectionIndex2 = int(input("Select: [1 - " + str(count2) + "]"))
        attempts2 = attempts2 - 1000000
    except (ValueError, IndexError):
        print("Please Enter A Valid Number")
        continue


if(selectionIndex2 == 1):
    print(description)
elif(selectionIndex2 == 2):
    print(str(creditHours))
elif(selectionIndex2 == 3):
    print(degreeAttributes)
elif(selectionIndex2 == 4):
    print(enrollmentType)
elif(selectionIndex2 == 5):
    print(courseType)