import feedparser

rss_url = input("Enter an RSS feed URL: ")

def show_rss(rss_url):
  try:
    rss = feedparser.parse(rss_url)

    print(rss.channel.title)

    items = rss.entries

    for item in items:
      print("-----------")
      print(item.title)
      print(item.description)
  except Exception as error:
    print("There was a problem processing the RSS feed:")
    print(error)
    print("Please check the address of the RSS feed.")

show_rss(rss_url)