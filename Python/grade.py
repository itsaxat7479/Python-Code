name=input("enter the name:")
Class=input("enter the class:")
section=input("enter the section:")
grade=input("enetr the grade:")

print("_________________________________________")

if grade=="A":
    print("Student name:",(name))
    print("student class:",(Class))
    print("student section:",(section))
    print("student grade:","OUTSTANDING")
   
    
elif grade=="B":
     print("Student name:",(name))
     print("student class:",(Class))
     print("student section:",(section))
     print("student grade:","EXCELLENT")
    
elif grade=="C":
     print("Student name:",(name))
     print("student class:",(Class))
     print("student section:",(section))
     print("student grade:","VERY GOOD")
    
elif grade=="D":
     print("Student name:",(name))
     print("student class:",(Class))
     print("student section:",(section))
     print("student grade:","good")
    
else:
    print("unrecognized")
