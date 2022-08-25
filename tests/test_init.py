import psutil
import psutil_home_assistant

def test_multiple_copies():
    """Test that multiple psutil instances can be created and do not interfere."""

    psutil1 = psutil_home_assistant.PsutilWrapper()
    psutil2 = psutil_home_assistant.PsutilWrapper()

    assert psutil._last_cpu_times is not psutil1.psutil._last_cpu_times
    assert psutil1.psutil._last_cpu_times is not psutil2.psutil._last_cpu_times
