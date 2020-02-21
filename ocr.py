import pytesseract
from PIL import Image
import os


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
files = os.listdir()
bads = [] #strings to ignore
ofs = open("hi.txt", "wt")
for file in files:
	if file[-3:] == ".py": continue
	if file[-4:] == ".txt": continue

	text = pytesseract.image_to_string(Image.open(file))
	text = text.split("\n")
	text = [x for x in text if len(x) > 0 and not(x.isspace())]
	ofs.write("> "+file+"\n")
	for t in text:
		if t not in bads:
			ofs.write(t+"\n")
	
	ofs.write("\n")
	print(file)
	
ofs.close()