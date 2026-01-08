# 3D Graphics Engine

https://github.com/user-attachments/assets/c709bc28-a0da-4aa5-9aed-d77376a32dc8

# Usage

```
  python
  pip install -r requirements.txt && python3 game.py
```


# Engine Overview
This 3D engine was made using perspecitve projection on a pygame window, using objects of 3D vertices and drawing them onto a 2D plane.


You can find the linear algebra that computes 2D points using 3D vertices in `transform.py`. You can also find the math behind projection [here](https://en.wikipedia.org/wiki/3D_projection).


Aside from rendering, the engine provides movement in space along the x and z axes for the camera, as well as rotation around the x and y axes (pitch and yaw).


You can load .obj files by creating a new instance of Item and pass a string of the file location. The engine will parse the file and load the vertices, however more complex assets can be intense on the cpu.


Due to the projection mirroring objects when crossing z=0, I needed to add clipping to stop mirrored objects from rendering.


Particles are scaled using the Euclidean distance formula, along with the camera's field of view to give a sense of depth.

# Features
- Perspective Projection
- Camera rotation (pitch and yaw)
- Movement in 3D space (x and z axes for now)
- Loading .obj files
- UI with players coordinates in the world
