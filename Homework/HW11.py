inside = 20 # C
outside = 35 # C
dT = outside - inside # temperature

# Gypsum
t_12 = 0.01 # m
k_gypsum = 0.5 # W/mK

# Brick
t_34 = 0.10 # m
k_brick = 1.0 # W/mK

# Insulation
t_23 = 0.08 # m
k_insulation = 0.03 # W/mK

# Support
k_support = 50 # W/mK

t_tot = t_12 + t_23 + t_34

L_a = 0.60 # m
L_b = 0.005 # m
L_tot = L_a + L_b

# Areas
A_gypsum = t_12 * L_tot # m^2
A_insulation = t_23 * L_a # m^2
A_support = t_23 * L_b # m^2
A_brick = t_34 * L_tot # m^2
A_tot = L_tot * t_tot # m^2

# Conduction Resistances (Length / (k * A))
R_gypsum = t_12 / (k_gypsum * A_gypsum)
R_insulation = t_23 / (k_insulation * A_insulation)
R_support = t_23 / (k_support * A_support)
R_brick = t_34 / (k_brick * A_brick)

R_series = R_gypsum + R_brick
R_parallel = 1 / (1 / R_insulation + 1 / R_support) # 1/R_parallel = 1/R_1 + 1/R_2 + ...
R_tot = R_series + R_parallel

Q_cond = dT / R_tot
heat_flux = Q_cond / A_tot

print(heat_flux, 'W/m^2')