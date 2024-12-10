import threading
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

        self.create_frames()
        self.create_visualization_area()
        self.create_input_fields()
        self.create_buttons()
        self.create_results_frame()

        # Create the view
        self.view = TSPView(self.root, self.canvas)

        # Flags and placeholders
        self.is_running = False  # To prevent multiple starts
        self.best_routes = []

    def create_frames(self):
        """Creates the three main frames: visualization, input, and buttons."""
        self.frame_visualization = tk.Frame(self.root, bg="#ffffff", height=300)
        self.frame_visualization.pack(fill="both", expand=True)

        self.frame_inputs = tk.Frame(self.root, bg="#f0f0f0", height=150)
        self.frame_inputs.pack(fill="x", padx=20, pady=10)

        self.frame_buttons = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.frame_buttons.pack(fill="x", padx=20, pady=10)

    def create_visualization_area(self):
        """Creates the visualization area in the top frame."""
        self.canvas = tk.Canvas(
            self.frame_visualization, bg="#ffffff", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

    def create_input_fields(self):
        """Creates input fields for TSP data in the middle frame."""
        for i in range(4):
            self.frame_inputs.columnconfigure(i, weight=1)

        self.inputs = {}

        self.create_labeled_input("Number of Cities", 0, 0)
        self.create_labeled_input("Population Size", 0, 2)
        self.create_labeled_input("Elite Size", 1, 0)
        self.create_labeled_input("Mutation Rate", 1, 2, is_float=True)
        self.create_labeled_input("Generations", 2, 0)

    def create_labeled_input(self, label, row, col, is_float=False):
        """Helper to create labeled input fields."""
        tk.Label(self.frame_inputs, text=label, font=self.font, bg="#f0f0f0").grid(
            row=row, column=col, sticky="w", padx=10, pady=5
        )
        self.inputs[label] = self.create_input_field(row, col + 1, is_float)

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
        self.frame_buttons.columnconfigure([0, 1, 2], weight=1)

        tk.Button(
            self.frame_buttons,
            text="Start Genetic Algorithm",
            command=self.start_algorithm_thread,
            font=self.font,
            bg="#219B9D",
            fg="#EEEEEE",
        ).grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tk.Button(
            self.frame_buttons,
            text="Clear",
            command=self.clear_inputs,
            font=self.font,
            bg="#EB5B00",
            fg="#EEEEEE",
        ).grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Button(
            self.frame_buttons,
            text="Show Results",
            command=self.toggle_results_frame,
            font=self.font,
            bg="#4C1F7A",
            fg="#EEEEEE",
        ).grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    def create_results_frame(self):
        self.frame_results = tk.Frame(self.root, bg="#f0f0f0")
        self.results_text = tk.Text(
            self.frame_results, font=self.font, height=10, bg="#ffffff"
        )
        self.results_text.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Button(
            self.frame_results,
            text="Hide Results",
            command=self.toggle_results_frame,
            font=self.font,
            bg="#D32F2F",
            fg="#ffffff",
        ).pack(pady=5)

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

    def start_algorithm_thread(self):
        """Start the algorithm in a separate thread."""
        if self.is_running:
            messagebox.showwarning("Warning", "The algorithm is already running.")
            return

        try:
            # Gather inputs
            cities_number = int(self.inputs["Number of Cities"].get())
            self.tsp_data = {
                "population": generate_city_list(cities_number),
                "pop_size": int(self.inputs["Population Size"].get()),
                "elite_size": int(self.inputs["Elite Size"].get()),
                "mutation_rate": float(self.inputs["Mutation Rate"].get()),
                "generations": int(self.inputs["Generations"].get()),
            }

            self.is_running = True
            threading.Thread(target=self.run_algorithm, daemon=True).start()
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please fill in all fields with valid values."
            )

    def run_algorithm(self):
        """Runs the genetic algorithm logic."""
        try:
            cities = self.tsp_data["population"]
            self.best_routes = []

            self.view.draw_cities(cities)
            pop = initial_population(self.tsp_data["pop_size"], cities)

            for _ in range(self.tsp_data["generations"]):
                pop = next_generation(
                    pop, self.tsp_data["elite_size"], self.tsp_data["mutation_rate"]
                )
                self.best_routes.append(self.best_route(pop))

            self.root.after(0, self.animate_paths, 0)
        finally:
            self.is_running = False

    def animate_paths(self, index):
        if index < len(self.best_routes):
            self.view.draw_path(self.best_routes[index], color="blue")
            self.root.after(200, self.animate_paths, index + 1)

    def best_route(self, pop):
        return pop[rank_routes(pop)[0][0]]

    def clear_inputs(self):
        for key in self.inputs:
            self.inputs[key].set("")
