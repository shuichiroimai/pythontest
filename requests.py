'''
Created on 2015/10/14

@author: shuichiro.imai
'''

import requests
if __name__ == '__main__':
    dir(requests)
    r = requests.get('http://connpass.com/api/v1/event/?keyword=python')
    print(r.status_code, r.headers['content-type'])