'''
This program contain a class for storing the student information like, rollno, prn, name, dob, email, contact etc. And define getter and setter method,constructor
and destructor.and menu driven program for performing following opration:
1. Add new student
2. Delete student by rollno, or prn give both the choice
3. Search student by prn, or name, or contact
4. Update the student information
5. List all the student
Store the student objects in a list
'''
class Student:
    
    def __init__(self, name, roll_no, prn, dob, email, contact_no):
        self.name=name
        self.roll_no=roll_no
        self.prn=prn
        self.dob=dob
        self.email=email
        self.contact_no=contact_no

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if(len(name)>=6 & len(name)<=10):
            self._name=name
        else:
            raise("Name should be between 6-10 characters")

         
       
    @property
    def roll_no(self):
        return self._roll_no

    @roll_no.setter
    def roll_no(self, roll_no):
        self._roll_no=roll_no

    @property
    def prn(self):
        return self.__prn

    @prn.setter
    def prn(self, prn):
        if(len(prn)==10):
            self.__prn=prn
        else:
            raise Exception("PRN should be only 10 digits")

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, dob):
        self._dob=dob

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email=email

    @property
    def contact_no(self):
        return self.__contact_no

    @contact_no.setter
    def contact_no(self, contact_no):
        if(len(contact_no)==10):
            self.__contact_no=contact_no
        else:
            raise("Contact number should be only 10 digits")
    
class sms(object):
    list = []

    def addstu(self):
        name = str(input("\nEnter the name of student : "))
        roll_no = int(input("Enter the roll number of student : "))
        prn = str(input("Enter the PRN of student : "))
        dob = str(input("Enter the date of birth of student : "))
        email = str(input("Enter the email ID of student : "))
        contact_no = str(input("Enter the contact number of student : "))
        sms.list.append(Student(name, roll_no, prn, dob, email, contact_no))
        print("\nStudent successfully added\n")

    def delstu(self):
        print("\nSelect your choice of deletion among the following :\n")
        print("1. Delete student details by roll number")
        print("2. Delete student details by PRN")
        ch=int(input("\nEnter your choice : "))
        c=0
        if(ch==1):
            delroll = int(input("\nEnter the roll number of the student to be deleted : "))
            for stud in sms.list:
                if(stud.roll_no == delroll):
                    del sms.list[c]
                    print("\nStudent deleted successfully\n")
                    break
                c = c+1
            else:
                print("\nRoll number not found\n")
        elif(ch==2):
            delprn = int(input("\nEnter the PRN of the student to be deleted : "))
            for stud in sms.list:
                if(int(stud.prn) == delprn):
                    del sms.list[c]
                    print("\nStudent deleted successfully\n")
                    break
                c = c+1
            else:
                print("\nPRN not found\n")
        else:
            print("\nWrong input\n")
    
    def searstu(self):
        print("\nSelect your choice of search among the following choices :\n")
        print("1. Search student by name")
        print("2. Search student by PRN")
        print("3. Search student by contact number")
        ch=int(input("\nEnter your choice : "))
        if(ch==1):
            sname = str(input("\nEnter the name you want to search : "))
            for stud in sms.list:
                if(stud.name == sname):
                    print("\nName\t\tRoll number\t\tPRN\t\tDate of birth\t\tEmail ID\t\tContact number")
                    print(stud.name,'\t\t',stud.roll_no,'\t\t',stud.prn,'\t\t',stud.dob,'\t\t',stud.email,'\t\t',stud.contact_no,'\n')
                    break
            else:
                print("\nName not found\n")
        elif(ch==2):
            sprn = int(input("\nEnter the PRN of the student you want to search : "))
            for stud in sms.list:
                if(int(stud.prn) == sprn):
                    print("\nName\t\tRoll number\t\tPRN\t\tDate of birth\t\tEmail ID\t\tContact number")
                    print(stud.name,'\t\t',stud.roll_no,'\t\t',stud.prn,'\t\t',stud.dob,'\t\t',stud.email,'\t\t',stud.contact_no,'\n')
                    break
            else:
                print("\nPRN not found\n")
        elif(ch==3):
            scont = int(input("\nEnter the contact number of the student you want to search : "))
            for stud in sms.list:
                if(int(stud.contact_no) == scont):
                    print("\nName\t\tRoll number\t\tPRN\t\tDate of birth\t\tEmail ID\t\tContact number")
                    print(stud.name,'\t\t',stud.roll_no,'\t\t',stud.prn,'\t\t',stud.dob,'\t\t',stud.email,'\t\t',stud.contact_no,'\n')
                    break
            else:
                print("\nContact number not found\n")
        else:
            print("\nWrong choice\n")
    
    def updstu(self):
        upname = str(input("\nEnter the name of student you want to update : "))
        c=0
        for stud in sms.list:
            if(stud.name == upname):
                print("\nEnter your choice among following :\n")
                print("1. Update name of student")
                print("2. Update roll number of student")
                print("3. Update PRN of student")
                print("4. Update date of birth of student")
                print("5. Update email ID of student")
                print("6. Update contact number of student")
                ch=int(input("\nEnter your choice : "))
                if(ch==1):
                    stud.name = str(input("\nEnter the name : "))
                    sms.list[c] = Student(stud.name, stud.roll_no, stud.prn, stud.dob, stud.email, stud.contact_no)
                elif(ch==2):
                    stud.roll_no = int(input("\nEnter the roll number : "))
                    sms.list[c] = Student(stud.name, stud.roll_no, stud.prn, stud.dob, stud.email, stud.contact_no)
                elif(ch==3):
                    stud.prn = str(input("\nEnter the PRN : "))
                    sms.list[c] = Student(stud.name, stud.roll_no, stud.prn, stud.dob, stud.email, stud.contact_no)
                elif(ch==4):
                    stud.dob = str(input("\nEnter the date of birth : "))
                    sms.list[c] = Student(stud.name, stud.roll_no, stud.prn, stud.dob, stud.email, stud.contact_no)
                elif(ch==5):
                    stud.email = str(input("\nEnter the email ID : "))
                    sms.list[c] = Student(stud.name, stud.roll_no, stud.prn, stud.dob, stud.email, stud.contact_no)
                elif(ch==6):
                    stud.contact_no = str(input("\nEnter the contact number : "))
                    sms.list[c] = Student(stud.name, stud.roll_no, stud.prn, stud.dob, stud.email, stud.contact_no)
            else:
                print("\nInput not found\n")
            c=c+1
    
    def liststu(self):
        for stud in sms.list:
            
            
            
            print(stud.name,'\t\t',stud.roll_no,'\t\t',stud.prn,'\t\t',stud.dob,'\t\t       ',stud.email,'\t\t      ',stud.contact_no)
            

def main():
    s=sms()
    print("-"*50)
    print("-"*50)
    while(True):
        print("Enter your choice number :\n")
        print("1. Add a new student")
        print("2. Delete a student")
        print("3. Search a student")
        print("4. Update a student")
        print("5. List all students")
        print("6. Close")
        c=int(input("\nEnter your choice : "))
        if(c==1):
            s.addstu()
        elif(c==2):
            s.delstu()
        elif(c==3):
            s.searstu()
        elif(c==4):
            s.updstu()
        elif(c==5):
            s.liststu()
        elif(c==6):
            print("\nThank you!!")
            break
        else:
            print("\n Invalid choice")


if __name__ == '__main__':
    main()
    
    
