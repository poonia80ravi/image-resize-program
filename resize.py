from PIL import Image
from sys import argv

n = int(argv[1])
infile = argv[2]
outfile = argv[3]

inimage = Image.open(infile)
width, height = inimage.size
outimage = inimage.resize((300, 300))
outimage.save(outfile)
