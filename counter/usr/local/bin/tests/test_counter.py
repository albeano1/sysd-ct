import pytest
import time
from datetime import datetime
from counter_service import handle_sigterm

def test_timestamp_format():
    """Test if the timestamp format is correct."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert len(timestamp) == 19  # Expected length of timestamp "YYYY-MM-DD HH:MM:SS"
    # Additional check to ensure the format is correct
    datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")  # This will raise ValueError if the format is wrong

def test_handle_sigterm(mocker):
    """Test if handle_sigterm writes the correct log message."""
    # Mock the open function and sys.exit
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    mock_sys_exit = mocker.patch("sys.exit")

    # Mock the username to ensure consistency
    mock_user = "test_user"
    mocker.patch("counter_service.user", mock_user)

    # Call the handle_sigterm function with SIGTERM signal
    handle_sigterm(15, None)  # SIGTERM is signal number 15

    # Verify that the file was opened in append mode
    mock_open.assert_called_once_with("/tmp/currentCount.out", "a")

    # Verify that the correct message was written to the file
    file_handle = mock_open()
    expected_message = f"{mock_user}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Received SIGTERM, exiting\n"
    file_handle.write.assert_called_once_with(expected_message)

    # Verify that sys.exit was called with exit code 0
    mock_sys_exit.assert_called_once_with(0)