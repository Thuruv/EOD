import urllib
import re
import json
url = "https://www.groupon.com/deals/gg-005-professional-3d-teeth-whitening-kit-1"
pat = re.compile('<script>\s+\s+var+\s+payload+\s+=+\s+(.+?)false};+\s')
sock = urllib.urlopen(url)
li = pat.findall(sock.read())
sock.close()

m = li[0].strip(',"stickyHeader":')
value = json.loads((m+'}'))


# Deal Images
for i in value['carousel']['dealImages']:
	print i['media']

# Deal Title
print value['productReviews']['dealTitle']
