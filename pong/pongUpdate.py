class Update:
    def __init__(self, paddle: str, paddleY: int, ballX: int, ballY: int, lScore: int, rScore: int, sync: int, move: str) -> None:
        self.paddle = paddle
        self.paddleY = paddleY
        self.ballX = ballX
        self.ballY = ballY
        self.lScore = lScore
        self.rScore = rScore
        self.sync = sync
        self.move = move

class GameState:
    def __init__(self):
        self.lPaddleY = 215
        self.rPaddleY = 215
        self.ballX = 320
        self.ballY = 240
        self.lscore = 0
        self.rscore = 0
        self.lmoving = ""
        self.rmoving = ""
        sync = 0

def updateGameState(currGameState: GameState, update: Update) -> GameState:
    # if first packet to get there
    if update.sync == currGameState.sync + 1:
        if update.paddle == "left":
            currGameState.lPaddleY = update.paddleY
            currGameState.lmoving = update.move
        else:
            currGameState.rPaddleY = update.paddleY
            currGameState.rmoving = update.move
        currGameState.lscore = update.lScore
        currGameState.rscore = update.rScore
        currGameState.ballX = update.ballX
        currGameState.ballY = update.ballY
        currGameState.sync = update.sync
    # if last to get there
    if update.sync == currGameState.sync:
        # only update paddle info
        if update.paddle == "left":
            currGameState.lPaddleY = update.paddleY
            currGameState.lmoving = update.move
        else:
            currGameState.rPaddleY = update.paddleY
            currGameState.rmoving = update.move
