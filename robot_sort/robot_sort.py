class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def check_if_done(self):
        if self.compare_item() == None:
            print("Done.")
            return True
        # let's try to have all interaction with the 'None' item happen at the start of the list
        # that way I can use conditions which lead to the None item being not-at-start become break triggers
        # this will allow my program to simply error out?
        # the alternative path is to use the None item as a position marker

    def fizzselect(self):
        if self.compare_item() > 0:
            self.swap_item()

    def move_to_end(self):
        # reusable logic for movement loops
        while True:
            if self.can_move_right():
                self.move_right()
            else:
                break

    def move_to_start(self):
        # reusable logic for movement loops
        while True:
            if self.can_move_left():
                self.move_left()
            else:
                break

    def seek_nothingness(self):
        self.move_to_start()
        print("Moving to start.")
        # this loop allows us to seek the None item I'm using as a marker
        while True:
            if self.can_move_right() and self.compare_item() == None:
                self.attain_nothingness()
                break
            elif self.can_move_right() == False and self.compare_item() == None:
                print("Attaining enlightenment via seek_nothingness.")
                self.set_light_on()
                break
            else:
                if self.can_move_right():
                    self.move_right()
                else:
                    print("Hit seek_nothingness else-else break")
                    break

    def attain_nothingness(self):
        self.swap_item()
        self.move_right()
        self.swap_item()
        if self.can_move_right():
            self.move_right()
        else:
            print("Attaining enlightenment via attain_nothingness")
            self.set_light_on()

    def cleaning_the_end(self):
        self.move_left()
        if self.compare_item() < 0:
            self.swap_item()
            self.move_right()
            self.swap_item()
        else:
            self.move_right()
            self.swap_item()

    def sort(self):
        """
        Sort the robot's list.
        """

        # let's initialize this sorting routine with a quick swap and then nudge to the right?
        # then proceed with a bubble sort? or the "fizzy" select sort`
        self.swap_item()  # None at 0
        self.move_right()

        # sorting... start!
        # Thinking about this a bit harder and writing a few methods
        # I'm going to go with the None-placeholder
        # That allows me to use None-at-end to mark "done"
        # We can do a "comparison dance" at the end to make sure we're holding the None object

        while True:
            if self.can_move_left() == False:
                if self.check_if_done() == True:
                    return
            else:
                if self.light_is_on():
                    self.cleaning_the_end()
                    break
                elif self.can_move_right():
                    self.move_right()
                    self.fizzselect()
                else:
                    print("Seeking nothingness.")
                    self.seek_nothingness()

        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
