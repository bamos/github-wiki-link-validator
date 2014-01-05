# Github Wiki Link Validator
Ensure all internal links in a Github Wiki are valid.

Github wiki's present a unique problem for link validation because
[traditional validation](http://en.wikipedia.org/wiki/Link_rot#Combating)
is usually done by checking page response (usually for 404).
However, the default behavior of a Wiki for an invalid link
is to direct to a page creating the page, and there is currently
no option to change this.
Creating new pages like this is easy, but in large Wiki's
links become difficult to manage and can lead to difficulties
validating links.

This is a Python 3.3 script to crawl a published Github wiki and
detect internal links pointing to invalid locations.

# Dependencies.
+ Python 3.3
+ BeautifulSoup 4

# Example.

```
$ ./link-validator.py https://github.com/bamos/github-wiki-link-validator/wiki
```

+ https://github.com/bamos/github-wiki-link-validator/wiki
  + https://github.com/bamos/github-wiki-link-validator/wiki/links
  + https://github.com/bamos/github-wiki-link-validator/wiki/invalid
+ https://github.com/bamos/github-wiki-link-validator/wiki/B
  + https://github.com/bamos/github-wiki-link-validator/wiki/C
+ https://github.com/bamos/github-wiki-link-validator/wiki/Valid
  + https://github.com/bamos/github-wiki-link-validator/wiki/C
  + https://github.com/bamos/github-wiki-link-validator/wiki/D
  + https://github.com/bamos/github-wiki-link-validator/wiki/E
+ https://github.com/bamos/github-wiki-link-validator/wiki/Link-Validator-Wiki
  + https://github.com/bamos/github-wiki-link-validator/wiki/links
  + https://github.com/bamos/github-wiki-link-validator/wiki/invalid
