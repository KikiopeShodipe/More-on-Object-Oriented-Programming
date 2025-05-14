class IOString:
    def __init__(self):
        self.str1 = "defult string"
    def get_string(self):
        self.str1 = input("Please enter a tring: ")
    def print_uppercase(self):
        print("The string in uppercase is: ", self.str1.upper())
my_string = IOString()
my_string.get_string()
my_string.print_uppercase()