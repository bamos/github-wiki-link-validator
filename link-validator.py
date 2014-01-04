#!/usr/bin/env python3.3
#
# link-validator.py
# Brandon Amos <http://bamos.io>

import argparse
import re
from urllib.request import urlopen
from urllib.parse import urljoin,urldefrag
from bs4 import BeautifulSoup, SoupStrainer

baseUrl = None
invalidWikiPages = []
visitedUrls = []

def validate(url):
  if url in visitedUrls: return

  visitedUrls.append(url)
  try:
    content = urlopen(url).read().decode("utf8")
  except:
    # Assume the content is binary.
    return

  wikiUrls = []
  invalidUrls = []
  for externalUrl in BeautifulSoup(content, parse_only=SoupStrainer('a')):
    if externalUrl.has_attr('href'):
      fullExternalUrl = urljoin(url, urldefrag(externalUrl['href']).url)
      if baseUrl in fullExternalUrl and \
          not fullExternalUrl.endswith('/_history'):
        wikiUrls.append(fullExternalUrl)
        if externalUrl.has_attr('class') and 'absent' in externalUrl['class']:
          invalidUrls.append(fullExternalUrl)

  if len(invalidUrls) > 0:
    invalidWikiPages.append((url, invalidUrls))

  for wikiUrl in wikiUrls:
    if wikiUrl not in visitedUrls:
      validate(wikiUrl)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('url', type=str,
      help='The base link to the GitHub Wiki to scrape. ' +
      'Example: http://github.com/bamos/github-wiki-link-validator/wiki')
  args = parser.parse_args()

  baseUrl = args.url
  validate(args.url)

  for url, invalidUrls in invalidWikiPages:
    print("+ [[ " + url + " ]]")
    for invalidUrl in invalidUrls:
      print(" + [[ " + invalidUrl + " ]]")
