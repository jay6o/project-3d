import numpy as np
from math import sin, cos

def x_rot_mat(theta: np.ndarray):
    return np.array([[1, 0, 0],
            [0, cos(theta[0]), -sin(theta[0])],
            [0, sin(theta[0]), cos(theta[0])]])

def y_rot_mat(theta: np.ndarray):
    return np.array([[cos(theta[1]), 0, -sin(theta[1])],
            [0, 1, 0],
            [sin(theta[1]), 0, cos(theta[1])]])

def z_rot_mat(theta: np.ndarray):
    return np.array([[cos(theta[2]), sin(theta[2]), 0],
            [-sin(theta[2]), cos(theta[2]), 0],
            [0, 0, 1]])

def camera_transform(model: np.ndarray, camera: np.ndarray, theta: np.ndarray):
    xrm = x_rot_mat(theta)
    yrm = y_rot_mat(theta)
    zrm = z_rot_mat(theta)

    d = (xrm @ yrm @ zrm @ (model - camera).T).T
    return d

def project(a: np.ndarray, c: np.ndarray, theta: np.ndarray) -> np.ndarray | None: 
    d = camera_transform(a, c, theta)
    if len(d.shape) == 1 and d[2] <= 0:
        return None


    e_x = 0
    e_y = 1 # vertically centered
    e_z = 300 # focal distance / projection distance
    if len(d.shape) == 2:
        if d[:,2] <= 0:
            return None

        b_x = (e_z / d[:, 2]) * d[:, 0] + e_x
        b_y = -((e_z / d[:, 2]) * d[:, 1]) + e_y
    else:
        b_x = (e_z / d[2]) * d[0] + e_x
        b_y = -((e_z / d[2]) * d[1]) + e_y
    return np.column_stack((b_x,b_y))

