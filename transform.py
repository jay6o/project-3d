import numpy as np
import numpy.typing as npt

def project_vertices(a: np.ndarray, c: np.ndarray, rotation: np.ndarray) -> tuple[npt.NDArray, npt.NDArray] | None: 
    d = rotation @ (a - c).T
    e_x = 0
    e_y = 1 # vertically centered
    e_z = 300 # focal distance / projection distance
    
    # Mask for V not in view (-z)
    mask = d[2,:] > 0
    d_valid = d[:, mask]
    if len(d_valid) == 0:
        return None
    
    bx = ((e_z / d_valid[2,:]) * d_valid[0,:]) + e_x
    by = ((e_z / d_valid[2,:]) * d_valid[1,:]) + e_y

    return (bx, by)
