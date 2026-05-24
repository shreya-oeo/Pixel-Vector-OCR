from PIL import Image

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

def load_grayscale(path):
    # Open image
    img = Image.open(path)

    # Handle PNG transparency properly
    if img.mode in ("RGBA", "LA"):
        # Convert to RGBA
        img = img.convert("RGBA")

        # White background
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))

        # Merge image with background
        img = Image.alpha_composite(bg, img)

    # Convert everything to grayscale
    img = img.convert("L")

    return img


# h,b
def analyze(h=8,b=8):
    img = Image.open("./characters/D.png").convert("RGBA")
    img = img.convert('L')
    img = img.resize((h,b))
    img.save("output.png")
    pixels = list(img.getdata())
    print(pixels)

    print("Grayscale Pixel Values:\n")

    # deep copying rows of empty
    grid = create_empty(h,b)
    binaryvector = create_empty(h,b)

    for i in range(len(pixels)//h):
        for j in range(h):
            grid[i][j] = pixels[i*h+j]
            if (grid[i][j] <= 128):
                binaryvector[i][j] = 1
            
    ## pixel vector
    print(grid)
    print(binaryvector)

analyze(8,8)