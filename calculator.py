// Program for calculator

while True:
    print("1.Addition")
    print("2.Subtractions")
    print("3.Multiplictions")
    print("4.Divisions")
    print("5.Exit")
    ch=raw_input('Enter your choice')

    while True:
        n=raw_input('Enter 1st no:')
        n1=raw_input('Enter 2nd no:')

        if(ch==1):
            z=(x+y)
            return(z)

        elif(ch==2):
            z=x-y
            return z

        elif(ch==3):
            z=x*y
           return z

        elif(ch==4):
            z=x/y
            return z

        elif(ch==5):
            break
