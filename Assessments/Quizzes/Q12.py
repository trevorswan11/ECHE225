# This is the solution to quiz 12, as my work was wrong
def Nussult(Re, Pr, correlation: str, mixed_BL: bool = True):
    Re_crit = 5 * (10 ** 5)
    # Laminar BL
    if Re < Re_crit:
        if correlation == "local":
            return 0.332 * (Re ** 0.5) * (Pr ** (1/3))
        elif correlation == "average":
            return 0.664 * (Re ** 0.5) * (Pr ** (1/3))
    # Turbulent BL
    elif Re > Re_crit:
        if correlation == "local":
            return 0.0296 * (Re ** (4/5)) * (Pr ** (1/3)) 
        elif correlation == "average":
            if mixed_BL:
                return (0.037 * (Re ** (4/5)) - 871) * (Pr ** (1/3))
            return 0.037 * (Re ** (4/5)) * (Pr ** (1/3))
    return None
    
def question(question: int, correlation: str,  mixed_BL: bool = True):
    if question not in [3, 4]: return None
    # Given values
    rho = 0.823           # Density of air in kg/m^3
    u = 8.00              # Velocity of air in m/s
    dim_one = 6.00        # Plate length in m
    dim_two = 1.50        # Plate width in m
    mu = 2.096e-5         # Dynamic viscosity in kg/m·s
    Pr = 0.7154           # Prandtl number (dimensionless)
    k = 0.02953           # Thermal conductivity in W/m·K
    T_plate = 140         # Plate temperature in °C
    T_infinity = 20       # Ambient air temperature in °C

    # Determine L based on question number
    L = dim_one if question == 3 else dim_two

    # Calculate Reynolds number (Re)
    Re = (rho * u * L) / mu

    Nu = Nussult(Re, Pr, correlation, mixed_BL)

    # Calculate convective heat transfer coefficient (h)
    h = (Nu * k) / L

    # Calculate area of the plate (A)
    A = dim_one * dim_two

    # Calculate temperature difference (ΔT)
    delta_T = T_plate - T_infinity

    # Calculate heat transfer rate (Q)
    Q = h * A * delta_T  # in Watts

    # Convert to kilowatts (kW) and round to the nearest hundredths
    Q_kW = round(Q / 1000, 2)
    print(Re, Nu, h, Q_kW)

question(3, "average")
question(4, "average")