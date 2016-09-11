# coding: utf-8
import web

# 一个匹配目录,如果有人使用浏览器访问"/"这一级目录
# web.py框架将找到并加载 class index,从而用它来处理
# 这个浏览器请求
urls = (
    '/', 'index',
    '/cph', 'caoPH'
)

# ?
app = web.application(urls, globals())
# 它将会去 templates 路径下查找相应的HTML文件
render = web.template.render('templates/')


class index:
    def GET(self):
        greeting = "Hello World"
        # 将 templates 路径下的index.html文件作为返回值
        return render.index(greeting=greeting)
        # 用于显示另一种情况,详情看HTML文件
        # return render.index(greeting=False)


class caoPH:
    def GET(self):
        abc = "Hello CPH"
        return abc


# 判断是否以当前文件作为起始main执行程序
# 如果是,则执行当前程序,如果不是则不运行(例如被其他文件import时)
if __name__ == "__main__":
    app.run()
