# File forensics using bash tools
### Google Code-In 2019 Task made by Fedora

## Task
```
This file has been infused with a hidden flag, using basic linux tools. You might have to install a package or two. find the git repository, download the image file, and look for the flag. if you're stuck for too long you may ask for a hint.

https://github.com/iamzubin/gci-ctf
```
### Attachment:
![binwalk.jpeg](binwalk.jpeg)

## Resolve
```binwalk.jpeg``` suggested me I should try putting this image into [binwalk](https://github.com/ReFirmLabs/binwalk) and it gave me following output:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
32985         0x80D9          Zip archive data, at least v2.0 to extract, uncompressed size: 17, name: notflag.txt
33178         0x819A          End of Zip archive, footer length: 22
```
Since then, I decided to extract ZIP Archive from this JPEG File using ```dd```.

```dd if=binwalk.jpeg of=flag.zip bs=1 skip=32985``` gave me ```flag.zip``` archive with ```notflag.txt``` file inside.
### notflag.txt content:
```
WubbaLubbaDubDub
```
And I think it is a flag.