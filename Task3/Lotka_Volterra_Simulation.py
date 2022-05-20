import numpy as np
import matplotlib.pyplot as plt


#dx/dt = alpha x - beta x y
#dy/dt = delta x y - gamma y

def Calculate_Lotka_Volterra(initial_predator, initial_prey, time_steps, alpha, beta, delta, gamma):
    prey = []
    predator = []
    prey.append(initial_prey)
    predator.append(initial_predator)
    for i in range(time_steps):
        change_of_prey = alpha * prey[i] - beta * prey[i] * predator[i]
        change_of_predator = delta * prey[i] * predator[i] - gamma * predator[i]
        prey.append(prey[i] + change_of_prey)
        predator.append(predator[i] + change_of_predator)
    return prey, predator

def main():
    alpha = 0.1
    beta = 0.02
    delta = 0.02
    gamma =  0.4
    initial_predator = 10
    initial_prey = 10
    time_steps = 200
    prey, predator = Calculate_Lotka_Volterra(initial_predator, initial_prey, time_steps, alpha, beta, delta, gamma)
    fig, ax = plt.subplots()
    print(prey)
    print(predator)
    print("hello")
    ax.plot(prey, label = "prey")
    ax.plot(predator, label = "predator")
    ax.legend()
    plt.show()

main()
