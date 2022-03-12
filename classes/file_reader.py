from constants import *


class Reader:
    def __init__(self):
        score_file = open(BEST_SCORE_FILE_PATH, 'r')
        self.best_score = score_file.read()
        score_file.close()

    def update_best_score(self, new_best_score):
        score_file = open(BEST_SCORE_FILE_PATH, 'w')
        score_file.write(new_best_score)
        score_file.close()