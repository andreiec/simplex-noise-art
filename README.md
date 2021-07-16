# Simplex Noise Art
Small python script to generate procedural art using simplex noise and random coloring. 

## How to run
1. Either fork or download the repository
2. Install pygame dependency using `npm i` command
3. Run the program

## How does it work
1. Generate an empty matrix of determined `WIDTH` and `HEIGHT`
2. Get a seed
3. For each value in the matrix, calculate the noise function at that position
4. Apply circular mask
5. Get a random color and apply it for each value (the value in the matrix represents the luminosity of the color)
6. Render image

## Examples
<p>Below you can find some examples.</p>

- **Seed 927**
<img src="/examples/927.png" alt="iamge not found" width="200">

- **Seed 404**
<img src="/examples/404.png" alt="iamge not found" width="200">

- **Seed 251**
<img src="/examples/251.png" alt="iamge not found" width="200">

- **Seed 867**
<img src="/examples/867.png" alt="iamge not found" width="200">

- **Seed 902**
<img src="/examples/902.png" alt="iamge not found" width="200">

