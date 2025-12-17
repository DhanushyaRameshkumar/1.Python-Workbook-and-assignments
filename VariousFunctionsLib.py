class Variousfunctions():
    def Subfields():
        subfields=["Machine Learning","Neutral Network","vision","Robotics","Speech Processing","NLP"]
        print("Sub-fields in AI are:")
        for fields in subfields:
            print(fields)
            
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
        return 
    
    def ElegibilityForMarriage():
        gender=input("Your gender:")
        age=int(input("Your Age:"))
        if(gender=="Male" and age<21):
            print("NOT ELIGIBLE")
        elif(gender=="Female" and age<18):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
            
    def Precentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=print("Total:",sub1+sub2+sub3+sub4+sub5)
        print("Percentage:",(sub1+sub2+sub3+sub4+sub5)/5)
        
    def triangle():
        Height=float(input("Height:"))
        Breadth=float(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2)")
        print("Area of Triangle:",(Height*Breadth)/2)
        Height1=float(input("Height1:"))
        Height2=float(input("Height2:"))
        Breadth2=float(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = Height1 + Height2 + Breadth2
        print("Perimeter of Triangle:",perimeter)    

        