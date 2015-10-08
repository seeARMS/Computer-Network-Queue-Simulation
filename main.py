#!/usr/bin/python

import sys

queueType = 0;
ticks = 0;
lambdaVar = 0;
L = 0;
C = 0;

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

        if queueType != 0:
                # Create K length Queue
		
		t_arrival = calc_arrival_time
		
		for i in range(0,ticks):
			arrival()
			departure()

		create_report();

def calc_arrival_time():
	u = rand(0,1) #generate random number between 0...1
	arrival_time = ((-1/lambdaVar)*log(1-u) * 1000000)
	return arrival_time

def arrival():
	if( t >= packet_arrival_time):
		packet_queue.add(new_packet)
		t_arrival=t + calc_arrival_time()
		t_departure= t+ (packet_size/transmission_rate)
		#Also need to consider packet loss case when queue is full


def departure():
	if(t>=t_departure):
		queue.pop()

def create_report():
	print("Data")

main();
