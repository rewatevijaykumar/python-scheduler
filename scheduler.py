import schedule
import os
from time import time

def job():
    os.system('python run.py')
    print(time())

schedule.every().minute.do(job)

while(True):
    schedule.run_pending()