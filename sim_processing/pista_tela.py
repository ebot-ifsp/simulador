def desenha_pista(pista, tipo):
    background(30, 125, 30)
    # desenha a pista
    stroke(0,0,0)
    strokeWeight(5)
    if(tipo==1):
        for i in range(len(pista) - 1):
            line(pista[i][0], pista[i][1], pista[i+1][0], pista[i+1][1])
        noStroke()
    if(tipo==2):
        for i in range(len(pista)):
            noFill()
            curve(pista[i%len(pista)][0], pista[i%len(pista)][1], pista[(i+1)%len(pista)][0], pista[(i+1)%len(pista)][1],pista[(i+2)%len(pista)][0],pista[(i+2)%len(pista)][1],pista[(i+3)%len(pista)][0],pista[(i+3)%len(pista)][1])
        noStroke()