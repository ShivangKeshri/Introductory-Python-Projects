import qrcode

# Base URL of your live server
base_url = "https://example-redirect-server.com"

# Define the redirect code
redirect_code = "code1"  # This can be updated dynamically

# Construct the dynamic link
dynamic_url = f"{base_url}/{redirect_code}"

# Generate the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(dynamic_url)
qr.make(fit=True)

# Save the QR code as an image
img = qr.make_image(fill="black", back_color="white")
img.save("dynamic_qr_code.png")

print(f"QR code generated! It points to: {dynamic_url}")
