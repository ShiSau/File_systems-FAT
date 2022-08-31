# File Allocation Table 
<BR>
It is a simple, minimal, ubiquitous file system. In the code I have implemented a rough approximation of how FAT works.
<BR>
  
### Brief Intro
> Disks are accessed by block, common block sizes – 512, 1024 (1K), 4096 (4K)

 #### Types of blocks
* File Allocation Table (FAT) (only one!).
  
* File data chunk (many)
* Directory entry (many)


File Allocation Table
* Occupies one block
* Just an array of integers
* Like a “map” of all blocks, and their status


File Data Chunk
* Just a piece of a file
* One file may span many blocks
* Example
– File size: 1027 bytes
– Block size: 512 bytes
– Breakdown: 512b , 512b, 3b

Directory Entry
* Each directory entry occupies one block
* Array of directory entry structures
– Entry type (dir, file, etc)
– Starting block
– Metadata (file size, etc)
– Name


Directory Entry
* All directory entries begin with two listings
– . reference to self
– .. reference to parent

  <br>
#### Block Implementation in code

Block 0 – Boot Sector, Drive Info
* Information about this drive
– FAT version
– Media type
– Disk telemetry information
– Volume label
– etc


Block 1 – File Allocation Table
* A “map” of all blocks status
– 0x0000 : drive info
– 0x0001 : File allocation table
– 0x???? : Next block in sequence
– 0xfefe : End of block sequence
– 0xffff : Unallocated


Block 2 – Root Directory Entry
* Represents the base of the directory tree
– Like C:\ on Windows
Or / on Linux
