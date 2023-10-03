import qrcode
img=qrcode.make("https://www.timetravelturtle.com/visiting-taj-mahal-india/")
img.save("tajmahal.img")

img=qrcode.make("https://www.thoughtco.com/who-designed-the-statue-of-liberty-1991696")
img.save("sol.img")