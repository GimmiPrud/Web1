pag_10 = '''<!DOCTYPE html>
<html>
    <head>
        <style>
            body {   
        background-position: center;
        background-image: url(image/maxresdefault.jpg);
        }
        .grid-container {
        display: grid;
        height: 400px;
        align-content: center;
        display: table;
        }
        .grid-item {
        background-color: rgba(243, 239, 20, 0.8);
        border: 1pc solid rgba(226, 9, 117, 0.8);
        padding: 20px;
        font-size: 30px;
        text-align: center;
        }
        </style>
    </head>
        <body>
            <center>
                <font style="color: rgb(255, 217, 4);">
                <h1>COMPONENTI COMPUTER </h1>
            </font>'''

pag_11  =  '''
    <div class="grid-container">
    <div class="grid-item">
        <div class="row">
            <div class="col">
                <img src="image/cpu.png" alt="CPU">
            </div>
            <div class="col">
                <p>
                    <font style = "margin: auto; color: rgb(83, 24, 138);">
                    <h3>
                        CPU
                    </h3>
                    </font>
                </p>
            </div>
          </div>
    </div>'''

pag_12 = '''  <div class="grid-item">
        <div class="row">
            <div class="col">
              <img src="image/scheda_madre.webp" style="height: 30pc;">
            </div>
            <div class="col">
                <p>
                    <font style = "margin: auto; color: rgb(83, 24, 138);">
                    <h3>
                        schede madri
                    </h3>
                    </font>
                </p>
            </div>
          </div>
    </div>'''

pag_13 = '''<div class="grid-item">
        <div class="row">
            <div class="col">
                <img src="image/scheda_video.png" alt="schede video" style="height: 30pc;">
            </div>
            <div class="col">
                <p>
                    <font style = "margin: auto; color: rgb(83, 24, 138);">
                    <h3>
                        schede video
                    </h3>
                    </font>
                </p>
            </div>
          </div>
    </div>  '''

N = 3
pag = pag_10 + pag_11 + N * pag_12 + pag_13

with open("esercizio2.html", "w") as file:
    file.write(pag)
