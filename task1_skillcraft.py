# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:57:57 2026

@author: ASHISH
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, scale):
    if scale.lower() == "celsius":
        print(f"{value} °C = {celsius_to_fahrenheit(value):.2f} °F")
        print(f"{value} °C = {celsius_to_kelvin(value):.2f} K")
    elif scale.lower() == "fahrenheit":
        print(f"{value} °F = {fahrenheit_to_celsius(value):.2f} °C")
        print(f"{value} °F = {fahrenheit_to_kelvin(value):.2f} K")
    elif scale.lower() == "kelvin":
        print(f"{value} K = {kelvin_to_celsius(value):.2f} °C")
        print(f"{value} K = {kelvin_to_fahrenheit(value):.2f} °F")
    else:
        print("Invalid scale! Please choose Celsius, Fahrenheit, or Kelvin.")

# Example usage
temp = float(input("Enter the temperature value: "))
scale = input("Enter the scale (Celsius/Fahrenheit/Kelvin): ")
convert_temperature(temp, scale)
