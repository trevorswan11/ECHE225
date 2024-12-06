def convert_to_meters(value: float, unit: str) -> float:
    """
    Converts a float value to meters based on the provided unit.
    
    Parameters:
        value (float): The numerical value to convert.
        unit (str): The unit of the value (e.g., 'cm', 'mm', 'km', 'in', 'ft', 'yd', 'mi').
    
    Returns:
        float: The converted value in meters.
    """
    # Conversion factors to meters
    conversion_factors = {
        'm': 1,           # meters
        'cm': 0.01,       # centimeters
        'mm': 0.001,      # millimeters
        'um': 1e-6,       # micrometers (microns)
        'km': 1000,       # kilometers
        'in': 0.0254,     # inches
        'ft': 0.3048,     # feet
        'yd': 0.9144,     # yards
        'mi': 1609.34     # miles
    }
    
    unit = unit.lower()  # Make unit case-insensitive
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}. Supported units are {', '.join(conversion_factors.keys())}.")

print_to_meters = lambda value, str: print(convert_to_meters(value, str), 'm')

def main():
    print_to_meters(3, 'cm')
    print('hello')

if __name__ == '__main__': main()