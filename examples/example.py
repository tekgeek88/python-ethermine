from src.python_ethermine.ethermine_client import EthermineClient

eth_address = "ADDRESS"

if __name__ == '__main__':
    print("Running...")
    client = EthermineClient()

    # Miner Tests
    dashboard = client.Miner.get_dashboard(address=eth_address)
    history = client.Miner.get_history(address=eth_address)
    payouts = client.Miner.get_payouts(address=eth_address)
    rounds = client.Miner.get_rounds(address=eth_address)
    settings = client.Miner.get_settings(address=eth_address)
    statistics = client.Miner.get_statistics(address=eth_address)

    # Worker tests
    all_worker_stats = client.Worker.get_all_worker_stats(address=eth_address)
    individual_worker_stats = client.Worker.get_individual_worker_stats(address=eth_address, worker="miner01")
    individual_historical_worker_stats = client.Worker.get_individual_historical_worker_stats(address=eth_address, worker="miner01")
    # worker_monitoring = client.Worker.get_worker_monitoring(address=eth_address, worker="thebeast")

    # Pool stats
    basic_pool_stats = client.Pool.get_basic_pool_stats()
    mined_blocks_stats = client.Pool.get_mined_blocks_stats()
    network_statistics = client.Pool.get_network_statistics()
    server_hashrate_stats = client.Pool.get_server_hashrate_stats()


    print("Done!")


