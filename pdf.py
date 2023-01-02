from fpdf import FPDF
from card import Bingo
import PIL

def bingo_card(bingo_matriz):

def print_bingo_deck(n):
    """ 
    crate a pdf file with n quantity of bingo cards
    :param n: number of bingo cards to print

    """
    # setting pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)

    # creating a set of Card object using Bingo init
    bingo = Bingo(n)
    for card in bingo.deck:
        bingo_card(card.matriz)