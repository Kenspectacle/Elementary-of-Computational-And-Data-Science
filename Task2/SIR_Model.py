import numpy as np
import matplotlib.pyplot as plt






#dS(t)/dt = - alpha * S(t) * I(t)
#dI(t)/dt = alpha * S(t) * I(t) - gamma * I(t) - beta * I(t)
#dR(t)/dt = gamma * I(t)]

#dS(t)/dt = - beta * S(t) * I(t) / N
#dI(t)/dt = beta * S(t) * I(t) / N - gamma * I(t)
#dR(t)/dt = gamma * I(t)]


def calculate_SIR(time_steps, initial_population, initial_infected_people, alpha, beta, gamma):
    S = []
    I = []
    R = []
    D = []
    dS = 0
    dI = 0
    dR = 0
    S.append(initial_population)
    I.append(initial_infected_people)
    R.append(0)
    D.append(0)
    N = initial_population
    for i in range(0, time_steps):
        #Explicit Euler Method
        dS = -alpha * S[i] * I[i]/N
        S.append(S[i] + dS)
        dI = alpha * S[i] * I[i]/N - (gamma * I[i]) -(beta * I[i])
        I.append(I[i] + dI)
        dR = beta * I[i]
        R.append(R[i] + dR)
        dD = gamma * I[i]
        D.append(D[i] + dD)
    return S,I,R,D

if __name__ == "__main__":
    alpha = 0.9
    beta = 0.012
    gamma = 0.1
    time_steps = 100
    initial_population = 10000
    initial_infected_people = 100
    S, I, R, D = calculate_SIR(time_steps, initial_population, initial_infected_people, alpha, beta, gamma)
    print(S)
    print(I)
    print(R)
    print("Hello World")
    fig, ax = plt.subplots()
    ax.plot(S, label = "Survivor")
    ax.plot(I, label = "Infected")
    ax.plot(R, label = "Recovered")
    ax.plot(D, label = "Death")
    plt.xlabel("timestep")
    plt.ylabel("population")
    ax.legend()
    plt.show()
