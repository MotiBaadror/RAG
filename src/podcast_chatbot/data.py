import feedparser
from unstructured.partition.html import partition_html

podcast_atom_link = "https://api.substack.com/feed/podcast/1084089.rss" # latent space podcast
parsed = feedparser.parse(podcast_atom_link)
episode = [ep for ep in parsed.entries if ep['title'] == "RAG Is A Hack - with Jerry Liu from LlamaIndex"][0]

episode_summary = episode['summary']

parsed_summary = partition_html(text=''.join(episode_summary))

