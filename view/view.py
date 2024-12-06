class TSPView:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

    def draw_cities_and_solution(self, cities, best_order):
        # Draw points on the canvas and connect them with lines
        for i in range(len(best_order) - 1):
            start_city = best_order[i]
            end_city = best_order[i + 1]

            LINE_COLOR = "#A895FF"
            self.canvas.create_line(
                start_city.get_x,
                start_city.get_y,
                end_city.get_x,
                end_city.get_y,
                width=2,
                fill=LINE_COLOR,
            )

            POINT_OUTLINE = "#E4E5FF"
            POINT_COLOR = "#1F0068"
            self.canvas.create_oval(
                start_city.get_x - 5,
                start_city.get_y - 5,
                start_city.get_x + 5,
                start_city.get_y + 5,
                width=3,
                outline=POINT_OUTLINE,
                fill=POINT_COLOR,
            )
