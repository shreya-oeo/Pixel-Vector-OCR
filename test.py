from PIL import Image
import copy

#4x4 Grid Comparison
def create_empty():
    empty = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    return empty

A = [[0,1,1,0],
     [1,0,0,1],
     [1,1,1,1],
     [1,0,0,1]]

B = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

img = Image.open("input.jpg")
img = img.convert('L')
img = img.resize((4,4))
img.save("output_4x4_grayscale.png")
pixels = list(img.getdata())
print(pixels)

print("4x4 Grayscale Pixel Values:\n")

# deep copying rows of empty
grid = create_empty()
binaryvector = create_empty()

for i in range(len(pixels)//4):
    for j in range(4):
        grid[i][j] = pixels[i*4+j]
        if (grid[i][j] <= 128):
            binaryvector[i][j] = 1
        
        
        

## pixel vector
print(grid)
print(binaryvector)
