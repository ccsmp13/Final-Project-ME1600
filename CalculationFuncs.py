import numpy as np
from numpy.polynomial import Polynomial as ply


# #Air Resistance calc 
# def air_Res(p,v,cd,a):
#     Ra=.5*p*(v**2)*cd*a
#     return Ra

# #Grade Load 
# def grade_load(Wo,Gp):
#     Gl=Wo*Gp
#     return Gl

# #Rrolling Calc
# def Rrolling (f,W,a):
#     rrolling = f*W*np.cos(a)
#     return rrolling

# #Road Load
# def roadload(rrolling,Gl,Ra):
#     R = rrolling+Gl+Ra

# #torque at the differential 
# def torque_diff(tw,nw):
#     td=tw*nw
#     return td

# #Total Traction
# def total_traction(td,r):
#     P = td/r
#     return P

# #angular velocity of the driving wheel
# def ang_vel(v,r):
#     Ww= v/r



def fitDyno(rpm, torque):
    torquePoly = ply.fit(rpm, torque, 2)
    return torquePoly
