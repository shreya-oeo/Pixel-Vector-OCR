# Python OCR Raw 🖥️

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzY4dW9zNjN5N3g3Z25jenU1NGpvMGx0ejA0N2hncGdncWs1bjF4eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5NE2L7vdWZ9V39Sjq8/giphy.gif" width="300" align="right">

A tiny OCR engine built from scratch in Python. no ML, no fancy libraries, just raw pixel comparison.

Takes an image, squishes it into a grid, turns pixels into 1s and 0s, and finds the closest match from your character templates. Simple as that.

## How it works

1. Load image → convert to grayscale → crop to bounding box → resize to NxN grid
2. Binarize pixels (threshold at 128) → create a flat binary vector
3. Compare against stored character templates using pixel difference
4. Lowest score wins → that's your prediction

## Quick start

```bash
pip install Pillow
python main.py
```

It'll load everything in `characters/`, then ask you for an image name to classify.

## Adding characters

Drop a PNG into the `characters/` folder, named after the character. Re-run and you're good.

```python
# tweak the grid size
analyze(path, h=16, b=16)
```

Bigger grid = more detail, slower. Smaller = faster, less accurate.

## Example

```
$ python main.py
Hello from python-ocr-raw!
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
Image Name: test_d.png
D 12
C 45
B 67
```

## Caveats

Works best when your input looks like your templates. Sensitive to scale, rotation, and font differences. For real OCR, go use Tesseract or a neural net.This is just a fun experiment.