import feedparser
import subprocess
from sqlite import get_all_shows

shows = get_all_shows()

# search anime through the feed
picks = []
print("Searching Nyaa.si")
for show in [n for n in shows if n[1] != "Chobits"]:
  title = show[1].replace(' ', '+')
  episode = str(show[4]) if show[4] > 9 else '0' + str(show[4]) 
  text = title + "+" + episode
  Anime = feedparser.parse("https://nyaa.si/?page=rss&f=0&c=1_2&q=" + text + "&s=seeders&o=desc")
  # find all the entries with the episode and then download the highest seeded one dont get chobits
  clean = [n for n in Anime.entries if n.title.find(" " + episode + " ") >= 0]
  print("I pick: " + clean[0].title)
  print(clean[0])
  picks.append(clean[0])


print("Writing torrents to file...")
contents = ''
for show in picks:
  contents += show.link + "\n\tdir=C:\\Users\\Abacaxi\\Desktop\\anime\n\tseed-time=1\n"

f = open("torrents.txt", "w+")
f.write(contents)
f.close()

subprocess.call(r'aria2\aria2c.exe -i torrents.txt')

