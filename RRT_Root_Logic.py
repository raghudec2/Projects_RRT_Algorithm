import random
import math
import pygame

class RRTMap:


     def __init__(self,start,goal,MapParameters, obsdim,obsnum) : #Start -- Startpoint    Goal -- Goalpoint or Destination Point
                                                                  #MapParameters -- Parameters like width and height.
        self.start = start
        self.goal = goal
        self.MapParameters = MapParameters
        self.Maph,self.Mapw =self.MapParameters                 #Maph -- Height Parameter #Mapw -- Width Parameter

        #Window Settings
        self.MapWindowName = 'Rapidly Exploring Random Tree - Planning'   #Name the Mapping Window.

        pygame.display.set_caption(self.MapWindowName)

        self.map=pygame.display.set_mode((self.Mapw,self.Maph))
        self.map.fill((255,255,255))                              #color code for Filling the Canvas as White color
        self.nodeRadius = 2                                       #intializing node dimension - Radius = 2
        self.nodeThickness = 1                                    #intializing node thickness = 1
        self.edgeThickness = 2                                    #intializing edge thickness = 2


        self.obstacles=[]                                         #obstacles list
        self.obsdim=obsdim                                        #obstacle dimension
        self.obsNumber =obsnum                                    #obstacle number


         #colorsschemes
        self.grey = (70,70,70)
        self.blue = (0, 0, 255)
        self.Green = (0,255,0)
        self.Red = (255, 0, 0)
        self.white = (255,255,255)

        #Defining funtions for drawing the start and goal nodes :

     def drawMap(self, obstacles):

        pygame.draw.circle(self.map, self.Green, self.start, self.nodeRadius+5, 0)
        pygame.draw.circle(self.map, self.Green, self.goal, self.nodeRadius+20, 1)
        self.drawObs(obstacles)

        #Defining functions for drawing obstacles: obstacle shape chosen as rectangle

     def drawObs(self,obstacles):
        obstaclesList = obstacles.copy()
        while (len(obstaclesList)>0):
            obstacle = obstaclesList.pop(0)
            pygame.draw.rect(self.map, self.grey,obstacle)



class RRTGraph:


    def __init__(self, start, goal, MapParameters, obsdim, obsnum) :

        (x,y)= start
        self.start = start
        self.goal = goal
        self.MapParameters = MapParameters
        self.Maph, self.Mapw = self.MapParameters
        self.x = []
        self.y = []
        self.parent = []
        #intialize the tree :

        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)

        #theobstacles
        self.obstacles  = []
        self.obsDim = obsdim
        self.obsNum = obsnum

        #path
        self.goalstate = None
        self.path = []

    #Defining functions for randomn Rectangles:
    def makeRandomRect (self):
        uppercornerx = int(random.uniform(0,self.Mapw-self.obsDim))
        uppercornery = int(random.uniform(0,self.Maph-self.obsDim))
        return (uppercornerx, uppercornery)

    #Making Obs
    def makeobs(self):
        obs = []

        for i in range(0,self.obsNum):
            rectang = None
            startgoalcol =True
            while startgoalcol:
                upper = self.makeRandomRect()
                rectang = pygame.Rect(upper,(self.obsDim, self.obsDim))
                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startgoalcol = True

                else:
                    startgoalcol = False

            obs.append(rectang)
        self.obstacles = obs.copy()
        return obs


    #Defining Methods for adding new node :
    def add_node(self, n, x,y):
        self.x.insert(n,x)
        self.y.append(y)

    #Defining Fucntions for removing the node
    def remove_node(self,n):

        self.x.pop(n)
        self.y.pop(n)
    #Defining functions for adding edge:

    def add_edge(self,parent,child):

        self.parent.insert(child, parent)

    #Defining functions for removing Edges:

    def remove_Edge(self):
        self.parent.insert(child, parent)

    #Defining the functions for calculating the node value n:
    def number_of_nodes(self):

        return len(self.x)


    #Defining functons for distance calculation :
    def distance (self, n1, n2):
        (x1, y1) = (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        px = (float(x1) - float (x2))**2
        py = (float(y1) - float(y2)) ** 2
        return (px + py)**(0.5)


    #Defining Sample Environment
    def sample_envir(self):

        x = int(random.uniform(0,self.Mapw))
        y = int(random.uniform(0,self.Maph))
        return x, y


    #Defining Functions for checking / Collision Detection
    def isFree (self):
        n = self.number_of_nodes() - 1
        (x, y) = (self.x[n], self.y[n])
        obs = self.obstacles.copy()
        while len(obs)>0:
            rectang = obs.pop(0)
            if rectang.collidepoint(x,y):
                self.remove_node(n)
                return  False
        return True

    #interpoloation Method : to check collision point
    def crossobstacle (self, x1,x2,y1,y2):
        obs= self.obstacles.copy()
        while len(obs)>0 :
            rectang = obs.pop(0)
            for i in range (0,101):
                u = i/100
                x = x1*u + x2*(1-u)
                y = y1*u + y2*(1-u)
                if rectang.collidepoint(x,y):
                    return True
        return False

    #Method for Connecting two points:
    def connect (self, n1,n2):
        (x1, y1)= (self.x[n1], self.y[n1])
        (x2, y2) = (self.x[n2], self.y[n2])
        if self.crossObstacle(x1,x2,y1,y2):
            self.remove_node(n2)
            return False

        else:

            self.add_edge(n1, n2)
            return True


    #Method for Finding the shortest distance between start to goal point:







