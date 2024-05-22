import datetime as dt
import hashlib as hl
import json as js


class Blockchain:
    def __init__(self):
        self.chain = list()
        initialBlock = self.createBlock(data="genesis block", proof=1, previousHash="0", index=1)
        self.chain.append(initialBlock)

    def mineBlock(self, data: str) -> dict:
        previousBlock = self.getPreviousBlock()
        previousProof = previousBlock["proof"]
        index = len(self.chain) + 1
        proof = self.proofOfWork(previousProof=previousProof, index=index, data=data)
        previousHash = self.hash(block=previousBlock)
        block = self.createBlock(data=data, proof=proof, previousHash=previousHash, index=index)
        self.chain.append(block)
        return block

    def createBlock(self, data: str, proof: int, previousHash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previousHash": previousHash,
        }
        return block

    def getPreviousBlock(self) -> dict:
        return self.chain[-1]

    def toDigest(self, newProof: int, previousProof: int, index: int, data: str) -> bytes:
        digest = f"{newProof ** previousProof + index}{data}"
        return digest.encode()

    def proofOfWork(self, previousProof: int, index: int, data: str) -> int:
        newProof = 1
        checkProof = False
        while not checkProof:
            digest = self.toDigest(newProof, previousProof, index, data)
            hashOperation = hl.sha256(digest).hexdigest()
            if hashOperation[:3] == "000":
                checkProof = True
            else:
                newProof += 1
        return newProof

    def hash(self, block: dict) -> str:
        encodedBlock = js.dumps(block, sort_keys=True).encode()
        return hl.sha256(encodedBlock).hexdigest()

    def isChainValid(self) -> bool:
        previousBlock = self.chain[0]
        blockIndex = 1
        while blockIndex < len(self.chain):
            block = self.chain[blockIndex]
            if block["previousHash"] != self.hash(previousBlock):
                return False
            previousProof = previousBlock["proof"]
            index, data, proof = block["index"], block["data"], block["proof"]
            hashOperation = hl.sha256(
                self.toDigest(newProof=proof, previousProof=previousProof, index=index, data=data)
            ).hexdigest()
            if hashOperation[:3] != '000':
                return False
            previousBlock = block
            blockIndex += 1
        return True



