# Code generated by font_to_py.py.
# Font: Arial.ttf Char set: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_
# Cmd: font_to_py.py Arial.ttf 9 arial9.py -x -c ABCDEFGHIJKLMNOPQRSTUVWXYZ'_
version = '0.33'
def height():
    return 9

def baseline():
    return 7

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 39

def max_ch():
    return 95

_font =\
b'\x05\x00\x70\x88\x08\x30\x20\x00\x20\x00\x00\x02\x00\x80\x80\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x10\x28\x28\x44\x7c\x44\x82\x00'\
b'\x00\x06\x00\x70\x48\x48\x78\x48\x48\x70\x00\x00\x07\x00\x38\x44'\
b'\x40\x40\x40\x44\x38\x00\x00\x07\x00\x78\x44\x44\x44\x44\x44\x78'\
b'\x00\x00\x06\x00\x7c\x40\x40\x7c\x40\x40\x7c\x00\x00\x06\x00\x78'\
b'\x40\x40\x70\x40\x40\x40\x00\x00\x07\x00\x38\x44\x40\x4c\x44\x44'\
b'\x38\x00\x00\x07\x00\x44\x44\x44\x7c\x44\x44\x44\x00\x00\x03\x00'\
b'\x40\x40\x40\x40\x40\x40\x40\x00\x00\x05\x00\x10\x10\x10\x10\x10'\
b'\x90\xe0\x00\x00\x06\x00\x44\x48\x50\x60\x50\x48\x44\x00\x00\x05'\
b'\x00\x40\x40\x40\x40\x40\x40\x78\x00\x00\x07\x00\x82\xc6\xc6\xaa'\
b'\xaa\xaa\x92\x00\x00\x07\x00\x44\x64\x64\x54\x4c\x4c\x44\x00\x00'\
b'\x07\x00\x38\x44\x44\x44\x44\x44\x38\x00\x00\x06\x00\x78\x48\x48'\
b'\x78\x40\x40\x40\x00\x00\x07\x00\x38\x44\x44\x44\x44\x48\x3c\x00'\
b'\x00\x07\x00\x78\x44\x44\x78\x48\x44\x44\x00\x00\x06\x00\x30\x48'\
b'\x40\x30\x08\x48\x30\x00\x00\x05\x00\xf8\x20\x20\x20\x20\x20\x20'\
b'\x00\x00\x07\x00\x44\x44\x44\x44\x44\x44\x38\x00\x00\x07\x00\x82'\
b'\x82\x44\x44\x28\x28\x10\x00\x00\x09\x00\x88\x80\x94\x80\x55\x00'\
b'\x55\x00\x55\x00\x55\x00\x22\x00\x00\x00\x00\x00\x05\x00\x88\x50'\
b'\x50\x20\x50\x50\x88\x00\x00\x07\x00\x44\x28\x28\x10\x10\x10\x10'\
b'\x00\x00\x06\x00\xfc\x08\x10\x20\x40\x80\xfc\x00\x00\x05\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xf8\x00'

_index =\
b'\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x16\x00\x21\x00\x2c\x00\x37\x00\x42\x00'\
b'\x4d\x00\x58\x00\x63\x00\x6e\x00\x79\x00\x84\x00\x8f\x00\x9a\x00'\
b'\xa5\x00\xb0\x00\xbb\x00\xc6\x00\xd1\x00\xdc\x00\xe7\x00\xf2\x00'\
b'\xfd\x00\x08\x01\x1c\x01\x27\x01\x32\x01\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x3d\x01\x48\x01'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)
def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 39 + 1) if oc >= 39 and oc <= 95 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 9
    return _mvfont[doff + 2:next_offs], 9, width
 