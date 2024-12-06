from math import exp, pi
import unit_conversion as uc

STEFAN_BOLTZMANN = 5.67e-8 # W / (m^2 K^4)

def blackbody_emissive_power(T_s: float) -> float:
    return STEFAN_BOLTZMANN * (T_s ** 4)

def spectral_blackbody_emissive_power(wavelength: float, T: float) -> float:
    c_1 = 3.74e8
    c_2 = 1.44e4
    exponential = exp(c_2 / (wavelength * T))
    denominator = wavelength * (exponential - 1)
    return c_1 / denominator

def weins_to_get_T(wavelength: float) -> float:
    return 2897.8 / wavelength

def weins_to_get_wavelength(T: float) -> float:
    return 2897.8 / T

def emissivity(E_of_T: float, E_b_of_T: float) -> float:
    return E_of_T / E_b_of_T

def emissive_power(emissivity: float, T_s: float) -> float:
    return emissivity * blackbody_emissive_power(T_s)

def Q_emitted(emissivity: float, T_s: float, A_s: float) -> float:
    return A_s * emissive_power(emissivity, T_s)

def question_():
    print()
    
def question_():
    print()

def main():
    print('hello')

if __name__ == '__main__': main()
