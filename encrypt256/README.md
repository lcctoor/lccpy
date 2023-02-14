# 项目描述

一个用于加密str型和bytes型数据的加密器。

* 此包是基于pycryptodome进行二次封装，底层加密算法为AES-CBC-256。
* 加密时，会自动创建随机salt、随机iv、原始明文的校验值，并把校验值添加到密文中。
* 解密时，会自动根据校验值校验“解密得到的明文”与“原始明文”是否一致。

# 安装、文档与源码

安装：`pip install encrypt256`

文档：[https://www.yuque.com/lcctoor/lcctopen/encrypt256](https://www.yuque.com/lcctoor/lcctopen/encrypt256)

源码：[https://github.com/lcctoor/lcctopen/tree/main/encrypt256](https://github.com/lcctoor/lcctopen/tree/main/encrypt256)

# 关于作者

作者：许灿标，一个90后程序员。爱思考，爱钻研，善归纳。

更多信息：[关于作者](https://www.yuque.com/lcctoor/support/author)

个人主页：[语雀](https://www.yuque.com/lcctoor)

邮箱：lcctoor@outlook.com

微信：

![微信二维码](https://raw.githubusercontent.com/lcctoor/support/main/author/WeChatQR200_200.jpg)

交流群：目前我们有微信交流群>高质量读书会、Python技术交流，若有兴趣加入，请与我联系后获取。

# 语法预览

导入：

```
from encrypt256 import Encrypt256
```

创建加密器：

```
password1 = 123456789  # 支持int型密钥
password2 = '黄河之水天上来'  # 支持str型密钥
password3 = '床前明月光'.encode('utf8')  # 支持bytes型密钥

enctool = Encrypt256(password1)  # 创建加密器
```

加密：

```
# 加密str型数据
p1 = '人生自古谁五死'
c1 = enctool.encrypt(p1, checkSize=32)

# 加密bytes型数据
p2 = '莎士比亚'.encode('utf8')
c2 = enctool.encrypt(p2, checkSize=64)
```

解密：

```
p11 = enctool.decrypt(c1)
p22 = enctool.decrypt(c2)

assert p1 == p11
assert p2 == p22

assert type(p1) is type(p11)
assert type(p2) is type(p22)
```
