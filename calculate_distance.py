class Robot:
    def __init__(self):
        pass

    def move(self, command):
        pass

    def turn(self, command):
        pass

    def displacement(self):
        return 0

    def validate_commands(self,command_list):
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
            print(self.displacement())


if __name__ == "__main__":
    robo = Robot()
    robo.main("F1,L1,F3,R1,B4")
