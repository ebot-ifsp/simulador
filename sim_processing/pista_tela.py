def desenha_pista(pista):
    background(30, 125, 30)
    # desenha a pista
    stroke(0,0,0)
    strokeWeight(5)
    for i in range(len(pista) - 1):
        line(pista[i][0], pista[i][1], pista[i+1][0], pista[i+1][1])
    noStroke()