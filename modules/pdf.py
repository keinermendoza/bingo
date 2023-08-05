from fpdf import FPDF
import datetime
import os

class PDF(FPDF):
    """Extending the FPDF class of the fpdf library"""

    def bingo_card(
        self,
        card_matriz: list,
        card_id: int,
        max_id: int,
        title_background: tuple,
        title_color: tuple,
        title_text: str,
        title_size: int,
        title_aling: str,
        font_family: str,
    ):
        """
        Create a PDF with -n number of bingo cards, 6 by page.

        :param card_matriz: an 2D array of int. There is a list within 5 list within 5 integers. Represent a bingo card
        :type card_matriz: list

        :param card_id: number identification of a card in the deck
        :type card_id: int

        :param max_id: the number identification of the last card in the deck
        :type max_id: int

        :param title_background: the background color of card header in RGB format
        :type title_background: tuple

        :param title_color: the font color of card header background in RGB format
        :type title_background: tuple

        :param title_text: text for bingo header
        :type title_text: str

        :param title_size: font size of text for bingo header
        :type title_size: int

        :param title_aling: justify content of text in bingo header
        :type title_aling: str

        :param font_family: font family for all the text (including the numbers) in the bingo card
        :type font_family: str

        :raise IndexError: if card_matriz is not a list 5x5
        :raise TypeError: if card_id is not an integer
        :raise TypeError: if max_id is not an integer
        :raises AttributeError: if title_text is not a string
        :raises TypeError: if the title_background or title_color are not a tuple of 3 int
        :raises ValueError: if the title_background or title_color not contain 3 int in range 0-255
        :raises ValueError: if title_aling is not in ["C","R","L"]
        :raises fpdf.errors.FPDFExceptions: if font_family is not in ["helvetica", "times", "courier", "symbol", "zapfdingbats"]

        :return: None
        :rtype: None

        """

        col_width = 18
        col_height = 12
        space_end_of_card = 5
        zeros = len(str(max_id))
        # # Colors, line width and bold font:
        self.set_fill_color(*title_background)
        self.set_text_color(*title_color)

        # interpolate the print in two columns
        # moving the cursor up and to right
        if card_id % 2 == 0:
            self.x += 100
            self.y -= (col_height * 7) + space_end_of_card

        # printing title
        self.set_font(font_family, "", title_size)
        self.cell(
            col_width * 5,
            col_height,
            title_text,
            border=1,
            align=title_aling,
            fill=True,
        )

        # printing id card
        self.x -= col_width
        self.set_font(font_family, "", 8)
        self.cell(
            col_width,
            col_height,
            f"{card_id:0{zeros}}/{max_id}",
            border=0,
            align="R",
            fill=False,
        )
        self.set_font(font_family, "", 16)
        self.ln()

        # expresion for interpolate the print in two columns
        # moving the cursor to right
        if card_id % 2 == 0:
            self.x += 100

        # printing the header row "BINGO"

        for char in "BINGO":
            self.cell(col_width, col_height, char, border=1, align="C", fill=True)
        self.ln()

        # setting the text color to black
        self.set_text_color(0, 0, 0)
        for row in card_matriz:

            # expresion for interpolate the print in two columns
            # moving the cursor to right
            if card_id % 2 == 0:
                self.x += 100

            for i in range(5):

                # for the center of bingo
                if i == 2 and row[i] == 0:
                    self.set_font("zapfdingbats", "", 20)
                    self.cell(
                        col_width, col_height, "D", border=1, align="C", fill=True
                    )
                    self.set_font(font_family, "", 16)
                else:
                    self.cell(
                        col_width,
                        col_height,
                        str(row[i]),
                        border=1,
                        align="C",
                        fill=False,
                    )
            self.ln()

        # adding vertical blank space between cards
        self.y += space_end_of_card

        # adding a new page if this has 6 cards already printed
        if card_id < max_id and card_id % 6 == 0:
            self.add_page()

    @staticmethod
    def build_filename(title: str) -> str:
        """
        Takes a string, uses it to create a path in the bingo folder.
        :param title: a string
        :type title: str
        :returns: the created path
        :rtype: str
        """
        # create bingo folder if it doesn't exist
        os.makedirs("bingo", exist_ok=True)
        bingo_folder = os.path.relpath("bingo")

        # replacing problematic characters
        cleaning = title.strip().lower()
        cleaning = (
            cleaning.replace(" ", "_")
            .replace(".", "")
            .replace("/", "")
            .replace("\\", "")
            + "_"
        )

        # taking the present date
        today = str(datetime.date.today())

        # joining the parts and adding the pdf ectension
        filename = os.path.join(bingo_folder, cleaning + today + ".pdf")
        return filename

    @staticmethod
    def hexa_to_rgb(s: str) -> tuple:
        """
        Converts a string in format hexadecimal to a tuple in RGB format
        :param s: string of 6 hexadecimal charachters
        :type s: str
        :return: tuple of 3 integers in the range 0-255
        :rtype: tuple
        """
        return tuple(int(s[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def auto_set_font_size(s: str) -> tuple:
        """
        Determinates the size of the font and how to justify the title in the header of the bingo card
        :param s: title text
        :type s: str
        :return: tuple with an integer and a letter
        :rtype: tuple
        """
        if len(s) <= 15:
            return (16, "C")
        elif len(s) > 15:
            return (12, "L")