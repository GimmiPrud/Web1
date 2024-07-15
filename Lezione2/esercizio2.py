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
pag = pag_11 + N * pag_12 + pag_13

with open("esercizio2.html", "w") as file:
    file.write(pag)
