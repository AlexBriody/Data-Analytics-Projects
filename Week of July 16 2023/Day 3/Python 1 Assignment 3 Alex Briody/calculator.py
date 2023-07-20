from math import pi 

def sq_footage (length: float, width: float):
    num = length * width
    rounded_num = round(num, 2)
    formatted_num = format(rounded_num, ",")
    return f"{formatted_num} sq ft"

def circle_circum (radius: float):
    num = 2 * pi * radius
    rounded_num = round(num, 2)
    formatted_num = format(rounded_num, ",")
    return formatted_num

def feet_to_in (feet: float):
    num = feet * 12
    rounded_num = round(num, 2)
    formated_num = format(rounded_num, ",")
    return f"{formated_num} in"


