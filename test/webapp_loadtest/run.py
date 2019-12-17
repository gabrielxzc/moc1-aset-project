import urllib.request
import sys
import threading
import time

def worker(num_of_requests):
	sum_time = 0
	
	for i in range(num_of_requests):
		start_time = time.time()
		contents = urllib.request.urlopen("http://127.0.0.1:5000/search?query=23").read()
		stop_stime = time.time()
		
		sum_time += stop_stime - start_time
	
	if num_of_requests > 0:
		print("avg time", sum_time / num_of_requests)

# usage: python3 run.py <number_of_requests> [number_of_threads]

num_of_requests = int(sys.argv[1])
num_of_threads = (100 if len(sys.argv) < 3 else int(sys.argv[2]))

base = num_of_requests // num_of_threads
thread_requests = [base] * num_of_threads

for i in range(num_of_requests % num_of_threads):
	thread_requests[i] += 1

threads = []
for i in range(num_of_threads):
	threads.append(threading.Thread(target = worker, args = (thread_requests[i], )))

for thread in threads:
	thread.start()
