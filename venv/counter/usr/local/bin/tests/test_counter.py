import pytest
import time
from datetime import datetime
from counter_service import handle_sigterm

def test_timestamp_format():
    """Test if the timestamp format is correct."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert len(timestamp) == 19  # Expected length of timestamp "YYYY-MM-DD HH:MM:SS"

def test_handle_sigterm(mocker):
    """Test if handle_sigterm writes the correct log message."""
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    mock_sys_exit = mocker.patch("sys.exit")

    handle_sigterm(15, None)  # Simulate SIGTERM

    mock_open.assert_called_once_with("/tmp/currentCount.out", "a")
    file_handle = mock_open()
    file_handle.write.assert_called()  # Check if write was called
    mock_sys_exit.assert_called_once()