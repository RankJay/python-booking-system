import csv

class ConferenceRoomBooking:
    """A class to manage bookings for a conference room."""

    def __init__(self):
        self.booked_intervals = []

    def book(self, start, end):
        """Attempt to book an interval. Return True if successful, False otherwise."""
        for interval in self.booked_intervals:
            if start < interval[1] and end > interval[0]:
                return False
        self.booked_intervals.append((start, end))
        return True

    def remove_interval(self, index):
        """Remove an interval based on its index."""
        if index < 0 or index >= len(self.booked_intervals):
            raise ValueError("Invalid index: Interval does not exist.")
        del self.booked_intervals[index]

def process_bookings(file_path):
    """Process a CSV file of booking requests."""
    booking_system = ConferenceRoomBooking()

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2 or not all(item.isdigit() for item in row):
                    raise ValueError("Invalid input: Each row must contain exactly two numeric values.")
                start, end = map(int, row)
                if start == 0:
                    booking_system.remove_interval(end)
                    print(f"Removed interval at index {end}")
                else:
                    result = booking_system.book(start, end)
                    status = "Booked" if result else "Failed"
                    print(f"Interval {start}-{end}: {status}")
    except FileNotFoundError:
        print("[Error]: File not found")
    except ValueError as e:
        print(f"[Error]: {e}")

if __name__ == "__main__":
    process_bookings("./test.csv")
