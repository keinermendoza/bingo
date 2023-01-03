from fpdf import FPDF
from card import Bingo
import PIL

class PDF(FPDF):
    def bingo_card(self, bingo_matriz, card_id, max_id, img=None):
        """
        :param max_id: the id of the last card inside the bingo object
        :type max_id: int
        :param card_id: the id of the current bingo card
        :type card_id: int
        :param bingo_matriz: an 2D array of int. each list represent a sorted column of a bingo card
        :type bingo_matriz: list
        :param img: the path of an image for insert as background of each bingo card
        :type img: str
        """
        col_width = 16
        col_height = 14
        space_end_of_card = 5
        # # Colors, line width and bold font:
        # self.set_fill_color(255, 100, 0)
        # self.set_text_color(255)
        # self.set_draw_color(255, 0, 0)
        # self.set_line_width(0.3)

        # expresion for interpolate the print in two columns
        # moving the cursor up and to right 
        if card_id % 2 == 0:
            self.x += 100
            self.y -= (col_height*6) + space_end_of_card
        
        if img:

            # storing the current position
            x = self.x
            y = self.y

            # inserting image 
            self.image(img, h=col_height*6, w=col_width*5)

            # resoring the before position

            self.x = x
            self.y = y

        # printing the 2D array over the image
        for char in "BINGO":
            self.cell(col_width, col_height, char, border=1, align="C", fill=False)
        self.ln()

        for row in bingo_matriz:
            
            # expresion for interpolate the print in two columns
            # moving the cursor to right
            if card_id % 2 == 0:
                self.x += 100

            for i in range(5):
                self.cell(col_width, col_height, str(row[i]), border=1, align="C", fill=False)
            self.ln()

        self.y += space_end_of_card

        # adding a new page if this has 6 cards already printed
        if card_id < max_id and  card_id % 6 == 0:
            self.add_page()


async  def print_bingo_deck(n):
    """ 
    crate a pdf file with n quantity of bingo cards
    :param n: number of bingo cards to print

    """
    # setting pdf
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)

    # creating a set of Card object using Bingo init
    bingo = Bingo(9)
    for card in bingo.deck:
        pdf.bingo_card(card.matriz, card.id, bingo.times, "car.jpg" )
    pdf.output("bingo_deck.pdf")
