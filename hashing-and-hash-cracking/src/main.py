#!/usr/bin/env python
import hashlib
from sys import argv, exit


def compute_md5_hash(input):
    md5_hash = hashlib.md5()
    md5_hash.update(input.encode('utf-8'))
    return md5_hash.hexdigest()


def compute_sha1_hash(input):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input.encode('utf-8'))
    return sha1_hash.hexdigest()


def compute_sha224_hash(input):
    sha224_hash = hashlib.sha224()
    sha224_hash.update(input.encode('utf-8'))
    return sha224_hash.hexdigest()


def compute_sha256_hash(input):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input.encode('utf-8'))
    return sha256_hash.hexdigest()


def compute_sha384_hash(input):
    sha384_hash = hashlib.sha384()
    sha384_hash.update(input.encode('utf-8'))
    return sha384_hash.hexdigest()


def compute_sha512_hash(input):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(input.encode('utf-8'))
    return sha512_hash.hexdigest()


if __name__ == "__main__":
    usage = """
            Usage:
            for encoding: python main.py --encode <algorithm> <input>
            for decoding: python main.py --decode <algorithm> <input> -w <wordlist>
    """

    if "--encode" in argv:
        algorithm = argv[argv.index("--encode")+1]
        _input = ' '.join(argv[3:])
        if algorithm == "md5":
            print(f"[+] {_input} ------> md5({compute_md5_hash(_input)})")
        elif algorithm == "sha1":
            print(f"[+] {_input} ------> sha1({compute_sha1_hash(_input)})")
        elif algorithm == "sha224":
            print(f"[+] {_input} ------> sha224({compute_sha224_hash(_input)})")
        elif algorithm == "sha256":
            print(f"[+] {_input} ------> sha256({compute_sha256_hash(_input)})")
        elif algorithm == "sha384":
            print(f"[+] {_input} ------> sha384({compute_sha384_hash(_input)})")
        elif algorithm == "sha512":
            print(f"[+] {_input} ------> sha512({compute_sha512_hash(_input)})")

    elif "--decode" in argv:
        _input = argv[3]
        algorithm = argv[argv.index("--decode")+1]
        wordlist = open(argv[argv.index("-w")+1], "r")
        if algorithm == "md5":
            calculate_hash = compute_md5_hash
        elif algorithm == "sha1":
            calculate_hash = compute_sha1_hash
        elif algorithm == "sha224":
            calculate_hash = compute_sha224_hash
        elif algorithm == "sha256":
            calculate_hash = compute_sha256_hash
        elif algorithm == "sha384":
            calculate_hash = compute_sha384_hash
        elif algorithm == "sha512":
            calculate_hash = compute_sha512_hash
        print(f"[i] Trying to decode {_input}")
        print(algorithm)
        for word in wordlist:
            print(f"[i] Trying {word[:len(word)-1]}")  # cut \n from the end of every line
            if calculate_hash(word[:len(word)-1]) == _input:
                print(f"[+] Hash decoded: {_input} ------> {word}")
