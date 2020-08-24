class Student(object):

    def __init__(self, prn, name):

        self.prn = prn
        self.name = name

    @property
    def prn(self):
        print "Getter Called"
        return self.__prn

    @prn.setter
    def prn(self, prn):
        print "Setter Called"
        self.__prn = prn

    def getName(self):
        return self.__name

    def setName(self, name):
        if len(name)>6 and len(name)<20:
            self.__name = name
        else:
            raise Exception("In valid Name length")
    
    name = property(getName, setName)

    def __str__(self):
        return "PRN: " + str(self.prn) + " Name: " +self.name

s = Student(123, "ABCDEFG")

print s.name

# try:
#     s.setName("XYZ")
# except:
#     print "Error occured"
# print s
