# pyfiglet_investigation.py

import pyfiglet
f = pyfiglet.figlet_format("Python Introduction", font="slant")
print(f)

pf = pyfiglet.Figlet()

fonts = pf.getFonts()

print (fonts)

for font in fonts:
    f = pyfiglet.figlet_format(font, font=font)
    print(f)


