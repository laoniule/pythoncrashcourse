def make_great(magiclist,greatmagiclist):
    while magiclist:
        current=magiclist.pop()
        current="the great "+current
        greatmagiclist.append(current)

def show_megicians(greatmagiclist):
    for magic in greatmagiclist:
        print(magic)

magicians=["luopang","ziwei","qianhui","duomu"]
greatmagic=[]
make_great(magicians,greatmagic)
show_megicians(greatmagic)
