### gimphtml2pythoncode.py 1.0

`gimphtml2pythoncode.py` converts a sprite-image, that's exported from GIMP as "HTML table", to Python code.

I'd like to create sprite-image-code for my Pygame-games with GIMP. When I create a very small new image in GIMP with a size of let's say 8x8 pixels, switch on the grid and set the pen-size to 1 pixel, I can use GIMP to draw a simple sprite-image. I'd like to export that image in a format, that's directly usable in Python-scripts, so I'd like to have an output for example like this:
```#!/usr/bin/python

spritedata = ("10111101",
              "11000011",
              "10111101",
              "01011010",
              "01111110",
              "10100101",
              "11000011",
              "00111100")```

It seems, GIMP can't directly export images to that format. But it can export to `HTML-Table`. In the dialog, diable `Create complete HTML document`, and set all borders to 0 units. If you do that, you get a file like `test.html` provided here.
You can then run `gimphtml2pythoncode.py` on it to get the output posted above.

License: GNU GPL 3.
