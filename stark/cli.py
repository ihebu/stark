import argparse

from .app import generate
from .args import add_arguments


# Create a custom help formatter class to disable disaplying metavar in help message
# https://github.com/python/cpython/blob/master/Lib/argparse.py
class CustomFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            (metavar,) = self._metavar_formatter(action, default)(1)
            return metavar
        else:
            parts = []
            parts.extend(action.option_strings)
            return ", ".join(parts)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=CustomFormatter,
        usage="stark [options]",
        description="stark generates random and strong passwords",
    )
    add_arguments(parser)
    args = parser.parse_args().__dict__
    length = args.pop("length")
    args = {key: value for key, value in args.items() if value}
    try:
        password = generate(length=length, types=args)
        print(password)
    except Exception as e:
        parser.error(str(e))
