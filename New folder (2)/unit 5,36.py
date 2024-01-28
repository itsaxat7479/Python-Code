#36. Create a subclass called Manager that inherits from the Employee class. Add parameter, h
#subordinates, to the constructor of the Manager class. Use super() to call the constructor 
#of the base class. Update the display method to include information about subordinates






class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, subordinates):
        super().__init__(name, employee_id)
        self.subordinates = subordinates

    def display(self):
        super().display()
        print(f"Subordinates: {', '.join(self.subordinates)}")

# Example usage:
manager = Manager("John Doe", "M123", ["Alice", "Bob", "Charlie"])
manager.display()
