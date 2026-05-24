from PIL import Image
import copy

#4x4 Grid Comparison
def create_empty(i,j):
    l = list()
    for a in range(i):
        m = list()
        for b in range(j):
            m.append(0)
        l.append(m)
    return l

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
img = img.resize((8,8))
img.save("output_4x4_grayscale.png")
pixels = list(img.getdata())
print(pixels)

print("4x4 Grayscale Pixel Values:\n")

# deep copying rows of empty
grid = create_empty(8,8)
binaryvector = create_empty(8,8)

for i in range(len(pixels)//8):
    for j in range(8):
        grid[i][j] = pixels[i*8+j]
        if (grid[i][j] <= 128):
            binaryvector[i][j] = 1
        
## pixel vector
print(grid)
print(binaryvector)
