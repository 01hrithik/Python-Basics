# Let's define a human
human = "alive"

# Define a Person class
class Person :
     
    # it's constructor to initialize person object
    def __init__(self, name ,age , gender) :
        self.name = name
        self.age = age
        self.gender = gender

   # it's method to reporting details about person
    def input_details(self) :
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))     
        self.gender = input("Enter your gender (M/F/O): ")

    # it's method to show details about person
    def display_details(self) :
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)      
     

     # Create a Person object
person1 = Person("", 0, "")
person1.input_details()
person1.display_details()

p2 = Person("Alice", 30, "F")
p2.input_details()
p2.display_details()


 

      
