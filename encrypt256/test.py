from random import randbytes
from os.path import abspath
from pathlib import Path as libpath
from encrypt256 import Encrypt256


# 字符串和字节串
plaTextList = [
    '黄', '黄河之水天上来'*100, '黄河之水天上来'*1000, '黄河之水天上来'*10000,
    randbytes(1), randbytes(100), randbytes(1000), randbytes(10000),
]

passwordList = [
    '床', '床前明月光'*100, '床前明月光'*1000, '床前明月光'*10000,
    randbytes(1), randbytes(100), randbytes(1000), randbytes(10000),
    6, 71395003615, 323167948471395003615, 3546013789103174987223167948471395003615,
]

checkSizeList = [0, 50, 100, 150, 200, 255]

for plaText in plaTextList:
    for password in passwordList:
        for checkSize in checkSizeList:
            cipText = Encrypt256(password=password).encrypt(text=plaText, checkSize=checkSize)
            NewPlaText = Encrypt256(password=password).decrypt(text=cipText)
            assert plaText != cipText
            assert plaText == NewPlaText


print('测试通过')