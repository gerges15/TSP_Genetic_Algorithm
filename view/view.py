class TSPView:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

    def draw_cities(self, cities):
        self.canvas.delete("all")

        min_x, min_y = float("inf"), float("inf")
        max_x, max_y = float("-inf"), float("-inf")

        for i, city in enumerate(cities):
            x = city.get_x
            y = city.get_y
            self.canvas.create_oval(
                x - 5,
                y - 5,
                x + 5,
                y + 5,
                fill="#1F0068",
                width=0,
                tags=city,
                outline="#E4E5FF",
            )  # Smoother nodes
            self.canvas.create_text(
                x, y - 15, text=f"C{i + 1}", font=("Arial", 10, "bold"), tags=city
            )
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        for city1 in cities:
            for city2 in cities:
                if city1 != city2:
                    x1, y1 = city1.get_x, city1.get_y
                    x2, y2 = city2.get_x, city2.get_y
                    self.canvas.create_line(
                        x1, y1, x2, y2, fill="#A895FF", width=1, smooth=True
                    )

        for city in cities:
            self.canvas.tag_raise(city)

        self.canvas.config(
            scrollregion=(min_x - 50, min_y - 50, max_x + 50, max_y + 50)
        )
