from inspect import currentframe


def dPrint(content=''):
    """Generate a debug print line
    as a modifier to the original print function

    Args:
        content (): the content to be printed to the terminal
    """
    print(f"{currentframe().f_back.f_lineno}: {content}")
