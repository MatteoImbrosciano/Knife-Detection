import hashlib
import sys

def calculate_md5(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

if len(sys.argv) != 2:
    print("Usage: python calculate_hash.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
md5_hash = calculate_md5(file_path)
print(f"L'HASH MD5 del file è: {md5_hash}")

