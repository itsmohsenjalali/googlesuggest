from lxml import etree
import requests


def get_google_suggest(word):

    r = requests.get('http://www.google.com/complete/search',
                     params={'q': word, 'hl': 'en-IR', 'ie': 'utf_8', 'oe': 'utf_8', 'output': 'toolbar', 'gl': 'ir'})

    root = etree.XML(r.text)
    sugs = root.xpath('//suggestion')
    sugstrs = [s.get('data') for s in sugs]
    return sugstrs


if __name__ == "__main__":
    print(get_google_suggest("سلام"))
