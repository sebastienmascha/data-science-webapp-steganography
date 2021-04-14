# Steganography Tools

**Authors:** Sébastien Mascha & Thomas Le Couédic

## Installation

`pip install steganography-tools`

## References

### Module: Steganography for Image, Sounds, Text

**Available formats**
- PNG
- JPEG

**Importation**

`from steganography_tools import st`

**Usage**

```
# Encoding
steg = st.LSBSteganography(cv2.imread("image.jpg"))
img_encoded = steg.encode_text("my message")
cv2.imwrite("image_enc.png", img_encoded)
plt.imshow(img_encoded)

# Decoding
im = cv2.imread("image_enc.png")
steg = st.LSBSteganography(im)
print("Text value:",steg.decode_text())
```

**Compare original and encoded images**

```
original = cv2.imread('image.jpg')
lsbEncoded = cv2.imread("image_enc.png")
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
lsb_encoded_img = cv2.cvtColor(lsbEncoded, cv2.COLOR_BGR2RGB)

compare_images = st.Compare(original, lsb_encoded_img)
compare_images.get_results()
```

### Module: Image processing

**Importation**

`from steganography_tools import image_processing as st_processing`

**Usage**

```
TEST_PHOTO = "image.jpg"

# This function allows us to get the basic information of an image
st_processing.img_information(TEST_PHOTO)

# Check for potential metadata
st_processing.get_metadata(TEST_PHOTO)

# TRANSFORMATION

st_processing.rgb2grayscale(TEST_PHOTO_GRAYSCALE)

TEST_PHOTO = cv2.imread(TEST_PHOTO) 
print("Type: ",type(TEST_PHOTO))
TEST_PHOTO = TEST_PHOTO[:,:,0]

st_processing.plot_histogram(TEST_PHOTO)
st_processing.thresholding(TEST_PHOTO, 55)

# Left to right : grayscale image | contrast increased
st_processing.display_images(TEST_PHOTO)

# Image manipulation and numpy arrays
st_processing.image_manipulation("image_grayscale.jpg")

# Geometrical transformations
st_processing.geo_transfomation(TEST_PHOTO)

# Blurring
st_processing.blurring(TEST_PHOTO)

# Sharpenning
st_processing.sharpenning(TEST_PHOTO)

# Denoising
st_processing.denoising(TEST_PHOTO)
```

## CLI

```
Command Line Arguments:
 -h, --hide                      To hide data in an image file
 -r, --recover                   To recover data from an image file
 -i, --input TEXT                Path to an bitmap (.bmp or .png) image
 -s, --secret TEXT               Path to a file to hide in the image
 -o, --output TEXT               Path to an output file
 --help                          Show this message and exit.
```