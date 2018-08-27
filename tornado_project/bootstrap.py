import os
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options, define

define("port", default=8000, type=int)


class IndexHandler(RequestHandler):

        def get(self):
           # 获取get方式传递的参数
           # items = ["安静", "思念", "伤感",'运动','古风','浪漫']
           items = ["安静", "思念", "伤感",'运动','古风','浪漫']
           self.render("base1.html", title="My title", items=items,query_result = '')

        def post(self):

            song_detail = self.get_argument('song_detail')

            self.render('t.html',query_result = song_detail)


class MusicType(RequestHandler):


    def post(self, *args, **kwargs):
        song_detail = self.get_argument('song_detail')

        print(song_detail)




if __name__ == "__main__":
   settings = {

       'template_path': os.path.join(os.path.dirname(__file__), "template"),
       'static_path': os.path.join(os.path.dirname(__file__), "static"),
       # 'static_url_prefix': '/sss/',
       # 'cookie_secret': "asdasd",
       # 'xsrf_cokkies': True,

        'debug':True

   }


   app = Application([(r"/section1", IndexHandler),
                      (r"/section2", IndexHandler)




                      ],**settings



                     )

   app.listen(8000)

   IOLoop.current().start()

