import json
import os.path
import csv
import turtle

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return "[]" if list_dictionaries is None or list_dictionaries == "[]" else json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        list_dic = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        lists = cls.to_json_string(list_dic)
        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string and len(json_string) > 0 else []

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_str = f.read()
        list_cls = cls.from_json_string(list_str)
        return [cls.create(**item) for item in list_cls]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                  "height": int(elm[2]), "x": int(elm[3]),
                                  "y": int(elm[4])} if cls.__name__ == "Rectangle" else \
                                  {"id": int(elm[0]), "size": int(elm[1]),
                                   "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except Exception:
            pass
        return my_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(5)

        def draw_shape(shape):
            turtle.penup()
            turtle.goto(shape.x, shape.y)
            turtle.color("black")
            turtle.pendown()
            for _ in range(2):
                turtle.forward(shape.width)
                turtle.left(90)
                turtle.forward(shape.height)
                turtle.left(90)

        for rectangle in list_rectangles:
            draw_shape(rectangle)

        for square in list_squares:
            draw_shape(square)

        turtle.penup()
        window.exitonclick()
