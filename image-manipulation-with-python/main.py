from PIL import Image
from sys import exit
from os import path, remove, listdir, chdir


def _get_input_file():
    filename = input('[?] Enter image path: ')
    try:
        img = Image.open(filename)
    except FileNotFoundError:
        exit(f'[!] File {filename} not found.')
    else:
        return img


def get_aspect_ratio(img):
    width, height = img.size
    aspect_ratio = width / height
    print(f'[i] Old image resolution: {width}x{height}')
    print(f'[i] Image aspect ratio: {aspect_ratio}')
    return aspect_ratio


def resize_image(img, aspect_ratio):
    BASE_SIZE = 400
    if aspect_ratio > 1:
        return img.resize((BASE_SIZE, int(BASE_SIZE / aspect_ratio)), Image.ANTIALIAS)
    elif aspect_ratio < 1:
        return img.resize((int(BASE_SIZE * aspect_ratio), BASE_SIZE), Image.ANTIALIAS)
    else:
        return img.resize((BASE_SIZE, BASE_SIZE), Image.ANTIALIAS)


def _save_image(img, output_file):
    quality = 95
    MAXIMUM_SIZE = 65536
    img.save(output_file, quality=100)
    out_size = path.getsize(output_file)
    while out_size > MAXIMUM_SIZE:
        try:
            remove(output_file)
            img.save(output_file, quality=quality, format='JPEG')
        except FileNotFoundError:
            pass
        out_size = path.getsize(output_file)
        quality -= 5
    print(f'[+] File {output_file} saved successfully. (JPEG Quality: {quality})')


if __name__ == "__main__":
    print("Working modes: \n"
          "[1] Single image\n"
          "[2] Whole directory")
    try:
        mode = int(input("> "))
    except ValueError:
        exit('[!] Invalid Value (expected a number)')

    if mode == 1:
        img = _get_input_file()
        aspect_ratio = get_aspect_ratio(img)
        img = resize_image(img, aspect_ratio)
        output_file = input('[?] Where do you want to save resized image? ')
        if img.format != 'JPEG':
            img = img.convert('RGB')
            filename, ext = path.splitext(output_file)
            output_file = filename + '.jpg'
        _save_image(img, output_file)

    elif mode == 2:
        dirname = input('[?] Enter images directory path: ')
        if not path.isdir(dirname):
            exit(f'[!] {dirname} is not a directory.')
        output_dir = input('[?] Enter output directory path: ')
        if not path.isdir(output_dir):
            exit(f'[!] {output_dir} is not a directory.')
        output_dir = path.abspath(output_dir)
        chdir(dirname)
        for f in listdir():
            img = Image.open(f)
            print(f'[i] {f} opened.')
            aspect_ratio = get_aspect_ratio(img)
            img = resize_image(img, aspect_ratio)
            output_file = f
            if img.format != 'JPEG':
                img = img.convert('RGB')
                filename, ext = path.splitext(f)
                output_file = filename + '.jpg'
            _save_image(img, path.join(output_dir, output_file))
