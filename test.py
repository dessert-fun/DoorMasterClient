# import threading
# from time import ctime,sleep
#
#
# def music(func):
#     for i in range(2):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print ("I was at the %s! %s" %(func,ctime()))
#         sleep(5)
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.start()
#
#     print ("all over %s" %ctime())



import datetime
import time
import threading


def setTime():
    WEEK=['一,二','三','四','五','六','日']

    while True:
        hour = datetime.datetime.now().hour
        menute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        week = datetime.datetime.now().weekday()
        week = WEEK[week]

        print(hour,menute,second,sep=':')
        time.sleep(1)

t1=threading.Thread(target=setTime)
t1.start()
print('hello world')
