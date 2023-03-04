import casadi as cas

import numpy as np

N = 50
T = 1.0
deltaT = T/N


cost = 0
cost_constraints = []

opti_prob = cas.Opti()
opti_prob.minimize(cost)
opti_prob.subject_to(cost_constraints)
