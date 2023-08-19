from dataclasses import dataclass
import numpy as np
import numpy.typing as npt

@dataclass
class Body():
    name: str
    type: str
    position: np.array
    velocity: np.array
    mass: float

    def __init__(self, name, type, position, velocity, mass):
        self.name = name
        self.type = type
        self.position = position
        self.velocity = velocity
        self.mass = mass


class Bodies():
    def __init__(self):
        self.bodies = []
        # self.build_home()

    def add_body(self, body_name, body_type, position, velocity, mass):
        body = Body(body_name, body_type, position, velocity, mass)
        self.bodies.append(body)

    def build_home(self):
        # self.add_body("sun", "star", np.array([0,0], np.float64), np.array([0,0.00005365069249], np.float64), 333000)
        self.add_body("mercury", "planet", np.array([0.387,0], np.float64), np.array([0,-0.159], np.float64), 0.055)
        self.add_body("venus", "planet", np.array([0.723,0], np.float64), np.array([0,-0.118], np.float64), 0.815)
        self.add_body("earth", "planet", np.array([1,0], np.float64), np.array([0,-0.1], np.float64), 1)
        self.add_body("mars", "planet", np.array([1.52,0], np.float64), np.array([0,-0.0808], np.float64), 0.107)
        self.add_body("jupiter", "planet", np.array([5.20,0], np.float64), np.array([0,-0.0439], np.float64), 317)
        self.add_body("saturn", "planet", np.array([9.58,0], np.float64), np.array([0,-0.0325], np.float64), 95.2)
        self.add_body("uranus", "planet", np.array([19.2,0], np.float64), np.array([0,-0.0228], np.float64), 14.5)
        self.add_body("neptune", "planet", np.array([30.1,0], np.float64), np.array([0,-0.0182], np.float64), 17.1)

        return



    

