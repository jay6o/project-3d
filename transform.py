import numpy as np
from math import sin, cos

def x_rot_mat(theta: list[float | int]):
    return np.array([[1, 0, 0],
            [0, cos(theta[0]), sin(theta[0])],
            [0, -sin(theta[0]), cos(theta[0])]])

def y_rot_mat(theta: list[float | int]):
    return np.array([[cos(theta[1]), 0, -sin(theta[1])],
            [0, 1, 0],
            [sin(theta[1]), 0, cos(theta[1])]])

def z_rot_mat(theta: list[float | int]):
    return np.array([[cos(theta[2]), sin(theta[2]), 0],
            [-sin(theta[2]), cos(theta[2]), 0],
            [0, 0, 1]])

def camera_transform(a: list[float | int], c: list[float | int], theta: list[float | int]):
    xrm = x_rot_mat(theta)
    yrm = y_rot_mat(theta)
    zrm = z_rot_mat(theta)

    d = xrm @ yrm @ zrm @ (np.subtract(a, c))
    return d

def project(d, theta):
    e_x = 0
    e_y = 1 # vertically centered
    e_z = 400 # focal distance / projection distance

    b_x = ((e_z / d[2]) * d[0]) + e_x
    b_y = ((e_z / d[2]) * d[1]) + e_y
    return (b_x, b_y)

def compute_2d(a, c, theta):
    d = camera_transform(a, c, theta)

    # if it mirrors we must clip it
    if d[2] <= 0:
        return None
    return project(d, theta)


