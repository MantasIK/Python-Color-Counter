import subprocess
import sys
from PIL import Image
import argparse
import json
import webbrowser


# Ensure Pillow is installed
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package])


install_package('PIL')

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description='Count unique pixel colors in an image')
parser.add_argument('image',
                    nargs='?',
                    default='.',
                    help='Image file to process')
args = parser.parse_args()

# Open the image
image = Image.open(args.image)
colorCount = {}  # Dictionary to store color counts

# Process image data
for pixel in image.getdata():
    if isinstance(pixel, tuple):
        key = str(pixel)
    else:
        key = str((pixel, pixel, pixel, 1))
    colorCount[key] = colorCount.get(key, 0) + 1

# Convert dictionary to JSON
dataJSON = json.dumps(colorCount)

# Create an HTML file for visualization
with open('pixelCounter.html', 'w') as f:
    html = f"""
    <html>
    <head><title>Pixel Counter</title></head>
    <body>
        <img src="{args.image}" alt="Image">
        <pre>{dataJSON}</pre>
    </body>
    </html>
    """
    f.write(html)

# Open the HTML file in a web browser
webbrowser.open('pixelCounter.html')
