from termcolor import colored
from hashlib import sha256
import time
import os

difficulty = 10000 * 60
target = (2**224) * ((2**32) - 1) // difficulty

def poshit():
  max = (2**32) - 1
  nonce = 0
  extranonce = 0
  
  version = 1
  height = 1
  prevHash = sha256(sha256(os.urandom(1)).digest()).digest()
  merkle = sha256(sha256(os.urandom(1)).digest()).digest()
  timestamp = str(time.time())
  while nonce <= max:
    blockHash = sha256(sha256(nonce.to_bytes(32, "big") + height.to_bytes(4, "big") + extranonce.to_bytes(32, "big") + target.to_bytes(32, "big") + version.to_bytes(4, "big") + prevHash + merkle + timestamp.encode("utf-8")).digest()).hexdigest()
    print(colored(f"Mining - Current Hash: {blockHash}", "yellow", attrs=["bold"]))
    if os.path.exists("hashes.txt"):
      with open("hashes.txt", "a") as a:
        a.write(blockHash + "\n")
    else:
      with open("hashes.txt", "w") as w:
        w.write(blockHash + "\n")
    if int(blockHash, 16) <= target:
      print(colored("Block Has Been Mined!", "green", attrs=["bold"]))
      break
    nonce += 1
    if nonce > max:
      extranonce += 1

poshit()
  
