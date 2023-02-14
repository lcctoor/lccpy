# 项目描述

让Python容器（如：list）可以使用R语言风格的索引和切片。

R语言风格索引：从1开始，1表示第1个元素，-1表示倒数第1个元素。

R语言风格切片：双闭区间。如：[3: 5]表示提取第3、4、5三个元素。

# 安装、文档与源码

安装：`pip install rstyleslice`

文档：[https://www.yuque.com/lcctoor/lcctopen/rstyleslic](https://www.yuque.com/lcctoor/lcctopen/rstyleslice)

源码：[https://github.com/lcctoor/lcctopen/tree/main/rstyleslice](https://github.com/lcctoor/lcctopen/tree/main/rstyleslice)

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
from rstyleslice import rslice, rindex
```

创建R风格容器：

```
obj = rslice([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 理论上，Python中任何可以索引和切片的对象都可以转化成R风格容器
```

索引取值：

```
obj[1]
# >>> 1
```

索引赋值：

```
obj[1] = 111
obj[:]
# >>> [111, 2, 3, 4, 5, 6, 7, 8, 9]
```

切片取值：

```
obj[3:7]  # >>> [3, 4, 5, 6, 7]
obj[7:3]  # >>> [7, 6, 5, 4, 3]
obj[3:7:2]  # >>> [3, 5, 7]
obj[8:2:3]  # >>> [8, 5, 2]
```

切片赋值：

```
obj[4:6] = [44, 55]
obj[:]
# >>> [111, 2, 3, 44, 55, 7, 8, 9]

obj[4:6] = []
obj[:]
# >>> [111, 2, 3, 8, 9]

obj[4:] = [1, 2, 3, 4, 5]
obj[:]
# >>> [111, 2, 3, 1, 2, 3, 4, 5]

obj[4:100] = ['1', 2, 3, 4, 5]
obj[:]
# >>> [111, 2, 3, '1', 2, 3, 4, 5]
```

调用Python容器的原生方法：

| 代码                              |  结果  |                  解释                  |
| :-------------------------------- | :----: | :------------------------------------: |
| rslice('abcd').count('a')         |   1   |                                        |
| rslice('abcd').index('b')         |   1   |  原生index方法返回Python风格的索引值  |
| rslice('abcd').index_('b')        |   2   | 在原生方法后加"_"表示将返回值+1, 1+1=2 |
| rslice('ABCd').lower()            | 'abcd' |                                        |
| rslice('ABCd').lower().count('a') |   1   |                                        |

| 代码                                | 结果 |                                           解释                                           |
| :---------------------------------- | :--: | :--------------------------------------------------------------------------------------: |
| rslice([6,7,8,9]).pop(1)            |  7  |                               原生pop方法按Python索引取值                               |
| rslice([6,7,8,9]).pop( rindex(1) )  |  6  |                         使用rindex将R风格的索引转化成Python索引                         |
| rslice([6,7,8,9]).pop_(1)           |  8  |                          在原生方法后加"_"表示将返回值+1, 7+1=8                          |
| rslice([6,7,8,9]).pop_( rindex(1) ) |  7  | 先用rindex将R索引转化为Python索引, 然后再将返回值+1<br />相当于: [6, 7, 8, 9].pop(0) + 1 |
