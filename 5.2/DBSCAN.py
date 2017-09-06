def regionQuery(self,P,eps):
    result = []
    for d in self.dataSet:
        if (((d[0]-P[0])**2 + (d[1] - P[1])**2)**0.5)<=eps:
            result.append(d)
    return result
def expandCluster(self,point,NeighbourPoints,C,eps,MinPts):
        
    C.addPoint(point)
        
    for p in NeighbourPoints:
        if p not in self.visited:
            self.visited.append(p)
            np = self.regionQuery(p,eps)
            if len(np) >= MinPts:
                for n in np:
                    if n not in NeighbourPoints:
                        NeighbourPoints.append(n)
                    
        for c in self.Clusters:
            if not c.has(p):
                if not C.has(p):
                    C.addPoint(p)
                        
        if len(self.Clusters) == 0:
            if not C.has(p):
                C.addPoint(p)
                        
    self.Clusters.append(C)


