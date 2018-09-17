# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:53:06 2018

@author: Ian-A
"""
"""
import discord
import threading
import time

class Discordclient(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, token=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.client = discord.Client()
        self.token = token
        return
    def run(self):
        self.client.run(self.token)
        return

mythread = Discordclient(token=("NDg1NzgyNjg0NzMyMjI3NTk1.Dm2BWg.n2Vy6XF18PjG0S0ccUK7MrIbQPo"))
mythread.start()
while (1):
    pythoncommand= input("Command:")
    print(pythoncommand)
    if (pythoncommand == "stop"):
        break
mythread.

"""
import threading
import time
import logging
tmptime = time.time()
print(tmptime)
"""
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other things')

if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(name='blocking', 
                      target=wait_for_event,
                      args=(e,))
    t1.start()

    t2 = threading.Thread(name='non-blocking', 
                      target=wait_for_event_timeout, 
                      args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('Event is set')
    """