#!/usr/bin/python 

import time

def get_starting_time():
    t = time.localtime()
    starting_time = time.strftime("%H:%M:%S", t)
    print(starting_time)

def job():
    print("Hello")

get_starting_time()