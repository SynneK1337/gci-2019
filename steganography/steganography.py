# Basic steganography
# Just put a hidden message at the end of the file

from sys import argv, stdout

if len(argv) < 2:
    print("Usage:")
    print("For encoding: python steganography.py -e <filename> <message>")
    print("For decoding: python steganography.py -d <filename>")

if argv[1] == "-d":
    image = bytearray(open(argv[2], "rb").read())
    eof_bytes = {'jpg': 0xD9,
                 'png': 0x44}
    file_extension = argv[2].split('.')[1]
    message = []

    for byte in image[::-1]:
        if byte == eof_bytes[file_extension]:
            break
        message.append(byte)

    for char in message[::-1]:
        stdout.write(chr(char))

elif argv[1] == "-e":
    image = open(argv[2], "ab")
    message = ' '.join(argv[3:])
    image.write(message.encode('utf-8'))