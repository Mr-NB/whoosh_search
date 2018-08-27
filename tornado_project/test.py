import json,traceback


with open('All_Songs.json','r') as songs:
    song_list  = songs.readlines()
    a = 0
    for  i in song_list:
        try:
            if not 'TaiheHot' in i:
                continue
            b = json.loads(i)
            # Name = b['Name']
            # AlbumName = b['AlbumName']
            # Lyric = b['Lyric']['Content']
            # Source = b['Source']['From']
            # ArtistName = b['ArtistName']
            # if Lyric == '':
            #
            #     continue
            #
            # print(Name,AlbumName,Lyric,Source,ArtistName)
            SongName = b['SongName']
            Lyric = b['Lyric']
            SingerName = b['SingerName']
            Comment_num = b['TaiheHot']['Comment']
            Listen_num = b['TaiheHot']['Listen']

            a+=1
        except Exception as e:
            continue
    print(a)
