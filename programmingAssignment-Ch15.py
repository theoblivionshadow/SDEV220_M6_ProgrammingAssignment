'''15.1 Use multiprocessing to create three separate 
processes. Make each one wait a random number of 
seconds between zero and one, print the current time,
and then exit.'''

# import modules
import multiprocessing
import time
from datetime import datetime
from random import randint

#define task 1
def task1 ():
    # set random number of seconds between 0 and 1
    seconds = randint(0, 1)
    # set wait time
    time.sleep(seconds)
    # set format for time
    fmt = "%H:%M:%S"
    # get current time
    currentTime = datetime.now()
    # format current time
    cTime = currentTime.strftime(fmt)
    # print task w/ current time
    print(f"Task 1 complete at {cTime}.")

#define task 2
def task2 ():
    # set random number of seconds between 0 and 1
    seconds = randint(0, 1)
    # set wait time
    time.sleep(seconds)
    # set format for time
    fmt = "%H:%M:%S"
    # get current time
    currentTime = datetime.now()
    # format current time
    cTime = currentTime.strftime(fmt)
    # print task w/ current time
    print(f"Task 2 complete at {cTime}.")

#define task 3
def task3 ():
    # set random number of seconds between 0 and 1
    seconds = randint(0, 1)
    # set wait time
    time.sleep(seconds)
    # set format for time
    fmt = "%H:%M:%S"
    # get current time
    currentTime = datetime.now()
    # format current time
    cTime = currentTime.strftime(fmt)
    # print task w/ current time
    print(f"Task 3 complete at {cTime}.")

# main program run
if __name__ == "__main__":
    # call task functions
    task1()
    task2()
    task3()
    # set multiprocessing for task 1
    p = multiprocessing.Process(target=task1)
    # start process
    p.start()
    # end process
    p.terminate()
    # set multiprocessing for task 2
    p2 = multiprocessing.Process(target=task2)
    # start process
    p2.start()
    # end process
    p2.terminate()
    # set multiprocessing for task 3
    p3 = multiprocessing.Process(target=task3)
    # start process
    p3.start()
    # end process
    p3.terminate()