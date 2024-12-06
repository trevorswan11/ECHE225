from math import pi
import unit_conversion as uc

def Nussult(Re: float, 
            Pr: float, 
            correlation: str, 
            mixed_BL: bool = True) -> float:
    Re_crit: float = 5 * (10 ** 5)
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

def Reynolds(rho: float, U_inf: float, x: float, mu: float) -> float:
    numerator: float = rho * U_inf * x
    return numerator / mu

def Reynolds_D_h(rho: float, 
                 U_inf: float, 
                 A_c: float, 
                 P: float, 
                 mu: float) -> float:
    D_h: float = (4 * A_c) / P
    return Reynolds(rho, U_inf, D_h, mu)

def calculate_convective_heat_transfer_coef(Nu: float, 
                                            x: float, 
                                            k_fluid: float) -> float:
    return (Nu * k_fluid) / x

def calculate_convective_flux(h: float, T_diff: float) -> float:
    return h * T_diff

def calculate_convective_flow(h: float, T_diff: float, A_s: float) -> float:
    q: float = calculate_convective_flux(h, T_diff)
    return q * A_s

def calculate_conductive_flux(k_fluid: float, T_diff: float, L: float) -> float:
    return (k_fluid * T_diff) / L

def calculate_conductive_flow(k_fluid: float, 
                              T_diff: float, 
                              L: float, 
                              A_s: float) -> float:
    q: float = calculate_conductive_flux(k_fluid, T_diff, L)
    return q * A_s

def question_():
    print()
    
def question_():
    print()

def main():
    print('hello')

if __name__ == '__main__': main()
