class Car:
    def __init__(self, make, model, year):
        """        
        :param make: The make of the car (e.g., Toyota)
        :param model: The model of the car (e.g., Camry)
        :param year: The year of the car (e.g., 2022)
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Print out the car's information.
        """
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage
# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)
my_car = Car(make="Toyota", model="Hilux", year=2019)

# Call the display_info method to print out the car's information
my_car.display_info()
