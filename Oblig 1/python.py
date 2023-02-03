import numpy as np
import matplotlib.pyplot as plt

#Initial variables -----------------------------------------------
height = 50
dtime = 0.01    # Vary these two based on what you need
n = 1300       #    
initTime = 0.0
C = 0.05
mass = 0.1
g = 9.81
velocity = 0
acceleration = -g
WithoutResistance = False
WithResistance = True
check = 0

#Functions -------------------------------------------------------
def calculations(height, velocity, airResistance, dtime, n):

    heightList = []
    velocityList = []
    timesList = np.linspace(initTime, n*dtime, n + 1)

    for i in range(n):
        if (height < 0):
            height = 0

        heightList.append(height)
        velocityList.append(velocity)
        gWithResistance = (C / mass) * velocity**2

        if (airResistance == True):
            modifier = gWithResistance
        else: modifier = 0

        acceleration = -g + modifier    
        velocity = velocity + acceleration * dtime
        height = height + velocity * dtime
        print(f'Height: {height}\nAccelereation: {acceleration}\nVelocity: {velocity}\n')
    return timesList, heightList, velocityList


def plot_graph(time, height, line):
    global check
    check += 1

    if (line == 'Air resistance') and (check < 2):
        x1 = time[:-1]
        y1 = height
        plt.plot(x1, y1, label=line)

    if (line == 'No air resistance') and (check >= 2):
        plt.plot(time[:-1], height, label=line)
        plt.xlabel('Time (s)')
        plt.ylabel('Height (m)')
        plt.title('Position of the ball as a function of time')
        plt.legend()
        plt.show()
            
def result_WithResistance():
    global time, height, velocity, gWithResistance
    velocity = 0
    height = 50
    time, height, velocity = calculations(height, velocity, WithResistance, dtime, n)
    plot_graph(time, height, 'Air resistance')
    
def result_WithoutResistance():
    global time, height, velocity, gWithoutResistance
    velocity = 0
    height = 50
    time, height, velocity = calculations(height, velocity, WithoutResistance, dtime, n)
    plot_graph(time, height, 'No air resistance')

    
#Program ---------------------------------------------------------
if __name__=="__main__":
    result_WithResistance()
    result_WithoutResistance()