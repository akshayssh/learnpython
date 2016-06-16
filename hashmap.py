def new(num_buckets=256): ## this is the initializer.
	"""Initializes a Map with the given number of buckets."""
	aMap = []               ## created aMap variable that has a list
	for i in range(0, num_buckets): ## then put num_buckets inside the aMap list
		aMap.append([])
	return aMap
	
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's buckets."""
	return hash(key) % len(aMap) ## uses a builtin Python function to convert string to number. Then use modulus operator with len(aMap) to get a bucket where this key can go.
	
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
    ##this function uses the hash_key to find the bucket that a key could be in.
    ## since I did a % len(aMap) in hash_key function, I know whatever bucket_id i get will fit into aMap list.
    ## using the bucket_id I can then get the bucket where the key could be.
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key and value of a slot found in a bucket.
	Returns -1, key and default (None if not set) when not found.
	"""
    ##this function uses get_bucket to get the bucket the key could be in, it simply rolls through every element in the bucket until it finds a matching key. Once it does, it returns the tuple of (i, k, v) which is the index the key was found in and key itself and the value set for that key.
	bucket = get_bucket(aMap, key)
	
	for i, kv in enumerate(bucket):
		k,v = kv
		if key == k:
			return i, k, v
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
    ## this is a convenience function, it uses get_slot to get i, k, v and just returns v.
	i, k, v = get_slot(aMap, key, default=default)
	return v
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
    ## to set a key value pair, I need to get the bucket, and append the new key, value pair so it can be found later. 
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		#the key does not, append to create it
		bucket.append((key, value))

def delete(aMap, key):
	"""Deletes the give key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
	
