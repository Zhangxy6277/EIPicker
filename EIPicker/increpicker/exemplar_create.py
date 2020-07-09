import json
import os
import cv2
from lib.opts import opts
import copy
def create_exempalr(datadir,N):
    anno = json.load(open(os.path.join(datadir,'annotations/train.json')))
    dir = os.path.join(datadir,'images/')
    w_dir = './exemplar_dataset/'
    num1,num2=0,0
    if not os.path.exists(w_dir):
        os.makedirs(w_dir)
    if not os.path.isfile(w_dir+'exemplar.json'):
        b={}
        b['images']=[]
        b['annotations'] = []
        b['categories']=anno['categories']
    else:
        b = json.load(open(w_dir+'exemplar.json'))
        num1=b['images'][-1]['id']+1
        num2=b['annotations'][-1]['id']+1
    images=copy.deepcopy(anno['images'])
    annotation=anno['annotations']
    j=annotation[N]['image_id']
    print('---------choosing images-------------')
    k=num1
    for i in range(j+1):
        file=images[i]['file_name']
        anno['images'][i]['id'] = k
        k+=1
        b['images'].append(anno['images'][i])
        img=cv2.imread(dir+file)
        print(file)
        cv2.imwrite(w_dir+file,img)
    for i in range(len(anno['annotations'])):
        if(anno['annotations'][i]['image_id']<=j):
            anno['annotations'][i]['image_id']+=num1
            anno['annotations'][i]['id']+=num2
            b['annotations'].append(anno['annotations'][i])
    json.dump(b, open(w_dir+'exemplar.json', 'w'))

opt = opts().parse()
N=opt.sample_number
data=opt.data
print(N)
create_exempalr(data,N)

