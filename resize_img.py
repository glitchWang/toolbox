#-*-coding: utf-8-*-

"""
刘鑫-MarsLiu
今天的问题是你有一个目录，装了很多照片，把它们的尺寸变成都不大于iphone5分辨率的大小#每天一个小程序#
1136 x 640
"""
import os, Image, sys

res = {
    "ip5" : (1136, 640),
    "ip4" : (960, 640),
}

def t(src_img, frame_size):
    w, h = src_img.size
    src_img.thumbnail(frame_size) \
        if w >= h else src_img.thumbnail(tuple(reversed(frame_size)))
    return src_img

def transform(src, model="ip5"):
    try:
        src_img = Image.open(src)
        dst_img = t(src_img, res[model])
        fname, ext = src[0:src.rindex(".")], src[src.rindex(".")+1:]
        dst_img.save("%s.%s.%s" % (fname, model, ext), "JPEG")
    except IOError, e:
        print(e)
    
def transform_dir(basedir, model="ip5"):
    for root,dirs, files in os.walk(basedir):
        for f in files:
            if not (".%s." % model) in f:
                print(f)
                transform(os.path.join(root, f), model)

if __name__ == '__main__':
    basedir, model = sys.argv[1], sys.argv[2]
    transform_dir(os.path.abspath(basedir), model)
