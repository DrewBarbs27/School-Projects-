def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def unit_converter():
    print("Unit Converter")
    print("Select conversion:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Feet to Meters")
    print("4. Meters to Feet")
    print("5. Miles to Kilometers")
    print("6. Kilometers to Miles")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please enter a valid option.")
        return

    value = float(input("Enter the value to convert: "))

    if choice == '1':
        result = meters_to_kilometers(value)
        conversion = "Meters to Kilometers"
    elif choice == '2':
        result = kilometers_to_meters(value)
        conversion = "Kilometers to Meters"
    elif choice == '3':
        result = feet_to_meters(value)
        conversion = "Feet to Meters"
    elif choice == '4':
        result = meters_to_feet(value)
        conversion = "Meters to Feet"
    elif choice == '5':
        result = miles_to_kilometers(value)
        conversion = "Miles to Kilometers"
    elif choice == '6':
        result = kilometers_to_miles(value)
        conversion = "Kilometers to Miles"

    print(f"{conversion} result: {result}")

# Example usage:
unit_converter()
