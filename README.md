# btc-pki-bruteforce
A tool for testing the security of pubkey privkey infrastructure used in popular cryptocurrencies.

https://discord.gg/PY5SQ3DXmv

https://bigcointalk.org/viewtopic.php?t=7

"Bitcoin uses public key cryptography to create a key pair that controls access to bitcoin. The key pair consists of a private key and—derived from it—a unique public key. The public key is used to receive funds, and the private key is used to sign transactions and spend funds."

## Features
 - VERY FAST because it doesn't communicate with the network
 - A current list of 30M funded wallets (~1.5GB Dec. 2022)
 - Multiple instances (per core)
 - Debug mode for testing
 - Writes findings to file (output.txt)

**Funded Wallets:**

https://bigcointalk.org/download/wallets1.txt (~377MB)

https://bigcointalk.org/download/wallets2.txt (~686MB)

or visit...

https://bitcointalk.org/index.php?topic=5254914.0

## Requirements
Python3, base58, bit

## Todo
- [x] Add support for brainwallets
- [ ] Add support for BIP39 mnemonic
- [ ] Get balance of matched public key from Mainnet
- [ ] Distributed browser-based bruteforce

https://bigcointalk.org/

Disclaimer: This article is for informational purposes only. Neither the company nor the author nor GitHub is responsible, directly or indirectly, for any damage or loss caused or alleged to be caused by or in connection with the use of or reliance on any content, goods or services mentioned here.
