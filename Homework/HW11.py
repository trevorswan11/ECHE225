inside = 20 # C
outside = 35 # C
dT = outside - inside # temperature

# Gypsum
t_12 = 0.01 # m
t_34 = 0.10 # m

# Brick


# Insulation
k = 0.03 # W/mK
t_23 = 0.08 # m

L_a = 0.60 # m
L_b = 0.005 # m

L_tot = L_a + L_b

t_tot = t_12 + t_23 + t_34
A_c = L_tot * t_tot # m^2