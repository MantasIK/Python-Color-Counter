# Python Pixel Color Counter

---

I've been wanting to try out **Python** for a while now and this was my first time getting my hands wet with it.

The script takes an image as an argument and counts all unique color pixels and their quantity before converting it to _JSON_ for easy use with anything else.

I found many cool ways on how to build a color pixel counter but wanted to make mine unique in order to understand **Pythons** syntax better.

To use the script, simply call the colorCounter.py file with the image file name you want processed:

_use the python3 command unless you created an alias_

```
python colorCounter.py exampleImage.jpg
```

The script will create an **HTML** file with the image and **JSON** underneath for demonstration purposes.
This idea is to change:

```
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
```

to anything that suits your needs since at this point the **JSON** is stored in `dataJSON`
