import hashlib
import json
from datetime import datetime
import time

max_nonce = 2 ** 32 # 4 billion

def hash(block):
    block_string = json.dumps(block).encode()
    return hashlib.sha256(block_string).hexdigest()

def proof_of_work(new_block, bits):

    # calcurate the difficulty target
    exp = bits >> 24
    coef = bits & 0xffffff
    target = coef * 2**(8*(exp-3))

    print("This difficulty target: {0:064x}".format(target))

    for nonce in range(max_nonce):
        new_block['nonce'] = nonce
        hash_result = hash(new_block)

        if int(hash_result, 16) < target:
            print("Success with nonce {0}".format(nonce))
            return (hash_result, nonce)

        # print(hash_result)

    print("Failed after {0} tries".format(max_nonce))
    return (0, max_nonce)

genesis_bits = 0x1e00ffff

genesis_block = {'index':0, 'timestamp':int(datetime.now().timestamp()), 'nonce':0, 'prev_block':'', 'tx':'Hello Blockchain Network!'}

start_time = time.time()
(hash_result, nonce) = proof_of_work(genesis_block, genesis_bits)
end_time = time.time()
elapsed_time = end_time - start_time
print("Calcurate time {0}".format(elapsed_time))
if elapsed_time > 0:
    hash_power = int(nonce)/elapsed_time
    print("Hash Power: {0} hashes per seconds".format(hash_power))
