from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt

def Rosenbrock(x, y):
    a = 1
    b = 100
    return (a - x) ** 2 + b * ((y - (x ** 2)) ** 2)

def Derivatives(x, y):
    f_x = -400 * (y - x ** 2) * x - 2 * (1 - x)
    f_y = 200 * (y - x ** 2)
    return f_x , f_y

def Steepest_Gradient_Descent(step_dampener, step_multiplier, f_x, f_y, current_x, current_y):
    #compute direction step
    direction_step = [-f_x, -f_y]
    #compute multiplied step
    multiplied_step = direction_step * step_multiplier
    #compute new step multiplier
    new_step_multiplier = step_multiplier * step_dampener
    #compute new position
    new_x, new_y = [current_x + multiplied_step[0], current_y + multiplied_step[1]]
    return new_x, new_y, new_step_multiplier;

if __name__ == "__main__":
    Rosenbrock_result = []
    samples = 20
    #sample X and Y
    x = np.linspace(-1,1, num=samples)
    y = np.linspace(-1,1, num=samples)
    X, Y = np.meshgrid(x, y)
    Rosenbrock_result = Rosenbrock(X, Y)

    #plot the Rosenbrock function
    ax = plt.figure().add_subplot(projection='3d')
    ax.contour3D(X, Y, Rosenbrock_result, 500, cmap='viridis')


    #shows the plot
    plt.show()

    current_x = 0.5
    current_y = 0.5
    iteration_count = 0
    step_multiplier = 1.0
    step_dampener = 0.5
    epsilon = 0.01
    print("hello World")

    f_x, f_y = Derivatives(current_x, current_y)
    step_size_x = step_multiplier * f_x
    step_size_y = step_multiplier * f_y
    step_size_magnitude = sqrt(step_size_x ** 2 + step_size_y ** 2)
    print(step_size_magnitude)
    while(step_size_magnitude < epsilon or iteration_count < 10):
        print("Iteration Number: ", iteration_count)
        print("Current_x:", current_x)
        print("Current_y:", current_y)
        iteration_count += 1
        f_x, f_y = Derivatives(current_x, current_y)
        step_size_x = step_multiplier * f_x
        step_size_y = step_multiplier * f_y
        step_size_magnitude = sqrt(step_size_x ** 2 + step_size_y ** 2)
        current_x, current_y, step_multiplier = Steepest_Gradient_Descent(step_dampener, step_multiplier, f_x, f_y, current_x, current_y)

