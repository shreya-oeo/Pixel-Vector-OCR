from PIL import Image,ImageOps,ImageFilter
import os

#AxB Grid Comparison
def create_empty(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def fit_to_canvas(img, size=16):
    # Crop whitespace
    bbox = img.getbbox()

    if bbox:
        img = img.crop(bbox)

    # Original dimensions
    w, h = img.size

    # Scale proportionally
    scale = min(size / w, size / h)

    new_w = int(w * scale)
    new_h = int(h * scale)

    # Resize while preserving ratio
    img = img.resize((new_w, new_h))

    # Create white canvas
    canvas = Image.new("L", (size, size), 255)

    # Center image
    x = (size - new_w) // 2
    y = (size - new_h) // 2

    canvas.paste(img, (x, y))

    return canvas

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

    # convert to grayscale
    img = img.convert("L")

    img = ImageOps.autocontrast(img) # auto contrast

    return img


# h,b
def analyze(path, width=16, height=16):

    img = load_grayscale(path)
    #img = img.filter(ImageFilter.FIND_EDGES)

    bw = img.point(lambda p: 0 if p < 128 else 255)

    inv = ImageOps.invert(bw)

    bbox = inv.getbbox()

    if bbox:
        img = img.crop(bbox)

    #img = img.resize((width, height))
    img = fit_to_canvas(img, 16)

    pixels = list(img.getdata())

    grid = create_empty(height, width)
    binaryvector = create_empty(height, width)

    for y in range(height):
        for x in range(width):

            pixel = pixels[y * width + x]

            grid[y][x] = pixel

            if pixel <= 128:
                binaryvector[y][x] = 1

    return binaryvector

def main():
    print("Hello from python-ocr-raw!")
    chars = os.listdir('characters')
    print(chars)
    images = {}
    for i in chars:
        images.update({i:flatten(analyze('./characters/'+i))})
    cname = input("Image Name: ")
    img = flatten(analyze(cname))
    
    char, confidence = predict(img, images)

    print(f"Predicted: {char}")
    print(f"Confidence: {confidence:.2f}%")


def difference(a, b):
    score = 0

    for i in range(len(a)):
        score += abs(a[i] - b[i])

    return score

def predict(vector, patterns):
    best_char = None
    best_score = float("inf")
    best_percent = 0
    for char in patterns:
        score = difference(vector, patterns[char])

        max_score = len(vector)

        similarity = 1 - (score / max_score)

        percent = similarity * 100

        print(f"{char}: {percent:.2f}%")

        if score < best_score:
            best_score = score
            best_char = char
            best_percent = percent

    print("\nPrediction:", best_char)

    return best_char, best_percent

def flatten(vec): 
    fin = []
    for a in vec:
        for b in a:
            fin.append(b)
    return fin

if __name__ == "__main__":
    main()
