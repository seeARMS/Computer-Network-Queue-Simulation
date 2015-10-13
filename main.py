#!/usr/bin/python
from __future__ import division
import sys
import numpy as np

from collections import deque

_queue_type = 0;
_lambda = 0;
_L = 0;
_C = 0;
_t_arrival = 0;
_t_transmission = 0;
_currently_serving = -1;


# Statistics
_s_idle_sum = 0 # Total amount idle
_s_queue_sum = 0 # Total queue size
_s_num_loops = 0 # Counter for number of ticks processed
_s_num_delays = 0
_s_delay_sum = 0

def main():
	global _lambda
        global _queue_type
        global _L
        global _C
        global _currently_serving
        global _t_arrival
        global _t_departure
        global _q
        global _s_num_loops
        global _packets_lost

        _queue_type = int(input("0 for M/D/1 or K for M/D/1/K: "))
	ticks = int(input("enter tick amount: "))
	# Average number of packets generated /arrived (packets per second)
	_lambda = float(input("enter lambda: "))
	# Length of a packet in bits
	_L = float(input("Enter L: "))
	# The service time received by a packet.
	# (Example: The transmission rate of the output link in bits per second.)
	_C = float(input("Enter C: "))

        _t_transmission = _L / _C
        _t_departure = _t_transmission

	_q = deque() # Create Queue

        _t_arrival = calc_arrival_time(); #calculate first packet arrival time
	print ("t_arrival: ")
        print(_t_arrival)

	_packets_lost = 0
        start_simulation(ticks)
	create_report();

def start_simulation(ticks):
    global _s_num_loops
    global _s_queue_sum
    global _q

    for t in range(0,ticks):
        _s_num_loops += 1
        _s_queue_sum += len(_q)

        arrival(t)
        departure(t)

def calc_arrival_time():
	#generate random number between 0...1
	# this needs to include 1 though?
	# currently its [0, 1)
	randomNum = np.random.uniform(0,1,1)[0]
	arrival_time = ((-1 / _lambda)*np.log( 1-randomNum ) * 1000000) # lambdaVar is packets per second
	return arrival_time

def arrival(t):
    global _t_arrival
    global _queue_type
    global _t_departure
    global _t_transmission
    global _q
    global _currently_serving
    global _packets_lost

    # Check if the randomly generated arrival time has
    # passed, by decrementing
    _t_arrival -= 1
    if(_t_arrival <= 0):
        # If queue is either infinite or finite but
        # still has spots available
        if (_queue_type == 0 or len(_q) < _queue_type): # K size Queue
            #TODO(Colin_: append left?
            _q.appendleft(t)
            # if nothing is currently being serviced,
            # push to server
            if (_currently_serving == -1):
                _currently_serving = t
                # TODO(Colin): Supposed to be t + _t_transmission?
                _t_departure = _t_transmission
        else:
            _packets_lost += 1

        # t + calc_arrival_time???
        _t_arrival = calc_arrival_time()


def departure(t):
    global _q
    global _currently_serving
    global _t_departure
    global _t_transmission
    global _s_num_delays
    global _s_delay_sum

    # if the queue is not empty, proceed with servicing
    if (len(_q) != 0):
        if (_currently_serving == -1):
            _t_departure -= 1
            if (_t_departure == 0):
                _s_delay_sum += t - _currently_serving
                _s_num_delays += 1
                _q.pop()
                _currently_serving = -1
        else:
            _currently_serving = _q[0]
            _t_departure = _t_transmission

def create_report():
    global _s_idle_sum
    global _s_queue_sum
    global _s_num_loops
    global _s_delay_sum
    global _s_num_delays

    print("Average Queue Size:")
    print(_s_queue_sum / _s_num_loops)
    print("Packet Delay:")
    if _s_num_delays == 0:
        print ("No packet delay!")
    else:
        print(_s_delay_sum / _s_num_delays)
	# NEED: Packet Delay, Server Busy Time, Server Idle Time, Average Queue Size
    print("Data")

main();
