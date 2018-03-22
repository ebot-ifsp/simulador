
class robo(object):
    """
    Guarda as propriedades, regras e estados do robo    
    """
    def __init__(self, x, y, v=5, theta = -PI/2,if1=(-10, 10), if2=(0.001, 0.0010), if3=(10, 10)):
        self.x = x
        self.y = y
        self.v = v
        self.theta = theta
        self.dt = 0.5
        self.if1 = if1
        self.if2 = if2
        self.if3 = if3
        self.comprimento = 38
        self.largura = 20
        self.estado = 1
        self.vmax = 5
        self.dtheta = 3.141519/18.0
        self.if1_atual, self.if2_atual, self.if3_atual = [0, 0], [0, 0], [0, 0]
        self.if1_theta = tan(if1[1]/if1[0])
        self.if1_mod = sqrt(if1[0]**2 + if1[1]**2)
        self.if2_theta = tan(if2[1]/if2[0])
        self.if2_mod = sqrt(if2[0]**2 + if2[1]**2)
        self.if3_theta = tan(if3[1]/if3[0])
        self.if3_mod = sqrt(if3[0]**2 + if3[1]**2)
        self.carroP1, self.carroP2, self.carroP3 = [0, 0], [0, 0], [0, 0]

    def desenha(self):
        fill(0, 0, 255)
        s1_rgb, s2_rgb, s3_rgb = self.le_sensorIF()
        self.atualizaPontoCarro()
        self.atualizaPosSensores()
        triangle(self.carroP1[0], self.carroP1[1],
                 self.carroP2[0], self.carroP2[1],
                 self.carroP3[0], self.carroP3[1])
        s1 = s1_rgb == (0, 0, 0) 
        s2 = s2_rgb == (0, 0, 0) 
        s3 = s3_rgb == (0, 0, 0)
        if s1:
            fill(255, 0, 0)
        else:
            fill(255, 255, 0)
        ellipse(self.if1_atual[0], self.if1_atual[1], 3, 3)
        if s2:
            fill(255, 0, 0)
        else:
            fill(255, 255, 0)
        ellipse(self.if2_atual[0], self.if2_atual[1], 3, 3)
        if s3:
            fill(255, 0, 0)
        else:
            fill(255, 255, 0)
        ellipse(self.if3_atual[0], self.if3_atual[1], 3, 3)

    def controle(self):
        s1_rgb, s2_rgb, s3_rgb = self.le_sensorIF()
        s1 = s1_rgb == (0, 0, 0) 
        s2 = s2_rgb == (0, 0, 0) 
        s3 = s3_rgb == (0, 0, 0)
        
        # controle simples para teste sem a maquina de estado
        if s1:
            self.theta = self.theta - self.dtheta
        elif s3:
            self.theta = self.theta + self.dtheta
        self.anda()
        
        # Maquina de estado do marcio
        # if self.estado == 1:
        #     if s1 == 0 and s3 == 0:
        #         self.v = self.v*1.1
        #         if self.v > 5:
        #             self.v = 5
        #     elif s1 == 1:
        #         self.estado = 2
        #     else:
        #         self.estado = 3
        #     self.anda()
        # if self.estado == 2:
        #     if s2 == 0 or s1 == 1:
        #         self.theta = self.theta - self.dtheta
        #     else:
        #         self.estado = 1
        # elif self.estado == 3:
        #     if s2 == 0 or s3 == 1:
        #         self.theta = self.theta + self.dtheta
        #     else:
        #         self.estado = 1
        

    def anda(self):
        vx = self.v*cos(self.theta)
        vy = self.v*sin(self.theta)
        self.x = self.x + vx*self.dt
        self.y = self.y + vy*self.dt
        return self.x, self.y

    def atualizaPontoCarro(self):
        self.carroP1[0] = self.largura*cos(float(self.theta) + PI/2.0) + self.x
        self.carroP1[1] = self.largura*sin(float(self.theta) + PI/2.0) + self.y
        self.carroP2[0] = self.largura*cos(float(self.theta - PI/2.0)) + self.x
        self.carroP2[1] = self.largura*sin(float(self.theta - PI/2.0)) + self.y
        self.carroP3[0] = self.comprimento*cos(self.theta) + self.x
        self.carroP3[1] = self.comprimento*sin(self.theta) + self.y

    def atualizaPosSensores(self):
        self.if1_atual[0] = self.x + self.if1_mod*cos(self.theta + self.if1_theta)
        self.if1_atual[1] = self.y + self.if1_mod*sin(self.theta + self.if1_theta)
        self.if2_atual[0] = self.x + self.if2_mod*cos(self.theta + self.if2_theta)
        self.if2_atual[1] = self.y + self.if2_mod*sin(self.theta + self.if2_theta)
        self.if3_atual[0] = self.x + self.if3_mod*cos(self.theta + self.if3_theta)
        self.if3_atual[1] = self.y + self.if3_mod*sin(self.theta + self.if3_theta)
        
        # self.if1_atual[0] = self.if1[0]*cos(self.theta) - self.if1[1]*sin(self.theta) + self.x
        # self.if1_atual[1] = self.if1[0]*sin(self.theta) + self.if1[1]*cos(self.theta) + self.y
        # self.if2_atual[0] = self.if2[0]*cos(self.theta) - self.if2[1]*sin(self.theta) + self.x
        # self.if2_atual[1] = self.if2[0]*sin(self.theta) + self.if2[1]*cos(self.theta) + self.y
        # self.if3_atual[0] = self.if3[0]*cos(self.theta) - self.if3[1]*sin(self.theta) + self.x
        # self.if3_atual[1] = self.if3[0]*sin(self.theta) + self.if3[1]*cos(self.theta) + self.y

    def le_sensorIF(self):
        self.atualizaPosSensores()
        cor_if1 = get(int(self.if1_atual[0]), int(self.if1_atual[1]))
        cor_if2 = get(int(self.if2_atual[0]), int(self.if2_atual[1]))
        cor_if3 = get(int(self.if3_atual[0]), int(self.if3_atual[1]))
        return (red(cor_if1), green(cor_if1), blue(cor_if1)), \
               (red(cor_if2), green(cor_if2), blue(cor_if2)), \
               (red(cor_if3), green(cor_if3), blue(cor_if3))
    
    
    
    
    
    
