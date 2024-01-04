class Customer:
    def __init__(self, name):
        self.name = name

    def request_car(self, car_rental, car_id, num_cars, rental_period):
        return car_rental.rent_car(car_id, num_cars, rental_period)

    def return_car(self, car_rental,car_id, num_cars_to_return):
        return car_rental.return_car(self.name,car_id, num_cars_to_return)


