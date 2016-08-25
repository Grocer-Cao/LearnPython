# coding: utf-8
# 输出字符串
print "Mary had a little lamb."
# 输出字符串,snow是一个字符串而非变量
print "Its fleece was white as %s." % 'snow'
# 输出字符串
print "And everywhere that Mary went."
# 输出点“.”输出10遍
print "." * 10  # what'd that do?

# 变量赋值
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happends
# 组合输出
print end1 + end2 + end3 + end4 + end5 + end6
# 组合输出
print end7 + end8 + end9 + end10 + end11 + end12

# 附加题中的逗号输出,注意逗号后输出会自动空一格（且仅有一格）
print end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12
