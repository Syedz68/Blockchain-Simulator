# Blockchain-Simulator

This project is a simple blockchain simulator that demonstrates the basic principles of how a blockchain operates. It starts with a "genesis block" as the initial block in the blockchain. Users can then mine new blocks, which involves finding a valid proof of work and appending the block to the chain. The simulator also includes functionality to verify the integrity of the blockchain by ensuring that each block’s previous hash is correct.

The simulator is implemented entirely in Python, utilizing FastAPI to provide an interactive web interface. This interface allows users to easily interact with the blockchain by mining new blocks, viewing the current blockchain, and checking its validity.

## Features
- **Genesis Block**: Initializes the blockchain with a genesis block.
- **Block Mining**: Users can mine new blocks by providing data.
- **Blockchain Validation**: Ensures the integrity of the blockchain by verifying hashes.
- **Interactive Interface**: FastAPI is used to create a user-friendly web interface.

## Project Structure
- `main.py`: Contains the FastAPI application setup and endpoints.
- `blockchain.py`: Contains the Blockchain class and related methods for blockchain operations.

Below are images of the simulator:

![bc6](https://github.com/Syedz68/Blockchain-Simulator/assets/107263740/5836f6aa-def8-44a8-b911-0119ed7d2718)
![bc1](https://github.com/Syedz68/Blockchain-Simulator/assets/107263740/bd2857a5-7596-4e29-afc7-6ec9321b05a0)
![bc2](https://github.com/Syedz68/Blockchain-Simulator/assets/107263740/18f50f9c-bcdc-4b39-b5f4-56384f1a1884)
![bc3](https://github.com/Syedz68/Blockchain-Simulator/assets/107263740/877a66d2-fc91-489b-a174-1061477a3ff4)
![bc4](https://github.com/Syedz68/Blockchain-Simulator/assets/107263740/de3651ec-65d5-481a-aed7-4fcde2337b0e)
![bc5](https://github.com/Syedz68/Blockchain-Simulator/assets/107263740/574bb59b-2020-4f2f-89c6-69a9d92ebd6a)
