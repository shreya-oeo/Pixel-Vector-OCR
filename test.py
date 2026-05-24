from PIL import Image


#4x4 Grid Comparison

empty = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

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

print("4x4 Grayscale Pixel Values:\n")

for i in range(0, 16, 4):
    print(pixels[i:i+4])