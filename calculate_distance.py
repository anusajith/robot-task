class Robot:
    """
    This is the class which has all the characteristics defined for the Robot.
    This class contains functions to calculate the movement and direction Robot will
    be following according to the commands given.
    """

    def __init__(self, start_x=0, start_y=0, direction="N"):
        self.direction = direction
        self.start_x = start_x
        self.start_y = start_y
        self.new_x = start_x
        self.new_y = start_y

    def move(self, command):
        """
        Function to define the movement of the robot according to command.
        Param : command eg: 'F1' or 'B2'
        Ultimately sets the current co-ordinates of the robot.
        """
        if command[0] == "F":
            if self.direction == "N":
                self.new_y = self.new_y + int(command[1])
            elif self.direction == "S":
                self.new_y = self.new_y - int(command[1])
            elif self.direction == "E":
                self.new_x = self.new_x + int(command[1])
            elif self.direction == "W":
                self.new_x = self.new_x + int(command[1])
        else:
            if self.direction == "N":
                self.new_y = self.new_y - int(command[1])
            elif self.direction == "S":
                self.new_y = self.new_y + int(command[1])
            elif self.direction == "E":
                self.new_x = self.new_x - int(command[1])
            elif self.direction == "W":
                self.new_x = self.new_x + int(command[1])

    def turn(self, command):
        """
        Function to define the direction the robot is facing according to the command.
        Param : command eg: 'L1' or 'R2'
        Ultimately sets the direction of the robot.
        """
        direction = ["N", "W", "S", "E"]
        unit = int(command[1])
        if command[0] == "L":
            # To decide the direction after running the command
            new_index = (direction.index(self.direction) + unit) % len(direction)
            self.direction = direction[new_index]
        else:
            new_index = (direction.index(self.direction) - unit) % len(direction)
            self.direction = direction[new_index]

    def displacement(self):
        """
        Function to calculate the units robot has to take to reach the starting co-ordinates.
        Returns total displacement units.
        """
        total_units = abs(self.start_x - self.new_x) + abs(self.start_y - self.new_y)
        return total_units

    def validate_commands(self, command_list):
        """
        Function to validate the commands given to robot.
        Param : command_list   eg: ['F1','R1','B2','L1','B3']
        Returns True for valid inputs else False.
        """
        for item in command_list:
            if item[0] in ("F", "B", "L", "R"):
                print("Validated commands successfully")
                return True
            else:
                print("Invalid Input Commands")
                return False

    def main(self, command):
        """
        This is main function which performs all the functions according to command.
        Param : command eg:'F1,R1,B2,L1,B3'
        Returns the units robot has to take to reach back home!
        """
        command_list = command.split(",")
        success = self.validate_commands(command_list)
        if success:
            for item in command_list:
                if item[0] in ("F", "B"):
                    self.move(item)
                else:
                    self.turn(item)
            print(
                "The total units robot has to take to be back home: {}".format(
                    self.displacement()
                )
            )
