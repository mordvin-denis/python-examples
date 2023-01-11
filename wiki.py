# From  https://pypi.org/project/Wikipedia-API/

import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())
print("Page - Title: %s" % page_py.title)
print("Page - Summary: %s" % page_py.summary[0:60])
print("Page - Full Url: %s" % page_py.fullurl)
print("Page - Canonical Url: %s" % page_py.canonicalurl)

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" % page_missing.exists())
