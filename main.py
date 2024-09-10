from PIL import Image

# Convert text to binary
def text_to_binary(text):
    # Convert text to binary string
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

# Convert binary to image
def binary_to_image(binary_data, img_width, img_height):
    # Convert binary string to list of integers (0 or 1)
    binary_chunks = [int(b) for b in binary_data]
    
    # Create a new binary (1-bit) image
    img = Image.new('1', (img_width, img_height))
    img.putdata(binary_chunks[:img_width * img_height])  # Ensure it fits the image

    return img

# Extract binary data from image
def image_to_binary(img):
    # Get the pixel values (0 or 1) - filter only valid values
    pixels = list(img.getdata())
    
    # Convert pixel values to binary string ('0' or '1')
    binary_data = ''.join('1' if pixel > 0 else '0' for pixel in pixels)
    
    return binary_data

# Convert binary back to text
def binary_to_text(binary_data):
    # Split binary string into chunks of 8 bits
    byte_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    
    # Convert each byte chunk back to a character
    text = ''.join(chr(int(byte, 2)) for byte in byte_chunks if len(byte) == 8)
    
    return text

# Determine flexible image dimensions
def get_flexible_image_dimensions(binary_data):
    length = len(binary_data)
    img_width = int(length**0.5)
    img_height = (length + img_width - 1) // img_width  # Ensure all data fits
    return img_width, img_height

# Test: Converting text to image and back
inputData = input("Enter a String:\n")
binary = text_to_binary(inputData)

# Determine image dimensions based on binary data
img_width, img_height = get_flexible_image_dimensions(binary)

# Convert binary to image
img = binary_to_image(binary, img_width, img_height)
img.save("binary_image.png")
img.show()

# Now, recreate the text from the image
recreated_img = Image.open("binary_image.png")  # Load the saved image
recreated_binary = image_to_binary(recreated_img)  # Extract binary data
recreated_text = binary_to_text(recreated_binary)  # Convert back to text

print("Recreated text:", recreated_text)