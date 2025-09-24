import socket
import numpy as np
import time
from multiprocessing.pool import ThreadPool
from datetime import date

def utility_function(board, player):
    #utility function je samo score difference i računa score
    #the function takes the board and the current player
    if player == 1:
        #if it's player one
        #set players index to 6
        player_store = 6
        #set opponents index at 13
        opponent_store = 13
    else:
        #if it's player 2
        #ser players index to 13
        player_store = 13
        #set opponents index at 6
        opponent_store = 6

    #calculate the score difference
    score_diff = board[player_store] - board[opponent_store]
    #subtract the opponents store stones from the players store stones

    return score_diff #return the differenc in the score




def minimax(board, depth, turn, player):
    #see if gam has ended
    terminal = sum(board[0:6]) == 0 or sum(board[7:13]) == 0

    #return if depth=0
    if depth == 0 or terminal:
        return utility_function(board, player), None

    #set valid moves to an empty list
    valid_moves = []
    start_index = 0 if turn == 1 else 7  #Player 1 starts from index 0, Player 2 from index 7

    #dodaj valid_moves u listu
    for i in range(6):
        if board[start_index + i] > 0:
            valid_moves.append(i + 1)
            #print(valid_moves)
    #print(valid_moves)

    #if there aro no valid moves left calculate the score
    if not valid_moves:
        return utility_function(board, player), None

    #maximize if it's our player's turn
    if turn == player:
        #postavi na najnizi moguci
        max_eval = float('-inf')
        best_move = None
        for move in valid_moves:
            #Kopiraš board and simulate it
            new_board, next_turn = play(turn, move, board.copy())
            #print(new_board)
            #print(next_turn)
            eval_score, uslesess_var = minimax(new_board, depth - 1, next_turn, player)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        #print(best_move)
        #print(max_eval)
        return max_eval, best_move
    else:
        #opponent's turn
        #bukvalno ti je sve isto samo samo +inf
        min_eval = float('inf')
        best_move = None
        for move in valid_moves:
            new_board, next_turn = play(turn, move, board.copy())
            #print(new_board, next_turn)
            eval_score, uslesess_var = minimax(new_board, depth - 1, next_turn, player)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        return min_eval, best_move


def decide_move(boardIn, playerTurnIn):
    useless_var, best_move = minimax(boardIn, depth=3, turn=playerTurnIn, player=playerTurnIn)
    #ff minimax didn't select a move chose the firstv alid move.
    if best_move is None:
        #if there are no best move found then find a valid move
        valid_moves = []
        if playerTurnIn == 1:
            for i in range(6):
                if boardIn[i] > 0:
                    valid_moves.append(i + 1)  #appenduj valid_moves
        else:
            for i in range(6):
                if boardIn[i + 7] > 0:
                    valid_moves.append(i + 1)
                    #prvi valid move or deafult to one

        #postavi best_move na prvi valid move ako postoji u valid_moves
        if len(valid_moves) > 0:
            #print(valid_moves[0])
            best_move = valid_moves[0]
        #otherwise postavi na 1
        else:
            best_move = 1
    return str(best_move), "minimax"

def play(playerTurn, playerMove, boardGame):
    # playerTurn ar 1 eller 2
    # playerMove ar 1..6
    # boardGame ar en 1x14 vektor
    if not correctPlay(playerMove, boardGame, playerTurn):
        print("Illegal move! break")
        return boardGame, 3 - playerTurn

    # Determine starting index based on player and move.
    idx = playerMove - 1 + (playerTurn - 1) * 7 #-1 for p1, +6 for p2
    # grab stones from hole
    numStones = boardGame[idx]
    boardGame[idx] = 0
    hand = numStones
    while hand > 0:
        # idx next hole
        idx = (idx + 1) % 14
        # Skip the opponent's store.
        if idx == 13 - 7 * (playerTurn - 1): #13 for p1, 6 for p2
            continue
        # add stone in hole,
        boardGame[idx] += 1
        hand -= 1

    # end in store? get another turn. otherwise other players turn
    nextTurn = 3 - playerTurn
    if idx == 6 + 7 * (playerTurn - 1):
        nextTurn = playerTurn

    #end on own empty hole? score stone and opposite hole
    if boardGame[idx] == 1 and idx in range((playerTurn - 1) * 7, 6 + (playerTurn - 1) * 7):
        boardGame[idx] -= 1  # Remove the stone.
        boardGame[6 + (playerTurn - 1) * 7] += 1  # Add to player's store.
        boardGame[6 + (playerTurn - 1) * 7] += boardGame[12 - idx]  # Capture opposite pit stones.
        boardGame[12 - idx] = 0
    return boardGame, nextTurn


def correctPlay(playerMove, board, playerTurn):
    correct = 0
    if playerMove in range(1, 7) and board[playerMove - 1 + (playerTurn - 1) * 7] > 0:
        correct = 1
    return correct

def receive(socket):
    msg = ''.encode()
    try:
        data = socket.recv(1024)
        msg += data
    except:
        pass
    return msg.decode()


def send(socket, msg):
    socket.sendall(msg.encode())


# Set the player name to your own: "Name_LastName"
playerName = 'Mirza_Sijamic'
host = '127.0.0.1'
port = 30000

s = socket.socket()
pool = ThreadPool(processes=1)
gameEnd = False
MAX_RESPONSE_TIME = 20

print('The player: ' + playerName + ' starts!')
s.connect((host, port))
print('The player: ' + playerName + ' connected!')

while not gameEnd:
    asyncRetult = pool.apply_async(receive, (s,))
    startTime = time.time()
    currentTime = 0
    received = 0
    data = []
    while received == 0 and currentTime < MAX_RESPONSE_TIME:
        time.sleep(0.01)
        if asyncRetult.ready():
            data = asyncRetult.get()
            received = 1
        currentTime = time.time() - startTime
    if received == 0:
        print('No response in ' + str(MAX_RESPONSE_TIME) + ' sec')
        gameEnd = True
    if data == 'N':
        send(s, playerName)
    if data == 'E':
        gameEnd = True
    if len(data) > 1:
        # Reconstruct the board: 14 numbers encoded as two digits each.
        board = [0] * 14
        playerTurn = int(data[0])
        i = 0
        j = 1
        while i <= 13:
            board[i] = int(data[j]) * 10 + int(data[j + 1])
            i += 1
            j += 2
        (move, botname) = decide_move(board, playerTurn)
        send(s, move)
print("Compiled?")