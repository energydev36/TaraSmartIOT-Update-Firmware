# add_header.py
import sys

model = b"T8i-Timer-V2".ljust(32, b'\0')
version = b"2.004".ljust(16, b'\0')

with open("firmware.bin", "rb") as f:
    bin_data = f.read()

with open("firmware_with_header.bin", "wb") as f:
    f.write(model)
    f.write(version)
    f.write(bin_data)

with open("firmware_with_header.bin", "rb") as f:
    model_bytes = f.read(32)
    version_bytes = f.read(16)

model = model_bytes.rstrip(b'\0').decode('utf-8')
version = version_bytes.rstrip(b'\0').decode('utf-8')

print("MODEL:", model)
print("VERSION:", version)