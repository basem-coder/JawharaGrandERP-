class ErrorHandler:
    def handle(self, error):
        """Handles generic errors by logging and providing feedback."""
        print(f'Error occurred: {error}')


class DatabaseErrorHandler(ErrorHandler):
    def handle(self, error):
        """Handles database-specific errors."""
        print(f'Database error occurred: {error}')


class InputValidator:
    @staticmethod
    def validate(input_data):
        """Validates input data and throws error if invalid."""
        if not input_data:
            raise ValueError('Input cannot be empty.')
        # Additional validation logic...
        print('Input is valid.')


# Example usage:
try:
    InputValidator.validate('some input')
except ValueError as e:
    ErrorHandler().handle(e)

try:
    # Simulate database operation
    raise Exception('Database connection failed.')
except Exception as e:
    DatabaseErrorHandler().handle(e)