class multiplefunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        number = int(input("Enter a number: "))
        if (number % 2 == 0):
            print("52452 is Even number")
        else:
            print("52452 is Odd number")
    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if (gender == "Male" and age >= 21):
            print("ELIGIBLE")
        elif (gender == "Female" and age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        Subject1 = 98
        Subject2 = 87
        Subject3 = 95
        Subject4 = 95
        Subject5 = 93
        
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print("Total :", Total)
    
        Percent = (Total / 500) * 100
        print("Percentage :", Percent)
    def triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        Area = (Height * Breadth) / 2
        print("Area of Triangle:", Area)
        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        Breadth2 = int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1 + Height2 + Breadth2
        print("Perimeter of Triangle:", Perimeter)