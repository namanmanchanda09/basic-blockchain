from time import time
import json
import hashlib
class BlockChain(object):
    def __init__(self,index=0,timestamp=None,data=None,previousHash=0,Hash=0,newBlock={}):
        self.index=0
        self.timestamp=time()
        self.data=None
        self.previousHash=0
        self.Hash=0
        self.newBlock = {
            'index':self.index,
            'timestamp':self.timestamp,
            'data':self.data,
            'Hash':self.Hash,
            'previousHash':self.previousHash
            }
        self.genesisBlock = {
            'index':0,
            'timestamp':time(),
            'data':"GenesisBlock",
            'Hash':123,
            'previousHash':456
            }
        self.chain = [self.genesisBlock]
    def calculateHash(self):
        #blockString = json.dumps(self.newBlock,sort_keys = True).encode()
        #return hashlib.sha256(blockString).hexdigest()
        blockString=json.dumps(self.newBlock,sort_keys=True).encode()
        hashObject = hashlib.sha512(blockString)
        return hashObject.hexdigest()
        
    def addBlock(self):
        self.index = input("Enter index :     ")
        self.timestamp = input("Enter timestamp  :      ")
        self.data = input("Enter data   :      ")
        x = self.chain[len(self.chain)-1]
        self.previousHash = x['Hash']
        self.Hash = self.calculateHash()
        self.newBlock = {
            'index':self.index,
            'timestamp':self.timestamp,
            'data':self.data,
            'previousHash':self.previousHash,
            'Hash':self.Hash
            }
        self.chain.append(self.newBlock)

    def show(self):
        print (json.dumps(self.chain,sort_keys=True,indent=4))


t=BlockChain()

        
