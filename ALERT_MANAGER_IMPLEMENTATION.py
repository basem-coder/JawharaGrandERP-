class AlertManager:
    def __init__(self):
        self.low_cash_threshold = 100.0  # Define a threshold for low cash alerts
        self.overdue_rent_alerts = []
        self.error_messages = []

    def check_low_cash(self, current_cash):
        if current_cash < self.low_cash_threshold:
            self.trigger_low_cash_alert(current_cash)

    def trigger_low_cash_alert(self, current_cash):
        message = f"Low cash alert: Current cash is ${current_cash:.2f}"
        self.error_messages.append(message)
        print(message)

    def check_overdue_rent(self, rent_due_date, current_date):
        if current_date > rent_due_date:
            self.trigger_overdue_rent_alert(rent_due_date)

    def trigger_overdue_rent_alert(self, rent_due_date):
        message = f"Overdue rent alert: Rent due since {rent_due_date.strftime('%Y-%m-%d')}"
        self.overdue_rent_alerts.append(message)
        print(message)

    def display_alerts(self):
        print("Alerts:")
        for message in self.error_messages:
            print(message)
        for message in self.overdue_rent_alerts:
            print(message)

    def handle_error(self, error_message):
        self.error_messages.append(error_message)
        print(f"Error: {error_message}")

# Usage Example
if __name__ == '__main__':
    alert_manager = AlertManager()
    alert_manager.check_low_cash(50.0)  # Will trigger low cash alert
    alert_manager.check_overdue_rent(datetime.date(2026, 3, 27), datetime.date(2026, 3, 28))  # Will trigger overdue rent alert
    alert_manager.display_alerts()