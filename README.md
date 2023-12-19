# Conference Booking System

The code in [`main.py`](command:_github.copilot.openRelativePath?%5B%22main.py%22%5D "main.py") is for a simple conference room booking system. Here's a brief explanation of the key parts:

- [`ConferenceRoomBooking`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22ConferenceRoomBooking%22%5D "main.py") is a class that represents a booking system. It has a list of [`booked_intervals`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22booked_intervals%22%5D "main.py") which stores the start and end times of each booking.

- The [`book`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22book%22%5D "main.py") method takes a start and end time and checks if the room is available during that time. If it is, it adds the booking to [`booked_intervals`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22booked_intervals%22%5D "main.py") and returns `True`. If the room is already booked during that time, it returns `False`.

- The [`remove_interval`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22remove_interval%22%5D "main.py") method removes a booking from [`booked_intervals`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22booked_intervals%22%5D "main.py") based on its index.

- The [`process_bookings`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22process_bookings%22%5D "main.py") function reads a CSV file where each row represents a booking or a removal of a booking. If the start time is 0, it removes the booking at the index specified by the end time index. Otherwise, it attempts to book the room for the specified start and end times.

- The `if __name__ == "__main__"` block is the entry point of the script. It calls [`process_bookings`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22process_bookings%22%5D "main.py") with the path to the CSV file.

The [venv](venv/) directory is a virtual environment for Python. It contains the Python interpreter, installed packages, and scripts. The [`test.csv`](command:_github.copilot.openRelativePath?%5B%22test.csv%22%5D "test.csv") file is used to test the booking system.

# Local Setup

1. **Install Python**: Make sure you have Python installed on your local machine. You can download it from the official Python website.

2. **Install pip**: pip is a package manager for Python. It's used to install and manage Python packages. If you installed Python from the official website, pip should have been installed automatically.

3. **Create a virtual environment (optional)**: This is not strictly necessary, but it's a good practice to create a virtual environment for each Python project. This helps to keep the dependencies for each project separate and avoid conflicts. You can create a virtual environment using the `venv` module:

    ```bash
    python3 -m venv env
    ```

    This will create a new virtual environment in a folder called `env`.

4. **Activate the virtual environment**: Before you can use the virtual environment, you need to activate it:

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source env/bin/activate
        ```

    When the virtual environment is activated, your shell prompt will change to show the name of the virtual environment.

5. **Install the required packages**: If your project has a `requirements.txt` file, you can install all the required packages with one command:

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the main script**: You can run the main script with the following command:

    ```bash
    python main.py
    ```

    NOTE: If you want to test with different set of data. Feel free to update the `test.csv` file content and execute the program again to see the new output.

    This will execute the `main.py` script and print the results to the console.

7. **Run the tests**: If your tests are written using a framework like `pytest`, you can run them with the following command:

    ```bash
    pytest main_test.py
    ```

    This will run all the tests in `main_test.py` and print the results to the console.

8. **Deactivate the virtual environment**: When you're done, you can deactivate the virtual environment by running:

    ```bash
    deactivate
    ```

    This will return your shell prompt to normal.