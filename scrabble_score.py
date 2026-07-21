LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
POINTS = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

# Build Point Dictionary
letter_to_points = {
  letter:point 
  for letter, point in zip(LETTERS, POINTS)}

# Allow blank/invalid entries or lowercase lookup safely
def score_word(word):
  """Return the Scrabble score for a word."""
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total
brownie_points = score_word('BROWNIE')
print(brownie_points)

# Score Initial Game
player_to_words = {"player1": ['BLUE', 'TENNIS', 'EXIT'], "wordNerd": ['EARTH', 'EYES', 'MACHINE'], "Lexi Con": ['ERASER', 'BELLY', 'HUSKY'], "Prof Reader": ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = sum(score_word(word) for word in words)
  player_to_points[player] = player_points

print("Initial Scores:", player_to_points)

# Functions to play new words & update score
def play_word(player, word):
  """Add a new word for a player and update their score."""
  player_to_words[player].append(word)
  player_to_points[player] += score_word(word)
  return player_to_points[player]

updated_score = play_word("player1", "HELLO")

print(updated_score)

play_word("player1", "HELLO")
