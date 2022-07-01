import re
import subprocess
from io import StringIO
import multiprocessing
import time
'''

這邊使用了multiprocess來進行ping多個server主機
By Kan 2021/04/16

'''
def check_alive(ip):
    result = subprocess.call('ping -w 1000 -n 1 %s' %ip,stdout=subprocess.PIPE,shell=True)  #每個process先ping一次 等待一千毫秒 一次回應
    if result == 0 : #ping的通的話
        h = subprocess.getoutput('ping '+ip)
        returnnum = h.split('平均 = ')[1]      #擷取平均
        print(' \n \033[34m%s\033[0m能ping通，延遲平均值為：%s \n' %(ip,returnnum))
        '''
        \033[34m%s\033[0m ->為顏色語法
        '''
    elif result == 1:
        with open('noreponse.txt','a') as f:
            f.write(ip)
        print('\n \033[31m%s\033[0m不能ping到 \n'%ip)
    else:
        print('something is wrong')
    
if __name__ == '__main__':
    print("--------開始批次ping ip!--------")
    with open('ip.txt','r') as f:           #ip.txt記錄所有要被ping的ip file
        for i in f:
            p = multiprocessing.Process(target=check_alive, args=(i,))
            p.start()
