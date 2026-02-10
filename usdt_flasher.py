#!/usr/bin/env python3
"""
USDT Transaction Simulator - Educational Tool Only

This tool simulates USDT (Tether) cryptocurrency transactions for educational
and testing purposes. It generates mock transaction data to help understand
how cryptocurrency transactions work.

WARNING: This is for EDUCATIONAL PURPOSES ONLY. 
- This tool does NOT interact with real blockchain networks
- It does NOT create real USDT tokens
- It does NOT perform actual cryptocurrency transactions
- Using this tool for fraudulent purposes is illegal

Purpose: Educational demonstration of cryptocurrency transaction concepts
"""

import json
import random
import hashlib
import time
from datetime import datetime
from typing import Dict, List


class USDTFlasher:
    """Educational USDT transaction simulator"""
    
    def __init__(self):
        self.transactions = []
        self.wallet_addresses = {}
        
    def generate_wallet_address(self, owner_name: str = "User") -> str:
        """Generate a mock wallet address"""
        random_part = ''.join(random.choices('0123456789abcdef', k=40))
        address = f"0x{random_part}"
        self.wallet_addresses[owner_name] = address
        return address
    
    def generate_transaction_hash(self, from_addr: str, to_addr: str, 
                                  amount: float, timestamp: float) -> str:
        """Generate a mock transaction hash"""
        data = f"{from_addr}{to_addr}{amount}{timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def create_mock_transaction(self, from_wallet: str, to_wallet: str, 
                                amount: float, note: str = "") -> Dict:
        """
        Create a simulated USDT transaction
        
        Args:
            from_wallet: Source wallet address or owner name
            to_wallet: Destination wallet address or owner name
            amount: Amount of USDT to simulate
            note: Optional transaction note
            
        Returns:
            Dictionary containing mock transaction details
        """
        # Get or create wallet addresses
        if from_wallet.startswith("0x"):
            from_addr = from_wallet
        else:
            from_addr = self.wallet_addresses.get(from_wallet) or \
                       self.generate_wallet_address(from_wallet)
        
        if to_wallet.startswith("0x"):
            to_addr = to_wallet
        else:
            to_addr = self.wallet_addresses.get(to_wallet) or \
                     self.generate_wallet_address(to_wallet)
        
        timestamp = time.time()
        tx_hash = self.generate_transaction_hash(from_addr, to_addr, 
                                                 amount, timestamp)
        
        transaction = {
            "transaction_hash": tx_hash,
            "from_address": from_addr,
            "to_address": to_addr,
            "amount": amount,
            "currency": "USDT",
            "timestamp": timestamp,
            "datetime": datetime.fromtimestamp(timestamp).isoformat(),
            "status": "simulated",
            "note": note,
            "warning": "THIS IS A SIMULATED TRANSACTION - NOT REAL"
        }
        
        self.transactions.append(transaction)
        return transaction
    
    def generate_transaction_receipt(self, transaction: Dict) -> str:
        """Generate a formatted transaction receipt"""
        receipt = f"""
{'='*60}
SIMULATED USDT TRANSACTION RECEIPT
{'='*60}
⚠️  WARNING: THIS IS NOT A REAL TRANSACTION ⚠️
This is a simulated transaction for educational purposes only.
{'='*60}

Transaction Hash: {transaction['transaction_hash']}
From:            {transaction['from_address']}
To:              {transaction['to_address']}
Amount:          {transaction['amount']:.2f} {transaction['currency']}
Date/Time:       {transaction['datetime']}
Status:          {transaction['status'].upper()}
Note:            {transaction['note'] or 'N/A'}

{'='*60}
EDUCATIONAL USE ONLY - NO REAL VALUE
{'='*60}
"""
        return receipt
    
    def display_transaction(self, transaction: Dict):
        """Display a transaction receipt"""
        print(self.generate_transaction_receipt(transaction))
    
    def get_transaction_history(self) -> List[Dict]:
        """Get all simulated transactions"""
        return self.transactions
    
    def export_transactions(self, filename: str = "simulated_transactions.json"):
        """Export transaction history to JSON file"""
        with open(filename, 'w') as f:
            json.dump({
                "warning": "These are SIMULATED transactions for educational purposes only",
                "transactions": self.transactions
            }, f, indent=2)
        print(f"Transactions exported to {filename}")


def main():
    """Main function demonstrating the USDT flasher tool"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║         USDT TRANSACTION SIMULATOR - EDUCATIONAL TOOL            ║
╚══════════════════════════════════════════════════════════════════╝

⚠️  IMPORTANT DISCLAIMER ⚠️
This tool is for EDUCATIONAL PURPOSES ONLY!
- Does NOT create real USDT tokens
- Does NOT interact with actual blockchain networks
- Does NOT perform real cryptocurrency transactions
- All transactions are SIMULATED for learning purposes

Using this tool for fraudulent purposes is ILLEGAL and UNETHICAL.
""")
    
    # Create flasher instance
    flasher = USDTFlasher()
    
    # Example 1: Generate wallet addresses
    print("\n1. Generating sample wallet addresses...")
    sender_addr = flasher.generate_wallet_address("Alice")
    receiver_addr = flasher.generate_wallet_address("Bob")
    print(f"   Alice's wallet: {sender_addr}")
    print(f"   Bob's wallet:   {receiver_addr}")
    
    # Example 2: Create a simulated transaction
    print("\n2. Creating simulated transaction...")
    tx1 = flasher.create_mock_transaction(
        from_wallet="Alice",
        to_wallet="Bob",
        amount=100.50,
        note="Educational demonstration payment"
    )
    flasher.display_transaction(tx1)
    
    # Example 3: Create another transaction
    print("\n3. Creating another simulated transaction...")
    tx2 = flasher.create_mock_transaction(
        from_wallet="Bob",
        to_wallet="Alice",
        amount=50.25,
        note="Return payment simulation"
    )
    flasher.display_transaction(tx2)
    
    # Example 4: Show transaction history
    print("\n4. Transaction History:")
    print(f"   Total simulated transactions: {len(flasher.get_transaction_history())}")
    
    # Example 5: Export transactions
    print("\n5. Exporting transaction history...")
    flasher.export_transactions()
    
    print("\n" + "="*60)
    print("Demo completed. Remember: These are SIMULATED transactions only!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
