
# python-ethermine

## What it is

An API Wrapper for the Ethermine API. Easily allows you to create a client and access the data for your mining
operation

## How to use it
```
from python_ethermine import EthermineClient

WORKER = "sanyi"
ETH_ADDRESS = "0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8"

client = EthermineClient()

# Miner Tests
dashboard = client.Miner.get_dashboard(address=ETH_ADDRESS)
history = client.Miner.get_history(address=ETH_ADDRESS)
payouts = client.Miner.get_payouts(address=ETH_ADDRESS)
rounds = client.Miner.get_rounds(address=ETH_ADDRESS)
settings = client.Miner.get_settings(address=ETH_ADDRESS)
statistics = client.Miner.get_statistics(address=ETH_ADDRESS)

# Worker tests
all_worker_stats = client.Worker.get_all_worker_stats(address=ETH_ADDRESS)
individual_worker_stats = client.Worker.get_individual_worker_stats(address=ETH_ADDRESS, worker=WORKER)
individual_historical_worker_stats = client.Worker.get_individual_historical_worker_stats(address=ETH_ADDRESS, worker=WORKER)

# Pool stats
basic_pool_stats = client.Pool.get_basic_pool_stats()
mined_blocks_stats = client.Pool.get_mined_blocks_stats()
network_statistics = client.Pool.get_network_statistics()
server_hashrate_stats = client.Pool.get_server_hashrate_stats()

```

## The latest version

The current version of this program is written for Python 3.8

## Licensing

Copyright 2021 Carl Argabright

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

## Contact
carl.argbright@gmail.com
