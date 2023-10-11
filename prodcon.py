import threading
import time
 
# Shared Memory variables
CAPACITY = int(input("Enter capacity of producing and consuming:"))
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
 
# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
 
# Producer Thread Class
class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < CAPACITY:
      empty.acquire()
      mutex.acquire()
       
      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)
       
      mutex.release()
      full.release()
       
      time.sleep(1)
       
      items_produced += 1
 
# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
     
    items_consumed = 0
     
    while items_consumed < CAPACITY:
      full.acquire()
      mutex.acquire()
       
      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)
       
      mutex.release()
      empty.release()      
       
      time.sleep(2.5)
       
      items_consumed += 1
 
# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()
'''
Way to create an object of Semaphore :  
Case 1 :                                                                                                                                                                            
object_name.Semaphore()
In this case, by default value of the count variable is 1 due to which only one thread is allowed to access. It is exactly the same as the Lock concept.

Case 2 : 
object_name.Semaphore(n) 
In this case, a Semaphore object can be accessed by n Threads at a time. The remaining Threads have to wait until releasing the semaphore.
''' 
