from ComputePerceptualHash import aHash, dHash
from HammingDistance import hammingRatio
import sys

def compareFiles(file1, file2, method = 'aHash'):
    if method == 'aHash':
        hash1 = aHash(file1)
        hash2 = aHash(file2)
    elif method == 'dHash':
        hash1 = dHash(file1)
        hash2 = dHash(file2)
    else:
        return 'Invalid method'
    
    similar, hd = hammingRatio(hash1, hash2, 64)
    if similar:
        print(file1 + " was found to be similar to " + file2 + " with a Hamming Distance of {} using ".format(hd) + method + " method")
    else:
        print(file1 + " was found to not be similar to " + file2 + " with a Hamming Distance of {} using ".format(hd) + method + " method")
        

if (len(sys.argv) == 3):
    compareFiles(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    compareFiles(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    raise Exception("Incorrect number of arguments")

'''        
og_file = "Unity.jpg"
compareFiles(og_file, "Unity-Blurred.jpg")
compareFiles(og_file, "Unity-Sharpened.jpg")
compareFiles(og_file, "Unity-Embossed.jpg")
compareFiles(og_file, "InkedUnity.jpg")

compareFiles(og_file, "Unity-Blurred.jpg", method = 'dHash')
compareFiles(og_file, "Unity-Sharpened.jpg", method = 'dHash')
compareFiles(og_file, "Unity-Embossed.jpg", method = 'dHash')
compareFiles(og_file, "InkedUnity.jpg", method = 'dHash')
'''




