import matplotlib.pyplot as plt
from Timer import timer
import numpy as np

class Graphics():

    def __init__(self, view_size):

        self.x = 5

        self.fig = plt.figure(figsize=(9, 9))
        self.ax = self.fig.add_subplot(111)

        self.xmin = -view_size
        self.xmax = view_size
        self.ymin = -view_size
        self.ymax = view_size

        plt.grid(visible=True)

        self.points = self.ax.scatter([1], [1], animated=True)
        plt.show(block=False)
        plt.pause(0.1)
        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.ax.draw_artist(self.points)
        self.fig.canvas.blit(self.fig.bbox)

        self.axislim()

    def axislim(self):
        plt.xlim(self.xmin, self.xmax)
        plt.ylim(self.ymin, self.ymax)
        plt.show(block=False)
        plt.pause(0.1)
        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.ax.draw_artist(self.points)
        self.fig.canvas.blit(self.fig.bbox)


    def shift_left(self):
        self.xmin -= 1
        self.xmax -= 1
        self.axislim()

    def shift_up(self):
        self.ymin += 1
        self.ymax += 1
        self.axislim()

    def shift_right(self):
        self.xmin += 1
        self.xmax += 1
        self.axislim()

    def shift_down(self):
        self.ymin -= 1
        self.ymax -= 1
        self.axislim()

    def zoom_in(self):
        self.xmin += 1
        self.xmax -= 1
        self.ymin += 1
        self.ymax -= 1 

        self.axislim()

    def zoom_out(self):
        self.xmin -= 1
        self.xmax += 1
        self.ymin -= 1
        self.ymax += 1 

        self.axislim()

    def update_graphic(self, bodies_dict):

        coords, sizes, colours = self.make_coords(bodies_dict)

        self.fig.canvas.restore_region(self.bg)

        self.points.set_offsets(coords)
        self.points.set_sizes(sizes)
        self.points.set_color(colours)

        self.ax.draw_artist(self.points)
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()

        return
    
    def make_coords(self, bodies):

        coords = []
        sizes = []
        colours = []
        for body_name, body_props in bodies.items():
            coords.append(body_props["position"])
            sizes.append(np.log(body_props["mass"]*10000))
            if body_props["type"] == "star":
                colours.append([1,0,0])
            elif body_props["type"] == "planet":
                colours.append([0,0,1])
            elif body_props["type"] == "rock":
                colours.append([0.2,0.2,0.2])
            elif body_props["type"] == "belt":
                colours.append([0,1,0.2])

        return np.asarray(coords), np.asarray(sizes), np.asarray(colours)

