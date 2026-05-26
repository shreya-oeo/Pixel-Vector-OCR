from PIL import Image
import os

#4x4 Grid Comparison
def create_empty(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

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
def analyze(path, width=16, height=16):
    #img = Image.open("./characters/D.png").convert("RGBA")
    #img = img.convert('L')
    img = load_grayscale(path)
    # threshold
    bw = img.point(lambda p: 255 if p < 128 else 0)

    bbox = bw.getbbox()

    if bbox:
        img = img.crop(bbox)
    img = img.resize((h,b))
    img.save("output.png")
    pixels = list(img.getdata())
    print(pixels)

    print("Grayscale Pixel Values:\n")

    # deep copying rows of empty
    grid = create_empty(h,b)
    binaryvector = create_empty(h,b)

    for i in range(b):
        for j in range(h):
            grid[i][j] = pixels[i*h+j]
            if (grid[i][j] <= 128):
                binaryvector[i][j] = 1
            
    ## pixel vector
    #print(grid)
    return (binaryvector)


def main():
    print("Hello from python-ocr-raw!")
    chars = os.listdir('characters')
    print(chars)
    images = {}
    for i in chars:
        images.update({i:flatten(analyze('./characters/'+i))})
    cname = input("Image Name: ")
    img = flatten(analyze(cname))
    predict(img,images)


def difference(a, b):
    score = 0

    for i in range(len(a)):
        score += abs(a[i] - b[i])

    return score

def predict(vector, patterns):
    best_char = None
    best_score = float("inf")

    for char in patterns:
        score = difference(vector, patterns[char])

        print(char, score)

        if score < best_score:
            best_score = score
            best_char = char

    return best_char

def flatten(vec): 
    fin = []
    for a in vec:
        for b in a:
            fin.append(b)
    return fin

if __name__ == "__main__":
    main()
