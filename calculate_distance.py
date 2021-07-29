class Robot:
    def __init__(self, start_x=0, start_y=0, direction="N"):
        self.direction = direction
        self.start_x = start_x
        self.start_y = start_y
        self.new_x = start_x
        self.new_y = start_y

    def move(self, command):
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
        direction = ["N", "W", "S", "E"]
        unit = int(command[1])
        if command[0] == "L":
            new_index = (direction.index(self.direction) + unit) % len(direction)
            self.direction = direction[new_index]
        else:
            new_index = (direction.index(self.direction) - unit) % len(direction)
            self.direction = direction[new_index]

    def displacement(self):
        total_units = abs(self.start_x - self.new_x) + abs(self.start_y - self.new_y)
        return total_units

    def validate_commands(self, command_list):
        for item in command_list:
            if item[0] in ("F", "B", "L", "R"):
                print("Validated commands successfully")
                return True
            else:
                print("Invalid Input Commands")
                return False

    def main(self, command):
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
