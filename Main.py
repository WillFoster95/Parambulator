import numpy as np
import time
# import UI
# import Graphics
import Graphics2
# import Bodies
import Bodies2
# import Simulate
import Simulate2

view_size = 5

G = 0.00000003
time_step = 0.1

if __name__ == "__main__":

    # ui = UI.UI() 
    # bodies = Bodies.Bodies()
    bodies = Bodies2.Bodies()
    bodies.add_body("sun", "star", np.array([0,0], np.float64), np.array([0,0.00005365069249], np.float64), 333000)
    # bodies.build_home()


    # simulate = Simulate.Simulate(G, time_step)
    # graphic = Graphics.Graphics(view_size)
    graphic = Graphics2.Graphics(view_size)


    iters = 0
    while True:
        t1 = time.time()
        if iters%1000 == 0:
            bodies.build_home()

        # updates_dict = ui.ui_step(simulate, graphic, bodies)

        # bodies_dict = bodies.get_bodies()
        # bodies_dict = simulate.simulate(bodies_dict)
        Simulate2.simulate(bodies.bodies, G, time_step)
        # bodies.set_bodies(bodies_dict)

        # if iters%10 == 0:
        graphic.update_graphic(bodies.bodies)

        t2 = time.time()
        # print(f"Hz: {round(1/(t2-t1), 3)}   ")

        # print(f"Total iterations: {iters}")
        iters += 1

        # print('\x1B[2A')


