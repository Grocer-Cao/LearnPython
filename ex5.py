# coding: utf-8
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % \
      (age, height, weight, age + height + weight)

# ++++++++++++++++++++++++++附加题++++++++++++++++++++++++++++++
print "=====================附加题==================="
# Python的所有格式化字
# %c        转换成字符（ASCII 码值，或者长度为一的字符串）
charA = 65
print "65使用%%c输出：%c" % charA
# %s        优先用str()函数进行字符串转换
text = "I am %d years old." % 24
print "I said: %s." % text
# %r        优先用repr()函数进行字符串转换（Python2.0新增）
print "I said: %r." % text
# %r打印时能够重现它所代表的对象
# rper() unambiguously recreate the object it represents
#
# %d/%i     转成有符号十进制数
# %u        转成无符号十进制数
Num1 = 0xFF
print "0xFF转化成十进制分别为：%u和%d" % (Num1, Num1)
# %x/%X     转成无符号十六进制数（x/X代表转换后的十六进制字符的大小写）
# %#x/%#X   加井号可以自动补全0x/0X
Num2 = 251
print "251转化为十六进制分别为：%#x和%#X" % (Num2, Num2)
# %e/%E     转成科学计数法（e/E控制输出e/E）
Num3 = 12000
print "12000转化为科学技术法分别为：%e和%E" % (Num3, Num3)
# %f/%F     转成浮点数（小数部分自然截断）
Num4 = 123
print "123转化为浮点数分别为：%f和%F" % (Num4, Num4)
# %g/%G     %e和%f / %E和%F 的简写
print "12000转化为科学技术法分别为：%g和%G" % (Num3, Num3)
print "123转化为浮点数分别为：%g和%G" % (Num4, Num4)
# %%	    输出%
#
# %[(name)][flags][width].[precision]typecode
# (name)为命名
# flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。
#      ' '为一个空格，表示在正数的左侧填充一个空格，
#      从而与负数对齐。0表示使用0填充。
# width表示显示宽度
# precision表示小数点后精度
Num5 = 123.1415
print "规定输出格式：% 19.2f" % Num5
# -------------------------------------------------------------
