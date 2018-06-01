from helpers import Map, load_map, show_map
import math
import heapq as h
def shortest_path(graph,start,goal):
    closedSet=set([])
    openSet=set([start])
    cameFrom={}
    availableroads=list(graph.intersections.keys())
    gScores={road : float("inf") for road in availableroads}
    gScores[start]=0
    fScores={road: float("inf") for road in availableroads}
    fScores[start]=heuristics_path(graph,start,goal)
    frontier=[(fScores[start], start)]
    while openSet:
        current=h.heappop(frontier)
        if current[1]==goal:
            print("shortest path called")
            reversepath=reconstruction_paths(cameFrom, current[1])
            reversepath.reverse()
            print(reversepath)
            return reversepath
        if current[1] in openSet:    
            openSet.remove(current[1])
            closedSet.add(current[1])
        for i in graph.roads[current[1]]:
            if i in closedSet:
                continue
            if i not in openSet:
                openSet.add(i)
            tentative_gScores=gScores[current[1]]+heuristics_path(graph, current[1], i)
            if tentative_gScores>=gScores[i]:
                continue
            cameFrom[i]=current[1]
            gScores[i]=tentative_gScores
            fScores[i]=(gScores[i] + heuristics_path(graph, i, goal))
            h.heappush(frontier, (fScores[i], i))
    return ("Function has been failed")
def heuristics_path(graph, sn, en):
    abs_diff_x_square=math.pow((graph.intersections[sn][0]-graph.intersections[en][0]),2)
    abs_diff_y_square=math.pow((graph.intersections[sn][1]-graph.intersections[en][1]),2) 
    distance_bet_nodes=math.sqrt(abs_diff_x_square+abs_diff_y_square)
    return distance_bet_nodes
def reconstruction_paths(cameFrom, current):
    path=[]
    total_path=[current]
    while current in cameFrom:
        current=cameFrom[current]
        total_path.append(current)     
    return total_path