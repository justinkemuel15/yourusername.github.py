
class Grab:
    def __init__(self, name, car_type, kilometer):
        self.name = name
        self.car_type = car_type
        self.kilometer = kilometer

    def display_info(self):
        return f"Driver: {self.name}  | Car_type: {self.car_type}  | Kilometer: {self.kilometer}"

Grabs = []

def add_grab(name, car_type, kilometer):
    try:
        kilometer = float(kilometer)  # Try to convert to number
        book = Grab(name, car_type, kilometer)
        Grabs.append(book)
        print(f"Added Grab: {book.display_info()}")
    except ValueError:
        print("❌ Invalid input for kilometer. Please enter a number.")

def view_all_grab():
    print("\n📋 View All Grabs")
    if Grabs:
        for book in Grabs:
            print(book.display_info())
    else:
        print("⚠️ No grabs found.")

def search_grab(name):
    print(f"\n🔍 Search Grab for: {name}")
    found = False
    for book in Grabs:
        if book.name.lower() == name.lower():
            print(book.display_info())
            found = True
            break
    if not found:
        print("❌ Grab not found.")

def cancel_grab():
    print("\n❌ Cancel All Bookings")
    if Grabs:
        Grabs.clear()
        print("✅ All bookings have been cancelled.")
    else:
        print("⚠️ No bookings to cancel.")

while True:
    print("\n----- Grab Booking -----")
    print("1.) Add Grab")
    print("2.) View All Grab")
    print("3.) Search Grab")
    print("4.) Cancel All Grab")
    print("5.) Exit The Program")

    try:
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter the name: ")
            car_type = input("Enter the car type: ")
            kilometer = input("Enter the kilometers: ")
            add_grab(name, car_type, kilometer)

        elif choice == '2':
            view_all_grab()

        elif choice == '3':
            name = input("Enter the name to search: ")
            search_grab(name)

        elif choice == '4':
            cancel_grab()

        elif choice == '5':
            print("👋 Exiting the program.")
            break

        else:
            print("⚠️ Invalid input. Please choose 1 to 5.")

    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
