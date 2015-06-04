my_dir = 'C:/Users/c_thv/Desktop/Waste Workds/GreyRamper/EOD/payload/test/'
import os
import urllib
import re
import json
import PIL
import Image
from image_hash import dhash


urls = ["https://www.groupon.com/deals/gg-full-set-of-pique-fabric-car-seat-covers"]
pat = re.compile('<script>\s+\s+var+\s+payload+\s+=+\s+(.+?)false};+\s')


for url in urls:
    sock = urllib.urlopen(url)
    li = pat.findall(sock.read()) # payload scrapper bot
    sock.close()

    gotcha = li[0].strip(',"stickyHeader":')
    value = json.loads((gotcha+'}'))
    
    # Deal Images
    temp = []
    for i,j in enumerate(value['carousel']['dealImages']):
        temp.insert(i,j['media'])

# Image Duplicate checking Part
def get_image_from_output(out_list):
    if os.path.exists(os.getcwd() + '/test/'):
        print 'Writing in to Dir'
        for num in range(len(out_list)):
            urllib.urlretrieve(out_list[num],os.path.join(os.getcwd()+'/test/' + str(out_list[num]).split('/',-1)[4] + '.jpg'))
    else:
        print 'Creating Dir. . .'
        print 'Writing in to Dir'
        os.mkdir(os.getcwd()+'/test/')
        #os.path.join(os.getcwd(),'test')
        for num in range(len(temp)):
            urllib.urlretrieve(out_list[num],os.path.join(os.getcwd()+'/test/' + str(out_list[num]).split('/',-1)[4] + '.jpg'))

get_image_from_output(temp)

# Image Hash Checker
##rms = math.sqrt(reduce(operator.add,
##	map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

test_images = os.listdir(os.getcwd()+'/test/')
m = [os.getcwd()+'/test/'+i for i in test_images]
for i in m:
    img_hash = dhash(Image.open(i))
    dups =[dup for dup in img_hash if dup not in img_hash]
    if dups:
        print dups

#print value['productReviews']['dealTitle']
