def convert_length():
    print("\n--- Length Conversion ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Enter sub-choice (1 or 2): ").strip()
    
    val_str =input("Enter value: ").strip()

    try:
        value = float(val_str)
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == '1':
        result = value * 0.621371
        print(f"{value} km = {result:.2f} miles")
    elif choice == '2':
        result = value / 0.621371
        print(f"{value} miles = {result:.2f} km")
    else:
        print("Invalid choice.")

def convert_weight():
    print("\n--- Weight Conversion ---")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    choice = input("Enter sub-choice (1 or 2): ").strip()
    
    val_str = input("Enter value: ").strip()
    try:
        value = float(val_str)
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == '1':
        result = value * 1000
        print(f"{value} kg = {result:.2f} g")
    elif choice == '2':
        result = value / 1000
        print(f"{value} g = {result:.2f} kg")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("\n--- Temperature Conversion ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter sub-choice (1 or 2): ").strip()
    
    val_str = input("Enter value: ").strip()
    try:
        value = float(val_str)
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value} C = {result:.2f} F")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(f"{value} F = {result:.2f} C")
    else:
        print("Invalid choice.")

def convert_time():
    print("\n--- Time Conversion ---")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    choice = input("Enter sub-choice (1 or 2): ").strip()
    
    val_str = input("Enter value: ").strip()
    try:
        value = float(val_str)
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == '1':
        result = value * 60
        print(f"{value} hours = {result:.2f} minutes")
    elif choice == '2':
        result = value / 60
        print(f"{value} minutes = {result:.2f} hours")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\n==============================")
        print("     UNIT CONVERSION SYSTEM")
        print("==============================")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Time")
        print("5. Exit")
        
        choice = input("Enter menu choice (1-5): ").strip()
        
        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            convert_temperature()
        elif choice == '4':
            convert_time()
        elif choice == '5':
            print("Exiting Unit Conversion System. Goodbye!")
            break
        else:
            print("Invalid choice. Select 1 to 4.")

if __name__ == "__main__":
    main()