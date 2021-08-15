# pHash
Program that finds and compare perceptual hashes of two images

Requires numpy and Pillow libraries.

To compare two images 
python CompareImages.py Image1 Image2 Algorithm

Algorithm defaults to aHash. Other available algorithm is dHash which uses a DCT to hash. Hash is 64 bits.

After running will return whether two images are similar and the Hamming Distance between the two images. Images with hamming distances greater than 5 are deemed dissimilar.
