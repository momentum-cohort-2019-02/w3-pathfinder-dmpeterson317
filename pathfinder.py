from PIL import Image, ImageDraw

class MapDataDrawer:

    def __init__(self, filename):
        '''Reads in text file, places elevations into list, and finds highest and lowest elevations'''
        # self.elevations = []
        with open(filename) as file:
            self.elevations = [[int(e) for e in line.split()] for line in file]
            # for line in file:
            #     self.elevations.append([int(e) for e in line.split()])
 
        self.highest_elevation = max([max(row) for row in self.elevations])
        self.lowest_elevation = min([min(row) for row in self.elevations])

    def get_elevation(self, x, y):
        '''Adjust coordinates order'''
        return self.elevations[y][x]

    def color(self, x, y): 
        return int(
                (self.get_elevation(x, y) - self.lowest_elevation) / (self.highest_elevation - self.lowest_elevation) * 255
            )

    def draw_map(self):
        self.picture = Image.new('RGBA', (len(self.elevations[0]), len(self.elevations)))
        self.draw = ImageDraw.Draw(self.picture)
        for x in range(len(self.elevations[0])):
            for y in range(len(self.elevations)):
                self.picture.putpixel((x, y), (self.color(x, y), self.color(x, y), self.color(x, y)))
        self.picture.save('map.png')
        

if __name__ == '__main__':

    elevation_map = MapDataDrawer('elevation_small.txt')
    elevation_map.draw_map()