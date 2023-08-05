import argparse
import re
from modules.pdf import PDF
from modules.deck import Bingo
from modules.utils import progres_bar

def main():
    # parsing the arguments form the comand line
    parser = argparse.ArgumentParser(
        description="Create a PDF file with bingo cards in it.",
      )
    parser.add_argument(
        "-n",
        required=True,
        help="Number of bingo cards to create. Must be an integer between 1 and 2000. Example: -n 80",
        type=limit_cards_by_deck,
    
    )
    parser.add_argument(
        "-t",
        default="My Bingo",
        help="Bingo card title, also used to create the filename. Can be between 1 and 29 characters. Example: t- 'My First Bingo'",
        type=limit_title_len,
    )
    parser.add_argument(
        "-bc",
        default="ffffff",
        help="Background color for the header of bingo cards, in hexadecimal format. Example: bc- '0000ff'",
        type=hexadecimal_format,
    )
    parser.add_argument(
        "-c",
        default="000000",
        help="Color for the header of bingo cards, in hexadecimal format. Example: c- '0000ff'",
        type=hexadecimal_format,
    )
    parser.add_argument(
        "-f",
        default="helvetica",
        choices=["helvetica", "times", "courier", "symbol", "zapfdingbats"],
        help="font-family to use in the document. Example: f- 'times'",
        type=str,
    )

    args = parser.parse_args()

    # setting the arguments for use in the PDF
    font_family = args.f
    title_color = PDF.hexa_to_rgb(args.c)
    title_background = PDF.hexa_to_rgb(args.bc)

    title_text = args.t
    title_size, title_aling = PDF.auto_set_font_size(args.t)
    filename = PDF.build_filename(args.t)

    bingo = Bingo(args.n)
    max_id: int = bingo.times

    # setting pdf
    pdf = PDF()
    pdf.add_page()

    # iterating over each card in the bingo deck
    # and printing to the PDF one at a time
    print(f"\n\nPrinting Bingo Cards in {filename}")
    for card in bingo.deck:
        pdf.bingo_card(
            card.matriz,
            card.id,
            max_id,
            title_background,
            title_color,
            title_text,
            title_size,
            title_aling,
            font_family,
        )
        progres_bar(card.id, max_id)
    pdf.output(filename)
    
    print("\n\nPDF Created Successfully!")


### This 3 next functions are for the parser
def hexadecimal_format(arg: str) -> str:
    """
    Cheack that a string has 6 characters in hexadecimal format
    :param arg: string to check
    :raises argparse.ArgumentTypeError: if string is not in hexadecimal format
    :return: the same string if has the right format
    :rtype: str
    """
    if not re.search(r"^([a-f0-9]{6})$", arg):
        raise argparse.ArgumentTypeError(
            "arg must be in hexadecimal format. Example: '0000ff'",
        )
    return arg


def limit_title_len(arg: str) -> str:
    """
    Cheack that a string has less or equal than 29 characters
    :param arg: string to check
    :raises argparse.ArgumentTypeError: if string has more than 29 characters
    :return: the same string if has the less or equal than 29 characters
    :rtype: str
    """

    if len(arg) > 29:
        raise argparse.ArgumentTypeError(
            "Title cannot have more than 29 characters",
        )
    return arg

def limit_cards_by_deck(arg: int) -> int:
    """
    Cheack that a arg be an intger, and check if is in range 1 to 2000
    :param arg: an intger to check
    :raises argparse.ArgumentTypeError: if arg is not an integer or if is less than 1 or greater than 2000
    :return: the same integer
    :rtype: int
    """
    try:
        n = int(arg)      
        if n < 1 or n > 2000:
            raise ValueError
    except:
        raise argparse.ArgumentTypeError(
            "-n must be an integer between 1 and 2000",
        )
    return n


if __name__ == "__main__":
    main()
