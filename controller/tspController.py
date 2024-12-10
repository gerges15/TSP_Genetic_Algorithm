import tkinter as tk
from tkinter import ttk, messagebox

from model.ga import genetic_algorithm
from model.city import generate_city_list
from view.view import TSPView
from model.generations import next_generation
from model.population import initial_population
from model.selection import rank_routes


class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Genetic Algorithm Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.font = ("JetBrains Mono", 11)
        self.results_frame_visible = False
        self.is_running = False

        self.create_frames()
        self.create_input_fields()
        self.create_visualization_area()
        self.create_buttons()
        self.create_results_text()

        # Create the view
        self.view = TSPView(self.root, self.canvas)

    def create_frames(self):
        """Creates the three main frames: visualization, input, and buttons."""
        # Visualization Frame
        self.frame_visualization = tk.Frame(self.root, bg="#ffffff", height=300)
        self.frame_visualization.pack(fill="both", expand=True)

        # Input Frame
        self.frame_inputs = tk.Frame(self.root, bg="#f0f0f0", height=150)
        self.frame_inputs.pack(fill="x", padx=20, pady=10)

        # Button Frame
        self.frame_buttons = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.frame_buttons.pack(fill="x", padx=20, pady=10)
        # Result Frame
        self.frame_results = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.frame_results.pack(side="right", fill="y", padx=20, pady=10)

    def create_visualization_area(self):
        """Creates the visualization area in the top frame."""
        self.canvas = tk.Canvas(
            self.frame_visualization, bg="#ffffff", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)
        self.set_default_inputs()

    def set_default_inputs(self):
        """Sets default values for the input fields."""
        self.inputs["Number of Cities"].set("20")
        self.inputs["Population Size"].set("100")
        self.inputs["Elite Size"].set("3")
        self.inputs["Mutation Rate"].set("0.02")
        self.inputs["Generations"].set("500")

    def create_input_fields(self):
        """Creates input fields for TSP data in the middle frame."""
        for i in range(4):
            self.frame_inputs.columnconfigure(i, weight=1)

        self.inputs = {}

        tk.Label(
            self.frame_inputs, text="Number of Cities", font=self.font, bg="#f0f0f0"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.inputs["Number of Cities"] = self.create_input_field(0, 1)

        tk.Label(
            self.frame_inputs, text="Population Size", font=self.font, bg="#f0f0f0"
        ).grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.inputs["Population Size"] = self.create_input_field(0, 3)

        tk.Label(
            self.frame_inputs, text="Elite Size", font=self.font, bg="#f0f0f0"
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.inputs["Elite Size"] = self.create_input_field(1, 1)

        tk.Label(
            self.frame_inputs, text="Mutation Rate", font=self.font, bg="#f0f0f0"
        ).grid(row=1, column=2, sticky="w", padx=10, pady=5)
        self.inputs["Mutation Rate"] = self.create_input_field(1, 3, is_float=True)

        tk.Label(
            self.frame_inputs, text="Generations", font=self.font, bg="#f0f0f0"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.inputs["Generations"] = self.create_input_field(2, 1)

    def create_input_field(self, row, col, is_float=False):
        var = tk.StringVar()
        entry = ttk.Entry(self.frame_inputs, textvariable=var, font=self.font)
        entry.grid(row=row, column=col, padx=10, pady=5)

        if is_float:
            var.trace("w", lambda *args: self.validate_float(var))
        else:
            var.trace("w", lambda *args: self.validate_integer(var))
        return var

    def create_buttons(self):
        self.frame_buttons.columnconfigure(0, weight=1)
        self.frame_buttons.columnconfigure(1, weight=1)
        self.frame_buttons.columnconfigure(2, weight=1)

        start_button = tk.Button(
            self.frame_buttons,
            text="Start Genetic Algorithm",
            command=self.start_algorithm,
            font=self.font,
            bg="#219B9D",
            fg="#EEEEEE",
        )
        start_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        clear_button = tk.Button(
            self.frame_buttons,
            text="Clear",
            command=self.clear_inputs,
            font=self.font,
            bg="#EB5B00",
            fg="#EEEEEE",
        )
        clear_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        show_button = tk.Button(
            self.frame_buttons,
            text="Show Plot",
            command="",
            font=self.font,
            bg="#4C1F7A",
            fg="#EEEEEE",
        )
        show_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    def create_results_text(self):
        self.results_text = tk.Text(
            self.frame_results, font=self.font, height=10, bg="#ffffff"
        )
        self.results_text.pack(fill="both", expand=True, padx=10, pady=10)

        hide_button = tk.Button(
            self.frame_results,
            text="Hide Results",
            command=self.toggle_results_frame,
            font=self.font,
            bg="#D32F2F",
            fg="#ffffff",
        )
        hide_button.pack(pady=5)

    def toggle_results_frame(self):
        if self.results_frame_visible:
            self.frame_results.pack_forget()
        else:
            self.frame_results.pack(side="bottom", fill="x", padx=20, pady=10)
        self.results_frame_visible = not self.results_frame_visible

    def validate_integer(self, var):
        value = var.get()
        if not value.isdigit():
            var.set("")

    def validate_float(self, var):
        value = var.get()
        try:
            if value and (float(value) < 0 or float(value) > 1):
                var.set("")
        except ValueError:
            var.set("")

    def start_algorithm(self):
        """Resets everything, sets defaults, and starts the algorithm."""
        self.reset_app()  # Reset everything
        if self.is_running:
            messagebox.showerror("Error", "Algorithm is already running.")
            return

        try:
            cities_number = int(self.inputs["Number of Cities"].get())
            self.tsp_data = {
                "population": generate_city_list(cities_number),
                "pop_size": int(self.inputs["Population Size"].get()),
                "elite_size": int(self.inputs["Elite Size"].get()),
                "mutation_rate": float(self.inputs["Mutation Rate"].get()),
                "generations": int(self.inputs["Generations"].get()),
            }

            self.view.draw_cities(self.tsp_data["population"])
            self.is_running = True

            # Run the genetic algorithm logic in the background
            self.root.after(100, self.run_algorithm)
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please fill in all fields with valid values."
            )

    def reset_app(self):
        """Clears the canvas, results text, and resets inputs to default."""
        self.canvas.delete("all")
        self.results_text.delete("1.0", tk.END)
        self.is_running = False
        self.set_default_inputs()

    def run_algorithm(self):
        try:
            cities = self.tsp_data["population"]
            self.best_routes = []

            pop = initial_population(self.tsp_data["pop_size"], cities)
            initial_dist = self.best_distance(pop)

            self.root.after(
                0,
                lambda: self.results_text.insert(
                    "end", f"Initial distance: {initial_dist:.2f}\n"
                ),
            )

            for generation in range(self.tsp_data["generations"]):
                pop = next_generation(
                    pop, self.tsp_data["elite_size"], self.tsp_data["mutation_rate"]
                )
                best_route = self.best_route(pop)
                self.best_routes.append(best_route)

                best_dist = self.best_distance(pop)
                self.view.draw_path(
                    best_route, color="orange"
                )  # Draw current iteration path

                self.root.after(
                    0,
                    lambda g=generation, d=best_dist: self.results_text.insert(
                        "end", f"Generation {g + 1}: Best distance = {d:.2f}\n"
                    ),
                )
                self.root.update_idletasks()

            final_dist = self.best_distance(pop)
            self.root.after(
                0,
                lambda: self.results_text.insert(
                    "end", f"Final distance: {final_dist:.2f}\n"
                ),
            )
        finally:
            self.is_running = False

    def best_distance(self, pop):
        return 1 / rank_routes(pop)[0][1]

    def best_route(self, pop):
        best_route_index = rank_routes(pop)[0][0]
        return pop[best_route_index]

    def clear_inputs(self):
        for key in self.inputs:
            self.inputs[key].set("")
