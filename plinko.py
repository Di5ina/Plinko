
#from numpy import random
import numpy

"""
This program will run monte-carlo simulation of a set number of games of plinko
It will provide detailed statistics on return to player (RTP) and how often
1000x hits take
"""

num_games = 15000000
bet = 1000
rtp = 0

#for tracking how often we hit 1000x bonuses
big_wins = list()
last1000x = -1
max1000x = -1
min1000x = -1

#For reference
gates = [   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,   16]
payit = [1000, 130,  26,   9,   4,   2, 0.2, 0.2, 0.2, 0.2, 0.2,   2,   4,   9,  26, 130, 1000]

#Tracking how many balls drop in each bracket
winit = [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,    0]

#Variables for tracking statistics in a rolling range
#the idea is to see what the biggest win streaks and
#loss streaks exist in a larger simulation.
rolling_sample_range = 300000
rolling_rtp = list()
rolling_rtp_sum = 0.0
rtp_min = 999999999999999999.9
rtp_max = 0.0
rolling_big_wins = list()
rolling_big_wins_min = 9999999999
rolling_big_wins_max = 0

try:
	print("1000x:")
	for i in range(num_games):
		x = 0 # variable for storing results of coin flips

		# initialize the min/max tracking variables once we get to the range
		if i == rolling_sample_range:
			rolling_big_wins_min = len(rolling_big_wins)
			rolling_big_wins_max = len(rolling_big_wins)

		# flip 16 coins and record the results
		for _ in range(16):
			x += numpy.random.choice([0,1])

		#Record which gate the ball went through
		winit[x] += 1

		#Did we win big?
		if x == 0 or x == 16:
			print( i )
			big_wins.append( i )
			rolling_big_wins.append( i )

			#check the list of big wins and make sure that there are no wins in the list
			#further away from the current win than the sample range
			while i - rolling_big_wins[0] > rolling_sample_range and len(rolling_big_wins) > 0:
				rolling_big_wins.pop(0)
				# if we have poped off a win from our list and only have 1 win left then we must have
				#had a period greater than the range
				if len(rolling_big_wins) == 1:
					rolling_big_wins_min = 0

			#Check to see if our stats need to be updated
			#TODO: add mechanic to detect zero wins in range
			d = len(rolling_big_wins)
			if d > rolling_big_wins_max:
				rolling_big_wins_max = d
			if d < rolling_big_wins_min:
				rolling_big_wins_min = d
		
		#update the rolling rtp lists
		if len(rolling_rtp) >= rolling_sample_range:
			#initialize the tracking variable the first time we have a full range
			if rolling_rtp_sum == 0.0:
				rolling_rtp_sum = sum(rolling_rtp)

			#Check for new min or max
			a = ( bet + ( rolling_rtp_sum / rolling_sample_range ) )/10
			if a > rtp_max:
				rtp_max = a
			if a < rtp_min:
				rtp_min = a

			#Since running a sum() function on a large list is super inefficient keep
			#a running tally of what the current rtp is but also use a queue to track
			#what the we need to remove from the running sum.
			rolling_rtp_sum -= rolling_rtp[0]
			rolling_rtp.pop(0)
		rolling_rtp.append( (bet * payit[x]) - bet)
		rolling_rtp_sum += (bet * payit[x]) - bet

except:
	print("[forced shutdown]")


finally:
	print("\nStats:")
	print(winit)
	for i in range(17):
		z = ( -bet * winit[i] ) + ( bet * winit[i] * payit[i] )
		print("winit: ", winit[i], " payit: ", payit[i], " z: ", z)
		rtp += z

	print("\nprofits: ", rtp)
	print("rtp: ", rtp / num_games)
	print("rtp percent: ", ( bet + ( rtp / num_games ) )/10 )

	win_deltas = list()
	for i in big_wins:
		if last1000x == -1:
			last1000x = max1000x = min1000x = i
			win_deltas.append(max1000x)
		else:
			delta = i - last1000x
			win_deltas.append(delta)
			if delta > max1000x:
				max1000x = delta
			elif delta < min1000x:
				min1000x = delta
		last1000x = i

	print("Max time to 1000x: ", max1000x)
	print("Min time to 1000x: ", min1000x)

	print("Average time to win: ", numpy.mean(win_deltas) )
	print("Median time to win: ", numpy.median(win_deltas) )

	print("RTP Min: ", rtp_min)
	print("RTP Max: ", rtp_max)

	print("Rolling 1000x Min: ", rolling_big_wins_min)
	print("Rolling 1000x Max: ", rolling_big_wins_max)
	

