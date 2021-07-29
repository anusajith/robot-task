import calculate_distance
import yaml
import os


def test_robo():
    print(
        "Choose the option of input:\n"
        "1. Enter the command string\n"
        "2. Select from input file"
    )
    option = input("Enter 1 or 2 to select the input method:")
    while not (option == "1" or option == "2"):
        print("Invalid option, please enter valid option")
        option = input("Enter 1 or 2 to select the input method:")

    if option == "1":
        command = input("Enter the command as string:")
        command = command[1:-1]
        robo = calculate_distance.Robot(0, 0, "N")
        robo.main(command)

    elif option == "2":
        file = open(os.path.dirname(__file__) + "/input.yml")
        parsed_input_file = yaml.load(file, Loader=yaml.FullLoader)
        command_list = parsed_input_file.get("input_list")
        for item in command_list:
            robo = calculate_distance.Robot(0, 0, "N")
            robo.main(item)


if __name__ == "__main__":
    test_robo()
