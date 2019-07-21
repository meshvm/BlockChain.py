from BlockChain.chain import Block
import datetime
def genesis_block():
	return Block(0,datetime.datetime.now(),"Genesis Block","0")