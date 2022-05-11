from matplotlib.colors import PowerNorm
import argumentParser as ag 
import commerce

import numpy as np
import random

def calculateFirstPath(points : list) -> list:
    path : list = []

    for i in range(len(points)):
        path.append(i)

    random.shuffle(path)
    path.append(path[0])
    return path

# swap two points in a list : points[i] become points[j] and points[j] become points[j]
# PRECOND : i,j should be in ]0,len(points)-2[

def permuteTwoEdges(path, i1 : int, i2 : int):
    if (i1 > 0 and i1 < len(path) - 2 and i2 > 0 and i1 < len(path) - 2):
        pathList = path.tolist()
        i1,i2 = min(i1,i2),max(i1,i2)

        edge1 : list = [pathList[i1],pathList[i1+1]]
        edge2 : list = [pathList[i2],pathList[i2+1]]

        copy : list = pathList[:i1+1]
        copy.append(pathList[i2])

        sub = pathList[i1+2:i2]
        sub.reverse()

        for i in sub:
            copy.append(i)

        copy.append(pathList[i1+1])
        copy.append(pathList[i2+1])

        for i in pathList[i2+2:]:
            copy.append(i)

        return copy
    else:
        print("indexes are not between 0 and len(points)-2")

def permuteAlgo(points : list, path : list, LIMIT : int = 10**6) -> tuple :
    np_points = np.array(points)
    np_path = np.array(path)

    #initial length
    pathLen : int = commerce.distance_chemin(np_points,np_path)

    cmp : int = 0
    tmp_cmp : int = 0
    
    while(1):
        for i in range(1,len(np_path)-2):
            for j in range(1,len(np_path)-2):
                if(tmp_cmp <= LIMIT):
                    if(j >= i+2 or j <= i-2 ):
                        newPath = permuteTwoEdges(np_path,i,j)
                        newPathLength: int = commerce.distance_chemin(np_points,newPath)
                        if(newPathLength < pathLen):
                            tmp_cmp = tmp_cmp + 1
                            pathLen = newPathLength
                            np_path = np.array(newPath)
                else:
                    return np_path.tolist(), pathLen, cmp
        if(tmp_cmp == cmp):
            return np_path.tolist(), pathLen, cmp
        else:
            cmp = tmp_cmp


    return np_path.tolist(), pathLen, cmp


points : list = [[1,2],[3,1],[6,5],[5,4],[5,8],[6,4],[5,2],[3,9]]  
print("points :",points)

path = calculateFirstPath(points)
print("first path :",path)

print("final result :")
res = permuteAlgo
print("path :",permuteAlgo(points,path)[0])
print("length of the path :",permuteAlgo(points,path)[1])
print("number of permutations computed :",permuteAlgo(points,path)[2])
