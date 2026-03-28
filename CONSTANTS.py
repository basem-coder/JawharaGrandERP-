# CONSTANTS.py

# Database Tables
DATABASE_TABLES = {
    'users': 'users',
    'products': 'products',
    'orders': 'orders',
    'payments': 'payments',
}

# UI Messages
UI_MESSAGES = {
    'welcome': 'Welcome to Jawhara Grand ERP!',
    'error': 'An error occurred, please try again!',
    'success': 'Operation completed successfully!',
}

# Account Types
ACCOUNT_TYPES = {
    'admin': 'Administrator',
    'customer': 'Customer',
    'vendor': 'Vendor',
}

# Payment Methods
PAYMENT_METHODS = {
    'credit_card': 'Credit Card',
    'paypal': 'PayPal',
    'bank_transfer': 'Bank Transfer',
}

# Other Configuration Values
CONFIG = {
    'max_upload_size': 10 * 1024 * 1024,  # 10 MB
    'currency': 'USD',
    'timezone': 'UTC',
}