#adding new block to the block
from BlockChain.chain import Block
import datetime

def new_block(last_block):
	this_index = last_block.index +1
	this_timestamp = datetime.datetime.now()
	this_data = "Creating  Block Number +" str(this_index)
	this_hash = this_block.hash
	return Block(this_index,this_timestamp,this_data,this_hash)
	