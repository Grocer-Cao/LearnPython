# coding: utf-8
import web, datetime, os
from bin import map

# 创建一个元组
urls = (
    '/', 'Index',
    '/hello', 'SayHello',
    '/image', 'Upload',
    '/game', 'GameEngine',
    '/entry', 'Entry'
)

# app是一个由web框架里的application类创建的对象
app = web.application(urls, locals())

# 没有看懂.....
# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None, 'name': 'Jedi'})
    web.config._session = session
else:
    session = web.config._session

# render是web架构中的布局信息,它传递的应该是布局信息的路径
render = web.template.render('templates/', base="layout")


# 索引页面,他只有Get方法
class Index:
    def GET(self):
        # 在templates文件夹下有很多的HTML文件,这里应该是调用了其中的index.html,下面类似
        return render.index()


# 显示欢迎界面,他有Get与Post方法
class SayHello:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="hello")
        if form.name == '':
            form.name = "Nobody"
        if form.greet == '':
            form.greet = "Hello"
        greeting = "%s, %s" % (form.greet, form.name)
        return render.hello(greeting=greeting)


# 上传页面,同样提供了Get与Post方法
class Upload:
    ''' using cgi to upload and show image'''

    def GET(self):
        return render.upload_form()

    def POST(self):
        # 获取到了这张图片
        form = web.input(myfile={})
        # web.debug(form['myfile'].file.read())
        # get the folder name
        upload_time = datetime.datetime.now().strftime("%Y-%m-%d")
        # create the folder 使用到了os的一些方法,通过这种方式来创造一个文件夹
        folder = os.path.join('./static', upload_time)
        if not os.access(folder, 1):
            os.mkdir(folder)
        # get the file name
        filename = os.path.join(folder, form['myfile'].filename)
        print (type(form['myfile']))
        # 典型文件操作
        with open(filename, 'wb') as f:
            f.write(form['myfile'].file.read())
            f.close()
        # 显示该图片
        return render.show(filename=filename)


class count:
    def GET(self):
        session.count += 1
        return str(session.count)


class reset:
    def GET(self):
        session.kill()
        return ""


class Entry(object):
    def GET(self):
        return render.entry()

    def POST(self):
        form = web.input(name="Jedi")
        if form.name != '':
            session.name = form.name
        session.room = map.START
        # session.description = session.room.description
        web.seeother("/game")


class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room, name=session.name)
        else:
            # why is there here? do you need it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        web.debug(session.room.name)
        if session.room and session.room.name != "The End" and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

# 这句放在这里是干什么用的?
if __name__ == "__main__":
    app.run()
