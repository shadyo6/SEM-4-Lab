# termwork_4

class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def disp(self):
        # print("Person:")
        print(self.fname, self.lname, self.email)


class Customer(Person):
    def __init__(self, fname, lname, email, no):
        super().__init__(fname, lname, email)  # calling person's init
        self.no = no

    def disp(self):
        Person.disp(self)
        print("Customer No: ", self.no)


class Employee(Person):
    def __init__(self, fname, lname, email, pan):
        super().__init__(fname, lname, email)  # calling person's init
        self.pan = pan

    def disp(self):
        Person.disp(self)
        print("Pan No: ", self.pan)


def show(ob):
    if isinstance(ob, Customer):
        print("Customer: ")
        ob.disp()
    elif isinstance(ob, Employee):
        print("Employee: ")
        ob.disp()
    elif isinstance(ob, Person):
        print("Person: ")
        ob.disp()


def main():
    choice = 'y'
    while choice == 'y':
        fname, lname, email = input("Enter first name, last name and email: ").split()
        print("1:Customer 2:Employee 3:Person")
        opt = int(input("Enter your option: "))
        if opt == 1:
            no = int(input("Enter the customer no: "))
            c = Customer(fname, lname, email, no)
            show(c)
        elif opt == 2:
            pan = input("Enter the employee pan: ")
            e = Employee(fname, lname, email, pan)
            show(e)
        elif opt == 3:
            p = Person(fname, lname, email)
            show(p)
        else:
            print("Invalid option")
        choice = input("Continue(y/n)?: ")
        
if __name__ == '__main__':
    main()
