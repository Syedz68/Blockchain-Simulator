import fastapi as fast
import blockchain

bc = blockchain.Blockchain()
app = fast.FastAPI()


@app.post("/mine_block/")
def mine_block(data: str):
    if not bc.isChainValid():
        return fast.HTTPException(status_code=400, detail="The blockchain is invalid")
    block = bc.mineBlock(data=data)
    return block


@app.get("/blockchain/")
def get_blockchain():
    if not bc.isChainValid():
        return fast.HTTPException(status_code=400, detail="The blockchain is invalid")
    chain = bc.chain
    return chain


@app.get("/validate/")
def is_blockchain_valid():
    if not bc.isChainValid():
        return fast.HTTPException(status_code=400, detail="The blockchain is invalid")
    return bc.isChainValid()


@app.get("/blockchain/last/")
def previous_block():
    if not bc.isChainValid():
        return fast.HTTPException(status_code=400, detail="The blockchain is invalid")
    return bc.getPreviousBlock()
