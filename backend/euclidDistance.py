import math
def distances_between(x_y_z_coordinates):
    distances=[]
    iss=x_y_z_coordinates["iss"]
    for debri in x_y_z_coordinates["debris"]:
        euclid_distance=math.sqrt((iss["x"]-debri["x"])**2+(iss["y"]-debri["y"])**2+(iss["z"]-debri["z"])**2)
        distances.append({"catnr":debri["catnr"],"distance":euclid_distance})
    return distances    