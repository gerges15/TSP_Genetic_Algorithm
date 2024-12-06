class TSPView:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.city_positions = {}  # Store normalized city positions

    def draw_cities(self, cities, paths=None):
        """Draw cities and optionally the best path."""
        self.canvas.delete("all")

        # Scaling and margins
        margin = 50
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()

        # Find the bounds of city coordinates
        min_x = min(city.get_x for city in cities)
        min_y = min(city.get_y for city in cities)
        max_x = max(city.get_x for city in cities)
        max_y = max(city.get_y for city in cities)

        # Normalize city positions to fit within the canvas
        def normalize(value, min_val, max_val, canvas_size):
            return margin + ((value - min_val) / (max_val - min_val)) * (
                canvas_size - 2 * margin
            )

        self.city_positions = {}  # Reset positions
        for i, city in enumerate(cities):
            x = normalize(city.get_x, min_x, max_x, width)
            y = normalize(city.get_y, min_y, max_y, height)
            self.city_positions[city] = (x, y)

            # Draw city as a circle
            self.canvas.create_oval(
                x - 5, y - 5, x + 5, y + 5, fill="#1F0068", outline="#E4E5FF", width=0
            )
            # Label the city
            self.canvas.create_text(
                x, y - 15, text=f"C{i + 1}", font=("JetBrains Mono", 10, "bold")
            )

        # Draw paths (optional)
        if paths:
            for i in range(len(paths) - 1):
                city1, city2 = paths[i], paths[i + 1]
                x1, y1 = self.city_positions[city1]
                x2, y2 = self.city_positions[city2]
                self.canvas.create_line(
                    x1, y1, x2, y2, fill="#A895FF", width=2, smooth=True
                )

            # Connect the last city to the first (closing the loop)
            x1, y1 = self.city_positions[paths[-1]]
            x2, y2 = self.city_positions[paths[0]]
            self.canvas.create_line(
                x1, y1, x2, y2, fill="#FF5733", width=2, smooth=True
            )

    def draw_path(self, tour, color="blue"):
        """
        Draws the path connecting the cities in the given tour.

        Args:
            tour (list): A list of city objects representing the visiting order.
            color (str): The color of the path to draw.
        """
        # Delete the previous path with the same color
        self.canvas.delete(f"path_{color}")

        # Ensure the tour contains at least two cities to form a path
        if len(tour) < 2:
            return

        # Draw lines between consecutive cities in the tour
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            x1, y1 = self.city_positions[city1]
            x2, y2 = self.city_positions[city2]
            self.canvas.create_line(
                x1, y1, x2, y2, fill=color, tags=f"path_{color}", width=2, smooth=True
            )

        # Close the loop by connecting the last city back to the first city
        first_city = tour[0]
        last_city = tour[-1]
        x1, y1 = self.city_positions[last_city]
        x2, y2 = self.city_positions[first_city]
        self.canvas.create_line(
            x1, y1, x2, y2, fill=color, tags=f"path_{color}", width=2, smooth=True
        )
