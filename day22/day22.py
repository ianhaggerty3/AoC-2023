import sys
from dataclasses import dataclass

@dataclass
class Brick:
    x: int
    x_width: int
    y: int
    y_width: int
    z: int
    z_width: int

    def intersects(self, other):
        range_intersect = lambda a, b: a.start < b.stop and a.stop > b.start
        x1 = range(self.x, self.x + self.x_width)
        x2 = range(other.x, other.x + other.x_width)
        y1 = range(self.y, self.y + self.y_width)
        y2 = range(other.y, other.y + other.y_width)

        return range_intersect(x1, x2) and range_intersect(y1, y2)

def get_new_brick(brick):
    others = list(map(get_new_brick, filter(lambda other: brick != other and brick.intersects(other) and other.z < brick.z, bricks)))
    new_z = max(map(lambda other: other.z + other.z_width, others), default=0) + 1
    new_brick = Brick(x=brick.x, x_width=brick.x_width, y=brick.y, y_width=brick.y_width, z=new_z, z_width=brick.z_width)
    return new_brick

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

bricks = []
for line in lines:
    start, end = line.split('~')
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))
    bricks.append(Brick(x=min(start[0], end[0]), x_width=abs(end[0]-start[0]+1), y=min(start[1], end[1]), y_width=abs(end[1]-start[1]+1), z=min(start[2], end[2]), z_width=abs(end[2]-start[2]+1)))

new_bricks = []
for original_brick in bricks:
    new_bricks.append(get_new_brick(original_brick))

print(bricks)
print(new_bricks)