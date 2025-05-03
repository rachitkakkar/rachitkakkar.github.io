---
title: "How OpenGL Works"
date: 2025-02-19T17:00:00-00:00
summary: "and How to Roll Our Own"
thumbnail_image: OsakaSkyline.jpeg
thumbnail_caption: "A picture I took of the skyline in Osaka, Japan in the Summer of '24"
draft: true
---

This is some dummy text

## 1. The Big Picture: What OpenGL Does

At its core, OpenGL takes geometric data (like vertices, colors, and textures) and transforms it into a 2D image on your screen. It does this using the **GPU pipeline**, a series of stages that transform and rasterize data.

OpenGL doesn't dictate how hardware should be built, but rather provides **a specification** that hardware vendors implement in drivers. When you write OpenGL code, you're interacting with a state machine that tells the driver how to render your graphics.

## 2. OpenGL as a State Machine
OpenGL is fundamentally **a state machine**, which means it keeps track of the current state (like bound textures, shaders, buffers, etc.) and applies all rendering operations according to that state.

```
glBindTexture(GL_TEXTURE_2D, textureID);
glDrawArrays(GL_TRIANGLES, 0, 3);
```

This will draw a triangle using the currently bound texture. If you change the state before calling `glDrawArrays()`, you'll get different results.

## 3. The Graphics Pipeline
The core of OpenGL rendering is the graphics pipeline, which consists of several stages:

### Vertex Specification
Data starts as raw vertex data stored in Vertex Buffer Objects (VBOs). Each vertex typically includes:
- Position
- Normal vector
- Texture coordinates
- Color

This data is defined in arrays and sent to the GPU:
```
glBindBuffer(GL_ARRAY_BUFFER, vbo);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
```

### Vertex Shader
The vertex shader is the first programmable stage. It processes each vertex individually, typically transforming them from model space to clip space:

```
#version 330 core
layout(location = 0) in vec3 position;
uniform mat4 model, view, projection;
void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
}
```

### Primitive Assembly & Clipping
Vertices are assembled into primitives (points, lines, triangles). Primitives that lie outside the view frustum are clipped.

### Rasterization
Primitives are converted into fragments (potential pixels). Rasterization determines which screen pixels are covered by the primitive and interpolates values (like colors, normals, UVs) across those pixels.

### Fragment Shader
Each fragment is processed by the fragment shader, which calculates its final color:
```
#version 330 core
out vec4 FragColor;
void main() {
    FragColor = vec4(1.0, 0.0, 0.0, 1.0); // red color
}
```

### Per-Fragment Operations
Before writing to the framebuffer, several operations may be performed:
- Depth test
- Stencil test
- Alpha blending
- Dithering

## Buffers and Memory
OpenGL uses various buffers to manage data:

### Vertex Buffer Object (VBO)
Stores vertex data (positions, normals, etc.)

### Element Buffer Object (EBO)
Stores indices for indexed drawing, avoiding duplicate vertex data.

### Framebuffer
Stores the final rendered image. There’s a default framebuffer for on-screen rendering and custom framebuffers for off-screen rendering (FBOs).

### Uniform Buffer Object (UBO)
Stores data shared across many shaders (e.g., view/projection matrices).