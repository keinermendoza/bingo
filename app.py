import re
import os
import tempfile

# flask librarys
from flask import Flask, request, render_template, redirect, url_for, send_file, flash, session
from flask_session import Session
from werkzeug.utils import secure_filename
# personal
from pdf import print_bingo_deck
from validation import allowed_image
from req import get_images, get_one_image

app = Flask(__name__)

# UPLOAD_FOLDER = os.getcwd() + "\static"


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """Introduction page"""
    list_img = get_images()
    return render_template("index.html", list_img=list_img)


@app.route("/create", methods=["POST"])
async def create():


    # # check if the post request has the file part
    # if 'file' not in request.files:
    #     flash('No file part')
    #     return redirect(url_for("index"))

    file = request.files['file']
        
    # If the user does not select a file, the browser submits an
    # empty file without a filename.

    ### FIRST CHECKCING IF USER NOT UPLOAD A FILE

    if file.filename == "":

        ### CHECKING IF USER NOT SELECT AN IMAGE
        if request.form.get("url_image_selected") == "":
            ## RETURNING THE LAST VIEW
            return redirect(request.url)

        ## if user pick up an image
        else:
            fold = tempfile.TemporaryDirectory()
            url_img = request.form.get("url_image_selected")
            
            path_temp_img = get_one_image(url_img=url_img, path_folder=fold.name)

            await print_bingo_deck(n=request.form.get("quantity"), img=path_temp_img)
            return send_file("bingo_deck.pdf", as_attachment=True)

    
    elif not file or not allowed_image(file.filename):
        ## RETURNING THE LAST VIEW
        return redirect(request.url)
        
    else:
        # creating and temporal folder

        fold = tempfile.TemporaryDirectory()

        #file_temp_name = "temp_name.jpg"
        #path_temp_file = fold.name + file_temp_name

        # extra checking the filename
        filename = secure_filename(file.filename)
        
        path_temp_file = fold.name + file.filename   
        
        file.save(path_temp_file)
        
        

        
        # https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
        # h = request.args.get("fill_color").lstrip('#')
        # tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        # creating a pdf with the amount of bingo cards solicited by the client
        await print_bingo_deck(n=request.form.get("quantity"), img=path_temp_file)

        return send_file("bingo_deck.pdf", as_attachment=True)
        
        