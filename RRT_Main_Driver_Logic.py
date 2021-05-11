import pygame
from RRT_Root_Logic import RRTGraph
from RRT_Root_Logic  import RRTMap


def main():




    dimensions = (600, 1000) #Enter the Dimensions of the Map
    start = (50,50)          #Enter the Start Point Coordinates
    goal = (510, 510)        #Enter the Goal Point Coordinates
    obsdim = 50              #Enter the Obstacle Dimensions
    obsnum = 3               #input for entering the required No of Obstacles on the map

    iteration = 0


    pygame.init()

    map = RRTMap(start, goal, dimensions, obsdim, obsnum)       #Create Class Object : Class:

    graph = RRTGraph(start, goal, dimensions, obsdim, obsnum)   #Create graph Object

    obstacles = graph.makeobs()                                 #create Obstacles by call makeobs() function

    map.drawMap(obstacles)                                      #Draw obstacles on the developed map

    #Color_line = (0, 0, 128)

    while True :

        x,y = graph.sample_envir()
        n = graph.number_of_nodes()                             #Extract the no of nodes on the map

        print(n)                                                #Print the node Numbers for Reference

        graph.add_node(n, x, y)                                 #Add Nodes on the Map
        graph.add_edge(n-1,n)                                   #Add Edges on the Map

        x1, y1 = graph.x[n], graph.y[n]                         #Extract the x1y1 coordiantes
        x2, y2 = graph.x[n-1], graph.y[n-1]                     #Extract the x2y2 coordinates


        if (graph.isFree()):

            pygame.draw.circle(map.map, map.Red,(graph.x[n],graph.y[n]), map.nodeRadius, map.nodeThickness)

            if not graph.crossobstacle(x1, x2, y1, y2):

                pygame.draw.line(map.map, map.blue, (x1,y1), (x2,y2), map.edgeThickness)  #draw the line to connt the points

        pygame.display.update()




        map.drawMap(obstacles)
        pygame.display.update()                                         #update the display Function
        pygame.event.clear()                                            #clear the event
        pygame.event.wait(0)                                            #wait for the event






if __name__ ==  '__main__':
    main()



