import urllib, urllib2
import random
from string import ascii_letters
from xml.dom.minidom import parseString

api_key = ""

LIST_URI = "https://api.flickr.com/services/rest/"
INTERESTINGNESS_ATTRIBUTES = {
    "method": "flickr.interestingness.getList",
    "api_key": api_key
}

PHOTO_URI = "http://farm{farm}.staticflickr.com/{server}/{id}_{secret}_b.jpg"

N = 10

OUTPUT_DIR = ""

# The request
data = urllib.urlencode(INTERESTINGNESS_ATTRIBUTES)
req = urllib2.Request(LIST_URI, data)

# The response
response = urllib2.urlopen(req)
unparsed = response.read()

# Parse the response
dom = parseString(unparsed)
photo_records = [dict(photo.attributes.items()) for photo in dom.getElementsByTagName('photo')]
photo_uris = [PHOTO_URI.format(**record) for record in photo_records]

# Now fetch the top N photos and save them to the output directory
for uri in photo_uris[:N]:
    b = urllib2.urlopen(uri).read()
    filename = ''.join(random.choice(ascii_letters) for _ in range(20)) + '.jpg'
    with open(OUTPUT_DIR + filename, 'wb') as f:
        f.write(b)
