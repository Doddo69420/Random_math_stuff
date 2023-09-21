#  This code uses Euler's method to show approximated solutions of Ordinary Diffferential Equations (ODEs).
#  in particular, it deals with initial value problems, sp it shows just a single solution of the ODE, connected to a
#  particular Cauchy's problem.


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import PillowWriter


def func(x, y):  # here you can define the explicit ODE
    return 0.5 * (1 - y ** 2) * np.cos(x)


def f_esatta(x):  # if the solution of the EDO is known, it's possible to define it here
    return (2 * np.exp(np.sin(x)) + 1) / (2 * np.exp(np.sin(x)) - 1)


def euler(x0, xf, y0, h):  # this functions applies Euler's method in the interval [x0, xf]
    x = np.arange(x0, xf + h, h)
    y_app = np.zeros(len(x))
    y_app[0] = y0

    for i in range(0, len(x) - 1):
        y_app[i + 1] = y_app[i] + h * func(x[i], y_app[i])  # Euler's method

    plt.figure(figsize=(12, 8))  # these next lines are purely graphic aspects.
    plt.plot(x, y_app, '--ro', label='Approssimazione')
    plt.plot(x, f_esatta(x), 'm', label='Soluzione esatta')  # if the real solution isn't known, comment this line
    plt.title('Metodo di Eulero su una semplice EDO')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()


euler(0, 2, 3, 0.1)  # a try with this particular case, but it can work with any first-order ODE.
