import hashlib
import date
class Block:
	def __init__(self,index, timestamp, data, previous_hash):

        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    def hashing(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode()
              + str(self.timestamp).encode()
              + str(self.data).encode()
              + str(self.previous_hash).encode())
        return sha.hexdigest()    
if __name__ == '__main__':
  from BlockChain.genesis_block import genesis_block
  from BlockChain.new_block import new_block

  # Create the blockchain and add the genesis block
  blockchain = [genesis_block()]
  previous_block = blockchain[0]

  no_of_block=5
  for i in range(no_of_block):
  	add_block = new_block(previous_block)
  	blockchain.append(add_block)
  	previous_block = add_block
    print('Block %d is added to the Blockchain!\n' ,add_block.index)
    print("hash: %s \n",add_block.hash)
