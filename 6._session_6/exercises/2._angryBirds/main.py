import random

class Bird:

    def __init__(self, board_size):
        self.x_max = board_size[0]-1
        self.y_max = board_size[1]-1
        self.pos_x = random.randint(0, self.x_max)
        self.pos_y = random.randint(0, self.y_max)

    
    def bird_move(self, user_move):
        if user_move == 'a':
            if self.pos_x == 0:
                print("Already at left limit")
            
            else:
                self.pos_x -= 1

        elif user_move == 'w':
            if self.pos_y == 0:
                print("Already at upper height limit")
            
            else:
                self.pos_y -= 1

        elif user_move == 'd':
            if self.pos_x == self.x_max:
                print("Already at right limit")

            else:
                self.pos_x += 1

        elif user_move == 's':
            if self.pos_y == self.y_max:
                print("Already at lower limit")

            else:
                self.pos_y += 1
            
        else:
            print("Invalid move input")


class Pig:

    def __init__(self, board_size):
        self.pos_x = random.randint(0, board_size[0]-1)
        self.pos_y = random.randint(0, board_size[1]-1)


class Board:

    def __init__(self, board_size):
        self.board_x = board_size[0]
        self.board_y = board_size[1]
        self.pig = Pig(board_size)
        self.bird = Bird(board_size)
        while (self.validate()):
            self.bird = Bird(board_size)
        
    
    def validate(self):
        if (self.pig.pos_x == self.bird.pos_x and self.pig.pos_y == self.bird.pos_y):
            return True
        return False

    def is_bird_on_pig(self, board):
        if (self.bird.pos_x == self.pig.pos_x and self.bird.pos_y == self.pig.pos_y):
            return True
        return False

    def is_play_again(self, user_choice):
        if (user_choice == "n" or user_choice == "N"):
            return False
        return True

    
    def print_current_board(self):
        print('\n' + '\n' + '\n' + '\n')
        for y in range(self.board_y):

            for x in range (self.board_x):
                if x == self.pig.pos_x and y == self.pig.pos_y:
                    print("P", end="    ")

                elif x == self.bird.pos_x and y == self.bird.pos_y:
                    print ("B", end="    ")
                
                else:
                    print("*", end="    ")
            
            print('\n')


class Workspace:
    
    def __init__(self):
        pass
    
    def display_available_commands(self):
        print("Insert (a) to move left")
        print("Insert (w) to move upwards")
        print("Insert (d) to move right")
        print("Insert (s) to move down")

    def game_board_size(self):
        user_choice_pos_x = int(input("How many spots on the x axis: "))
        user_choice_pos_y = int(input("How many spots on the y axis: "))
        return [user_choice_pos_x, user_choice_pos_y]



class Game:
    run = True
    while(run):

        # Make board and get inputs for board size
        workspace = Workspace()
        # Create random positions for pig and bird for this given game
        board = Board(workspace.game_board_size())

        while(not board.is_bird_on_pig(board)):

            board.print_current_board()

            workspace.display_available_commands()

            board.bird.bird_move(input("Move direction: "))
        
        run = board.is_play_again(input("You win! Wanna play again? (Y/n): "))