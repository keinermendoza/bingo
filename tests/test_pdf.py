# Extra
from modules.pdf import PDF

def test_PDF_hexa_to_rgb():
    assert PDF.hexa_to_rgb("ff00ff") == (255, 0, 255)

def test_PDF_auto_set_font_size():
    assert PDF.auto_set_font_size("My bingo") == (16, "C")
    assert PDF.auto_set_font_size("The Greatest Bingo") == (12, "L")