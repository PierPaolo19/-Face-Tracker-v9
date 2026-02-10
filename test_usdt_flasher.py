#!/usr/bin/env python3
"""
Test suite for USDT Flasher Tool
Educational purposes only
"""

import json
import os
import sys
from usdt_flasher import USDTFlasher


def test_wallet_generation():
    """Test wallet address generation"""
    print("Testing wallet address generation...")
    flasher = USDTFlasher()
    
    # Test 1: Generate wallet address
    wallet1 = flasher.generate_wallet_address("TestUser1")
    assert wallet1.startswith("0x"), "Wallet should start with 0x"
    assert len(wallet1) == 42, f"Wallet should be 42 characters, got {len(wallet1)}"
    print("  ✓ Wallet address format is correct")
    
    # Test 2: Different users get different wallets
    wallet2 = flasher.generate_wallet_address("TestUser2")
    assert wallet1 != wallet2, "Different users should get different wallets"
    print("  ✓ Different users get unique wallets")
    
    # Test 3: Wallet is stored in dictionary
    assert "TestUser1" in flasher.wallet_addresses, "Wallet should be stored"
    print("  ✓ Wallet addresses are stored correctly")
    
    print("✓ All wallet generation tests passed!\n")


def test_transaction_creation():
    """Test transaction creation"""
    print("Testing transaction creation...")
    flasher = USDTFlasher()
    
    # Test 1: Create a transaction
    tx = flasher.create_mock_transaction(
        from_wallet="Sender",
        to_wallet="Receiver",
        amount=50.0,
        note="Test transaction"
    )
    
    assert "transaction_hash" in tx, "Transaction should have a hash"
    assert "from_address" in tx, "Transaction should have from_address"
    assert "to_address" in tx, "Transaction should have to_address"
    assert tx["amount"] == 50.0, "Transaction amount should match"
    assert tx["currency"] == "USDT", "Currency should be USDT"
    assert tx["status"] == "simulated", "Status should be simulated"
    print("  ✓ Transaction structure is correct")
    
    # Test 2: Transaction hash is unique
    tx2 = flasher.create_mock_transaction(
        from_wallet="Sender",
        to_wallet="Receiver",
        amount=50.0,
        note="Another test"
    )
    assert tx["transaction_hash"] != tx2["transaction_hash"], \
        "Different transactions should have different hashes"
    print("  ✓ Transaction hashes are unique")
    
    # Test 3: Transaction is stored
    assert len(flasher.transactions) == 2, "Transactions should be stored"
    print("  ✓ Transactions are stored in history")
    
    print("✓ All transaction creation tests passed!\n")


def test_transaction_hash():
    """Test transaction hash generation"""
    print("Testing transaction hash generation...")
    flasher = USDTFlasher()
    
    # Test 1: Hash is deterministic
    addr1 = "0x1234567890abcdef1234567890abcdef12345678"
    addr2 = "0xfedcba0987654321fedcba0987654321fedcba09"
    amount = 100.0
    timestamp = 1234567890.0
    
    hash1 = flasher.generate_transaction_hash(addr1, addr2, amount, timestamp)
    hash2 = flasher.generate_transaction_hash(addr1, addr2, amount, timestamp)
    
    assert hash1 == hash2, "Same inputs should produce same hash"
    print("  ✓ Hash generation is deterministic")
    
    # Test 2: Different inputs produce different hashes
    hash3 = flasher.generate_transaction_hash(addr2, addr1, amount, timestamp)
    assert hash1 != hash3, "Different inputs should produce different hashes"
    print("  ✓ Different inputs produce different hashes")
    
    # Test 3: Hash is hex string
    assert all(c in '0123456789abcdef' for c in hash1), \
        "Hash should be hexadecimal"
    print("  ✓ Hash is valid hexadecimal")
    
    print("✓ All hash generation tests passed!\n")


def test_export_functionality():
    """Test transaction export"""
    print("Testing transaction export...")
    flasher = USDTFlasher()
    
    # Create some transactions
    flasher.create_mock_transaction("Alice", "Bob", 100.0, "Test 1")
    flasher.create_mock_transaction("Bob", "Charlie", 50.0, "Test 2")
    
    # Export to test file
    test_file = "test_export.json"
    flasher.export_transactions(test_file)
    
    # Test 1: File exists
    assert os.path.exists(test_file), "Export file should be created"
    print("  ✓ Export file is created")
    
    # Test 2: File content is valid JSON
    with open(test_file, 'r') as f:
        data = json.load(f)
    assert "warning" in data, "Export should include warning"
    assert "transactions" in data, "Export should include transactions"
    assert len(data["transactions"]) == 2, "Should export all transactions"
    print("  ✓ Export file contains valid JSON")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    print("  ✓ Cleanup completed")
    
    print("✓ All export tests passed!\n")


def test_transaction_history():
    """Test transaction history retrieval"""
    print("Testing transaction history...")
    flasher = USDTFlasher()
    
    # Initially empty
    assert len(flasher.get_transaction_history()) == 0, \
        "Initial history should be empty"
    print("  ✓ Initial history is empty")
    
    # Add transactions
    flasher.create_mock_transaction("A", "B", 10.0)
    flasher.create_mock_transaction("B", "C", 20.0)
    flasher.create_mock_transaction("C", "A", 30.0)
    
    history = flasher.get_transaction_history()
    assert len(history) == 3, "Should have 3 transactions"
    assert history[0]["amount"] == 10.0, "First transaction amount should match"
    assert history[1]["amount"] == 20.0, "Second transaction amount should match"
    assert history[2]["amount"] == 30.0, "Third transaction amount should match"
    print("  ✓ Transaction history is correct")
    
    print("✓ All history tests passed!\n")


def run_all_tests():
    """Run all test suites"""
    print("="*60)
    print("USDT FLASHER TOOL - TEST SUITE")
    print("Educational Testing Only")
    print("="*60 + "\n")
    
    try:
        test_wallet_generation()
        test_transaction_creation()
        test_transaction_hash()
        test_export_functionality()
        test_transaction_history()
        
        print("="*60)
        print("✓ ALL TESTS PASSED!")
        print("="*60)
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        print("="*60)
        return 1
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}")
        print("="*60)
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
