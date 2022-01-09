# osmopy

> Version 0.0.2

> Tools for Osmosis wallet management and offline transaction signing


## Installing

#### Installing from PyPI [repository](https://pypi.org/project/osmopy):

```bash
pip3 install osmopy
```

#### Installing from source code:

```bash
git clone https://github.com/bro-n-bro/osmopy
cd cyberpy
pip3 install .
```

## Usage

### Generating a wallet

```python
from osmopy import generate_wallet
wallet = generate_wallet()
```

The value assigned to `wallet` will be a dictionary just like:

```python
{
    "seed": "arch skill acquire abuse frown reject front second album pizza hill slogan guess random wonder benefit industry custom green ill moral daring glow elevator",
    "derivation_path": "m/44'/118'/0'/0/0",
    "private_key": b'\xbb\xec^\xf6\xdcg\xe6\xb5\x89\xed\x8cG\x05\x03\xdf0:\xc9\x8b \x85\x8a\x14\x12\xd7\xa6a\x01\xcd\xf8\x88\x93',
    "public_key": b"\x03h\x1d\xae\xa7\x9eO\x8e\xc5\xff\xa3sAw\xe6\xdd\xc9\xb8b\x06\x0eo\xc5a%z\xe3\xff\x1e\xd2\x8e5\xe7",
    "address": "bostrom1uuhna3psjqfxnw4msrfzsr0g08yuyfxesqggqd",
}
 ```

### Converter functions

#### Mnemonic seed to private key

```python
from osmopy import seed_to_privkey
seed = "teach there dream chase fatigue abandon lava super senior artefact close upgrade"
privkey = seed_to_privkey(seed, path="m/44'/118'/0'/0/0")
 ```

#### Private key to public key

```python
from osmopy import privkey_to_pubkey
privkey = bytes.fromhex("6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa")
pubkey = privkey_to_pubkey(privkey)
 ```

#### Public key to address

```python
from osmopy import pubkey_to_address
pubkey = bytes.fromhex("03e8005aad74da5a053602f86e3151d4f3214937863a11299c960c28d3609c4775")
addr = pubkey_to_address(pubkey)
 ```

#### Private key to address

```python
from osmopy import privkey_to_address
privkey = bytes.fromhex("6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa")
addr = privkey_to_address(privkey)
 ```

#### Address to address

```python
from osmopy import address_to_address
addr = address_to_address(address, prefix)
 ```

### Signing transactions

#### Send transaction

```python
from osmopy import Transaction
tx = Transaction(
    privkey=bytes.fromhex("26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59"),
    account_num=11335,
    sequence=0,
    fee=0,
    gas=200000,
    memo="",
    chain_id="bostrom-testnet-1",
    sync_mode="broadcast_tx_sync", # "broadcast_tx_sync", "broadcast_tx_async", "broadcast_tx_commit"
)
tx.add_transfer(recipient="osmo103l758ps7403sd9c0y8j6hrfw4xyl70j4mmwkf", amount=387000)
tx.add_transfer(recipient="osmo1lzumfk6xvwf9k9rk72mqtztv867xyem393um48", amount=123)
```

One or more token transfers can be added to a transaction by calling the `add_transfer` method.

When the transaction is fully prepared, calling `get_pushable` will return a signed transaction in the form of a JSON string.

```python
pushable_tx = tx.get_pushable()
```

 This can be used as request body when calling endpoint of the `https://rpc_api:26657`, more detailes [here](https://docs.tendermint.com/master/rpc/#/Tx/broadcast_tx_sync)

```python
import requests

res = requests.post(url=<rpc_api>, data=pushable_tx)
```

Or you can call `broadcast(rps: str)` method and it will make a signed transaction and POST it with defined RPC_api.

```python
res = tx.broadcast(url=<RPC_api>)
```
