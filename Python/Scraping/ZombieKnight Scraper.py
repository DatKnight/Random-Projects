from lxml import html
import requests
page = requests.get("http://thezombieknight.blogspot.co.uk")
tree = html.fromstring(page.content)

page = tree.xpath('//h3[@class="post-title entry-title"]/text()')

print(page)
