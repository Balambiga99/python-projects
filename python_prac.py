# word1 = input("Word : ")

# # f-strings fro madlibs
# print(f"This is the madlib project for ya {word1}")

# computer has a secret number and we have to guess the secret number

# import random

# number = 0
# number = random.randint(0,11)
# # print(f"The randomly generated number is {number}")
# user_input = input()

# if user_input == number:
#     print(f"Matched ", user_input, number)
# else:
#    print(f"Not Matched ", user_input, number) 

# we have a secret number and the computer has to guess it

# import random

# def guess_user_number(x):
#     lower_limit = int(input())

#     upper_limit = int(input())

#     user_number = x

#     computer_guess = 0

#     while computer_guess != user_number:
#         computer_guess = random.randint(lower_limit,upper_limit)
#         print("Guesssing.....")

#     print(f"The computer guessed it right {computer_guess}. And your number is {user_number}")

# guess_user_number(45)

# --------------------roshambo---------------------

# import random
# def roshambo(choice):
    
#     roshambo_choices = ['paper','rock','scissors']

#     computer_choice_index = random.randint(0,2)
#     print(computer_choice_index)

#     user_choice_index = roshambo_choices.index(choice)

#     if user_choice_index == 0 and computer_choice_index == 2:
#         print("Computer has won")
#     elif user_choice_index < computer_choice_index:
#         print("User has won")
    
#     elif user_choice_index == computer_choice_index:
#         print("It is a tie!")
#     else:
#         print("Computer has won")

#     computer_choice = roshambo_choices[computer_choice_index]
    
#     print(f"User chose {choice} and computer chose {computer_choice}")



# roshambo("paper")

# --------------------hangman-------------------
# import random
# import string 

# words = [
#     'apple',
#     'banana',
#     'orange',
#     'lemon',
#     'grape',
#     'mango',
#     'cherry',
#     'peach',
#     'watermelon',
#     'strawberry',
#     'elephant',
#     'giraffe',
#     'lion',
#     'tiger',
#     'monkey',
#     'zebra',
#     'turtle',
#     'dolphin',
#     'penguin',
#     'kangaroo'
# ]


# word = random.choice(words)

# word = word.upper()

# # print(word)

# letters = set(word)

# # print(letters)

# alphabet = set(string.ascii_uppercase)
# print(alphabet)

# used_letters = set()



# while len(letters) > 0:
#     guess = input("Enter your guess letter : ").upper()

#     if guess in alphabet-used_letters:
#         if guess in letters:
#             letters.remove(guess)
#             # print(letters)
#         else:
#             alphabet.remove(guess)
#             used_letters.add(guess)
#     else:
#         print("You have already used this word")
#     print(used_letters)

# print(f"Congrats! You guessed the word! Its {word}")

# Tic-Tac-Toe

# import random
# import math 
# import time

# human vs computer

# row1 = [0,1,2]
# row2 = [3,4,5]
# row3 = [6,7,8]
# col1= [0,3,6]
# col2 = [1,4,7]
# col3 = [2,5,8]
# diag1 = [0,4,8]
# diag2 = [2,4,6]


# player_letter = 'X'

# computer_letter = 'O'

# player_board = set()

# computer_board = set()

# while player_position not in computer_board:

#     player_choice, player_position = input(f"Hello player you are {player_letter} and computer is {computer_letter}. Enter your letter and its position.")


# player_board.add(player_position)

# row_ind = player_position // 3


# for i in random.randint(0,8):
#     if i not in player_board:
#         computer_board.add(i)
#     else:
#         continue

# class Player():
#     def __init__(self,letter):
#         self.letter = letter

# class HumanPlayer(Player):
#     def __init__(self,letter):
#         super().__init__(letter)
#     def get_move(self,game):
#         valid_move = False
#         val = None
#         while not valid_move:
#             square = input(f"Choose a valid move from 0-8 for {self.letter}")
#             try:
#                 val = int(square)
#                 if val not in game.available_moves():
#                     raise ValueError
#                 valid_move = True
#             except ValueError:
#                 print('Invalid move.')
#         return val

# class ComputerPlayer(Player):
#     def __init__(self,letter):
#         super().__init__(letter)

#     def get_move(self,game):
#         square = random.choice(game.available_moves())
#         return square
    

# class TicTacToe():
#     def __init__(self):
#         self.board = self.make_board()
#         self.current_winner = None

#     @staticmethod
#     def make_board():
#         return [' ' for _ in range(9)]

#     def print_board(self):
#         for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')

#     def available_moves(self):
#         moves = []
#         for i, value in enumerate(self.board):
#             if value == ' ':
#                 moves.append(i)
#         return moves
    
#     def print_board_nums(self):
#         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
#             print('|'+ '|'.join(row)+'|')

#     def empty_squares(self):
#         return ' ' in self.board
    
#     def num_empty_squares(self):
#         return len(self.empty_squares())
    
#     def make_move(self,square,letter):
#         if self.board[square] == ' ':
#             self.board[square] = letter
#             if self.winner(square,letter):
#                 self.current_winner = letter
#             return True
#         return False

#     def winner(self,square, letter):
#         row_indx = square // 3 #divides and rounds the value
#         row = [self.board[row_indx*i:(row_indx+1)*3] for i in range(3)]
#         if all(s == letter for s in row): # checks if all the letters are same across a row 
#             return True
        
#         col_indx = square % 3
#         col = [self.board[col_indx+i*3] for i in range(3)] # think in terms of quotient x divisor + reminder = dividend
#         if all(s == letter for s in col): # checks if all the letters are same across a row 
#             return True

#         diagonal1 = [self.board[i] for i in [0,4,8]]
        
#         if all(s == letter for s in diagonal1): # checks if all the letters are same across a row 
#             return True
#         diagonal2 = [self.board[i] for i in [2,4,6]]
        
#         if all(s == letter for s in diagonal2): # checks if all the letters are same across a row 
#             return True
        
#         return False


# def play(game,x_player,o_player,print_game=True):
    
#     if print_game:
#         game.print_board_nums()
    
#     letter = 'X'

#     while game.empty_squares():
#         if letter == 'X':
#             square = x_player.get_move(game)
#             print('Hey')
#         else:
#             square = o_player.get_move(game)

#         if game.make_move(square,letter):
#             if print_game:
#                 print('Move Made')
#                 game.print_board()
#             if game.current_winner:
#                 if print_game:
#                     print(f"{letter} wins!")
#                 return letter
#             letter = 'O' if letter == 'X' else 'X'

#         time.sleep(.8)

#     if print_game:
#         print("Its a tie!!")

# if __name__ == '__main__':
#     tic = TicTacToe()
#     o_player  = ComputerPlayer('O')
#     x_player = HumanPlayer('X')
#     # tic.print_board_nums()
#     play(tic,x_player,o_player,print_game=True)

# binary search
import random
import math

def binary_search(element,arr, low=None, high=None):
    array_length = len(arr)
    if low ==None:
        low = 0
    if high ==None:
        high = array_length - 1
    if high < low:
        print("not found")
        return -1
    mid = (low + high) //2
    print(array_length,mid)
    if element == arr[mid]:
        return mid
    elif element > arr[mid]:
        # r_arr = arr[mid:] 
        return binary_search(element,arr,low=mid+1,high=high)
    else:
        # l_arr = arr[:mid]
        return binary_search(element,arr,low=low,high=mid-1)
# array = [i for i in range(random.randint(5,10))]
array = [1,2,3,4,5,6]
# redo with range() and .sort()
array.sort()
print(array)

answer = binary_search(10,array)

print("Answer: ", answer)