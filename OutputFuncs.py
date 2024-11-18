import matplotlib.pyplot as plt
import numpy as np




def plotDyno(rpm, torque, torquePoly):
    plt.subplot(2,2,1)
    x = np.linspace(rpm[0],rpm[len(rpm) - 1], 10000)
    y = torquePoly(x)
    plt.plot(x,y,'b--' )
    plt.plot(rpm, torque, 'r*')
    plt.show()