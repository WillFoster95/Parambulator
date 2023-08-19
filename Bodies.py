import numpy as np
import random, string

class Bodies():

    def __init__(self):
        self.bodies = {}

    def get_bodies(self):
        return self.bodies
    
    def set_bodies(self, bodies_dict):
        self.bodies = bodies_dict
        return

    def add_body(self, body_name, body_type, position, velocity, mass):

        self.bodies[body_name] = {}
        self.bodies[body_name]["mass"] = mass
        self.bodies[body_name]["position"] = position
        self.bodies[body_name]["velocity"] = velocity
        self.bodies[body_name]["type"] = body_type

        return

    def add_bodies(self, num):

        for i in range(num):
            name = self.randomword(5)
            self.bodies[name] = {}
            self.bodies[name]["mass"] = 0.001
            pos = (np.random.rand(2)-0.5)*view_size
            self.bodies[name]["position"] = pos
            vel = (np.random.rand(2)-0.5)*0.1
            self.bodies[name]["velocity"] = vel
            self.bodies[name]["type"] = "rock"

        return

    def match_orbit(self, num):

        for i in range(num):
            name = self.randomword(5)
            self.bodies[name] = {}
            self.bodies[name]["mass"] = 0.001
            pos = (np.random.rand(2)-0.5)*view_size*2
            pos = pos/np.linalg.norm(pos) * 5.2
            self.bodies[name]["position"] = pos
            self.bodies[name]["velocity"] = np.array([-pos[1], pos[0]])/np.linalg.norm(pos) * -0.0439
            self.bodies[name]["type"] = "rock"

        return

    def belt(self, num, alt, G):
        
        mass = 0.001
        for i in range(num):
            name = self.randomword(5)
            self.bodies[name] = {}
            self.bodies[name]["mass"] = mass
            pos = (np.random.rand(2)-0.5)
            pos = pos/np.linalg.norm(pos) * alt
            self.bodies[name]["position"] = pos
            idk = np.sqrt(G*(333000+mass)*((2/alt)-(1/alt)))
            vel = np.array([-pos[1], pos[0]])/np.linalg.norm(pos) * idk
            self.bodies[name]["velocity"] = vel
            self.bodies[name]["type"] = "belt"  

        return

    def build_home(self):
        self.add_body("sun", "star", np.array([0,0], np.float64), np.array([0,0.00005365069249], np.float64), 333000)
        self.add_body("mercury", "planet", np.array([0.387,0], np.float64), np.array([0,-0.159], np.float64), 0.055)
        self.add_body("venus", "planet", np.array([0.723,0], np.float64), np.array([0,-0.118], np.float64), 0.815)
        self.add_body("earth", "planet", np.array([1,0], np.float64), np.array([0,-0.1], np.float64), 1)
        self.add_body("mars", "planet", np.array([1.52,0], np.float64), np.array([0,-0.0808], np.float64), 0.107)
        self.add_body("jupiter", "planet", np.array([5.20,0], np.float64), np.array([0,-0.0439], np.float64), 317)
        self.add_body("saturn", "planet", np.array([9.58,0], np.float64), np.array([0,-0.0325], np.float64), 95.2)
        self.add_body("uranus", "planet", np.array([19.2,0], np.float64), np.array([0,-0.0228], np.float64), 14.5)
        self.add_body("neptune", "planet", np.array([30.1,0], np.float64), np.array([0,-0.0182], np.float64), 17.1)

        return


    def randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
