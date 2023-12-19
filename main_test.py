import pytest
from main import ConferenceRoomBooking  # Update with the correct import path


class TestConferenceRoomBooking:
    def setup_method(self):
        self.booking_system = ConferenceRoomBooking()

    def test_initial_booking(self):
        assert self.booking_system.book(10, 20) is True

    def test_non_overlapping_booking(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(20, 30) is True

    def test_overlapping_booking(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(15, 25) is False

    def test_booking_starting_before_and_ending_after_another(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(5, 25) is False

    def test_booking_within_another_booking(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(12, 18) is False

    def test_booking_with_same_start_and_end_times(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(10, 20) is False

    def test_remove_existing_interval(self):
        self.booking_system.book(10, 20)
        self.booking_system.remove_interval(0)
        assert self.booking_system.book(10, 20) is True

    def test_remove_non_existing_interval(self):
        self.booking_system.book(10, 20)
        with pytest.raises(ValueError) as excinfo:
            self.booking_system.remove_interval(30)
        assert "Invalid_Index_Exception" in str(excinfo.value)
        assert self.booking_system.book(15, 25) is False

    def test_booking_edge_case_exact_overlap(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(20, 30) is True

    def test_booking_edge_case_no_overlap(self):
        self.booking_system.book(10, 20)
        assert self.booking_system.book(21, 30) is True
