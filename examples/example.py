from python_ethermine import EthermineClient

WORKER = "miner01"
ETH_ADDRESS = "ETH Address"

if __name__ == '__main__':
    print("Running...")
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
    individual_historical_worker_stats = client.Worker.get_individual_historical_worker_stats(address=ETH_ADDRESS,
                                                                                              worker=WORKER)
    # This test is failing due to an API error
    # worker_monitoring = client.Worker.get_worker_monitoring(address=eth_address, worker="thebeast")

    # Pool stats
    basic_pool_stats = client.Pool.get_basic_pool_stats()
    mined_blocks_stats = client.Pool.get_mined_blocks_stats()
    network_statistics = client.Pool.get_network_statistics()
    server_hashrate_stats = client.Pool.get_server_hashrate_stats()

    print("Done!")
