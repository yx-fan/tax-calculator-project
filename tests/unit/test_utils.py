from app.utils import log_debug, log_info, log_warning, log_error

def test_logging():
    """
    Test that the logging functions log messages to the app.log file.
    """
    log_debug("Test Debug Message")
    log_info("Test Info Message")
    log_warning("Test Warning Message")
    log_error("Test Error Message")

    with open("app.log", "r") as log_file:
        logs = log_file.read()
    
    assert "Test Debug Message" in logs
    assert "Test Info Message" in logs
    assert "Test Warning Message" in logs
    assert "Test Error Message" in logs
    