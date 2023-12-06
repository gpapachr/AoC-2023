def parse_game_results(file_path):
    game_results = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Game"):
                game_id, rounds_str = line.split(":")
                game_id = int(game_id.split()[1])
                rounds = [round.strip() for round in rounds_str.split(";")]
                game_results.append((game_id, rounds))
    return game_results

def check_possible_games(game_results, red_count, green_count, blue_count):
    possible_games = []
    for game_id, rounds in game_results:
        valid_game = True
        for round in rounds:
            cubes = [cube.strip().split() for cube in round.split(',')]
            for cube in cubes:
                color, count = cube[1], int(cube[0])
                if color == 'red' and count > red_count:
                    valid_game = False
                    break
                elif color == 'green' and count > green_count:
                    valid_game = False
                    break
                elif color == 'blue' and count > blue_count:
                    valid_game = False
                    break
            if not valid_game:
                break
        if valid_game:
            possible_games.append(game_id)
    return possible_games

def findPowerOfMinimumSets(game_results):
    powers = []
    for game_id, rounds in game_results:
        need_of_reds = 0
        need_of_greens = 0
        need_of_blues = 0
        for round in rounds:
            cubes = [cube.strip().split() for cube in round.split(',')]
            for cube in cubes:
                color, count = cube[1], int(cube[0])
                if color == 'red' and count > need_of_reds:
                    need_of_reds = count
                elif color == 'green' and count > need_of_greens:
                    need_of_greens = count
                elif color == 'blue' and count > need_of_blues:
                    need_of_blues = count
        powers.append(need_of_reds * need_of_greens * need_of_blues)
    return powers

#################### Part 1 ####################
# Cube counts
red_count = 12
green_count = 13
blue_count = 14

# File path
file_path = 'day2/day2input.txt'

# Parse game results from the file
game_results = parse_game_results(file_path)

# Check which games are possible
possible_games = check_possible_games(game_results, red_count, green_count, blue_count)

# Sum of the IDs of the possible games
sum = 0
for id in possible_games:
    sum += id
print("Sum of the ids of the possible games: ", sum)

#################### Part 2 ####################
# game_results already parsed above

powers = findPowerOfMinimumSets(game_results)

# Sum of powers
sumOfPowers = 0
for p in powers:
    sumOfPowers += p
print("Sum of powers of the minimum sets: ", sumOfPowers)

