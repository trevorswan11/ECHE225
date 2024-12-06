from math import exp, log, pi
from convection_external_flow import Reynolds_D_h
import unit_conversion as uc

CONST_QS_NUSSULT_LAMINAR_CIRCULAR = 48 / 11
CONST_TS_NUSSULT_LAMINAR_CIRCULAR = 3.66

def constant_heat_flux_Q_using_A_s(q_s: float, A_s: float) -> float:
    return q_s * A_s

def constant_heat_flux_Q_using_in_out(m_dot: float, 
                                      C_p: float, 
                                      T_e: float, 
                                      T_i: float) -> float:
    return m_dot * C_p * (T_e - T_i)

def constant_heat_flux_Te_using_A_s(T_i: float, 
                                    q_s: float, 
                                    A_s: float, 
                                    m_dot: float, 
                                    C_p: float) -> float:
    numerator: float = q_s * A_s
    denominator: float = m_dot * C_p
    return T_i + numerator / denominator

def constant_heat_flux_Te_using_PL(T_i: float, 
                                    q_s: float, 
                                    P: float, 
                                    L: float,
                                    m_dot: float, 
                                    C_p: float) -> float:
    numerator: float = q_s * P * L
    denominator: float = m_dot * C_p
    return T_i + numerator / denominator

def constant_heat_flux_T_m_of_x(q_s: float, 
                           P: float, 
                           x: float, 
                           m_dot: float, 
                           C_p: float) -> float:
    return (q_s * P * x) / (m_dot * C_p)

def constant_heat_flux_T_s_of_x(T_m_of_x:float, q_s: float, h: float) -> float:
    return T_m_of_x + (q_s / h)

def constant_heat_flux_h(k_fluid: float, D: float) -> float:
    return CONST_QS_NUSSULT_LAMINAR_CIRCULAR * (k_fluid / D)

def constant_surface_temp_Q_conv(h: float, A_s: float, T_s: float, T_m_of_x) -> float:
    return h * A_s * (T_s - T_m_of_x)

def log_mean_temperature(T_e: float, T_i: float, T_s: float) -> float:
    delta_T_e = T_i - T_s
    delta_T_i = T_i - T_s
    numerator = delta_T_e - delta_T_i
    denominator = log(delta_T_e / delta_T_i)
    return numerator / denominator

def constant_surface_temp_Q_using_log_mean(h: float, 
                                           A_s: float, 
                                           log_mean_T: float) -> float:
    return h * A_s * log_mean_T

def constant_surface_temp_Q_using_in_out(m_dot: float, 
                                         C_p: float, 
                                         T_e: float, 
                                         T_i: float) -> float:
    return m_dot * C_p * (T_e - T_i)

def constant_surface_temp_T_e_using_PL(T_s: float, 
                                       T_i: float, 
                                       h: float, 
                                       P: float, 
                                       L: float, 
                                       m_dot: float, 
                                       C_p: float) -> float:
    numerator = h * P * L
    denominator = m_dot * C_p
    exponential = exp(-1 * (numerator / denominator))
    T_diff = T_s - T_i
    return T_s - T_diff * exponential

def constant_surface_temp_T_e_using_A_s(T_s: float, 
                                        T_i: float, 
                                        h: float, 
                                        A_s: float, 
                                        m_dot: float, 
                                        C_p: float) -> float:
    numerator = h * A_s
    denominator = m_dot * C_p
    exponential = exp(-1 * (numerator / denominator))
    T_diff = T_s - T_i
    return T_s - T_diff * exponential

def constant_surface_temp_T_m_of_x(T_s: float, 
                                   T_i: float, 
                                   h: float, 
                                   P: float, 
                                   x: float, 
                                   m_dot: float, 
                                   C_p: float) -> float:
    numerator = h * P * x
    denominator = m_dot * C_p
    exponential = exp(-1 * (numerator / denominator))
    T_diff = T_s - T_i
    return T_s - T_diff * exponential

def constant_surface_temp_h(k_fluid: float, D: float) -> float:
    return CONST_TS_NUSSULT_LAMINAR_CIRCULAR * (k_fluid / D)

def turbulent_flow_nussult(rho: float,
                           U_inf: float,
                           A_c: float,
                           P: float,
                           mu: float,
                           Pr: float,
                           n: float) -> float:
    Re_D = Reynolds_D_h(rho, U_inf, A_c, P, mu)
    return 0.023 * (Re_D ** (4/5)) * (Pr ** n)

def question_():
    print()
    
def question_():
    print()

def main():
    print('hello')

if __name__ == '__main__': main()
