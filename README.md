# CarRental
The provided Python code implements a simple car rental system with three main components: `CarRental`, `Customer`, and the main program in `main.ipynb`.

### CarRental (car_rental.py):
- Manages available and rented cars.
- Provides methods to display available cars, rent cars on an hourly, daily, or weekly basis, and return cars.
- Calculates bills based on the rental duration and type (hourly, daily, or weekly).
- Ensures proper handling of rental and return requests, including checking availability and generating appropriate messages.

### Customer (Customer.py):
- Represents a customer with a name.
- Has methods to request and return cars from a given `CarRental` instance.
- Acts as an interface between the user and the car rental system.

### main.ipynb: 
- Uses the `CarRental` and `Customer` classes to create a simple interactive car rental system.
- Allows users to display available cars, rent cars by specifying the car ID, quantity, and rental period, return cars by providing the car ID and quantity, and exit the program.
- Implements a loop to continuously prompt the user for actions until they choose to exit.

### How to Use: 
1. Users can run the `main.ipynb` script to interact with the car rental system.
2. The system displays available options, and users can choose to display available cars, rent a car, return a car, or exit.
3. Renting a car requires specifying the car ID, quantity, and rental period (hourly, daily, or weekly).
4. Returning a car requires specifying the car ID and quantity.
5. The system calculates bills based on the rental duration and type.
