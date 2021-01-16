from PIL import Image
import sys

img = Image.open('yourImageFile', 'r')  # just change your image file here
pix_val = list(img.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
sys.stdout=open("result.txt","w")
print (pix_val_flat)
sys.stdout.close()
