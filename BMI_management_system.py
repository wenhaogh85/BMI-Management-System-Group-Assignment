"""
Members:
1) Ahsan
2) Zheng Yang
3) Wen Hao
"""

from functools import reduce

patients = [{
     'name': 'Muhammad',
     'gender': 'Male',
     'weight': 90.0,
     'height': 1.62
 }, {
     'name': 'Luther',
     'gender': 'Male',
     'weight': 70.0,
     'height': 1.7
 }, {
     'name': 'Lucy',
     'gender': 'Female',
     'weight': 75.0,
     'height': 1.6
 }, {
     'name': 'Wen Hao',
     'gender': 'Male',
     'weight': 54.0,
     'height': 1.67
 }, {
     'name': 'Ahsan',
     'gender': 'Male',
     'weight': 62.0,
     'height': 1.83
 }, {
     'name': 'Zheng Yang',
     'gender': 'Male',
     'weight': 73.0,
     'height': 1.81
 }, {
     'name': 'Natalie',
     'gender': 'Female',
     'weight': 55.0,
     'height': 1.55
 }, {
     'name': 'Chun Li',
     'gender': 'Female',
     'weight': 57.0,
     'height': 1.63
 }]

# ---------------------------------------------------

# displays main menu
def mainMenu():
    print(
    "\n========================================" +
    "\nBMI calculator" +
    "\n========================================" +
    "\nPlease enter one of the following option" +
    "\n+---------+-----------------+" +
    "\n| Option  |  Function       |" +
    "\n+---------+-----------------+" +
    "\n|    1    | Add new patient |" +
    "\n+---------+-----------------+" +
    "\n|    2    | Calculate BMI   |" +
    "\n+---------+-----------------+" +
    "\n|    3    | Search patient  |" +
    "\n+---------+-----------------+" +
    "\n|    4    | Exit program    |" +
    "\n+---------+-----------------+"
    )

    choice = input("\nEnter choice: ")

    return choice

# gets option to select gender
def selectGender():

    print(
    "\nSelect one of the options:" +
    "\n1 for Male" +
    "\n2 for Female"
    )

    option = input("Enter option: ")

    return option

# creates and returns a patient profile in a dictionary
def createPatient(name, gender, weight, height):

    return {
        "name" : name,
        "gender" : gender,
        "weight" : weight,
        "height" : height
    }

# prompts user to create a profile for a patient
def processChoice1():

    name = input("\nEnter patient name: ")
    gender = "Male" if selectGender() == "1" else "Female"
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (meter): "))

    newpatient = createPatient(name, gender, weight, height)

    patients.append(newpatient)

    print("\nNew patient added to database")

# creates a function to be implemented by filter function
def createFilter(key, value):

    def filterBy(patient):
        return patient[key] == value

    return filterBy

# creates functions to filter by gender which will be implemented by filter function
isFemale = createFilter("gender", "Female")
isMale = createFilter("gender", "Male")

# redefines and returns patient profile to include name and BMI value
def patientBMI(patient, function):

    bmi = function(patient)

    return {
        "name" : patient["name"],
        "BMI" : bmi
    }

# calculates patient's BMI value and round it off to 2 decimal places
def calculateBMI(patient):

    DECIMAL_PLACES = 2

    return round(patient["weight"] / (patient["height"] ** 2), DECIMAL_PLACES)

# displays messages to user based on the patient's BMI value
def bmiCategory (bmi):

    message = "BMI category: "

    if bmi <= 18.5: return message + "Underweight"
    elif bmi <= 25.0: return message + "Normal"
    else: return message + "Overweight"

# displays advices to user based on the patient's BMI value
def bmiAdvice(bmi):

    message = "\nAdvice:\n"

    if bmi <= 18.5: return message + "- Eat more frequently\n- Choose nutrient-rich foods"
    elif bmi <= 25.0: return message + "- Exercise regularly and keep fit"
    else: return message + "- Exercise regularly\n- Follow a healthy-eating plan"

# sums up all the patient's BMI value and returns the output
def totalPatientsBMI(allPatientBMI):
    return reduce(lambda bmi, acc: bmi + acc, allPatientBMI)

# calculates average value of all patient's BMI value and return the output
def averagePatientsBMI(totalPatientsBMI, allPatientBMI):
    return totalPatientsBMI / len(allPatientBMI)

# caculates BMI values for either all patients or males or females based on user input
def processChoice2():

    print(
    "\nSelect one of the options to calculate BMI for:" +
    "\n1 All patients" +
    "\n2 Male patients " +
    "\n3 Female patients "
    )

    option = input("Enter option: ")

    if option == "1":
        allPatientNameAndBMI = list(map(lambda patient: patientBMI(patient, calculateBMI), patients))
        allPatientBMI = list(map(lambda patient: patient["BMI"], allPatientNameAndBMI))

        print("BMI for all Patients:", allPatientBMI)

        totalBMI = totalPatientsBMI(allPatientBMI)

        averageBMI = averagePatientsBMI(totalBMI, allPatientBMI)

        print("Average BMI values for all patients:", round(averageBMI, 2))

    elif option == "2":
        malePatients = list(filter(isMale, patients))
        malesBMI = [patientBMI(male, calculateBMI) for male in malePatients]
        printPatient(malesBMI)

    elif option == "3":
        femalePatients = list(filter(isFemale, patients))
        femalesBMI = [patientBMI(female, calculateBMI) for female in femalePatients]
        printPatient(femalesBMI)

    else:
        print("Invalid input!")

# applies a list of functions to the patients argument
def functions_apply(bmi, functions):
    return [function(bmi) for function in functions]

# creates a list of functions to categories and give advice based on BMI values
functions = [
    bmiCategory,
    bmiAdvice
]

# prints patient name and BMI value by recusively shrinking the list
def printPatient(patients):

    if len(patients) == 0:
        return
    
    print("\nName: {} \nBMI: {}".format(patients[0]["name"], patients[0]["BMI"]))

    return printPatient(patients[1:])

# prints patient profile
def printPatientDetails(patient):

    print("\nName: {}\nGender: {}\nWeight:{} \nHeight: {}".format(patient["name"], patient["gender"], patient["weight"], patient["height"]))

# finds patient name recursively (using recursive leap of faith)
def find_patient(patients, name):

    """"
    recursively find patient by name until list is empty
    """

    # base case: Exits function when list is empty
    if len(patients) == 0:
        return None

    # checks if patient name matches what user want to find using key value
    elif patients[0]["name"] == name:
        return patients[0]

    # recursively shrink the list by one element at a time until it is empty
    return find_patient(patients[1:], name)

# finds patient by name, calculate BMI value, categorise BMI value, and provide advices based on BMI value
def processChoice3():

    name = input("Search name: ")

    patient = find_patient(patients, name)

    if patient == None:
        print("Patient not found")
    else:
        printPatientDetails(patient)

        bmi = calculateBMI(patient)

        results = functions_apply(bmi, functions)

        for result in results:
            print(result)

# recusively controls the flow of the program
def looping():

    choice = mainMenu()

    if choice == "1":
        processChoice1()
        looping()
    elif choice == "2":
        processChoice2()
        looping()
    elif choice == "3":
        processChoice3()
        looping()
    elif choice == "4":
        return
    else:
        print("\nPlease choose option 1 to 4 only!")
        looping()

#-----------------------------------------
# starts the main program
looping()