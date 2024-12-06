from math import exp

def calculate_Biot_number(h: float, L_c: float, k: float) -> float:
    return (h * L_c) / k

def calculate_L_c(V: float, A_s: float, t: float = None) -> float:
    if t is None:
        return V / A_s
    else:
        return t / 2
    
def calculate_b_parameter(h: float, 
                          A_s: float, 
                          rho: float, 
                          V: float, 
                          C_p: float,
                          L_c: float = None) -> float:
    if L_c is None:
        numerator: float = h * A_s
        denominator: float = rho * V * C_p
        return numerator / denominator
    else:
        return h / (rho * L_c * C_p)
    
def calculate_T_of_t_LSA(h: float, 
                         A_s: float, 
                         rho: float, 
                         V: float, 
                         C_p: float,
                         t: float,
                         T_i: float,
                         T_inf: float,
                         L_c: float = None) -> float:
    b: float = calculate_b_parameter(h, A_s, rho, V, C_p, L_c)
    exponential: float = exp(-1 * b * t)
    T_diff: float = T_i - T_inf
    return exponential * T_diff + T_inf

def calculate_Q(h: float, A_s: float, T_inf: float, T_t: float) -> float:
    T_diff: float = T_inf - T_t
    return h * A_s * T_diff

def calculate_Q_total(m: float, 
                      C_p: float, 
                      T_t_final: float, 
                      T_i: float) -> float:
    T_diff: float = T_t_final - T_i
    return m * C_p * T_diff

def calculate_Q_max(m: float, C_p: float, T_inf: float, T_i: float) -> float:
    T_diff: float = T_inf - T_i
    return m * C_p * T_diff


