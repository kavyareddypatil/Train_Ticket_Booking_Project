
import random
from datetime import datetime


# ---------------- TRAIN CLASS ----------------

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination

       
        self.classes = {
            "SL": seats,
            "3AC": seats,
            "2AC": seats,
            "1AC": seats
        }

        self.booked_berths = {
            "SL": [],
            "3AC": [],
            "2AC": [],
            "1AC": []
        }

        
        self.waiting_list = {
            "SL": [],
            "3AC": [],
            "2AC": [],
            "1AC": []
        }

        self.waiting_number = 0

    def display_info(self):
        print(f"Train number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")

        print("Available seats:")
        print(f"SL  : {self.classes['SL']}")
        print(f"3AC : {self.classes['3AC']}")
        print(f"2AC : {self.classes['2AC']}")
        print(f"1AC : {self.classes['1AC']}")
        print()


    def generate_berth(self, class_type):
        berth_number = len(self.booked_berths[class_type]) + 1

        berth_types = ["L", "M", "U", "SL", "SU"]

        berth_type = berth_types[(berth_number - 1) % 5]

        return f"{berth_type}-{berth_number}"


    def allocate_berth(self, class_type, preference):

        available_seats = self.classes[class_type]

        if available_seats <= 0:
            return None

        berth_number = len(self.booked_berths[class_type]) + 1

        berth_types = ["L", "M", "U", "SL", "SU"]

        for i in range(available_seats):
            current_number = berth_number + i
            current_type = berth_types[(current_number - 1) % 5]

            berth = f"{current_type}-{current_number}"

            if current_type == preference:
                if berth not in self.booked_berths[class_type]:
                    self.booked_berths[class_type].append(berth)
                    self.classes[class_type] -= 1
                    return berth

     
        for i in range(available_seats):
            current_number = berth_number + i
            current_type = berth_types[(current_number - 1) % 5]

            berth = f"{current_type}-{current_number}"

            if berth not in self.booked_berths[class_type]:
                self.booked_berths[class_type].append(berth)
                self.classes[class_type] -= 1
                return berth

        return None


    def add_to_waiting_list(self, class_type, passenger):
        self.waiting_number += 1

        waiting_number = f"WL{self.waiting_number}"

        self.waiting_list[class_type].append(
            (waiting_number, passenger)
        )

        return waiting_number


    def book_tickets(self, passengers, class_type, preference):

        booking_details = []

        for passenger in passengers:

            # Try to allocate confirmed berth
            berth = self.allocate_berth(
                class_type,
                preference
            )

            pnr = random.randint(100000, 999999)

            booking_time = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            if berth is not None:

                booking_details.append({
                    "passenger": passenger,
                    "pnr": pnr,
                    "status": "CONFIRMED",
                    "berth": berth,
                    "class": class_type,
                    "date_time": booking_time
                })

            else:

                # No seat available -> waiting list
                waiting_number = self.add_to_waiting_list(
                    class_type,
                    passenger
                )

                booking_details.append({
                    "passenger": passenger,
                    "pnr": pnr,
                    "status": "WAITING",
                    "berth": waiting_number,
                    "class": class_type,
                    "date_time": booking_time
                })

        return booking_details




class Passenger:

    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")




class Ticket:

    def __init__(
        self,
        train,
        source,
        destination,
        passenger,
        booking_details
    ):
        self.train = train
        self.source = source
        self.destination = destination
        self.passenger = passenger
        self.booking_details = booking_details

    def display_info(self):

        print("\n--------------------------------")
        print("          TICKET DETAILS")
        print("--------------------------------")

        print(f"Train Number : {self.train.train_num}")
        print(f"Source       : {self.source}")
        print(f"Destination  : {self.destination}")

        print(f"Passenger    : {self.passenger.name}")
        print(f"Age          : {self.passenger.age}")
        print(f"Gender       : {self.passenger.gender}")
        print(f"Phone        : {self.passenger.phone}")

        print(f"Class        : {self.booking_details['class']}")
        print(f"Status       : {self.booking_details['status']}")

        if self.booking_details["status"] == "CONFIRMED":
            print(f"Berth        : {self.booking_details['berth']}")
        else:
            print(f"Waiting List : {self.booking_details['berth']}")

        print(f"PNR          : {self.booking_details['pnr']}")
        print(f"Booking Time : {self.booking_details['date_time']}")

        print("--------------------------------")




class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password




accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

logged_in_account = None




while True:

    print("\n1. Create an account")
    print("2. Login")

    choice = input("Enter choice: ")

    if choice == "1":

        username = input("Enter username: ")
        password = input("Enter password: ")

        accounts.append(
            Account(username, password)
        )

        print("Account created successfully!")

    elif choice == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in accounts:

            if (
                account.username == username
                and account.check_password(password)
            ):
                logged_in_account = account
                break

        if logged_in_account is None:
            print("Invalid username or password.")

        else:
            print(
                f"\nLogged in as {logged_in_account.username}"
            )
            break

    else:
        print("Invalid choice.")




if logged_in_account is not None:

    trains = [

        Train(
            "12737",
            "Tadepalligudem",
            "Secunderabad",
            40
        ),

        Train(
            "12728",
            "Tadepalligudem",
            "Visakhapatnam",
            50
        ),

        Train(
            "22863",
            "Vijayawada",
            "Bangalore",
            1
        )

    ]




print("\n----- Available Train Details -----\n")

for train in trains:
    train.display_info()




while True:

    try:

        train_num = input(
            "Enter Train Number: "
        )

        num_tickets = int(
            input("Enter Number of Tickets: ")
        )

        if num_tickets <= 0:
            raise ValueError(
                "Number of tickets should be greater than 0"
            )

        train = None

        for t in trains:

            if t.train_num == train_num:
                train = t
                break

        if train is None:
            raise ValueError(
                "Invalid Train Number."
            )

        break

    except ValueError as e:
        print(f"Invalid Input: {e}")



while True:

    print("\nSelect Class:")
    print("1. SL  - Sleeper")
    print("2. 3AC - AC 3 Tier")
    print("3. 2AC - AC 2 Tier")
    print("4. 1AC - AC First Class")

    class_choice = input(
        "Enter your choice: "
    )

    class_options = {
        "1": "SL",
        "2": "3AC",
        "3": "2AC",
        "4": "1AC"
    }

    if class_choice in class_options:

        class_type = class_options[class_choice]

        print(
            f"Selected Class: {class_type}"
        )

        break

    else:
        print("Invalid class choice.")



while True:

    print("\nSelect Berth Preference:")
    print("L  - Lower")
    print("M  - Middle")
    print("U  - Upper")
    print("SL - Side Lower")
    print("SU - Side Upper")

    preference = input(
        "Enter berth preference: "
    ).upper()

    if preference in ["L", "M", "U", "SL", "SU"]:
        break

    print("Invalid berth preference.")



passengers = []

for i in range(num_tickets):

    print(
        f"\nEnter details for Passenger {i + 1}:"
    )

    while True:

        try:

            name = input("Name: ")

            if not name:
                raise ValueError(
                    "Name cannot be empty"
                )

            age = int(
                input("Age: ")
            )

            if age <= 0 or age > 120:
                raise ValueError(
                    "Invalid Age"
                )

            gender = input(
                "Gender: "
            )

            phone = input(
                "Phone Number: "
            )

            if (
                not phone
                or len(phone) != 10
                or not phone.isdigit()
            ):
                raise ValueError(
                    "Invalid Phone Number"
                )

            passenger = Passenger(
                name,
                age,
                gender,
                phone
            )

            passengers.append(
                passenger
            )

            break

        except ValueError as e:
            print(
                f"Invalid Input: {e}"
            )



booking_details = train.book_tickets(
    passengers,
    class_type,
    preference
)



print(
    "\n============== BOOKING RESULT =============="
)

for i in range(num_tickets):

    ticket = Ticket(
        train,
        train.source,
        train.destination,
        passengers[i],
        booking_details[i]
    )

    ticket.display_info()



print(
    "\n------- Thank You -------"
)

print(
    "------- Safe Journey -------"
)

