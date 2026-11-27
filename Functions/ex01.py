# Exercise 1: Temperature converter
# Write celsius_to_fahrenheit(c) that returns the temperature in °F. Formula: F = C × 9/5 +
# 32.
# Test: celsius_to_fahrenheit(37) → 98.6 · celsius_to_fahrenheit(100) → 212.0

def temp_converter(value):
    fahrenheit=value*9/5+32
    return(fahrenheit)
print(temp_converter(37))
print(temp_converter(100))