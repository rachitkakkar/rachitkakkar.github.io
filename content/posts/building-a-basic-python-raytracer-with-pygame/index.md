---
title: "Building A Basic Python Raytracer With Pygame"
date: 2022-06-09T17:01:58-05:00
summary: "In this blog post, I will be detailing the process of creating a simple raytracing library using pygame. I first undertook the project in my middle school advanced coding class due to an interest in 3D rendering that emerged during quarantine."
thumbnail_image: thumbnail.png
draft: false
---
Work in progress!


{{< title >}} Introduction {{< /title >}}
In this blog post, I will be detailing the process of creating a simple raytracing library using pygame. I first undertook the project in my middle school advanced coding class due to an interest in 3D rendering that emerged during quarantine. The project was called {{< link href="https://github.com/rachitkakkar/resurgence_renderer/tree/main/Version1" >}}resurgence_renderer{{< /link >}} and served as an easy project to improve my python skills that could still generate beautiful images.
{{< line_break >}}
{{< line_break >}}
{{< title >}} Background {{< /title >}}
If you clicked on this post, you probably have a good idea of what raytracing is. In the interest of completeness, however, I will provide a basic description here. Raytracing is a form of 3D rendering that simulates realistic lighting conditions and utilizes rays that are shot out from the camera and then bounce around the scene, as well as towards the light source, which allows us to create beautiful and realistic scenes and that have accurate reflections, shadows, and other elements that are difficult and expensive to achieve accurately with traditional rasterization.
{{< line_break >}}
{{< line_break >}}
The following image better demonstrates this idea:
{{< line_break >}}
{{< line_break >}}
{{< title >}} Showcase & Code Link {{< /title >}}
....
{{< line_break >}}
{{< line_break >}}
{{< title >}} Vector Class {{< /title >}}
The code of the vector class is as follows:
{{< code_highlight >}}
from math import sqrt

class Vector3:  # Vector3 Class
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other_Vector3):  # Adding vector with another vector
        return Vector3(self.x + other_Vector3.x, self.y + other_Vector3.y, self.z + other_Vector3.z)

    def __sub__(self, other_Vector3):  # Subtracting vector with another vector
        return Vector3(self.x - other_Vector3.x, self.y - other_Vector3.y, self.z - other_Vector3.z)

    def __mul__(self, n):  # Multiplying vector with a number
        return Vector3(self.x * n, self.y * n, self.z * n)

    def __rmul__(self, n):  # Multiplying vector with a number (on the other side)
        return Vector3(self.x * n, self.y * n, self.z * n)

    def __truediv__(self, n):  # Dividing vector with a number
        return Vector3(self.x / n, self.y / n, self.z / n)

    def __str__(self):  # Representation method
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def dot_product(self, other_Vector3):  # dot product
        return self.x * other_Vector3.x + self.y * other_Vector3.y + self.z * other_Vector3.z

    def normalize(self):  # Normalize vector
        magnitude = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def negative(self):  # Multiply x, y, and z by -1
        return Vector3(self.x * -1, self.y * -1, self.z * -1)

    def to_color(self):  # Formatting to an rgb color
        r = int(self.x)
        b = int(self.y)
        g = int(self.z)

        if (r > 255): r = 255
        if (r < 0): r = 0
        if (b > 255): b = 255
        if (b < 0): b = 0
        if (g > 255): g = 255
        if (g < 0): g = 0

        return Vector3(r, b, g)

    def to_tuple(self):  # Converting to a tuple
        return (self.x, self.y, self.z)
{{< /code_highlight >}}