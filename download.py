
# -*- coding: utf-8 -*-
import requests
import os
import time
import datetime


def get_content(url):
    """
    得到API返回的JSON数据
    :param url: API链接
    :return: 返回的是一个字典
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()
    except:
        print("ERROR")


def get_img(url):
    """
    得到图片的内容
    :param url: 图片的真实链接
    :return: 返回的是byte类型的图片内容
    """
    try:
        r = requests.get(url)
        return r.content
    except:
        return None


def download(file_name, url, paths):
    if os.path.exists(paths + '\\' + file_name):
        print('Image downloaded already')
    else:
        img = get_img(url)
        with open(paths + '\\' + file_name,
                  'wb') as f:
            f.write(img)
        #print('Download success')
    

if __name__ == '__main__':

    years = datetime.datetime.now().year
    months = datetime.datetime.now().month  
    days = datetime.datetime.now().day
    paths = 'C:\Github\PythonBing\images' + '\\' + str(years) + '\\' + str(months) + '\\' + str(days)
    #print(paths)
    if os.path.exists(paths):
        print('Find Dir...')
    else:
        print("File dir did not exist, make dir...")
        try:
            os.makedirs(paths)
            print('makedirs dir success')
        except:
            print('Failed makedirs')
    if os.path.exists(paths):
        if os.path.exists(paths + '\\' + 'url.txt'):
            print('url.txt exists')
        else:
            with open(paths + '\\' + "url.txt", mode='w') as ff:
                print("文件创建成功！")
    else:
        exit
    
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    content = get_content(url)
    url_dict = content['images'][0]
    print(url_dict)
    pre_download_url = 'https://www.bing.com' + url_dict['urlbase']
    
    resolutions = [
        '1920x1200',
        '1920x1080',
        '1366x768',
        '1280x768',
        '1024x768',
        '800x600',
        '800x480',
        '768x1280',
        '720x1280',
        '640x480',
        '480x800',
        '400x240',
        '320x240',
        '240x320'
    ]
    
    with open(paths + '\\' + 'url.txt',"w") as f:
        for img in resolutions:
            f.writelines(pre_download_url + '_' + img + ".jpg" +'\n')   
  
    for img in resolutions:
        file_name = str(time.strftime('%Y%m%d%M%S',
                                                     time.localtime(time.time())) + "_" + img +'.jpg')                                 
        
        #print(file_name)
        download_url = pre_download_url + '_' + img + ".jpg";
        download(file_name, download_url, paths)
    
    

