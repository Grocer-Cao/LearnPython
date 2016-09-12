# coding: utf-8
import web

# 一个匹配目录,如果有人使用浏览器访问"/"这一级目录
# web.py框架将找到并加载 class index,从而用它来处理
# 这个浏览器请求
urls = (
    '/', 'index',
    '/cph', 'caoPH',
    '/hello', 'hello',
    '/fillform', 'fillform'
)

# ?
app = web.application(urls, globals())
# 它将会去 templates 路径下查找相应的HTML文件
# 通过增加 base 项来使他作为其它模板的基础模板
render = web.template.render('templates/',base="layout")


class index(object):
    def GET(self):
        greeting = "Hello World"
        # 将 templates 路径下的index.html文件作为返回值
        return render.index(greeting=greeting)
        # 用于显示另一种情况,详情看HTML文件
        # return render.index(greeting=False)


class caoPH(object):
    def GET(self):
        abc = "Hello CPH"
        return abc


class hello(object):
    def GET(self):
        # web.input中的变量名字可以随便取,不一定非要叫name
        # 在浏览器中输入 http://0.0.0.0:8080/hello?name=Oscar&greet=Hola
        # 这样就可以实现包含多个参数
        form = web.input(name="Nobody", greet=None)
        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            # 回传给HTML文件时也可以实现多参数会传
            return render.hello(greeting=greeting, another="Another line")
        else:
            return "ERROR: greet is required."


class fillform(object):
    def GET(self):
        return render.fform()

    def POST(self):
        # 下文中的name与greet与fform.html文件中input中的名字相对应
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.hello(greeting=greeting, another="Another line")


# 判断是否以当前文件作为起始main执行程序
# 如果是,则执行当前程序,如果不是则不运行(例如被其他文件import时)
if __name__ == "__main__":
    app.run()
