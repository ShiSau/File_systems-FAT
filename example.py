# This is just an example, showing how the Disk class can be used.
# Use this as a reference, but you'll need to write your own code.
import Disk
import os

DISK_FILE	= "disk.dmg"
BLOCK_SIZE	= 512
curdir = ["/"]
curblock = [2]
my_dict = {}
blockindex = 0

# Instantiate a new Disk, backed by the user-supplied file
d = Disk.Disk(DISK_FILE, BLOCK_SIZE)

# Write A's to the 0th block on the disk
# d.writeBlock(0, (b"A" * BLOCK_SIZE))

# Read the 0th block back off the disk.
# It should be the A's we just wrote
# block = d.readBlock(0)

# Print that data out, showing it worked
# print("{}".format(block))

print("Browsing:  {}".format(DISK_FILE))
print("Disk label: %s" % d.readBlock(0).decode('unicode_escape').strip())
print("\n")

while True:
   print("[DISK_FILE]:", *curdir, end='>')
   commands = input().lower().split()
   if commands[0] =="dir":
        my_dict = d.dir(0,d.readBlock(curblock[blockindex]), my_dict)
   if commands[0] =="pwd":
        ##update curdir values 
        print('home', *curdir)
   if commands[0] =="cd":
       ## .. goes to parent  directory 
       if commands[1] == '..':
           if len(curdir) != 0:
               del curdir[-1]
               del curblock[-1]
               blockindex = blockindex-1
           else:
                continue
       elif str(commands[1]) in my_dict:
                curdir.append(str(commands[1]+"/"))
                curblock.append(int(my_dict[commands[1]]))
                blockindex = blockindex+1
       else: 
            print("Not a directory")                   
   if commands[0] =="read":
       if str(commands[1]) in my_dict:
           print(d.readBlock(int(my_dict[str(commands[1])])).decode('unicode_escape'))
       else:
            print("Wrong filename")
   if commands[0] =="x":
        break
   if commands[0] == "help":
       print("Commands:\n"
              "dir         : Print the contents of the current directory\n"
              "cd <dir>    : Change to directory <dir> \n"
              "read <file> : Print the contents of <file> \n"
              "pwd         : print working directory\n")

   print("\n\n")



#print current working 
# Print statistics showing block read/writes
# Should be one read, one write
d.printStats()

del d
