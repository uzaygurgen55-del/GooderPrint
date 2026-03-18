import io

RESET = "\033[0m"
WARNING_COLOR = "\033[33m"
ERROR_COLOR = "\033[31m"
SUCCESS_COLOR = "\033[32m"
DEBUG_COLOR = "\033[90m"

def _build_message(*objects, sep=' ', end='\n'):
    buffer = io.StringIO()
    print(*objects, sep=sep, end=end, file=buffer)
    return buffer.getvalue().rstrip("\n")

def warn(*objects, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    print(WARNING_COLOR + msg + RESET, end=end)
    return msg

def error(*objects, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    print(ERROR_COLOR + msg + RESET, end=end)
    return msg

def success(*objects, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    print(SUCCESS_COLOR + msg + RESET, end=end)
    return msg

def debug(*objects, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    print(DEBUG_COLOR + msg + RESET, end=end)
    return msg

def raise_warning(*objects, exc_type=UserWarning, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    raise exc_type(msg)

def raise_error(*objects, exc_type=Exception, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    raise exc_type(msg)

def normal(*objects, sep=' ', end='\n'):
    msg = _build_message(*objects, sep=sep, end=end)
    print(msg)