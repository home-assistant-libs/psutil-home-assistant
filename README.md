# psutil-home-assistant

The `psutil` library relies on global variable to maintain state between calls. This wrapper 
allows making local copies of the `psutil` library, wrapped in an object to allow `psutil` to
be used more than once in a process.
