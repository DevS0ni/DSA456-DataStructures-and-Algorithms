#    Main Author(s): Sarah Haque 
#    Main Reviewer(s): Dev Soni

# If you are doing chaining for collision resolution, 
# copy your code from a1 into a1_partb.py and uncomment the next line
# from a1_partb import DoublyLinked

class HashTable:

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice as long as it is a hash table
	def __init__(self, cap = 32):
		self.cap = cap
		self.the_table = [None] * self.cap
		self.length = 0
		self.max_load_factor = 0.70

	def insert(self,key, value):
		""" Adds a new key-value pair to the table. If exists, return False, Othersise adds new key-value and return True. If adding the new record causes the load factor to exceed 0.7, 
        you must grow your table by doubling its capacity """
		self.length += 1
		hashed_key = hash(key) % self.cap
		
		while self.the_table[hashed_key] is not None:
			if self.the_table[hashed_key][0] == key:
				self.length -= 1
				return False

			hashed_key = self._hash(hashed_key)

		if self.length / float(self.cap) >= self.max_load_factor:
			self._grow()
		tuple = (key, value)
		self.the_table[hashed_key] = tuple
		return True

	def modify(self, key, value):
		""" Modifies existing key-value pair into the table. If no matching record, returns False. Otherwise, 
		modifies the changes the existing value into the one passed into the function and returns True """
		index = hash(key) % self.cap
		record = index
		while self.the_table[index] is not None and index != record - 1:
			if(self.the_table[index][0]==key and self.the_table[index][0] != None):
				self.the_table[index] = (key,value)
				return True

			index = self._hash(index)
		return False

	def remove(self, key):
		""" Removes the key-value pair with the matching key. If no matching key exists, return False. Otherwise, return True """
		count = 0

		for item in self.the_table:
			if(item is not None):
				if(item[0] == key):
					self.the_table[count] = None
					self.length -= 1
					return True
			count += 1
		return False

	def search(self, key):
		""" Returns value of record with matching key. If nothing matching, return None """
		for item in self.the_table:
			if (item is not None):
				if (item[0] == key):
					return item[1]
		return None

	def capacity(self):
		""" Checks for number of available spots in the table """
		return self.cap

	def __len__(self):
		""" Number of records stored in the table """
		if(self.length > self.cap):
			self.length -= 1
		return self.length

	def _grow(self):
		""" This function doubles the capacity of the table and rehashes all the key-value pairs """
		self.cap *= 2
		self.length = 1
		old_table = self.the_table
		self.the_table = [None] * self.cap
		for tuple in old_table:
			if tuple is not None:
				self.insert(tuple[0],tuple[1])

	def _hash(self, key):
		""" This function returns the index of the table where the key-value pair should be stored """
		return (key + 1) % self.cap 