name = input("Enter name:")
Class = input("Enter class: ")
section = input("Enter section: ")

EnglishMarks = int(input("Enter English mark: "))
HondiMarks = int(input("Enter hindi mark: "))
MathMarks = int(input("Enter Math mark: "))
HistoryMarks = int(input("Enter History mark: "))
EvsMarks = int(input("Enter evs mark: "))

avg = (EnglishMarks + HondiMarks +MathMarks+ HistoryMarks + EvsMarks)/5

print("\n")
print(f"Name: {name}")
print(f"Class: {Class}")
print(f"Section: {section}")
print(f"Percentage: {avg}") 


if avg < 0 or avg > 100:
    print("Error")
elif avg < 45:
    print("Fail!")
elif avg >= 45:
    print("Pass!")
    if avg >= 45 and avg < 60:
        print("Pass!")
    elif avg >= 60 and avg < 75:
        print("Remark: Good!")
    elif avg >= 75 and avg < 85:
        print("Remark: Very Good!")
    elif avg >= 85 and avg < 100:
        print("Remark: Excellent!")