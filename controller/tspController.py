import tkinter as tk
from tkinter import ttk, messagebox


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

    def create_visualization_area(self):
        """Creates the visualization area in the top frame."""
        self.canvas = tk.Canvas(
            self.frame_visualization, bg="#ffffff", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

    def create_input_fields(self):
        """Creates input fields for TSP data in the middle frame."""
        # Configure grid for alignment
        for i in range(4):
            self.frame_inputs.columnconfigure(i, weight=1)

        # Input fields dictionary for easy retrieval
        self.inputs = {}

        # Number of Cities
        tk.Label(
            self.frame_inputs, text="Number of Cities", font=self.font, bg="#f0f0f0"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.inputs["Number of Cities"] = self.create_input_field(0, 1)

        # Population Size
        tk.Label(
            self.frame_inputs, text="Population Size", font=self.font, bg="#f0f0f0"
        ).grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.inputs["Population Size"] = self.create_input_field(0, 3)

        # Elite Size
        tk.Label(
            self.frame_inputs, text="Elite Size", font=self.font, bg="#f0f0f0"
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.inputs["Elite Size"] = self.create_input_field(1, 1)

        # Mutation Rate
        tk.Label(
            self.frame_inputs, text="Mutation Rate", font=self.font, bg="#f0f0f0"
        ).grid(row=1, column=2, sticky="w", padx=10, pady=5)
        self.inputs["Mutation Rate"] = self.create_input_field(1, 3, is_float=True)

        # Number of Generations
        tk.Label(
            self.frame_inputs, text="Generations", font=self.font, bg="#f0f0f0"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.inputs["Generations"] = self.create_input_field(2, 1)

    def create_input_field(self, row, col, is_float=False):
        """Creates an input field with validation."""
        var = tk.StringVar()
        entry = ttk.Entry(self.frame_inputs, textvariable=var, font=self.font)
        entry.grid(row=row, column=col, padx=10, pady=5)

        if is_float:
            var.trace("w", lambda *args: self.validate_float(var))
        else:
            var.trace("w", lambda *args: self.validate_integer(var))
        return var

    def create_buttons(self):
        """Creates buttons to control the algorithm with space-evenly alignment."""
        # Configure the frame to distribute columns evenly
        self.frame_buttons.columnconfigure(0, weight=1)
        self.frame_buttons.columnconfigure(1, weight=1)
        self.frame_buttons.columnconfigure(2, weight=1)

        # Add buttons
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
            text="Show Results",
            command=self.toggle_results_frame,
            font=self.font,
            bg="#4C1F7A",
            fg="#EEEEEE",
        )
        show_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    def create_results_frame(self):
        """Creates a frame for showing results."""
        self.frame_results = tk.Frame(self.root, bg="#f0f0f0", height=200)
        self.frame_results.pack(fill="x", padx=20, pady=10, expand=False)
        self.frame_results.pack_forget()  # Initially hidden

        # Text Logger
        self.results_text = tk.Text(
            self.frame_results, font=self.font, height=10, bg="#ffffff"
        )
        self.results_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Hide Button
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
        """Toggles the visibility of the results frame."""
        if self.results_frame_visible:
            self.frame_results.pack_forget()
        else:
            self.frame_results.pack(fill="x", padx=20, pady=10)
        self.results_frame_visible = not self.results_frame_visible

    def validate_integer(self, var):
        """Ensures input is an integer."""
        value = var.get()
        if not value.isdigit():
            var.set("")

    def validate_float(self, var):
        """Ensures input is a float between 0 and 1."""
        value = var.get()
        try:
            if value and (float(value) < 0 or float(value) > 1):
                var.set("")
        except ValueError:
            var.set("")

    def start_algorithm(self):
        """Starts the genetic algorithm."""
        try:
            tsp_data = {
                "Number of Cities": int(self.inputs["Number of Cities"].get()),
                "Population Size": int(self.inputs["Population Size"].get()),
                "Elite Size": int(self.inputs["Elite Size"].get()),
                "Mutation Rate": float(self.inputs["Mutation Rate"].get()),
                "Generations": int(self.inputs["Generations"].get()),
            }
            print("Starting algorithm with:", tsp_data)
            # Example logger update:
            self.results_text.insert("end", f"Best Tour: {tsp_data}\n")
            self.results_text.insert("end", f"Distance: Example Distance\n")
            self.results_text.insert(
                "end", f"Current Distance: Example Current Distance\n"
            )
            self.results_text.insert("end", f"Generation: Example Generation\n")
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please fill in all fields with valid values."
            )

    def clear_inputs(self):
        """Clears all input fields."""
        for key in self.inputs:
            self.inputs[key].set("")
