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
    
    def __repr__(self) -> str:
        return f"{self.paddle},{self.paddleY},{self.ballX},{self.ballY},{self.lScore},{self.rScore},{self.sync},{self.move}"
    
    @classmethod
    def createWithString(cls, data: str) -> "Update":
        data = data.split(',')
        return Update(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

class GameState:
    def __init__(self) -> None:
        self.lPaddleY = 215
        self.rPaddleY = 215
        self.ballX = 320
        self.ballY = 240
        self.lscore = 0
        self.rscore = 0
        self.lmoving = ""
        self.rmoving = ""
        sync = 0
    
    def __repr__(self) -> str:
        return f"{self.lPaddleY},{self.rPaddleY},{self.ballX},{self.ballY},{self.lscore},{self.rscore},{self.lmoving},{self.rmoving},{self.sync}"
    
    @classmethod
    def createWithString(cls, data: str) -> "GameState":
        return Update(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

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
