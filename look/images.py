# coding:utf-8

import os
import time
import uuid

import falcon

def _media_type_to_ext(media_type):
    #剥离'/images/'前缀
    return media_type[6:]

def _generate_id():
    return str(uuid.uuid4())

class Resource(object):
    def on_get(self, req, resp):
        resp.body = '{"message":"Hello world"}'
        resp.status = falcon.HTTP_200

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_post(self,req,resp):
        image_id = _generate_id()
        ext = _media_type_to_ext(req.content_type)
        filename = image_id + '.' + ext
        #创建一个文件名

        image_path = os.path.join(self.storage_path, filename)
        with open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break

                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + image_id