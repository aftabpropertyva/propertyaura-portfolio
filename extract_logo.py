from PIL import Image

# Open the original image
img = Image.open('/home/ubuntu/propertyaura-portfolio/og-image.png')

# The logo is at the top center. Let's crop it.
# Based on the image view, the house logo is roughly in the top middle.
# Image size is 1536x1024 (from typical OG image sizes or similar)
# Let's get the actual size first.
width, height = img.size
print(f"Image size: {width}x{height}")

# Define the crop area for the house logo
# It's roughly in the top 30% of the image, centered.
left = width * 0.35
top = height * 0.02
right = width * 0.65
bottom = height * 0.35

logo = img.crop((left, top, right, bottom))

# Convert to RGBA if not already
logo = logo.convert("RGBA")

# Make it square
w, h = logo.size
size = max(w, h)
new_logo = Image.new("RGBA", (size, size), (255, 255, 255, 0))
new_logo.paste(logo, ((size - w) // 2, (size - h) // 2))

# Resize to standard favicon size
favicon = new_logo.resize((64, 64), Image.LANCZOS)
favicon.save('/home/ubuntu/propertyaura-portfolio/favicon.png')
print("Favicon saved as favicon.png")
