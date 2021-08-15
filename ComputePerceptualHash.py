from PIL import Image, ImageFilter
from DCT import DCT
import numpy as np

def aHash(FILE): # Uses an average Hash
    img = Image.open(FILE)

    size = 8, 8
    img_resized = img.resize(size) # Reduce image size to 64 pixels

    img_greyscaled = img_resized.convert("L") # Convert to grayscale

    px = np.array(list(img_greyscaled.getdata()))
    avg_px = px.mean() # average the colors

    a = np.where(px <= avg_px, 0, 1) # if pixel below average then 0 else 1
    
    hash = int('0b' + ''.join(map(str,a)), 2) # Construct the hash
    return hash

def dHash(FILE):
    img = Image.open(FILE)
    
    size = 32, 32
    img_resized = img.resize(size) # Reduce image size to 32 x 32 pixels

    img_greyscaled = img_resized.convert("L") # Convert to grayscale
    
    px = np.resize(list(img_greyscaled.getdata()), (size))
    d = DCT(px)[:8,:8].flatten()[1:] # Only take the top 8x8 values (exclude the first term for average calc)
    
    avg_d = d.mean() # Compute the average value, excluding the first term(the DC coeficient)
    
    a = np.where(d <= avg_d, 0, 1) # if DCT value below average then 0 else 1
    
    hash = int('0b' + ''.join(map(str,a)), 2) # Construct the hash
    return hash