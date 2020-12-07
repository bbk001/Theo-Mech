from math import sin
from math import cos
import matplotlib.pyplot as plt
g=9.81

#A=a/l
#G=(g/l)*(tau_c)^2
#M=M/m

def simulator(theta,phi,timesteps,time,A,M,G):
    thetas = [theta]
    phis = [phi]
    currentStep = 0
    thetadd=0
    thetad=0
    phidd=0
    phid=0
    deltat=time/timesteps
    while currentStep<timesteps:
        theta += thetad*deltat
        thetad += thetadd*deltat
        thetadd = (-M*A*thetad*phid*sin(theta-phi)-(M+.5)*G*sin(theta)+M*A*(thetad-phid)*sin(theta-phi)*phid-M*A*phidd*cos(theta-phi))/(M+(1/3))
        phi += phid*deltat
        phid += phidd*deltat
        phidd = (thetad*phid*sin(theta-phi)-G*sin(phi)+thetad*(thetad-phid)*sin(theta-phi)-thetadd*cos(theta-phi))/(1.5*A)
        currentStep += 1
        thetas += [theta]
        phis += [phi]
    plt.plot(thetas,"r-")
    plt.plot(phis,"b-")
    plt.show()

