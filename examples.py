#!/usr/bin/env python3
"""
Example usage of USDT Flasher Tool
Educational demonstration of the API
"""

from usdt_flasher import USDTFlasher

def example_basic_usage():
    """Basic usage example"""
    print("="*60)
    print("EXAMPLE 1: Basic Usage")
    print("="*60)
    
    # Create flasher instance
    flasher = USDTFlasher()
    
    # Generate wallets
    alice = flasher.generate_wallet_address("Alice")
    bob = flasher.generate_wallet_address("Bob")
    
    print(f"Alice's wallet: {alice}")
    print(f"Bob's wallet:   {bob}")
    
    # Create transaction
    tx = flasher.create_mock_transaction(
        from_wallet="Alice",
        to_wallet="Bob",
        amount=250.75,
        note="Payment for services"
    )
    
    # Display transaction
    flasher.display_transaction(tx)


def example_multiple_transactions():
    """Example with multiple transactions"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Multiple Transactions")
    print("="*60)
    
    flasher = USDTFlasher()
    
    # Create a network of transactions
    users = ["Alice", "Bob", "Charlie", "Dave"]
    
    print("\nGenerating wallets for users...")
    for user in users:
        wallet = flasher.generate_wallet_address(user)
        print(f"  {user}: {wallet[:20]}...")
    
    print("\nCreating transaction chain...")
    transactions = [
        ("Alice", "Bob", 100.0, "Initial payment"),
        ("Bob", "Charlie", 50.0, "Partial forward"),
        ("Charlie", "Dave", 25.0, "Final transfer"),
        ("Dave", "Alice", 10.0, "Return payment")
    ]
    
    for from_user, to_user, amount, note in transactions:
        tx = flasher.create_mock_transaction(from_user, to_user, amount, note)
        print(f"  {from_user} -> {to_user}: {amount} USDT ({note})")
    
    print(f"\nTotal transactions: {len(flasher.get_transaction_history())}")


def example_export():
    """Example of exporting transactions"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Exporting Transaction History")
    print("="*60)
    
    flasher = USDTFlasher()
    
    # Create some sample transactions
    flasher.create_mock_transaction("Merchant", "Supplier", 1000.0, "Inventory purchase")
    flasher.create_mock_transaction("Customer", "Merchant", 150.0, "Product sale")
    flasher.create_mock_transaction("Supplier", "Manufacturer", 800.0, "Raw materials")
    
    # Export to file
    filename = "example_transactions.json"
    flasher.export_transactions(filename)
    print(f"\nExported {len(flasher.get_transaction_history())} transactions to {filename}")
    print("Note: This file is excluded from git via .gitignore")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════╗
║              USDT FLASHER - USAGE EXAMPLES                       ║
║                 EDUCATIONAL TOOL ONLY                            ║
╚══════════════════════════════════════════════════════════════════╝

⚠️  All transactions shown here are SIMULATED for educational purposes ⚠️
""")
    
    example_basic_usage()
    example_multiple_transactions()
    example_export()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("Remember: All transactions are simulated for education only.")
    print("="*60 + "\n")
