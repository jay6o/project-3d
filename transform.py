import numpy as np

def project(a: np.ndarray, c: np.ndarray, rotation) -> np.ndarray | None: 
    d = rotation @ (a - c).T

    e_x = 0
    e_y = 1 # vertically centered
    e_z = 300 # focal distance / projection distance
    if len(d.shape) == 2:
        if d[:,2] <= 0:
            return None

        b_x = (e_z / d[:, 2]) * d[:, 0] + e_x
        b_y = -((e_z / d[:, 2]) * d[:, 1]) + e_y
    else:
        if d[2] <= 0:
            return None
        b_x = (e_z / d[2]) * d[0] + e_x
        b_y = -((e_z / d[2]) * d[1]) + e_y
    return np.column_stack((b_x,b_y))

