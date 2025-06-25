import feedparser

TECH_RSS_URL = (
    "https://news.google.com/rss/headlines/"
    "section/topic/TECHNOLOGY?hl=en-US&gl=US&ceid=US:en"
)

def get_tech_news():
    """Return a list of latest tech headlines from Google News RSS."""
    feed = feedparser.parse(TECH_RSS_URL)
    # each entry has .title, .link, .published, etc.
    return feed.entries
