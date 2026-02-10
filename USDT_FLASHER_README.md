# USDT Flasher Tool - Educational Cryptocurrency Simulator

## ⚠️ IMPORTANT DISCLAIMER ⚠️

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY!**

- This tool **DOES NOT** create real USDT (Tether) tokens
- This tool **DOES NOT** interact with actual blockchain networks
- This tool **DOES NOT** perform real cryptocurrency transactions
- All transactions generated are **SIMULATED** for learning purposes only

**Using this or similar tools for fraudulent purposes is ILLEGAL and UNETHICAL.**

This tool is designed to help understand how cryptocurrency transactions work by simulating the transaction process.

## Purpose

The USDT Flasher is an educational tool that demonstrates:
- How cryptocurrency wallet addresses are structured
- How transaction hashes are generated
- The basic structure of cryptocurrency transactions
- Transaction receipt formatting

## Features

- Generate mock wallet addresses
- Create simulated USDT transactions
- Generate transaction hashes
- Display formatted transaction receipts
- Export transaction history to JSON
- Clear labeling of all simulated data

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

No installation required. Simply run the Python script:

```bash
python3 usdt_flasher.py
```

## Usage

### Quick Demo

Run the demo program to see all features:

```bash
python3 usdt_flasher.py
```

### Examples

Run the examples script to see common usage patterns:

```bash
python3 examples.py
```

### Basic Usage

Run the demo program:

```bash
python3 usdt_flasher.py
```

This will demonstrate:
1. Wallet address generation
2. Transaction creation
3. Transaction receipt display
4. Transaction history
5. JSON export

### Advanced Usage (Library)

You can also import and use the `USDTFlasher` class in your own educational projects:

```python
from usdt_flasher import USDTFlasher

# Create a flasher instance
flasher = USDTFlasher()

# Generate wallet addresses
alice_wallet = flasher.generate_wallet_address("Alice")
bob_wallet = flasher.generate_wallet_address("Bob")

# Create a simulated transaction
transaction = flasher.create_mock_transaction(
    from_wallet="Alice",
    to_wallet="Bob",
    amount=100.00,
    note="Educational demo"
)

# Display the transaction
flasher.display_transaction(transaction)

# Export all transactions
flasher.export_transactions("my_simulations.json")
```

## API Reference

### `USDTFlasher` Class

#### Methods

- `generate_wallet_address(owner_name: str) -> str`
  - Generates a mock Ethereum-style wallet address
  - Parameters: `owner_name` - Name to associate with the wallet
  - Returns: A string representing the mock wallet address

- `create_mock_transaction(from_wallet: str, to_wallet: str, amount: float, note: str) -> Dict`
  - Creates a simulated USDT transaction
  - Parameters:
    - `from_wallet` - Source wallet (address or owner name)
    - `to_wallet` - Destination wallet (address or owner name)
    - `amount` - Amount of USDT to simulate
    - `note` - Optional transaction note
  - Returns: Dictionary containing transaction details

- `display_transaction(transaction: Dict)`
  - Prints a formatted transaction receipt

- `get_transaction_history() -> List[Dict]`
  - Returns all simulated transactions

- `export_transactions(filename: str)`
  - Exports transaction history to a JSON file

## Example Output

```
╔══════════════════════════════════════════════════════════════════╗
║         USDT TRANSACTION SIMULATOR - EDUCATIONAL TOOL            ║
╚══════════════════════════════════════════════════════════════════╝

⚠️  IMPORTANT DISCLAIMER ⚠️
This tool is for EDUCATIONAL PURPOSES ONLY!

============================================================
SIMULATED USDT TRANSACTION RECEIPT
============================================================
⚠️  WARNING: THIS IS NOT A REAL TRANSACTION ⚠️
============================================================

Transaction Hash: 7a3f8b2c...
From:            0x1a2b3c...
To:              0x4d5e6f...
Amount:          100.50 USDT
Date/Time:       2026-02-10T23:30:00
Status:          SIMULATED
Note:            Educational demonstration payment

============================================================
EDUCATIONAL USE ONLY - NO REAL VALUE
============================================================
```

## Educational Use Cases

This tool can be used to:
1. Learn about cryptocurrency transaction structure
2. Understand wallet address formats
3. Study transaction hashing mechanisms
4. Practice with cryptocurrency concepts without risk
5. Develop educational materials about blockchain technology
6. Test applications that need mock transaction data

## Legal and Ethical Considerations

- **Never** use this tool to deceive others
- **Never** claim simulated transactions are real
- **Never** use this for fraudulent purposes
- **Always** clearly indicate that transactions are simulated
- Use only for legitimate educational purposes

## License

This educational tool is provided as-is for learning purposes.

## Support

This is an educational demonstration tool. For questions about real cryptocurrency transactions, please consult official cryptocurrency documentation and legitimate financial advisors.

---

**Remember: Cryptocurrency fraud is a serious crime. This tool is for education only.**
