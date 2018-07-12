import numpy as np

#A = [1, 3, 4, 10]
#A = [1, 1, 2, 10, 7, 4, 7, 4, 4, 4, 4]
A = [1, 1, 2, 10, 7, 7, 4, 4, 7, 4, 7, 4, 7, 4]


def is_sorted(v):
	l = len(v)
	if l == 0:
		return True
	prev_nr = v[0]
	for i in range(1, l):
		current_nr = v[i]
		if current_nr < prev_nr:
			return False
		prev_nr = current_nr
	return True

# a sequence s is called a mountain if it can be split into two
# subsequences, s = xy, such that x and y are nonempty and x is an
# increasing sequence with at least two different elements, and y
# is a decreasing sequence with at least two different elements

# The function below is actually able to calculate the number of times
# a sequence switches between increasing and decreasing subsequences. 
# If this number equals 1, then the sequence is a mountain.
def is_mountain(v):
	l = len(v)
	if l == 0:
		return False
	# Keeps track of the monotonicity of the current function. Initialized at -1
	current_subsequence_increasing = -1
	# Keeps track of the number of subsequences of alternating monotonicity in the big sequence
	number_of_subsequences = 0
	prev_nr = v[0]
	for i in range(1, l):
		current_nr = v[i]
		if current_nr == prev_nr:
			continue
		else:
			if number_of_subsequences == 0:
				if current_nr < prev_nr:
					return False
				number_of_subsequences = 1
				current_subsequence_increasing = 1
			else:
				if current_subsequence_increasing == 1:
					if current_nr < prev_nr:
						number_of_subsequences += 1
						current_subsequence_increasing = 0
				elif current_subsequence_increasing == 0:
					if current_nr > prev_nr:
						number_of_subsequences +=1
						current_subsequence_increasing = 1
		prev_nr = current_nr
		if number_of_subsequences >2:
			return False
	if number_of_subsequences == 2:
		return True
	return False
	#return number_of_subsequences

# Given a sequence, find the length of the longest increasing subsequence
# We also find an example of a subsequence with that length

def longest_increasing_subsequence(v):
	l = len(v)
	longest_seq_len = np.ones(l)
	current_max_len = 1
	successor_dict = {}
	last_index_in_max_subsequence = 0
	for i in range(l):
		current = v[i]
		longest_subseq_len_for_current = 1
		successor = None
		# Find the successor of j, i.e. the index j whose value v[j] is <= v[i] and with
		# the longest subsequence ending in v[j]
		for j in range(0, i):
			if current >= v[j]:
				subseq_len_candidate = 1 + longest_seq_len[j]
				if subseq_len_candidate > longest_subseq_len_for_current:
					longest_subseq_len_for_current = subseq_len_candidate
					successor = j
		longest_seq_len[i] = longest_subseq_len_for_current
		successor_dict[i] = successor

		# Update the length of the longest increasing subsequence so far
		if longest_subseq_len_for_current > current_max_len:
			current_max_len = longest_subseq_len_for_current
			last_index_in_max_subsequence = i
	# return a list of the max length
	max_subseq = []
	current_index = last_index_in_max_subsequence
	while current_index != None:
		max_subseq.insert(0, v[current_index])
		current_index = successor_dict[current_index]
	return current_max_len, max_subseq

# BONUS:
# Given a sequence, find the length of the longest subsequence which is a mountain

# the idea is the following: keep a record of two arrays: mountain[] and increasing[]
# mountain[i] stores the length of the longest mountain ending in i
# increasing[i] stores the length of the longest increasing sequence ending in i
# For a given index i, update mountain[i] and increasing[i]
# updating increasing[i] is done in the previous program and we do the same thing
# updating mountain[i] is done in the following way: mountain[i] can be created
# by ending the increasing part at step j, and adding i to it, or it can be
# appended, by adding index i to an existing mountain ending at j.

def longest_mountain_subsequence(v):
	l = len(v)
	# the length of the longest increasing sequence ending in index i
	longest_len_increasing = np.ones(l)
	# the length of the longest mountain ending in index i
	longest_len_mountain = np.zeros(l)
	predecessor_dict_increasing = {}
	predecessor_dict_decreasing = {}
	max_len_mountain 		= 0
	last_index_mountain 	= -1
	pivot_index				= -1
	for i in range(l):
		current = v[i]
		current_max_len_increasing 		= 1
		current_max_len_new_mountain   	= 1
		current_max_len_old_mountain	= 1
		current_max_len_mountain 		= 1
		predecessor_in_increasing 		= None
		found_potential_mountainstart   = 0
		for j in range(i):
			if current > v[j]:
				# in this case we can only add to the increasing part
				current_len_increasing = 1 + longest_len_increasing[j]
				if current_len_increasing > current_max_len_increasing:
					current_max_len_increasing = current_len_increasing
					predecessor_in_increasing = j
			if current < v[j]:
				found_potential_mountainstart = 1
				# in this case we can either add to the mountain, or create a mountain
				current_len_new_mountain = 1 + longest_len_increasing[j]
				if current_len_new_mountain > current_max_len_new_mountain:
					current_max_len_new_mountain = current_len_new_mountain
					pred_in_new_mountain = j
				current_len_old_mountain = 1 + longest_len_mountain[j]
				if current_len_old_mountain > current_max_len_old_mountain:
					current_max_len_old_mountain = current_len_old_mountain
					pred_in_old_mountain = j
		longest_len_increasing[i] = current_max_len_increasing
		predecessor_dict_increasing[i] = predecessor_in_increasing
		if found_potential_mountainstart == 1:
			if current_max_len_new_mountain >= current_max_len_old_mountain:
				current_max_len_mountain = current_max_len_new_mountain
				predecessor_dict_decreasing[i] = pred_in_new_mountain
				longest_len_mountain[i] = current_max_len_mountain
				if current_max_len_mountain > max_len_mountain:
					max_len_mountain = current_max_len_mountain
					pivot_index = pred_in_new_mountain
					last_index_mountain = i
			else:
				current_max_len_mountain = current_max_len_old_mountain
				predecessor_dict_decreasing[i] = pred_in_old_mountain
				longest_len_mountain[i] = current_max_len_mountain
				if current_max_len_mountain > max_len_mountain:
					max_len_mountain = current_max_len_mountain
					last_index_mountain = i
	if last_index_mountain == -1:
		return -1, []
	max_mountain_subseq = []
	cur_index = last_index_mountain
	while cur_index != pivot_index:
		max_mountain_subseq.insert(0, v[cur_index])
		cur_index =  predecessor_dict_decreasing[cur_index]
	#cur_index = predecessor_dict_increasing[cur_index]
	while cur_index != None:
		max_mountain_subseq.insert(0, v[cur_index])
		cur_index = predecessor_dict_increasing[cur_index]
	return max_len_mountain, max_mountain_subseq

q = longest_mountain_subsequence(A)
print(q)

