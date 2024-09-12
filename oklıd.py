import math

points = [(5, 10), (10, 15), (15, 20), (20, 25)]

def euclideanDistance(Nokta1, Nokta2):
    x1, y1 = Nokta1
    x2, y2 = Nokta2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

mesafe = [] 

for i in range(len(points)):
    
    for j in range(i+1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        mesafe.append(dist)

# Minimum mesafenin bulunması

MinUzaklik = min(mesafe)

print("Minimum mesafe:", MinUzaklik)

print("Mesafeler: ", mesafe)