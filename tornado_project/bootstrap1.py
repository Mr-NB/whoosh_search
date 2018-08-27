#--**coding:utf-8**--

import os,requests,json
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options, define
import whoosh.index as index
from whoosh_search.config import indexdir_path
from whoosh import columns, fields, index, sorting
from whoosh.qparser import QueryParser,MultifieldParser,query

define("port", default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        # 获取get方式传递的参数
        # items = ["安静", "思念", "伤感",'运动','古风','浪漫']
        # items = {'One':['quiet',"安静"],'Two':['miss',"思念"] ,'Three': ['sad',"伤感"],'Four':['sport','运动'],'Five':['antiquity','古风'],'Six':['romance','浪漫']}
        items = {'One':['quiet',"安静"],'Two':['miss',"思念"] ,'Three': ['sad',"伤感"],'Five':['antiquity','古风']}
        self.render("section1.html", title="My title", items=items, query_result='')

    def post(self):
        song_detail = self.get_argument('song_detail')
        print(song_detail)
        self.render('section1.html', query_result=song_detail)

class SectionTwoHandler(RequestHandler):
    def get(self):
        # 获取get方式传递的参数
        # items = ["安静", "思念", "伤感",'运动','古风','浪漫']
        items = {'One':['music',"音乐指令",'1'],'Two':['non_music',"非音乐指令",'2'] }
        self.render("section2.html", title="My title", items=items, query_result='')

    def post(self):
        song_detail = self.get_argument('song_detail')

        self.render('section2.html', query_result=song_detail)

class SectionThreeHandler(RequestHandler):
    def get(self):


        self.render("section3.html",results = [],song_detail = '',song_num = '')

    def post(self):
        song_detail = self.get_argument('query')

        url = 'http://10.139.74.226:8080/submit'

        a = requests.post(url, params={'wish': song_detail}).text
        results = json.loads(a)
        song_num = len(results)
        if song_num==1:
            song_num = '0'

        self.render('section3.html',results = results,song_detail = song_detail,song_num = song_num)

class SectionFourHandler(RequestHandler):
    def get(self):


        self.render("section4.html",results = [],song_detail = '',song_num = '')

    def post(self):
        song_detail = self.get_argument('query')

        ix = index.open_dir(indexdir_path)
        facet = sorting.FieldFacet("comment_num", reverse=True)
        searcher = ix.searcher()

        qp = MultifieldParser(["artist_name", 'lyrics', 'music_name'], schema=ix.schema)
        q = qp.parse(song_detail)
        results = searcher.search(q, sortedby=facet)

        for r in results:

            print(r.fields())


        song_num = len(results)
        if song_num==1:
            song_num = '0'

        self.render('section4.html',results = results,song_detail = song_detail,song_num = song_num)


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

        'debug': True

    }

    app = Application([(r"/", IndexHandler),
                       (r"/section1", IndexHandler),
                       (r"/section2", SectionTwoHandler),
                       (r"/section3", SectionThreeHandler),
                       (r"/section4", SectionFourHandler),
                       (r'/musictype',MusicType)

                       ], **settings

                      )

    app.listen(8001)

    IOLoop.current().start()

