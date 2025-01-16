import pygame

class Maps():
    def __init__(self):
        self.colors = [(0,0,0),(255, 0, 0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,255,255)] # pre set colors, 0 is first, 7 is last
        self.sizes = [[(20,100),(20,200),(20,300),(20,500)],[(100,20),(200,20),(300,20),(500,20)]] # pre set sizes, first set is vertical, second set is vertical
        self.wall_image = pygame.image.load("x.jpg")
    def map_1(self, surface):
        barriers = [
            pygame.Rect(160, 500, *self.sizes[0][1]),  # Bottom start
            pygame.Rect(160, 0, *self.sizes[0][2]),  # Top start
            pygame.Rect(160, 300, *self.sizes[1][1]),  # Connector 1
            pygame.Rect(360, 300, *self.sizes[0][1]),  # Connector 2
            pygame.Rect(260, 400, *self.sizes[1][0]),  # Extruding connector 1
            pygame.Rect(360, 500, *self.sizes[1][1]),  # Connector 3
            pygame.Rect(450, 650, *self.sizes[0][1]),  # Extruding connector 2
            pygame.Rect(540, 300, *self.sizes[0][1]),  # Connector 4
            pygame.Rect(300, 180, *self.sizes[1][3]),  # Extruding connector 3
        ]

        # Draw barriers
        for barrier in barriers:
            pygame.draw.rect(surface, self.colors[1], barrier)

        return barriers  # Return the list of barriers
    
    def map_2(self, surface):
        barriers = [
            pygame.Rect(400,500,*self.sizes[1][2]), # start (right)
            pygame.Rect(0,500,*self.sizes[1][2]), # start (left)
            pygame.Rect(280,300,*self.sizes[0][1]), # connector 1 (left)
            pygame.Rect(460,300,*self.sizes[0][1]), # connector 1(right)
            pygame.Rect(460,100,*self.sizes[0][1]), # connector 2 (right)
            pygame.Rect(180,300,*self.sizes[1][1]), # connector 2 (left)
            pygame.Rect(200,190,*self.sizes[1][2]), # connector 3 (right)
            pygame.Rect(100,190,*self.sizes[1][1]), # connector 4 (right)
            pygame.Rect(100,300,*self.sizes[0][1]), # connector 5 (right)
            pygame.Rect(260,100,*self.sizes[1][0]), # connector 6 (right)
            pygame.Rect(340,0,*self.sizes[0][0]), # connector 7 (right)
            pygame.Rect(260,0,*self.sizes[0][0]), # connector 8 (right)
            pygame.Rect(150,100,*self.sizes[0][0]), # connector 9 (right)
            pygame.Rect(480,390,*self.sizes[1][0]), # extruding connector 4
            pygame.Rect(600,290,*self.sizes[1][0]), # extruding connector 3
            pygame.Rect(480,190,*self.sizes[1][0]), # extruding connector 2
            pygame.Rect(600,90,*self.sizes[1][0]), # extruding connector 1
        ]
    
        # Draw barriers
        for barrier in barriers:
            pygame.draw.rect(surface, self.colors[2], barrier)

        return barriers

    def map_3(self,surface):
        barriers = [
            pygame.Rect(500,565,*self.sizes[0][2]), # bottom start
            pygame.Rect(500,0,*self.sizes[0][3]), # top start
            pygame.Rect(300,565,*self.sizes[1][1]), # connector 1
            pygame.Rect(300,480,*self.sizes[1][1]), # connector 2
            pygame.Rect(300,570,*self.sizes[0][1]), # connector 3
            pygame.Rect(250,480,*self.sizes[1][0]), # connector 4.1
            pygame.Rect(225,480,*self.sizes[1][0]), # connector 4.2
            pygame.Rect(210,480,*self.sizes[0][0]), # connector 5.1
            pygame.Rect(210,530,*self.sizes[0][0]), # connector 5.2
            pygame.Rect(55,610,*self.sizes[1][0]), # connector 6
            pygame.Rect(120,330,*self.sizes[0][2]), # connector 7
            pygame.Rect(140,330,*self.sizes[1][2]), # connector 8
            pygame.Rect(-60,230,*self.sizes[1][3]), # connector 9
            pygame.Rect(60,120,*self.sizes[1][2]), # connector 10
            pygame.Rect(360,120,150,20), # connector 11
            pygame.Rect(260,350,20,70), # extruding connector 1.1
            pygame.Rect(340,410,20,70), # extruding connector 1.2
            pygame.Rect(420,350,20,70), # extruding connector 1.3
            pygame.Rect(0,330,50,20), # extruding connector 2.1
            pygame.Rect(70,420,50,20), # extruding connector 2.2
            pygame.Rect(0,500,50,20), # extruding connector 2.3
        ]

        # Draw barriers
        for barrier in barriers:
            pygame.draw.rect(surface, self.colors[3], barrier)

        return barriers