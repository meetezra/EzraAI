
# Hera AI - Your On-Chain Trading Coach

Hera AI is an advanced AI model designed to provide insightful trading analysis for users based on their on-chain trading activity. By simply tweeting your trading wallet address to Hera, you'll receive an in-depth review of your trading habits. Hera analyzes your transactions and provides valuable insights into factors like emotional impact, roundtrips, paperhanding, and much more. Hera is like having an on-chain trading coach that helps you understand your trading behavior and improve your performance.

## Features

- **AI-Powered Trading Analysis**: Hera uses advanced machine learning to analyze your trading behavior and offer feedback on your habits.
- **Emotional Impact Assessment**: Hera evaluates whether your trades are influenced by emotions, helping you make more rational decisions.
- **Roundtrip Identification**: Hera identifies when you're not exiting positions properly, causing potential roundtrips.
- **Paperhanding Detection**: Hera identifies moments where you might be selling too early, often due to fear or uncertainty.
- **Detailed Trading Reports**: Receive a comprehensive breakdown of your trading activity, including metrics like transaction volume, frequency, and performance.
- **Wallet Integration**: Simply tweet your Solana wallet address to interact with Hera and receive a personalized trading analysis.

## How to Use

### Twitter Integration

1. **Tweet Your Wallet**: To get started with Hera, simply tweet your Solana wallet address to the designated Twitter account (e.g., `@ImHeraAI`). Hera will automatically analyze your wallet activity and reply with a detailed review.
   
   Example tweet:
   ```
   @ImHeraAI Here's my wallet address: 5JzJ7e9uK27sMm38pK7cQz9dHeX5jYrmixvUjkQ98A4r
   ```

2. **Receive Your Analysis**: Hera will provide an in-depth analysis of your trading behavior, including feedback on emotional decision-making, paperhanding, roundtrips, and more. You'll receive a reply with a summary of your trading habits and tips to improve.

### Running Hera Locally

You can also run Hera directly from your local machine to analyze a specific wallet:

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/hera.git
```

2. **Navigate to the project directory**:

```bash
cd hera
```

3. **Set up the configuration files**:
   - Provide your Twitter API keys in `config/config.py`.
   - Set up Solana RPC node connection in `solana_rpc.py`.

4. **Provide your wallet address** and run the analysis:

```bash
python main.py --wallet "YourSolanaWalletAddress"
```

Hera will fetch your wallet's transaction data from the Solana blockchain and provide a detailed analysis based on your trading habits.

### Example Use Case

Tweet your wallet address at `@ImHeraAI`, and within minutes, Hera will reply with a detailed analysis of your trading behavior, providing actionable insights.

---

## How Hera Analyzes Your Trading

Hera’s AI model looks at several key factors in your trading history:

1. **Emotional Impact**: Hera evaluates whether your trades are influenced by market emotions like fear or greed. It looks for patterns of erratic behavior such as quick buys and sells.
   
2. **Roundtrips**: Hera identifies when you are buying and selling the same asset within a short time period, often indicative of overtrading or emotional decision-making.

3. **Paperhanding**: Hera detects situations where you might be selling assets prematurely, often due to fear of price dips, and provides feedback to help you hold your trades longer.

4. **Transaction Metrics**: Hera reviews metrics like transaction volume, frequency, and overall performance, giving you an idea of how successful your trades have been.

5. **Performance Feedback**: Based on your transaction data, Hera provides suggestions on how to improve your trading behavior and make smarter decisions.

---

## License

Hera is licensed under the MIT License. See the `LICENSE.md` file for more details.

## Contributing

We welcome contributions to Hera! If you have ideas or improvements, please fork the repository and submit a pull request.

### How to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your forked repository (`git push origin feature-branch`).
5. Create a pull request from your fork to the main repository.


Thank you for using Hera AI — your on-chain trading coach!
