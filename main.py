#!/usr/bin/python

import sys
from collections import deque

queueType = 0;
ticks = 0;
lambdaVar = 0;
L = 0;
C = 0;
t_arrival = 0;
packet_arrival_time = 0;
transmissionTime = 0;

def main():
	queueType = int(input("0 for M/D/1 or K for M/D/1/K: "))
	ticks = int(input("enter tick amount: "))
	# Average number of packets generated /arrived (packets per second) 
	lambdaVar = int(input("enter lambda: "))
	# Length of a packet in bits 
	L = input("Enter L: ")
	# The service time received by a packet.
	# (Example: The transmission rate of the output link in bits per second.) 
	C = input("Enter C: ")

	q = deque() # Create Queue

	t_arrival = calc_arrival_time(); #calculate first packet arrival time
	packet_arrival_time = t_arrival;
	print ("t_arrival: " + t_arrival)
	
	packetsLost = 0
	for t in range(0,ticks):
		if not arrival(t):
			packetsLost += 1
		departure(t)

	create_report();

def calc_arrival_time():
	u = rand(0,1) #generate random number between 0...1
	arrival_time = ((-1/lambdaVar)*log(1-u) * 1000000)
	return arrival_time

def arrival(t):
	success = True
	if(t >= packet_arrival_time):
		if queueType > 0: # K size Queue
			if len(q) < queueType:
				q.appendleft(t)
			else: # packet loss case when queue is full
				success = False
		else: # Infinite Queue
			q.appendleft(t)

		packet_arrival_time = t + calc_arrival_time()
		t_departure = t + (L/C) # t + packet_size / transmission_rate
		
	return success

def departure(t):
	if( t >= t_departure):
		q.pop() # pop front of queue

def create_report():
	# NEED: Packet Delay, Server Busy Time, Server Idle Time, Average Queue Size
	print("Data")

main();
