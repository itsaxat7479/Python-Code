name = input("Enter name: ")
Class = input("Enter class: ")
section = input("Enter section: ")

mark = int(input("Enter your marks: "))

print("\n")
print(f"Name: {name}")
print(f"Class: {Class}")
print(f"Section: {section}")
print(f"Subject marks: {mark}") 


if mark < 0 or mark > 100:
    print("Error: mark should be between 0 and 100 only.")
elif mark < 50:
    print("Fail!")
elif mark >= 50:
    print("Pass!")
    if mark >= 50 and mark < 60:
        print("Good!")
    elif mark >= 60 and mark < 80:
        print("Very Good!")
    elif mark >= 80 and mark < 100:
        print(" Outstanding!")