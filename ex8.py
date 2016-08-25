# coding: utf-8
formatter = "%r %r %r %r"

print formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",

    # 正常它外部的输出是单引号，
    # 但如果字符串中存在单引号，则外部用双引号
    "But it didn't sing.",

    "So I said goodnight."
)
# 对于这种内部既有单引号又有双引号的情况,外部将会优先是单引号，
# 但由于字符串中又必须要输出单引号，所以字符串输出时将在单引号
# 前面输出一个转意符用于说明这是字符串中的单引号，而不是表示字
# 符串结束的单引号
print "%r" % "He said it's \"good\",but it didn't sing."

print "%r" % 'He said it\'s "good",but it didn\'t sing.'

charA = "你好"
print "%s" % charA
# %r在输出中文时会显示乱码
print "%r" % charA
# %r 打印出来的是你作为程序员写在脚本里的东西，
# 而 %s 打印的是你作为用户应该看到的东西。
