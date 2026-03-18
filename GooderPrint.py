import io
import sys
from colorama import Fore, Style, init

init(autoreset=True)


COLORS = {
    "warn": Fore.YELLOW,
    "error": Fore.RED,
    "success": Fore.GREEN,
    "debug": Fore.LIGHTBLACK_EX,
    "normal": ""
}


ENABLE_COLOR = True


def _build_message(*objects, sep=' ', end='\n'):
    buffer = io.StringIO()
    print(*objects, sep=sep, end=end, file=buffer)
    return buffer.getvalue().rstrip("\n")


def _log(level, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    msg = _build_message(*objects, sep=sep, end=end)

    if ENABLE_COLOR and COLORS[level]:
        output = f"{COLORS[level]}{msg}{Style.RESET_ALL}"
    else:
        output = msg

    return msg

def warn(*objects, **kwargs):
    return _log("warn", *objects, **kwargs)


def error(*objects, **kwargs):
    print("error", *objects, **kwargs)


def success(*objects, **kwargs):
    print("success", *objects, **kwargs)


def debug(*objects, **kwargs):
    print("debug", *objects, **kwargs)


def normal(*objects, **kwargs):
    print("normal", *objects, **kwargs)


def print_raise(*objects, exc_type=Exception, sep=' ', end='\n', file=sys.stdout, flush=False):
    msg = _log("error", *objects, sep=sep, end=end, file=file, flush=flush)
    raise exc_type(msg)