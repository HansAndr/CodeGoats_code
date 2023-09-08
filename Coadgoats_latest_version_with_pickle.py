#Import module pickle to serialize and deserialize objects
import pickle 

#Import module os to read and write files
import os




#Create an empty list to store objects of the Office class.
office_list = []

#Create an dictionary to store the names of employees (keys) and their IDs (values).
dict_employees = {}




#Create an Office class
class Office: 


    #This __init__ function is used to initialize the attributes of the object and takes arguments:
    #office_name: The name of the office and capacity: The capacity of the office.
    #The __init__ function first sets the office_name attribute to the value of the office_name argument. 
    #Then, the __init__ function calls the set_places() method. 
    def __init__(self, office_name, capacity):
        self.office_name = office_name
        self.Monday = self.set_places(capacity)
        self.Tuesday = self.set_places(capacity)
        self.Wednesday = self.set_places(capacity)
        self.Thursday = self.set_places(capacity)
        self.Friday = self.set_places(capacity)
        self.Saturday = self.set_places(capacity)
        self.Sunday = self.set_places(capacity)


    #This method creates a list of the specified capacity for each weekday.
    #It takes capacity, the capacity of the office, as an argument.
    def set_places(self, capacity):                 
        seats_in_office = [None] * int(capacity)
        return seats_in_office
    

    #This method takes weekday (integer) as an argument.
    #The method first checks if the value of the weekday argument is between 1 and 7. 
    #If it is, the method returns the number of empty places in the office on that weekday. 
    #Otherwise, the method returns None.
    def get_empty_places(self, weekday):
        if weekday == 1:
            empty_places = self.Monday.count(None)
            return empty_places
        if weekday == 2:
            empty_places = self.Tuesday.count(None)
            return empty_places
        if weekday == 3:
            empty_places = self.Wednesday.count(None)
            return empty_places
        if weekday == 4:
            empty_places = self.Thursday.count(None)
            return empty_places
        if weekday == 5:
            empty_places = self.Friday.count(None)
            return empty_places
        if weekday == 6:
            empty_places = self.Saturday.count(None)
            return empty_places
        if weekday == 7:
            empty_places = self.Sunday.count(None)
            return empty_places
        

    #This method takes name (string) and weekday (integer) as arguments.
    #The method first checks if the value of the weekday argument is between 1 and 7. 
    #If it is, the method tries to find an empty place in the office on that weekday. 
    #If an empty place is found, the method adds the name of the person to the list of people who have reserved the office on that weekday. 
    #Otherwise, the method prints a message saying that the office is full.
    def make_reservation(self, name, weekday):
        if weekday == 1:
            for i, element in enumerate(self.Monday):
                if element is None:
                    self.Monday[i] = name
                    break
                if self.Monday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Monday
        
        if weekday == 2:
            for i, element in enumerate(self.Tuesday):
                if element is None:
                    self.Tuesday[i] = name
                    break
                if self.Tuesday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Tuesday
        
        if weekday == 3:
            for i, element in enumerate(self.Wednesday):
                if element is None:
                    self.Wednesday[i] = name
                    break
                if self.Wednesday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Wednesday
        
        if weekday == 4:
            for i, element in enumerate(self.Thursday):
                if element is None:
                    self.Thursday[i] = name
                    break
                if self.Thursday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Thursday
        
        if weekday == 5:
            for i, element in enumerate(self.Friday):
                if element is None:
                    self.Friday[i] = name
                    break
                if self.Friday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Friday
        
        if weekday == 6:
            for i, element in enumerate(self.Saturday):
                if element is None:
                    self.Saturday[i] = name
                    break
                if self.Saturday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Saturday
        
        if weekday == 7:
            for i, element in enumerate(self.Sunday):
                if element is None:
                    self.Sunday[i] = name
                    break
                if self.Sunday[-1] != None:       
                    print('This office is full, try it on an other day or a select an other office!')
                    break
            return self.Sunday


    #This method takes name (string) and weekday (integer) as arguments.
    #The method first checks if the value of the weekday argument is between 1 and 7. 
    #If it is, the method tries to find the name of the person in the list of people who have reserved the office on that weekday. 
    #If the name is found, the method removes the name from the list. 
    #Otherwise, the method prints a message saying that the person has not done a reservation .
    def cancel_reservation(self, name, weekday):
        if weekday == 1:
            for i, element in enumerate(self.Monday):
                if element == name:
                    self.Monday[i] = None
                    break
                if name not in self.Monday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Monday
        
        if weekday == 2:
            for i, element in enumerate(self.Tuesday):
                if element == name:
                    self.Tuesday[i] = None
                    break
                if name not in self.Tuesday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Tuesday
        
        if weekday == 3:
            for i, element in enumerate(self.Wednesday):
                if element == name:
                    self.Wednesday[i] = None
                    break
                if name not in self.Wednesday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Wednesday
        
        if weekday == 4:
            for i, element in enumerate(self.Thursday):
                if element == name:
                    self.Thursday[i] = None
                    break
                if name not in self.Thursday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Thursday
        
        if weekday == 5:
            for i, element in enumerate(self.Friday):
                if element == name:
                    self.Friday[i] = None
                    break
                if name not in self.Friday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Friday
        
        if weekday == 6:
            for i, element in enumerate(self.Saturday):
                if element == name:
                    self.Saturday[i] = None
                    break
                if name not in self.Saturday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Saturday
        
        if weekday == 7:
            for i, element in enumerate(self.Sunday):
                if element == name:
                    self.Sunday[i] = None
                    break
                if name not in self.Sunday:       
                    print('You have not made a reservation for this office on this weekday.')
                    break
            return self.Sunday


    #This method is a getter method. It takes no arguments and returns the name of the office.
    def get_office_name(self):
        return self.office_name




#This function takes nothing as input.
#The function prompts an administrator to enter the name and capacity of the new office. 
#It then creates a new Office object and adds it to the list of offices.
def create_offices():
    office_name = input("\nIn which city is the new office located?\nEnter your answer as follows: e.g. for St.Gallen --> St.Gallen\n==> ")
    office_capacity = int(input("\nHow many workplaces are available in this office?\n Enter your answer as follows: e.g. for 7 workplaces --> 7\n==> "))
    office_list.append(Office(office_name, office_capacity))
    


#This function takes nothing as input.
#The function prompts an administrator to enter the ID and name of the new employee the function adds it to the dictionary of employees.
def add_employee():
    key = int(input("\nCreate a unique ID for the new employee consisting of 4 numbers.\nEnter the ID as follows: e.g. for ID 1234 --> 1234\n==> "))
    value = input("\nNow assign the new employee his first name.\nEnter the first name as follows: e.g. for Robert --> Robert\n==> ")
    dict_employees[key] = value
    return dict_employees



#This function executes a reservation for the user. It takes office (office object), name (string)
#and weekday (integer) as input and does not return anything.
def choice_1(office, name, weekday):
    print(office.make_reservation(name, weekday))
    print(f"Remaining places: {office.get_empty_places(weekday)}")
    


#This function executes a cancelation for the user. It takes office (office object), name (string)
#and weekday (integer) as input and does not return anything.
def choice_2(office, name, weekday):
    office.cancel_reservation(name, weekday)
    office.get_empty_places(weekday)
  

#This function takes nothing as input.
#The function first prompts the user to enter their ID. 
#The function then checks if the ID is in the dictionary of employees. 
#If it is, the function returns the name of the employee associated with the ID. 
#Otherwise, the function prints a message that the ID is not found and prompts the user to enter their ID again.
def ID_input():
    while True:
        ID_employee = int(input("\nTo start, please enter your personal ID.\nEnter the ID as follows: e.g. for ID 1234 --> 1234\n==> "))
        if ID_employee in dict_employees.keys():
            break 
        else:
            print("Given ID not found")
    return dict_employees[ID_employee]


#This function takes nothing as input.
#The function first prompts the user to enter the name of the office they want to select.
#The function then iterates through the list of offices and checks if the name of the office entered by the user is in the list. 
#If it is, the function returns the name of the office. 
#Otherwise, the function prints a message that the input is not found and prompts the user to enter the name of the office again.
def location_office_input():
    while True:
        user_input_office = input("\nWhich office would you like to select?\nEnter your answer as follows: e.g. for St.Gallen --> St.Gallen\n==> ")
        for element in office_list:
            if element.get_office_name() == user_input_office:
                return user_input_office        
        print("Given input not found")


#This function takes nothing as input.
#The function first prompts the user to enter the weekday they want to make the reservation for. 
#The function then checks if the number entered by the user is between 1 and 7. 
#If it is, the function returns the number. 
#Otherwise, the function prints a message that the input is invalid and prompts the user to enter the weekday again.
def Weekday_input():
    while True:
        Weekday = int(input("Please enter the desired weekday.\n Enter the weekday as follows: e.g. for Monday --> 1, for Sunday --> 7\n==> "))
        if 1 <= Weekday <= 7:
            return Weekday
        else:
            print("Invalid input, insert an integer number between 1 and 7")




#This function is the main function of the program. It takes nothing as input.
def main():

    #Checks if file already exists. If the file exists, it is loaded (pickle) and if not, it is created. We assign the list from the file to office_list.
    #This part required the help of our tutors, since we faced some unsolvable problems.
    if os.path.exists("office_list_storage.pickle"):
        with open("office_list_storage.pickle", 'rb') as file:
            office_list = pickle.load(file)
            print("Office list has been loaded")

    else:
        with open("office_list_storage.pickle", 'wb') as file:
            pickle.dump(office_list, file)
            print("Office list has been created")


    #Checks if file already exists. If the file exists, it is loaded (pickle) and if not, it is created. We assign the dictionary from the file to dict_employees.
    #This part required the help of our tutors, since we faced some unsolvable problems.
    if os.path.exists("dict_employees_storage.pickle"):
        with open("dict_employees_storage.pickle", "rb") as file:
            dict_employees = pickle.load(file)
            print("Employees dictionary has been loaded")

    else:
        with open("dict_employees_storage.pickle", "wb") as file:
            pickle.dump(dict_employees, file)
            print("Employees dictionary has been created")


    #Function then enters a while-loop that repeatedly prompts the user for a choice
    #The code then executes the task corresponding to the user's choice.
    while True:
        print("\n\nWelcome to Office'er, valantic's internal application that helps employees managing their office.\n\nPlease choose below what you want to do:")
        print("1. Workplace reservation")
        print("2. Cancel workplace reservation")
        print("3. Request number of available workplaces")
        print("4. Add new employee (only allowed for administrators)")
        print("5. Add new office (only allowed for administrators)")
        print("6. Close application and save entries")
        print(" ")
        
        choice = input("Enter your choice by the corresponding number (1-6):\n==> ")


        #The following block is executed when the user chooses to make a workplace reservation. 
        #The code first prompts the user to enter their ID, the name of the office they want to reserve a workplace in, 
        #and the weekday they want to make the reservation for. The code then checks if the office exists. 
        # If it does, the code calls the choice_1() function to make the reservation.
        if choice == '1':
            print("\n\nWorkplace reservation")
            name = ID_input()
            location = location_office_input()
            weekday = Weekday_input()
            office_found = False
            for office in office_list:
                name_1 = office.get_office_name()
                if name_1 == location:
                    choice_1(office, name, weekday)
                    office_found = True
                    break
            if office_found == False:
                print("This office does not exist")
        

        #The following block is executed when the user chooses to cancel a workplace reservation. 
        #The code first prompts the user to enter their ID, the name of the office they want to cancel a workplace reservation in, 
        # and the weekday they want to make the cancellation for. The code then checks if the office exists. 
        #If it does, the code calls the choice_2() function to cancel the reservation. 
        elif choice == '2':
            print("\n\nCancel workplace reservation")
            name = ID_input()
            location = location_office_input()
            weekday = Weekday_input()
            office_found = False
            for office in office_list:
                name_1 = office.get_office_name()
                if name_1 == location:
                    choice_2(office, name, weekday)
                    office_found = True
                    break
            if office_found == False:
                print("This office does not exist")


        #The following block is executed when the user chooses to request the number of available workplaces in an office.
        #The code first prompts the user to enter their ID, the name of the office they want to request the number of available workplaces for, 
        #and the weekday they want to make the request for. The code then checks if the office exists. 
        #If it does, the code prints the number of available workplaces in the office for the specified weekday.
        elif choice == '3':
            print("\n\nRequest number of available workplaces")
            name = ID_input()
            location = location_office_input()
            weekday = Weekday_input()
            office_found = False
            for office in office_list:
                name_1 = office.get_office_name()
                if name_1 == location:
                    print(f"Available workplaces: {office.get_empty_places(weekday)}")
                    office_found = True
                    break
            if office_found == False:
                print("This office does not exist")


        #The following block is executed when an administrator chooses to add a new employee. 
        #The code calls the add_employee() function to add the new employee. 
        elif choice == '4':
            print("\n\nAdd new employee (only allowed for administrators)")
            add_employee()
            print("New employee has been added")
        

        #The follwing block is executed when an administrator chooses to add a new office.
        #The code calls the create_offices() function to add the new office.
        elif choice == '5':
            print("\n\nAdd new office (only allowed for administrators)")
            create_offices()
            #print(office_list)
            print("New office has been added")


        #he following block of code is executed when the user chooses to close the application. 
        #The code first saves the list of offices to the file office_list_storage.pickle and 
        #the dictionary of employees to the file dict_employees_storage.pickle. 
        #It then terminates the program.
        elif choice == '6':
            print("\n\nClose application and save entries")
            with open("office_list_storage.pickle", 'wb') as file:
                pickle.dump(office_list, file)
                print("Office list has been saved")

            with open("dict_employees_storage.pickle", "wb") as file:
                pickle.dump(dict_employees, file)
                print("Employees dictionary has been saved")
            break
       
       
        #The following block of code is executed when the user enters a choice that is not 1, 2, 3, 4, 5, or 6. 
        #In this case, the code prints a message that the choice is invalid and prompts the user to enter a valid choice.
        else:
            print("Invalid choice. Please enter a valid number (1-6).")




#The main function is called.
main()








