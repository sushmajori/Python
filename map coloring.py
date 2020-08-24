#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that 
no two adjacent vertices of the graph are colored with same color. Here coloring of a graph means assignment of colors to all vertices.

1)A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency matrix representation of the graph.
A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.
2) An integer m which is maximum number of colors that can be used.

Output:
An array color[V] that should have numbers from 1 to m. color[i] should represent the color assigned to the ith vertex. 
The code should also return false if the graph cannot be colored with m colors.


Backtracking Algorithm
The idea is to assign colors one by one to different vertices, starting from the vertex 0. Before assigning a color, 
we check for safety by considering already assigned colors to the adjacent vertices. If we find a color assignment which 
is safe, we mark the color assignment as part of solution. If we do not a find color due to clashes then we backtrack and return false.


'''
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                              for row in range(vertices)] 
  
    # A utility function to check if the current color assignment 
    # is safe for vertex v 
    def isSafe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    # A recursive utility function to solve m 
    # coloring  problem 
    def graphColourUtil(self, m, colour, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m+1): 
            if self.isSafe(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v+1) == True: 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColourUtil(m, colour, 0) == False: 
            return False
  
        # Print the solution 
        print "Solution exist and Following are the assigned colours:"
        for c in colour: 
            print c, 
        return True
  
# Driver Code 
g  = Graph(4) 
g.graph = [[0,1,1,1], [1,0,1,1], [1,1,0,1], [1,0,1,0]] 
m=3
g.graphColouring(m) 
  


# In[ ]:




