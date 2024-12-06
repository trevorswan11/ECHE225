from typing import List
from math import log, pi
import unit_conversion as uc

def conductive_resistance(L: float, k: float, A_c: float) -> float:
    return L / (k * A_c)

def conductive_resistance_cyl(r_1: float, r_2: float, L: float, K: float) -> float:
    numerator: float = log(r_2 / r_1)
    denominator: float = log(2 * pi * L * K)
    return numerator / denominator

def conductive_resistance_sph(r_1: float, r_2: float, K: float) -> float:
    numerator: float = r_2 - r_1
    denominator: float = 4 * pi * r_1 * r_2 * K
    return numerator / denominator

def convective_resistance(h: float, A_s: float) -> float:
    return 1 / (h * A_s)

def series_resistance(resistances: List[float]) -> float:
    return sum(resistances)

def parallel_resistances(resistances: List[float]) -> float:
    summ: List[float] = []
    for resistance in resistances:
        summ.append(1 / resistance)
    return 1 / sum(summ)

def calculate_Q_conduction(T_1: float, T_2: float, R_conduction: float) -> float:
    return (T_1 - T_2) / R_conduction

def calculate_Q_convection(T_1: float, T_2: float, R_convection: float) -> float:
    return (T_1 - T_2) / R_convection

def calculate_Q_series(T_first: float, T_last: float, R_total: float) -> float:
    return (T_first - T_last) / R_total 

def question_():
    print()
    
def question_():
    print()

def main():
    print('hello')

if __name__ == '__main__': main()
