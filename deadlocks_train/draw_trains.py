from graphics import *


class TrainAnim:
    def __init__(self, win, train_length):
        self.colours = [color_rgb(233, 33, 40), color_rgb(78, 151, 210),
                        color_rgb(251, 170, 26), color_rgb(11, 132, 54)]
        self.train_length = train_length
        track0 = Line(Point(10, 330), Point(790, 330))
        track1 = Line(Point(10, 470), Point(790, 470))
        track2 = Line(Point(330, 10), Point(330, 790))
        track3 = Line(Point(470, 10), Point(470, 790))
        self.draw_track(win, track0)
        self.draw_track(win, track1)
        self.draw_track(win, track2)
        self.draw_track(win, track3)
        self.train0 = Line(Point(10, 330), Point(10 - train_length, 330))
        self.train1 = Line(Point(470, 10), Point(470, 10 - train_length))
        self.train2 = Line(Point(790, 470), Point(790 + train_length, 470))
        self.train3 = Line(Point(330, 790), Point(330, 790 + train_length))
        self.draw_train(win, self.train0, self.colours[0])
        self.draw_train(win, self.train1, self.colours[1])
        self.draw_train(win, self.train2, self.colours[2])
        self.draw_train(win, self.train3, self.colours[3])
        self.boxes = [Rectangle(Point(350, 350), Point(360, 360)),
                      Rectangle(Point(450, 350), Point(440, 360)),
                      Rectangle(Point(450, 450), Point(440, 440)),
                      Rectangle(Point(350, 450), Point(360, 440))]
        for box in self.boxes:
            self.draw_crossing(win, box)

    def update_trains(self, trains, intersections):
        current_x = self.train0.getP2().getX() - 10 + self.train_length
        self.train0.move(trains[0].front - current_x, 0)
        current_x = 790 - self.train2.getP2().getX() + self.train_length
        self.train2.move(current_x - trains[2].front, 0)
        current_y = self.train1.getP2().getY() - 10 + self.train_length
        self.train1.move(0, trains[1].front - current_y)
        current_y = 790 - self.train3.getP2().getY() + self.train_length
        self.train3.move(0, current_y - trains[3].front)
        for i in range(4):
            if intersections[i].locked_by < 0:
                self.boxes[i].setFill(color_rgb(185, 185, 185))
            else:
                self.boxes[i].setFill(self.colours[intersections[i].locked_by])

    def draw_crossing(self, win, box):
        box.setFill(color_rgb(185, 185, 185))
        box.draw(win)

    def draw_track(self, win, line):
        line.setFill(color_rgb(185, 185, 185))
        line.setWidth(4)
        line.draw(win)

    def draw_train(self, win, line, colour):
        line.setFill(colour)
        line.setWidth(14)
        line.draw(win)
