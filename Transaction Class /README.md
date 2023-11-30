# Transaction System

This simple Python program demonstrates a basic transaction system. It consists of two classes: `Transaction` and `Amount`. The `Transaction` class is used to initiate and display transactions, while the `Amount` class represents an account with a name and balance.

## Usage

1. Create sender and recipient accounts:

    ```python
    sender = Amount("John", 1000)
    recipient = Amount("Alice", 500)
    ```

2. Initialize a transaction:

    ```python
    transaction = Transaction(sender, recipient, 300)
    ```

3. Execute the transaction:

    ```python
    transaction.send()
    ```

4. Display transaction details:

    ```python
    transaction.display()
    ```

## Transaction Details

The `display` method in the `Transaction` class provides detailed information about the transaction, including sender and recipient names, the amount sent, and balances before and after the transaction.

Example output:

---------------------------------
|         Transaction           |
---------------------------------
| Sender: John                  |
| Receiver: Alice               |
| Send Amount: 300              |
---------------------------------
| Before Transaction -          |
---------------------------------
| Sender Balance: 1300          |
| Receiver Balance: 200         |
---------------------------------
| After Transaction -           |
---------------------------------
| Sender Balance: 1000          |
| Receiver Balance: 500         |
---------------------------------

