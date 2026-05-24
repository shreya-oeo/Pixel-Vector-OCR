from PIL import Image

def analyze(h=8,b=8):
    img = Image.open("input.jpg")
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


def main():
    print("Hello from python-ocr-raw!")


if __name__ == "__main__":
    main()
