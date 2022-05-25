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

# def Steepest_Gradient_Descent(step_dampener, step_multiplier, f_x, f_y):
#     return 0

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
    #while(step_size < 0.5 || iteration_count < 10):

