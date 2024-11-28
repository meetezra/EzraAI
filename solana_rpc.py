import requests

class HeraSolanaRPC:
    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com"):
        """
        Initialize the connection to Solana's RPC endpoint.
        """
        self.rpc_url = rpc_url

    def _post_request(self, method, params):
        """
        Send a POST request to the Solana JSON RPC endpoint.
        """
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        }
        response = requests.post(self.rpc_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_account_balance(self, wallet_address):
        """
        Fetch the SOL balance of a given wallet address.
        """
        response = self._post_request("getBalance", [wallet_address])
        lamports = response.get("result", {}).get("value", 0)
        return lamports / 1_000_000_000  # Convert lamports to SOL

    def get_recent_transactions(self, wallet_address, limit=10):
        """
        Fetch recent transactions for a given wallet address.
        """
        params = {
            "account": wallet_address,
            "limit": limit,
        }
        response = self._post_request("getSignaturesForAddress", [wallet_address, {"limit": limit}])
        return response.get("result", [])

    def get_transaction_details(self, signature):
        """
        Fetch details of a specific transaction.
        """
        response = self._post_request("getTransaction", [signature, {"encoding": "json"}])
        return response.get("result", {})

    def get_token_accounts(self, wallet_address):
        """
        Fetch SPL token accounts for a given wallet address.
        """
        params = {
            "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
        }
        response = self._post_request("getTokenAccountsByOwner", [wallet_address, params])
        return response.get("result", {}).get("value", [])

    def get_token_balance(self, token_account):
        """
        Fetch the balance of a specific SPL token account.
        """
        response = self._post_request("getTokenAccountBalance", [token_account])
        return response.get("result", {}).get("value", {})

    def get_block_time(self, slot):
        """
        Fetch the block time for a specific slot.
        """
        response = self._post_request("getBlockTime", [slot])
        return response.get("result")

    def get_program_accounts(self, program_id):
        """
        Fetch all accounts interacting with a specific program.
        """
        response = self._post_request("getProgramAccounts", [program_id])
        return response.get("result", [])

    def get_slot(self):
        """
        Fetch the current slot on the Solana blockchain.
        """
        response = self._post_request("getSlot", [])
        return response.get("result")

    def get_recent_performance_samples(self):
        """
        Fetch recent performance samples of the network (e.g., transactions per second).
        """
        response = self._post_request("getRecentPerformanceSamples", [])
        return response.get("result", [])

    def get_minimum_balance_for_rent_exemption(self, data_length):
        """
        Fetch the minimum balance required for rent exemption for a given data size.
        """
        response = self._post_request("getMinimumBalanceForRentExemption", [data_length])
        return response.get("result")

# Example usage
if __name__ == "__main__":
    rpc = HeraSolanaRPC()
    wallet = "YourWalletAddressHere"

    # Test fetching account balance
    print("Balance (SOL):", rpc.get_account_balance(wallet))

    # Test fetching recent transactions
    print("Recent Transactions:", rpc.get_recent_transactions(wallet))

    # Fetch SPL token accounts
    print("Token Accounts:", rpc.get_token_accounts(wallet))

    # Get current blockchain slot
    print("Current Slot:", rpc.get_slot())

    # Test performance samples
    print("Performance Samples:", rpc.get_recent_performance_samples())
