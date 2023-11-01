### gimphtml2pythoncode.py 1.0

This script converts a sprite-image, that has been exported from GIMP as "HTML-Table", to Python code.

I'd like to create sprite image code for my Pygame-games with GIMP. When in GIMP I

- create a very small new image in GIMP with a size of let's say 8x8 pixels,
- configure the grid (in the menu "Image") and switch it on (in the menu "View"), and
- set the pen to a single pixel and the pen size to 1 pixel,

I can use GIMP to draw a simple sprite-image (see [this video tutorial](https://www.youtube.com/watch?v=PONe4IIYSnQ) by a user named `Matej Jan` for further information on using GIMP for pixel-art). I'd like to export that image in a format, that's directly usable in Python-scripts. So I'd like to have a program output for example like this:
```
#!/usr/bin/python

spritedata = ("10111101",
              "11000011",
              "10111101",
              "01011010",
              "01111110",
              "10100101",
              "11000011",
              "00111100")
```

It seems, GIMP can't directly export images to that format. But it can export to `HTML-Table`. In the saving dialog, disable `Create complete HTML document`, and set all borders to 0 units. If you do that, you get a file like `test.html` provided here.
You can then run `gimphtml2pythoncode.py` on it to get the output posted above.

License: GNU GPL 3.
