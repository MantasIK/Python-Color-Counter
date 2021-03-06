from PIL import Image
import argparse
import json
import webbrowser

# Arguments for the script

parser = argparse.ArgumentParser(description='Find the count of pixels for each unique color in the image')
parser.add_argument('image', nargs='?', default='.', help='Image to count')

args = parser.parse_args()

image = Image.open(args.image)
colorCount = {} # hashtable / object to hold my values

imageData = image.getdata() # using pillow library to get the image data

for x in (imageData):
    if type(x) is tuple:  # if the value is a tuple ex. (1,0,0,1)
        if len(x) == 4:
          (R, B, G, Opacity) = x # unpack the tuple
          key = "({0}, {1}, {2}, {3})".format(R, B, G, Opacity) # convert the tuple into string format to easier set up JSON format keys later
          if key in colorCount:
             colorCount[key] += 1
          else:
             colorCount[key] = 1
        else:  
          (R, B, G) = x # unpack the tuple
          key = "({0}, {1}, {2})".format(R, B, G) # convert the tuple into string format to easier set up JSON format keys later
          if key in colorCount:
             colorCount[key] += 1
          else:
             colorCount[key] = 1   
    else: # if not a tuple, it will be a single integer
        key = "({0}, {1}, {2}, {3})".format(x, x, x, 1) # the data returned by pillow gives 1 integer for any (x, x, x, 1) color, so I prepped it for easy HTML usage
        if key in colorCount:
            colorCount[key] += 1
        else:
            colorCount[key] = 1
    

dataJSON = json.dumps(colorCount) # convert to JSON

# This section creates a VERY barebones HTML file and displays the image with the JSON of the colors/counts for visualization purposes.
# It is meant to be deleted and replaced with whatever you want the JSON data to be used for.

f = open('pixelCounter.html','w')

html = """
<html>
<head>
<title>PixelCounter</title>
</head>
<body>
<img src="./{img}" alt="nothing">
<p>{data}</p>
</body>
</html>""".format(img = args.image, data = dataJSON)

f.write(html)
f.close()
