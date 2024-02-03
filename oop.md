# OOP Task Example 01

```python
import time

class TrafficSignal:
    def __init__(self):
        self.state = "red"

    def change_state(self, new_state):
        self.state = new_state
        print(f"Traffic signal changed to {new_state}.")

    def run_simulation(self, duration):
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.state == "red":
                self.change_state("green")
                time.sleep(5)  # Green light duration
            elif self.state == "green":
                self.change_state("yellow")
                time.sleep(2)  # Yellow light duration
            elif self.state == "yellow":
                self.change_state("red")
                time.sleep(3)  # Red light duration

if __name__ == "__main__":
    traffic_signal = TrafficSignal()
    simulation_duration = 30  # seconds
    traffic_signal.run_simulation(simulation_duration)
```

Explanation:

1. **Class Definition**: We define a class named `TrafficSignal` to represent our traffic signal.

2. **Initialization**: In the `__init__` method, we set the initial state of the traffic signal to "red".

3. **State Change Method**: The `change_state` method is used to change the state of the traffic signal. It prints a message indicating the new state.

4. **Simulation Method**: The `run_simulation` method simulates the traffic signal behavior for a specified duration. It uses a while loop to iterate until the specified duration is reached. Inside the loop, it checks the current state and changes it according to the traffic signal sequence (red -> green -> yellow -> red).

5. **Main Block**: In the main block, we create an instance of the `TrafficSignal` class and run the simulation for a duration of 30 seconds.


# OOP Task Example 02

Certainly! Let's create a simple Flight Booking System using Object-Oriented Programming (OOP) in Python. We'll model the system with classes representing flights, passengers, and a booking system.

```python
class Flight:
    def __init__(self, flight_number, destination, capacity):
        self.flight_number = flight_number
        self.destination = destination
        self.capacity = capacity
        self.passengers = []

    def display_info(self):
        print(f"Flight {self.flight_number} to {self.destination}")
        print(f"Capacity: {self.capacity} passengers")
        print(f"Available Seats: {self.capacity - len(self.passengers)} seats")

    def book_seat(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            print(f"Seat booked for {passenger_name}")
        else:
            print("Sorry, the flight is fully booked.")

class Passenger:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Passenger: {self.name}")


class BookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_flights(self):
        for flight in self.flights:
            flight.display_info()

    def book_flight(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight.book_seat(passenger_name)
                break
        else:
            print(f"Flight {flight_number} not found.")

if __name__ == "__main__":
    # Create flights
    flight1 = Flight("F123", "New York", 150)
    flight2 = Flight("F456", "London", 200)

    # Create a booking system and add flights
    booking_system = BookingSystem()
    booking_system.add_flight(flight1)
    booking_system.add_flight(flight2)

    # Display available flights
    print("Available Flights:")
    booking_system.display_flights()

    # Book seats for passengers
    booking_system.book_flight("F123", "Alice")
    booking_system.book_flight("F123", "Bob")
    booking_system.book_flight("F456", "Charlie")
    booking_system.book_flight("F456", "David")
```

Explanation:

1. **Flight Class**: Represents a flight with attributes like flight number, destination, capacity, and a list of passengers. It has methods to display flight information and book seats.

2. **Passenger Class**: Represents a passenger with a name. It has a method to display passenger information.

3. **BookingSystem Class**: Manages a list of flights and provides methods to add flights, display available flights, and book seats on a flight.

4. **Main Block**: Creates instances of flights, adds them to the booking system, displays available flights, and books seats for passengers.

Certainly! Let's go through the code line by line with explanations:

```python
class Flight:
    def __init__(self, flight_number, destination, capacity):
        self.flight_number = flight_number
        self.destination = destination
        self.capacity = capacity
        self.passengers = []
```

1. **Class Definition - Flight**: Defines a class named `Flight` to represent a flight in the flight booking system.
2. **Initializer Method (`__init__`)**: Initializes the attributes of a flight - `flight_number`, `destination`, `capacity`, and an empty list of `passengers`.

```python
    def display_info(self):
        print(f"Flight {self.flight_number} to {self.destination}")
        print(f"Capacity: {self.capacity} passengers")
        print(f"Available Seats: {self.capacity - len(self.passengers)} seats")
```

3. **Display Info Method**: Defines a method `display_info` to print information about the flight, including flight number, destination, capacity, and available seats.

```python
    def book_seat(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            print(f"Seat booked for {passenger_name}")
        else:
            print("Sorry, the flight is fully booked.")
```

4. **Book Seat Method**: Defines a method `book_seat` to book a seat for a passenger. Checks if there are available seats and adds the passenger to the list if there is space.

```python
class Passenger:
    def __init__(self, name):
        self.name = name
```

5. **Class Definition - Passenger**: Defines a class named `Passenger` to represent a passenger in the flight booking system.
6. **Initializer Method (`__init__`)**: Initializes the attribute `name` with the passenger's name.

```python
    def display_info(self):
        print(f"Passenger: {self.name}")
```

7. **Display Info Method**: Defines a method `display_info` to print information about the passenger, specifically their name.

```python
class BookingSystem:
    def __init__(self):
        self.flights = []
```

8. **Class Definition - BookingSystem**: Defines a class named `BookingSystem` to manage flights in the flight booking system.
9. **Initializer Method (`__init__`)**: Initializes an empty list `flights` to store instances of the `Flight` class.

```python
    def add_flight(self, flight):
        self.flights.append(flight)
```

10. **Add Flight Method**: Defines a method `add_flight` to add a flight to the list of flights in the booking system.

```python
    def display_flights(self):
        for flight in self.flights:
            flight.display_info()
```

11. **Display Flights Method**: Defines a method `display_flights` to display information about all the flights in the booking system by calling the `display_info` method of each `Flight` instance.

```python
    def book_flight(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight.book_seat(passenger_name)
                break
        else:
            print(f"Flight {flight_number} not found.")
```

12. **Book Flight Method**: Defines a method `book_flight` to book a seat for a passenger on a specific flight. It iterates through the list of flights, finds the matching flight by `flight_number`, and then calls the `book_seat` method of that flight.

```python
if __name__ == "__main__":
    # Create flights
    flight1 = Flight("F123", "New York", 150)
    flight2 = Flight("F456", "London", 200)
```

13. **Main Block**: Initiates the program when executed directly. Creates two instances of the `Flight` class, representing flights from New York to London.

```python
    # Create a booking system and add flights
    booking_system = BookingSystem()
    booking_system.add_flight(flight1)
    booking_system.add_flight(flight2)
```

14. Creates an instance of the `BookingSystem` class, adds the previously created flights to the booking system.

```python
    # Display available flights
    print("Available Flights:")
    booking_system.display_flights()
```

15. Prints a message and displays information about available flights by calling the `display_flights` method of the `BookingSystem` instance.

```python
    # Book seats for passengers
    booking_system.book_flight("F123", "Alice")
    booking_system.book_flight("F123", "Bob")
    booking_system.book_flight("F456", "Charlie")
    booking_system.book_flight("F456", "David")
```

16. Books seats for passengers on the available flights by calling the `book_flight` method of the `BookingSystem` instance.

