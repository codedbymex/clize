from clize import run
from clize.extra.parameters import argument_decorator


@argument_decorator
def capitalize(arg, *, capitalize:('c', 'upper')=False, reverse:'r'=False):
    """
    Options to qualify {param}:

    capitalize: Make {param} uppercased

    reverse: Reverse {param}
    """
    if capitalize:
        arg = arg.upper()
    if reverse:
        arg = arg[::-1]
    return arg


def main(*args:capitalize):
    """
    args: stuff
    """
    return ' '.join(args)


run(main)
