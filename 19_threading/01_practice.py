# Python — 多線程 : https://medium.com/jeasee%E9%9A%A8%E7%AD%86/python-%E5%A4%9A%E7%B7%9A%E7%A8%8B-eb36272e604b

import threading
import time
from queue import Queue


def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)
    
    
def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)
    
    
def multithreading():
    q =Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)
  
  
multithreading()
