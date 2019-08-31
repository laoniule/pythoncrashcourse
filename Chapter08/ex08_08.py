#!/usr/bin/python


def make_album(artist, album, nums=""):

    album = {'artist': artist, 'album': album}
    if nums:
        album['nums'] = nums
    return album


print("\nInput your favorite artist and album.")
print("INput 'T' to exit.")

while True:
    artist = input("your favorite artist is:  ")
    if artist == "t":
        break
    else:
        album = input("your favorite artist's album is: ")
        if album == "t":
            break
        else:
            nums = input("how many songs are there in this album?")
            if nums == "t":
                break
            else:
                artistAlbum = make_album(artist, album, nums)
                print(artistAlbum)
