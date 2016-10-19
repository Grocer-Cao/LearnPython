import falcon
import images

api = application = falcon.API()

images = images.Resource("/Users/oscarcao/PycharmProjects/LearnPython/look")
api.add_route('/images',images)