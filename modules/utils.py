# copied from "EL programador chapuzas"
def progres_bar(progres, total):
    percent = 100 * (progres / float(total))
    bar = ("|" * int(percent) + "_" * (100 - int(percent )))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")