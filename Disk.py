
from importlib.metadata import metadata
import os


class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


class Disk:

	# Disk constructor
	#
	# @param diskfile	Name of the disk file to be opened. Should
	#					be a multiple of `blocksize` in size
	# @param blocksize	Block size to use
	#
	# @return none
	def __init__(self, diskfile, blocksize):

		try:
			self.diskfile = open(diskfile, "r+b")
		except IOError:
			raise Exception("Failed to open disk file")

		self.blocksize = blocksize
		self.blockreads = 0
		self.blockwrites = 0
		self.my_dict = {}

	# Disk destructor
	#
	# @return none
	def __del__(self):

		self.diskfile.close()

	# Read a block from the disk
	#
	# @param n	Block number to read
	#
	# @return	`blocksize` number of bytes, from the block
	def readBlock(self, n):

		self.diskfile.seek(self.blocksize * n)
		data = self.diskfile.read(self.blocksize)

		self.blockreads += 1

		return data

	# Write a block to the disk
	#
	# @param n		Block number to write to
	# @param data	Data to be written to that block
	#
	# @return none
	def writeBlock(self, n, data):

		self.diskfile.seek(self.blocksize * n)
		self.diskfile.write(data)

		self.blockwrites += 1

	# List contents of the current directory
	#
	# @param n		Block number to read
	# @param my_dict  store files and directories with their block numbers
	#             
	# @return my_dict

	def dir(self, n, block, my_dict):
		my_dict = my_dictionary()
		#isfile = False

		for x in range(0, 512, 32):
			name = ''
			if(block[x] == 2):
				print("DIR", end='  ')
			elif block[x] == 3:
				print("File", end='  ')
				# file = True
			else:
				continue

			# values = (block[x+2])
			# my_dict.value = values
			my_dict.value = str(block[x+2])

			size = 0
			for x in range(x+4, x+6):
				size += block[x]
			print((size), "bytes", end=' ')

			print(end=' ')

			# for x in range(x, x+24):
			# 	name += (chr(block[x])) 
			name = block[x:x+24].decode('unicode_escape').strip()
			print(name, end='') 
			my_dict.key = name.replace("\x00", "").replace("\x07", "")
			my_dict.add(my_dict.key, my_dict.value)
			print("\n")
		return my_dict

	# Print statistics showing number of block read/writes
	#
	# @return none
	def printStats(self):

		print("")
		print("===== Disk usage statistics =====")
		print(" Total block reads:  {}".format(self.blockreads))
		print(" Total block writes: {}".format(self.blockwrites))
		print("=================================")
		print("")
