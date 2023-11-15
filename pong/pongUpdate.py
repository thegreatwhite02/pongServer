class Update:
    def __init__(self, paddleY: int, ballX: int, ballY: int, lScore: int, rScore: int, sync: int) -> None:
        self.paddleY = paddleY
        self.ballX = ballX
        self.ballY = ballY
        self.lScore = lScore
        self.rScore = rScore
        self.sync = sync