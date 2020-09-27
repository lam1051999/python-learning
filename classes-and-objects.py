import copy


class Point:
    """Represent a point"""


class Rectangle:
    """Represent a rectangle.
    attributes: width, height, corner.
    """


def print_point(pt):
    print("The x position: " + str(pt.x))
    print("The y position: " + str(pt.y))


def print_rect(rect):
    print("The width: " + str(rect.width))
    print("The height: " + str(rect.height))
    print("----corner----")
    print_point(rect.corner)


box = Rectangle()
box.width = 100
box.height = 200
# bottom-left corner
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    center = Point()
    center.x = rect.corner.x + rect.width/2
    center.y = rect.corner.y + rect.height/2
    return center


def grow_rectangle(rect, width, height):
    rect.width += width
    rect.height += height


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


deepcopy_box = copy.deepcopy(box)
move_rectangle(deepcopy_box, 50, 50)

print_rect(box)
print_rect(deepcopy_box)
