import os
import numpy as np
import random
from PIL import Image
from flask import Flask, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import time

UPLOAD_FOLDER = './projectAssest/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','bmp'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER






# Function use to find score of every character
def KNNScore(arr, arr2):
    score = 0
    for y in range(0, 250):
        for x in range(0, 250):
            if(arr[x][y] == arr2[x][y]):
                score += 1
    return score


# Break picture into pixel and convert into binary
def image_pixel(image):
    im = Image.open(image)
    pix = im.load()
    # im=bbxcrop(pix,im)

    arr = np.array([None for i in range(62500)])
    arr.shape = (250, 250)
    for y in range(0, im.height):
        for x in range(0, im.width):
            ny = pix[x, y]
            img_rgb_pix = ((ny[0]+ny[1]+ny[2])/3)

            if (img_rgb_pix) < 100:
                arr[x, y] = 0

            elif (img_rgb_pix) > 100:
                arr[x, y] = 1

    return arr


# print("              ************* WELCOME NEW USER ************\n\n\n")
# print("             Please enter the path link of your character\n")
# print("      Our sytem will detect that specific character using KNN algorithm\n")
# print("         And predect the result using artificial intelligance\n")
# print("                        Hope you will enjoy....... \n")
# print("             It will help in your childern learning process\n\n\n")
# print("            Press any key to continue, Except power button :P ")
# input("")


# Test array store user define picture given through path link
test = np.array([None for i in range(62500)])
test.shape = (250, 250)


# Using char from 65 to 91 in to open jpg files from database
myaplha = 65


# Initilization of arrays/lists
n = [None for i in range(30)]
charaterhold = [None for i in range(30)]
aplha = [None for i in range(26)]


# Store A to Z in alpha array/list
for i in range(len(aplha)):
    aplha[i] = chr(myaplha)
    myaplha += 1


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploadFile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print("Response staret ============", request.files['file'])
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print("this is file ====", file)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = str(int(round(time.time() * 1000)))
            print("this is filename ====", filename)
            print("this is file path =====",
                  app.config['UPLOAD_FOLDER'] + filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



            image = "./projectAssest/" + filename
            testn = image_pixel(image)


            for j in range(0,26):
                dh = str(aplha[j])
                datahold = (dh+".jpg")
                charaterhold[j] = image_pixel(datahold)

            myvarct=1
            for j in range(26,30):
                dhh = str(myvarct)
                datahold = (dhh+".jpg")
                charaterhold[j] = image_pixel(datahold)
                myvarct+=1



            for j in range(30):
                n[j] = (KNNScore(testn, charaterhold[j]))
            min2 = -1
            inx = -1

            
            for i in range(0, len(n)):
                if(min2 < n[i]):
                    inx = i
                    min2 = n[i]

            myvalhold=65+inx
            if myvalhold<91:
                print("\n\n_______________________________________")
                print("Your given character is ", (chr)(myvalhold))
                print("_______________________________________\n\n")
                return {"name": (chr)(65+inx)}
            elif myvalhold==91:
                return {"name": "Imran khan Niazi"}
            elif myvalhold==92:
                return {"name": "Main Muhammad Nawaz Shareef"}
            elif myvalhold==93:
                return {"name": "Khadim Rizvi"}
            elif myvalhold==94:
                return {"name": "Zulfikar Ali Bhutto"}
            

            


if __name__ == "__main__":
    app.run(debug=True, port=8080)
