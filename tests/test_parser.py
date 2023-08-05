import pytest
import argparse
from bingo import hexadecimal_format,\
                  limit_title_len

def test_argparse_hexadecimal_format():
    assert hexadecimal_format("00ff00") == ("00ff00")
    with pytest.raises(argparse.ArgumentTypeError):
        hexadecimal_format("00ff00ff")

def test_argparse_hexadecimal_format():
    assert limit_title_len("My Bingo") == "My Bingo"
    with pytest.raises(argparse.ArgumentTypeError):
        limit_title_len("raise ArgumentType error for more than twenty-nine characters")
