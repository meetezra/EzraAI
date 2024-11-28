import numpy as np
from neural_network_base import TradingNeuralNetwork
from datetime import datetime

class TradingAnalyzer:
    def __init__(self):
        """
        Initialize the trading analysis logic with an instance of the neural network.
        """
        self.nn = TradingNeuralNetwork(input_shape=(20,))  # Expanded features to 20
    
    def extract_features(self, transaction_data):
        """
        Extract enhanced features from wallet transaction data for analysis.
        
        Args:
            transaction_data (list): List of transactions (each containing timestamp, amount, token, etc.)
        
        Returns:
            ndarray: Extracted features for the model.
        """
        features = []

        # Basic features
        transaction_count = len(transaction_data)
        total_volume = sum(tx['amount'] for tx in transaction_data)
        avg_volume = total_volume / transaction_count if transaction_count else 0
        successful_transactions = sum(1 for tx in transaction_data if tx.get('status') == 'success')
        transaction_frequency = transaction_count / len(set(tx['date'][:7] for tx in transaction_data))  # Frequency per week

        features.append(transaction_count)
        features.append(total_volume)
        features.append(avg_volume)
        features.append(successful_transactions)
        features.append(transaction_frequency)

        # Advanced features (e.g., Profit/Loss ratio)
        profit_loss_ratio = self.calculate_profit_loss(transaction_data)
        features.append(profit_loss_ratio)

        # Date-based features
        days_active = (datetime.now() - datetime.strptime(transaction_data[-1]['date'], "%Y-%m-%d")).days
        features.append(days_active)

        # Add random features for now (to simulate complex analysis)
        features.extend(np.random.rand(10))  # Adding 10 random features to complete the 20 feature input

        return np.array(features).reshape(1, -1)

    def calculate_profit_loss(self, transaction_data):
        """
        Calculate the profit/loss ratio based on transaction success/failure and amount.
        
        Args:
            transaction_data (list): List of transactions.
        
        Returns:
            float: Profit/Loss ratio.
        """
        profit = sum(tx['amount'] for tx in transaction_data if tx.get('status') == 'success')
        loss = sum(tx['amount'] for tx in transaction_data if tx.get('status') == 'failure')
        if loss == 0:
            return profit
        return profit / loss

    def analyze_wallet(self, wallet_address, transaction_data):
        """
        Analyze a wallet's trading activity and make predictions.
        
        Args:
            wallet_address (str): The Solana wallet address.
            transaction_data (list): List of transactions related to the wallet.
        
        Returns:
            dict: Analysis result with a prediction.
        """
        features = self.extract_features(transaction_data)
        prediction = self.nn.predict(features)  # 0: Sell, 1: Buy (binary classification)

        # Enhanced analysis with multiple strategies
        regression_model = TradingNeuralNetwork(input_shape=(20,))  # Use another model for regression
        regression_result = regression_model.predict(features)  # Predict the success rate of a trade

        return {
            "wallet_address": wallet_address,
            "prediction": "Buy" if prediction[0] > 0.5 else "Sell",
            "predicted_success_rate": regression_result[0][0],  # Success rate from regression model
            "features": features.tolist(),
        }

# Example usage:
if __name__ == "__main__":
    # Sample transaction data (for illustration purposes)
    sample_transactions = [
        {"date": "2024-11-01", "amount": 1.5, "status": "success"},
        {"date": "2024-11-02", "amount": 0.5, "status": "success"},
        {"date": "2024-11-03", "amount": 2.0, "status": "failure"},
        {"date": "2024-11-05", "amount": 3.0, "status": "success"},
    ]
    wallet_address = "ExampleWallet123"
    
    analyzer = TradingAnalyzer()
    analysis_result = analyzer.analyze_wallet(wallet_address, sample_transactions)
    print(analysis_result)