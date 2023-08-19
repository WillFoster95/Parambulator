import PySimpleGUI as sg

class UI():

    def __init__(self):
        self.G_scale_factor = 1e6
        layout = [[sg.Text("Hello from PySimpleGUI")], 
                  [sg.Text("time_step:"), sg.Text("", key="time_step"), sg.Input(key="time_step_val"), sg.Button("Set time_step")], 
                  [sg.Text("G (10^-6):"), sg.Text("", key="G"), sg.Input(key="G_val"), sg.Button("Set G"), sg.Button("Reset G")],
                  [sg.Text("Number"), sg.Input(key="num"), sg.Text("Altitude"), sg.Input(key="alt"), sg.Button("belt")],
                  [sg.Button("<"), sg.Button("^"), sg.Button(">"), sg.Button("v"), sg.Button("IN"), sg.Button("OUT")]]
        # Create the window
        self.window = sg.Window("Demo", layout)



    def ui_step(self, simulate, graphic, bodies):
        self.read_ui(simulate, graphic, bodies)
        self.update_ui(simulate, graphic, bodies)

    def read_ui(self, simulate, graphic, bodies):

        event, values = self.window.read(timeout=1)
        if event == "Set time_step":
            try:
                simulate.time_step = float(values["time_step_val"])
            except ValueError:
                pass
        elif event == "Set G":
            try:
                simulate.G = float(values["G_val"])/self.G_scale_factor
            except ValueError:
                pass
        elif event == "Reset G":
            try:
                simulate.G = 0.00000003
            except ValueError:
                pass

        elif event == "<":
            try:
                graphic.shift_left()
            except ValueError:
                pass

        elif event == "^":
            try:
                graphic.shift_up()
            except ValueError:
                pass

        elif event == ">":
            try:
                graphic.shift_right()
            except ValueError:
                pass

        elif event == "v":
            try:
                graphic.shift_down()
            except ValueError:
                pass

        elif event == "IN":
            try:
                graphic.zoom_in()
            except ValueError:
                pass

        elif event == "OUT":
            try:
                graphic.zoom_out()
            except ValueError:
                pass

        elif event == "belt":
            try:
                bodies.belt(int(values["num"]), float(values["alt"]), simulate.G)
            except ValueError:
                pass


        elif event == sg.WIN_CLOSED:
            self.window.close()
            exit()

    
    def update_ui(self, simulate, graphic, bodies):
        self.window["time_step"].update(simulate.time_step)
        self.window["G"].update(round(simulate.G*self.G_scale_factor, 3))