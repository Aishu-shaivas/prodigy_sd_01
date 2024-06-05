
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def celsius_to_rankine(celsius):
    return celsius * 9/5 + 491.67

def rankine_to_celsius(rankine):
    return (rankine - 491.67) * 5/9

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

def temperature_conversion():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the temperature unit (Celsius, Fahrenheit, Kelvin, Rankine): ").strip().lower()

    if unit == 'celsius':
        celsius = temperature
        print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit")
        print(f"{celsius} Celsius is {celsius_to_kelvin(celsius)} Kelvin")
        print(f"{celsius} Celsius is {celsius_to_rankine(celsius)} Rankine")
    elif unit == 'fahrenheit':
        fahrenheit = temperature
        print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_celsius(fahrenheit)} Celsius")
        print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_kelvin(fahrenheit)} Kelvin")
        print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_rankine(fahrenheit)} Rankine")
    elif unit == 'kelvin':
        kelvin = temperature
        print(f"{kelvin} Kelvin is {kelvin_to_celsius(kelvin)} Celsius")
        print(f"{kelvin} Kelvin is {kelvin_to_fahrenheit(kelvin)} Fahrenheit")
    elif unit == 'rankine':
        rankine = temperature
        print(f"{rankine} Rankine is {rankine_to_celsius(rankine)} Celsius")
        print(f"{rankine} Rankine is {rankine_to_fahrenheit(rankine)} Fahrenheit")
    else:
        print("Invalid unit! Please enter Celsius, Fahrenheit, Kelvin, or Rankine.")

# Start the temperature conversion
temperature_conversion()
