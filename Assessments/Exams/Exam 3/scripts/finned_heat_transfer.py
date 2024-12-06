from math import cosh, tanh, sqrt, exp, pi
import unit_conversion as uc

def calculate_m_parameter(h: float, P: float, k: float, A_c: float) -> float:
    return sqrt((h * P) / (k * A_c))

def calculate_T_of_x_infinite(h: float, 
                     P: float, 
                     k: float, 
                     A_c: float, 
                     x: float, 
                     T_b: float, 
                     T_inf: float) -> float:
    m = calculate_m_parameter(h, P, k, A_c)
    exponential: float = exp(-1 * m * x)
    T_diff: float = T_b - T_inf
    return exponential * T_diff + T_inf

def calculate_T_of_x_adiabatic(h: float, 
                     P: float, 
                     k: float, 
                     A_c: float, 
                     x: float, 
                     L: float,
                     T_b: float, 
                     T_inf: float) -> float:
    m = calculate_m_parameter(h, P, k, A_c)
    numerator: float = cosh(m * (L - x))
    denominator: float = cosh(m * L)
    T_diff: float = T_b - T_inf
    return (numerator / denominator) * T_diff + T_inf

def calculate_Q_infinite(h: float, 
                     P: float, 
                     k: float, 
                     A_c: float, 
                     T_b: float, 
                     T_inf: float) -> float:
    square_root: float = sqrt(h * P * k * A_c)
    T_diff: float = T_b - T_inf
    return square_root * T_diff

def calculate_Q_adiabatic(h: float, 
                     P: float, 
                     k: float, 
                     A_c: float, 
                     L: float,
                     T_b: float, 
                     T_inf: float) -> float:
    m = calculate_m_parameter(h, P, k, A_c)
    square_root = sqrt(h * P * k * A_c)
    T_diff = T_b - T_inf
    hyperbolic = tanh(m * L)
    return square_root * T_diff * hyperbolic

def question_():
    print()
    
def question_():
    print()

def main():
    m = calculate_m_parameter(15, pi * 0.01, 237, pi * ((0.01 / 2) ** 2))
    print(m, 1- tanh(m * 0.5))
    print('hello')

if __name__ == '__main__': main()
