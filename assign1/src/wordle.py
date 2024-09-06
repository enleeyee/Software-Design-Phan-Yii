from enum import Enum
from re import I
import tarfile

TARGET_LENGTH = 5
MAX_ATTEMPTS = 6

class Matches(Enum):
    EXACT_MATCH = 'green'
    PARTIAL_MATCH = 'yellow'
    WRONG_MATCH = 'gray'
    
class Status(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WIN = "WIN"
    LOSS = "LOSS"

class PlayResponse(Enum):
    ATTEMPTS = "Attempts: "
    TALLY_RESPONSE = "Tally Response: "
    GAME_STATUS = "Game Status: "
    MESSAGE = "Message: "
   

def tally(target, guess):
    validate_guess(guess)
    return [tally_for_position(i, target, guess) for i in range(len(guess))]

def validate_guess(guess): 
    if len(guess) != TARGET_LENGTH: raise ValueError("The length of guess is not 5")
    if guess.isalpha() == False: raise ValueError("There are non alphabetical letters")
    

def tally_for_position(index, target, guess):
    if target[index] == guess[index]:
        return Matches.EXACT_MATCH

    letter_guess = guess[index]

    total_exact_occurrences = count_occurrences(target, guess, letter_guess)
    total_partial_occurrences = count_occurrences_until_index(len(target) - 1, target, letter_guess) - total_exact_occurrences

    total_occurrences_guess_until_position = count_occurrences_until_index(index, guess, letter_guess)

    if total_partial_occurrences >= total_occurrences_guess_until_position:
        return Matches.PARTIAL_MATCH

    return Matches.WRONG_MATCH

def count_occurrences(target, guess, letter):
    return sum(1 for i in range(len(target)) if target[i] == guess[i] == letter)

def count_occurrences_until_index(index, word, letter):
    matches = word[:index + 1].count(letter)
    return matches if matches else 0

def validate_number_of_attempts(target, guess, current_attempt):
    if current_attempt < MAX_ATTEMPTS-1:
        return tally(target, guess)
    elif current_attempt == MAX_ATTEMPTS-1:
        if tally(target, guess) != [Matches.EXACT_MATCH] * TARGET_LENGTH:
            return []
        else:
            return tally(target, guess)
    else:
        return []

def play(target, guess, attempt):
    tally_score = validate_number_of_attempts(target, guess, attempt)
    win_message = {0: "Amazing!",
                   1: "Splendid!",
                   2: "Awesome!",
                   3: "Yay!",
                   4: "Yay!",
                   5: "Yay!"}

    if tally_score != []: 
        game_status = Status.WIN if all(match == Matches.EXACT_MATCH for match in tally_score) else Status.IN_PROGRESS
        message = win_message[attempt] if game_status == Status.WIN else ""
        attempt += 1
    else:
        game_status = Status.LOSS
        message = "It was " + target + ", better luck next time!"

    return {PlayResponse.ATTEMPTS : attempt,
            PlayResponse.TALLY_RESPONSE : tally_score,
            PlayResponse.GAME_STATUS : game_status, 
            PlayResponse.MESSAGE : message }