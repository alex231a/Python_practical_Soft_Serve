class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.game_over:
            # Check if the words list is empty (first word)
            if not self.words:
                self.words.append(word)
                return self.words
            else:
                # Check if the word follows the rules
                if self.words[-1][-1] == word[0] and word not in self.words:
                    self.words.append(word)
                    return self.words
                else:
                    self.game_over = True
                    return "game over"
        else:
            return "game over"

    def restart(self):
        self.words = []  # Reset the words list
        self.game_over = False  # Reset the game state
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.play('apple')) # ['apple']

print(my_gallows.play('ear')) # ['apple', 'ear']
print(my_gallows.play('rhino')) # ['apple', 'ear', 'rhino']
print(my_gallows.words) # ['apple', 'ear', 'rhino']
# # Words should be accessible.
print(my_gallows.restart()) # "game restarted"
# # Words list should be set back to empty.
print(my_gallows.play('hostess')) # ['hostess']
# my_gallows.play('stash') # ['hostess', 'stash']
# my_gallows.play('hostess') # "game over"
# # Words cannot have already been said.
# my_gallows.play('apple') # ['apple']
# my_gallows.play('ear') # ['apple', 'ear']
# my_gallows.play('rhino') # ['apple', 'ear', 'rhino']
# # Corn does not start with an "o".
# my_gallows.play('corn') ##
# my_gallows.words # ['apple', 'ear', 'rhino']
# my_gallows.restart() # "game restarted"
# my_gallows.words # []
