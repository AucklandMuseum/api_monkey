from urlextract import URLExtract
import urllib.requests

extractor = URLExtract()
urls = extractor.find_urls("Let's have URL stackoverflow.com as an example.")
print(urls)