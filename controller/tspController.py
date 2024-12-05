import tkinter as tk

# import random
# from model.city import City, generate_city_list
# from view.view import TSPView
# from model.ga import genetic_algorithm


# class TSPController:
#     def __init__(self):
#         # Create the main window
#         self.root = tk.Tk()
#         self.root.title("Traveling Salesman Problem(TSP) Visualization")
#         self.CITY_NUMBERS = 5

#         self.tsp_data = {
#             "population": generate_city_list(self.CITY_NUMBERS),
#             "pop_size": 100,
#             "elite_size": 20,
#             "mutation_rate": 0.01,
#             "generations": 50,
#         }

#         # Set the window background color to indigo with opacity 0.8
#         self.root.configure(bg="#3D26B1")
#         self.root.resizable(width=0, height=0)
#         self.root.attributes("-alpha", 0.9)

#         # Set the size of the main window
#         WINDOW_WIDTH = 600
#         WINDOW_HEIGHT = 700
#         self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

#         # Create a canvas
#         CANVAS_WIDTH = 580
#         CANVAS_HEIGHT = 580
#         BG_COLOR = "#3D26B1"
#         self.canvas = tk.Canvas(
#             self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR
#         )
#         self.canvas.pack(fill=tk.BOTH, expand=False, padx=20, pady=20)
#         # Set pady to 10 for a 10-pixel space at the top

#         # Set borderwidth and highlightthickness to zero to remove the border
#         self.canvas.configure(borderwidth=0, highlightthickness=0)
#         self.canvas.pack()

#         # Create a slider to adjust the number of cities
#         LABEL_BG_COLOR = "#1F0068"
#         self.slider_label = tk.Label(
#             self.root, text="Number of Cities:", bg=LABEL_BG_COLOR
#         )
#         self.slider_label.pack()

#         SLIDER_MIN = 3
#         SLIDER_MAX = 50
#         SLIDER_INIT_VALUE = 5
#         SLIDER_FOREGROUND_COLOR = "#ABAFFF"
#         SLIDER_BG_COLOR = "#1F0068"
#         self.num_cities_slider = tk.Scale(
#             self.root,
#             from_=SLIDER_MIN,
#             to=SLIDER_MAX,
#             orient=tk.HORIZONTAL,
#             length=400,
#             command=self.update_cities,
#             foreground=SLIDER_FOREGROUND_COLOR,
#             bg=SLIDER_BG_COLOR,
#         )

#         # Set initial value
#         self.num_cities_slider.set(SLIDER_INIT_VALUE)

#         # Initialize cities and distances
#         self.initialize_cities()

#         # Create the view
#         self.view = TSPView(
#             self.root, self.canvas, self.slider_label, self.num_cities_slider
#         )

#         # Draw initial cities and solve TSP
#         self.view.draw_cities_and_solution(self.cities, self.best_order)
#         # Run the Tkinter event loop
#         self.root.mainloop()

#     def initialize_cities(self):
#         self.num_cities = self.num_cities_slider.get()
#         self.cities = self.tsp_data["population"]
#         self.solver = genetic_algorithm(self.tsp_data)

#         ordered_cities, min_distance = self.solver
#         self.best_order = ordered_cities
#         self.minimum_distance = min_distance

#     def update_cities(self, value):
#         self.num_cities = int(value)
#         self.cities = [
#             City(x=random.randint(20, 540), y=random.randint(20, 540))
#             for _ in range(self.num_cities)
#         ]
#         self.solver = genetic_algorithm(self.tsp_data)

#         ordered_cities, min_distance = self.solver
#         self.best_order = ordered_cities
#         self.minimum_distance = min_distance

#         # Clear canvas and redraw
#         self.clear_and_redraw()

#     def clear_and_redraw(self):
#         # Clear canvas and redraw
#         self.canvas.delete("all")
#         self.view.draw_cities_and_solution(self.cities, self.best_order)


import tkinter as tk


class TSPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Genetic Algorithm")

        # Frame 1: Visualization
        self.frame_visualization = tk.Frame(root, bg="white", height=400)
        self.frame_visualization.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame_visualization, bg="white", height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Frame 2: TSP Data Input
        self.frame_input = tk.Frame(root, bg="lightgray", height=150)
        self.frame_input.pack(fill=tk.BOTH)
        self.create_input_fields()

        # Frame 3: Buttons
        self.frame_buttons = tk.Frame(root, bg="gray", height=50)
        self.frame_buttons.pack(fill=tk.BOTH)
        self.create_buttons()

    def create_input_fields(self):
        """Creates input fields for TSP data."""
        labels = [
            "Number of Cities:",
            "Population Size:",
            "Elite Size:",
            "Mutation Rate:",
            "Generations:",
        ]
        self.inputs = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(self.frame_input, text=label_text, bg="lightgray")
            label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            entry = tk.Entry(self.frame_input)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.inputs[label_text] = entry

    def create_buttons(self):
        """Creates buttons to control the algorithm."""
        start_button = tk.Button(
            self.frame_buttons,
            text="Start Genetic Algorithm",
            command=self.start_algorithm,
        )
        start_button.pack(side=tk.LEFT, padx=10, pady=10)

        stop_button = tk.Button(
            self.frame_buttons, text="Stop", command=self.stop_algorithm
        )
        stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        continue_button = tk.Button(
            self.frame_buttons, text="Continue", command=self.continue_algorithm
        )
        continue_button.pack(side=tk.LEFT, padx=10, pady=10)

    def start_algorithm(self):
        """Starts the genetic algorithm."""
        # Collect data from input fields
        tsp_data = {
            "city_list": self.inputs["Number of Cities:"].get(),
            "population_size": self.inputs["Population Size:"].get(),
            "elite_size": self.inputs["Elite Size:"].get(),
            "mutation_rate": self.inputs["Mutation Rate:"].get(),
            "generations": self.inputs["Generations:"].get(),
        }
        print("Starting algorithm with:", tsp_data)
        # Visualization and logic will be implemented here

    def stop_algorithm(self):
        """Stops the algorithm."""
        print("Algorithm stopped.")

    def continue_algorithm(self):
        """Continues the algorithm."""
        print("Algorithm continued.")


# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = TSPGUI(root)
    root.mainloop()
