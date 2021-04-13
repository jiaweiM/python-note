import numpy as np


# y = wx + b
def compute_error_for_line_given_points(b, w, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]  # = points[i][0], numpy 的特殊用法
        y = points[i, 1]
        # compute mean-squared-error
        total_error += (y - (w * x + b)) ** 2
    return total_error / float(len(points))


def step_gradient(b_current, w_current, points, learingRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # grad_b = 2(wx+b-y)
        b_gradient += (2 / N) * ((w_current * x + b_current) - y)
        # grad_w = 2(wx+b-y)*x
        w_gradient += (2 / N) * x * ((w_current * x + b_current) - y)
    # update w'
    new_b = b_current - (learingRate * b_gradient)
    new_w = w_current - (learingRate * w_gradient)
    return [new_b, new_w]


def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations):
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), learning_rate)
    return [b, w]


def run():
    points = np.genfromtxt('data.csv', delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_w = 0
    num_iterations = 1000
    print(
        f"Starting gradient descent at b = {initial_b}, w = {initial_w}, error = {compute_error_for_line_given_points(initial_b, initial_w, points)}")
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print(
        f"After {num_iterations} iterations b = {b}, w = {w}, error = {compute_error_for_line_given_points(b, w, points)}")


if __name__ == '__main__':
    run()
