#!/usr/bin/python


def make_album(artist, album, nums=""):


    album = {'artist':artist, 'album':album}
    if nums:
        album['nums'] = nums
    return album

artistAlbum=make_album("Michael Jackson","Bad",nums=11)
print(artistAlbum)
