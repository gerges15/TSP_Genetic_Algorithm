import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


class TSPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Genetic Algorithm")

        # Set global font
        self.font_style = tkfont.Font(family="JetBrains Mono", size=10)
        self.root.option_add("*Font", self.font_style)

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
        """Creates input fields for TSP data (integer-only, horizontally aligned)."""
        labels = [
            "Number of Cities",
            "Population Size",
            "Elite Size",
            "Mutation Rate",
            "Generations",
        ]
        self.inputs = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(self.frame_input, text=f"{label_text}:", bg="lightgray")
            label.grid(row=i // 2, column=(i % 2) * 2, padx=10, pady=5, sticky=tk.E)

            if label_text == "Mutation Rate":
                # Special validation for Mutation Rate
                entry = tk.Entry(
                    self.frame_input,
                    validate="key",
                    validatecommand=(
                        self.root.register(self.validate_mutation_rate),
                        "%P",
                    ),
                )
            else:
                # Integer-only validation for other fields
                entry = tk.Entry(
                    self.frame_input,
                    validate="key",
                    validatecommand=(self.root.register(self.validate_integer), "%P"),
                )
            entry.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=10, pady=5)
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

    def validate_integer(self, value):
        """Validation function to allow only integers."""
        if value.isdigit() or value == "":
            return True
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return False

    def validate_mutation_rate(self, value):
        """Validation function to allow only numbers between 0 and 1 for Mutation Rate."""
        if value == "" or self.is_valid_mutation_rate(value):
            return True
        else:
            messagebox.showerror(
                "Invalid Input", "Mutation Rate must be a number between 0 and 1."
            )
            return False

    def is_valid_mutation_rate(self, value):
        """Checks if the input value is a valid mutation rate (0 <= value <= 1)."""
        try:
            val = float(value)
            return 0 <= val <= 1
        except ValueError:
            return False

    def start_algorithm(self):
        """Starts the genetic algorithm."""
        try:
            tsp_data = {
                "Number of Cities": int(self.inputs["Number of Cities"].get()),
                "Population Size": int(self.inputs["Population Size"].get()),
                "Elite Size": int(self.inputs["Elite Size"].get()),
                "Mutation Rate": float(
                    self.inputs["Mutation Rate"].get()
                ),  # Converted to float
                "Generations": int(self.inputs["Generations"].get()),
            }
            print("Starting algorithm with:", tsp_data)
            # Visualization and logic will be implemented here
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please fill in all fields with valid values."
            )

    def stop_algorithm(self):
        """Stops the algorithm."""
        print("Algorithm stopped.")

    def continue_algorithm(self):
        """Continues the algorithm."""
        print("Algorithm continued.")
