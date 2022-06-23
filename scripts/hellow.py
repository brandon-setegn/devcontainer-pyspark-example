"""
Hello World
"""
from utils import helper
import pandas as pd

# Formatting
pd.options.display.float_format = '{:,.1f}'.format

def main():
    """Say hello"""
    # Example using function from module un utils folder.
    helper.say_hello('my name is')

if __name__ == "__main__":
    main()
