#! /usr/bin/env python
# -*- coding:utf-8 -*-

import whoosh.index as index
from config import indexdir_path
from whoosh import columns, fields, index, sorting
from whoosh.qparser import QueryParser,MultifieldParser,query
import json
ix = index.open_dir(indexdir_path)
facet = sorting.FieldFacet("comment_num", reverse=True)
searcher = ix.searcher()

#对索引进行命名然后指定索引文件打开
# ix = index.create_in("indexdir", schema=schema, indexname="usages")
# ix = index.open_dir("indexdir", indexname="usages")

#测试索引文件是否存在
# exists = index.exists_in("indexdir")
# usages_exists = index.exists_in("indexdir", indexname="usages")

#删除文档
#删除文档通过field
# ix.delete_by_term('path', u'/a/b/c')
#删除文档通过query
#delete_by_query(query)
#
# ix.commit()
#更新索引  需要设置字段的唯一性 (设置惟一的字段必须被索引)
# schema = Schema (path=ID (unique=True),content=TEXT)
#writer.add_document(path=u"/a",content=u"the first document")
#writer.update_document(path=u"/a",content="Replacement for the first document")

#增量更新文档（通过文档的修改时间）
# modtime = os.path.getmtime(path)
#writer.add_document(path=path, content=content, time=modtime)





searchwords=u"周杰伦 我要一步一步往上爬"

# qp = QueryParser("artist_name", schema=ix.schema)
qp = MultifieldParser(["artist_name",'lyrics','music_name'], schema=ix.schema)
q = qp.parse(searchwords)
# a = list(searcher.lexicon("music_name"))
# for i in a:
#     print i
results = searcher.search(q, sortedby=facet)
#一页默认返回10

for i in results:
    print i.fields()['music_name']



#对结果进行筛选
# results = searcher.search_page(q, 1,pagelen=10)

# Only show documents in the "rendering" chapter
# allow_q = query.Term("music_name", "光阴")
# Don't show any documents where the "tag" field contains "todo"
# restrict_q = query.Term("music_name", "光阴")

# results = searcher.search(q,  filter = allow_q,mask=restrict_q)
#展示筛选的数量
# print results.filtered_count
# for i in results:
#     print i.fields()['music_name']
    # print i.fields()['music_name']
# print len(results)

