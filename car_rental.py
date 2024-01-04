from datetime import datetime, timedelta

class CarRental:
    def __init__(self, cars):
        self.cars = cars
        self.rented_cars = {}

    def display_available_cars(self):
        print(f"Available Cars: {self.cars}")

    def rent_hourly(self, car_id, num_cars):
        return self.rent_car(car_id, num_cars, 'hourly')

    def rent_daily(self, car_id, num_cars):
        return self.rent_car(car_id, num_cars, 'daily')

    def rent_weekly(self, car_id, num_cars):
        return self.rent_car(car_id, num_cars, 'weekly')

    def rent_car(self, car_id, num_cars, rental_period):
        if car_id in self.cars and self.cars[car_id] >= num_cars and num_cars > 0:
            current_time = datetime.now().replace(microsecond=0)
            self.rented_cars[car_id] = {'start_time': current_time, 'num_cars': num_cars, 'rental_period': rental_period}
            self.cars[car_id] -= num_cars
            return f"{num_cars} car(s) rented for {rental_period} period starting at {current_time}."
        else:
            return "Invalid rental request. Please check car availability and quantity."

    def return_car(self,customer_name, car_id, num_cars_to_return):
      if car_id in self.rented_cars:
          rental_info = self.rented_cars[car_id]
          rental_period = rental_info['rental_period']
          num_cars = rental_info['num_cars']
          start_time = rental_info['start_time']
          
          current_time = datetime.now().replace(microsecond=0)
          rental_duration = current_time - start_time
          
          bill = 0
          if rental_period == 'hourly':
              bill = (rental_duration.seconds / 3600) * 5 * num_cars_to_return
          elif rental_period == 'daily':
              bill = (rental_duration.days) * 20 * num_cars_to_return
          elif rental_period == 'weekly':
              bill = (rental_duration.days / 7) * 50 * num_cars_to_return
          
          if num_cars_to_return <= num_cars:  
                self.cars[car_id] += num_cars_to_return

                self.rented_cars[car_id]['num_cars'] -= num_cars_to_return
                if self.rented_cars[car_id]['num_cars'] == 0:
                    del self.rented_cars[car_id]
                return f"{num_cars_to_return} car(s) returned by {customer_name}. Total bill: ${bill:.2f}."
          else:
                return f"Invalid return request. Trying to return more cars than rented for car_id {car_id}."
    
      else:
          return "Invalid return request. Car not found in the rented list."






