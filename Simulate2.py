from Timer import timer
import numpy as np


def simulate(bodies, G, time_step):
    accelerate(bodies, G, time_step)
    displace(bodies, time_step)
    # boundary()
    
    # return bodies

def accelerate(bodies, G, time_step):
    
    for i in range(0, len(bodies), 1):
        for j in range(i+1, len(bodies), 1):
            t1 = bodies[i].type
            t2 = bodies[j].type
            if not ((t1 == "rock" or t1 == "belt") and (t2 == "rock" or t2 == "belt")):
                delta_v1, delta_v2 = calc_dv(bodies[i].position, bodies[j].position, bodies[i].mass, bodies[j].mass, G)
                bodies[i].velocity += (delta_v1*time_step)
                bodies[j].velocity += (delta_v2*time_step)  

def calc_dv(p1, p2, m1, m2, G):

    force_direction = p2-p1
    r = np.linalg.norm(force_direction)
    rsqd = np.square(r)

    acceleration1 = (G*m2)/rsqd
    delta_v1 = acceleration1 * (force_direction/r)

    acceleration2 = (G*m1)/rsqd
    delta_v2 = acceleration2 * (-force_direction/r)

    return delta_v1, delta_v2

def displace(bodies, time_step):
    for body in bodies:
        body.position += body.velocity*time_step

# def collisions(self, prox):

#     keys = list(self.bodies_dict.keys())

#     for i in range(len(self.bodies_dict)):
#         marked_self.bodies_dict = []
#         for j in range(i+1, len(self.bodies_dict), 1):
#             r = np.linalg.norm(self.bodies_dict[keys[i]]["position"]-self.bodies_dict[keys[j]]["position"])
#             if r < prox:
#                 marked_self.bodies_dict.append(keys[j])    

#         for body_name in marked_self.bodies_dict:
#             self.bodies_dict[keys[i]]["mass"] += self.bodies_dict[body_name]["mass"]

# @timer
# def boundary(self, limit):

#     marked = []
#     for body_name, body_props in self.bodies_dict.items():
#         if np.linalg.norm(body_props["position"]) > limit:
#             marked.append(body_name)

#     for body_name in marked:
#         self.bodies_dict.pop(body_name, None)