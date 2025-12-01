# temperature_converter.py

def convert_temperature(temp, unit):
    if unit.lower() == "c":
        return (temp * 9/5) + 32, "Fahrenheit"
    elif unit.lower() == "f":
        return (temp - 32) * 5/9, "Celsius"
    else:
        print("Invalid unit.")
        return None, None

def main():
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")
    converted_temp, converted_unit = convert_temperature(temp, unit)
    if converted_temp is not None:
        print(f"{temp} degrees {unit.upper()} is {converted_temp:.2f} degrees {converted_unit}")

if __name__ == "__main__":
    main()