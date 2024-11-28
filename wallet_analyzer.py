from solana_rpc import HeraSolanaRPC

class WalletAnalyzer:
    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com"):
        """
        Initialize the wallet analyzer with an RPC connection.
        """
        self.rpc = HeraSolanaRPC(rpc_url)

    def analyze_balance(self, wallet_address):
        """
        Analyze the SOL balance for a given wallet.
        """
        balance = self.rpc.get_account_balance(wallet_address)
        return {
            "wallet": wallet_address,
            "balance_SOL": balance,
            "balance_status": "Healthy" if balance > 1 else "Low",
        }

    def analyze_transactions(self, wallet_address, limit=10):
        """
        Analyze the recent transactions of a wallet.
        """
        transactions = self.rpc.get_recent_transactions(wallet_address, limit)
        transaction_data = []
        
        for tx in transactions:
            signature = tx.get("signature")
            transaction_details = self.rpc.get_transaction_details(signature)
            transaction_data.append({
                "signature": signature,
                "slot": transaction_details.get("slot"),
                "status": transaction_details.get("meta", {}).get("err", None) is None,
                "fee": transaction_details.get("meta", {}).get("fee", 0) / 1_000_000_000,  # Convert lamports to SOL
            })
        
        total_fees = sum(tx["fee"] for tx in transaction_data)
        successful_txs = sum(1 for tx in transaction_data if tx["status"])
        
        return {
            "transaction_count": len(transaction_data),
            "successful_transactions": successful_txs,
            "total_fees_SOL": total_fees,
            "average_fee_SOL": total_fees / len(transaction_data) if transaction_data else 0,
            "transactions": transaction_data,
        }

    def analyze_tokens(self, wallet_address):
        """
        Analyze SPL tokens held by the wallet.
        """
        token_accounts = self.rpc.get_token_accounts(wallet_address)
        token_summary = []

        for account in token_accounts:
            token_info = account.get("account", {}).get("data", {}).get("parsed", {}).get("info", {})
            token_address = token_info.get("mint")
            balance = token_info.get("tokenAmount", {}).get("uiAmount", 0)
            decimals = token_info.get("tokenAmount", {}).get("decimals", 0)

            token_summary.append({
                "token_address": token_address,
                "balance": balance,
                "balance_in_base_units": balance * (10 ** decimals),
            })
        
        return {
            "token_count": len(token_summary),
            "tokens": token_summary,
        }

    def generate_summary(self, wallet_address):
        """
        Generate an in-depth summary of wallet activity and performance.
        """
        balance_analysis = self.analyze_balance(wallet_address)
        transaction_analysis = self.analyze_transactions(wallet_address)
        token_analysis = self.analyze_tokens(wallet_address)

        summary = {
            "wallet_address": wallet_address,
            "balance_analysis": balance_analysis,
            "transaction_analysis": transaction_analysis,
            "token_analysis": token_analysis,
        }
        
        return summary

# Example usage
if __name__ == "__main__":
    analyzer = WalletAnalyzer()
    wallet = "YourWalletAddressHere"

    print("Analyzing Wallet:", wallet)
    
    balance = analyzer.analyze_balance(wallet)
    print("\nBalance Analysis:")
    print(balance)
    
    transactions = analyzer.analyze_transactions(wallet)
    print("\nTransaction Analysis:")
    for key, value in transactions.items():
        print(f"{key}: {value}")
    
    tokens = analyzer.analyze_tokens(wallet)
    print("\nToken Analysis:")
    print(tokens)

    summary = analyzer.generate_summary(wallet)
    print("\nFull Wallet Summary:")
    print(summary)