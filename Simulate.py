from Timer import timer
import numpy as np

class Simulate():

    def __init__(self, G, time_step):
        self.G = G
        self.time_step = time_step

    def simulate(self, bodies_dict):

        self.bodies_dict = bodies_dict

        self.accelerate()
        self.displace()
        # self.boundary()
        
        return self.bodies_dict
    
    def set_time_step(self, time_step):
        self.time_step = time_step

    def set_gravity(self, G):
        self.G = G


    @timer
    def accelerate(self):

        body_names = list(self.bodies_dict.keys())
        
        for i in range(0, len(body_names), 1):
            for j in range(i+1, len(body_names), 1):
                t1 = self.bodies_dict[body_names[i]]["type"]
                t2 = self.bodies_dict[body_names[j]]["type"]
                if not ((t1 == "rock" or t1 == "belt") and (t2 == "rock" or t2 == "belt")):
                    delta_v1, delta_v2 = self.calc_dv(self.bodies_dict[body_names[j]]["position"], self.bodies_dict[body_names[i]]["position"], self.bodies_dict[body_names[i]]["mass"], self.bodies_dict[body_names[j]]["mass"])
                    self.bodies_dict[body_names[i]]["velocity"] += (delta_v1*self.time_step)
                    self.bodies_dict[body_names[j]]["velocity"] += (delta_v2*self.time_step)  

    def calc_dv(self, p1, p2, m1, m2):

        force_direction = p1-p2
        r = np.linalg.norm(force_direction)
        rsqd = np.square(r)

        # mass_prod = m1 * m2
        # force = (G*mass_prod)/rsqd

        # acceleration1 = force/m1
        acceleration1 = (self.G*m2)/rsqd
        delta_v1 = acceleration1 * (force_direction/r)

        # acceleration2 = force/m2
        acceleration2 = (self.G*m1)/rsqd
        delta_v2 = acceleration2 * (-force_direction/r)


        return delta_v1, delta_v2

    @timer
    def displace(self):

        for body_name, body_props in self.bodies_dict.items():
            # if body_name != "sun":
            self.bodies_dict[body_name]["position"] = body_props["position"] + (body_props["velocity"]*self.time_step)

    def collisions(self, prox):

        keys = list(self.bodies_dict.keys())

        for i in range(len(self.bodies_dict)):
            marked_self.bodies_dict = []
            for j in range(i+1, len(self.bodies_dict), 1):
                r = np.linalg.norm(self.bodies_dict[keys[i]]["position"]-self.bodies_dict[keys[j]]["position"])
                if r < prox:
                    marked_self.bodies_dict.append(keys[j])    

            for body_name in marked_self.bodies_dict:
                self.bodies_dict[keys[i]]["mass"] += self.bodies_dict[body_name]["mass"]

    @timer
    def boundary(self, limit):

        marked = []
        for body_name, body_props in self.bodies_dict.items():
            if np.linalg.norm(body_props["position"]) > limit:
                marked.append(body_name)

        for body_name in marked:
            self.bodies_dict.pop(body_name, None)