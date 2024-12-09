def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed

    # Convert input to Celsius
    if from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    elif from_unit == 'C':
        celsius = value
    else:
        raise ValueError("Invalid 'from_unit'. Choose 'C', 'F', or 'K'.")

    # Convert Celsius to target unit
    if to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    elif to_unit == 'C':
        return celsius
    else:
        raise ValueError("Invalid 'to_unit'. Choose 'C', 'F', or 'K'.")
try:
    temp = float(input("Enter temperature value: "))
    from_unit = input("Enter current unit (C, F, K): ").strip().upper()
    to_unit = input("Enter target unit (C, F, K): ").strip().upper()
    result = convert_temperature(temp, from_unit, to_unit)
    print(f"{temp} {from_unit} = {result:.2f} {to_unit}")
except ValueError as e:
    print(f"Error: {e}")
