# -*- coding:utf-8 -*-
import re,json
import os
from config import db_path,indexdir_path
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT, NUMERIC,NGRAMWORDS
from whoosh.index import create_in
from jieba.analyse import ChineseAnalyzer
analyzer = ChineseAnalyzer()



if not os.path.exists(indexdir_path):
    os.mkdir(indexdir_path)





schema = Schema(artist_name=TEXT(stored=True,analyzer=analyzer),
                       music_name=TEXT(stored=True,analyzer=analyzer),
                       album_name=TEXT(stored=True,analyzer=analyzer),
                       lyrics=TEXT(stored=True,analyzer=analyzer),
                       comment_num=NUMERIC(stored=True,sortable=True),
                       listen_num=NUMERIC(stored=True,sortable=True))

ix = create_in(indexdir_path, schema)
writer = ix.writer()

with open('All_Songs.json','r') as songs:
    song_list  = songs.readlines()
    index = 0
    for  i in song_list:
        try:
            if not 'TaiheHot' in i:
                continue
            b = json.loads(i)

            SongName = b['SongName']
            Lyric = b['Lyric']
            SingerName = b['SingerName']
            Comment_num = b['TaiheHot']['Comment']
            Listen_num = b['TaiheHot']['Listen']


            index+=1

            writer.add_document(artist_name=SingerName, music_name=SongName,
                                lyrics=Lyric, comment_num=Comment_num, listen_num=Listen_num)
            print(index)
        except Exception as e:
            continue
    print('all index is {}'.format(index))


writer.commit()
