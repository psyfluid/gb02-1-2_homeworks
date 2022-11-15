# Задача 1. Создайте программу для игры в "Крестики-нолики".

# pip3 install pyqt6

import itertools
import random

from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QMessageBox, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tick-tack-toe')
        self.setFixedSize(150, 150)

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.buttons = [[QPushButton() for _ in range(3)] for _ in range(3)]
        for i, j in itertools.product(range(3), range(3)):
            btn = self.buttons[i][j]
            btn.setObjectName(f'{i}{j}')
            btn.setFixedSize(50, 50)
            btn.setCheckable(True)
            btn.clicked.connect(self.toggle_field)
            layout.addWidget(btn, i, j)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self._set_theme()
        self._restart_game()

    @staticmethod
    def _default_buttons():
        return [(i, j) for i in range(3) for j in range(3)]

    def _restart_game(self):
        self.winner = ''
        self.available_buttons = self._default_buttons()
        for row in self.buttons:
            for btn in row:
                btn.setText('')
                btn.setChecked(False)
                btn.setDisabled(False)

        self.player_turn = random.choice((False, True))
        if not self.player_turn:
            self.bot_move()

    def toggle_field(self):
        btn = self.sender()
        i, j = tuple(map(int, btn.objectName()))
        btn.setText('x' if self.player_turn else 'o')
        btn.setStyleSheet(
            "QPushButton {"
            f"    color: {'green' if self.player_turn else 'red'}"
            "}"
        )
        btn.setDisabled(True)
        self.available_buttons.remove((i, j))

        self.check_win()
        if self.winner or not self.available_buttons:
            self.show_winner()
            self._restart_game()
            return

        self.player_turn = not self.player_turn
        if not self.player_turn:
            self.bot_move()

    def bot_move(self):
        i, j = random.choice(self.available_buttons)
        self.buttons[i][j].animateClick()

    def check_win(self):
        player_diag_1 = 0
        player_diag_2 = 0
        bot_diag_1 = 0
        bot_diag_2 = 0
        for i in range(3):
            player_win = 3 in (
                [btn.text() for btn in self.buttons[i]].count('x'),
                [row[i].text() for row in self.buttons].count('x')
            )
            bot_win = 3 in (
                [btn.text() for btn in self.buttons[i]].count('o'),
                [row[i].text() for row in self.buttons].count('o')
            )
            if player_win:
                self.winner = 'player'
                return
            elif bot_win:
                self.winner = 'bot'
                return

            if self.buttons[i][i].text() == 'x':
                player_diag_1 += 1
            elif self.buttons[i][i].text() == 'o':
                bot_diag_1 += 1

            if self.buttons[i][-1 - i].text() == 'x':
                player_diag_2 += 1
            elif self.buttons[i][-1 - i].text() == 'o':
                bot_diag_2 += 1

        if player_diag_1 == 3 or player_diag_2 == 3:
            self.winner = 'player'
        elif bot_diag_1 == 3 or bot_diag_2 == 3:
            self.winner = 'bot'

    def show_winner(self):
        if self.winner == 'player':
            winner_text = 'You win! \U0001F642'
        elif self.winner == 'bot':
            winner_text = 'You lose... \U0001F615'
        else:
            winner_text = 'Draw. \U0001F610'

        msg = QMessageBox()
        msg.setWindowTitle('Game Over')
        msg.setText(winner_text)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.buttonClicked.connect(msg.close)
        msg.exec()

    def _set_theme(self):
        self.setStyleSheet(
            "* {"
            "    font: 42px;"
            "    color: rgb(40, 40, 40);"
            "}"
            "QPushButton {"
            "    border-top: 1px solid;"
            "    border-left: 1px solid;"
            "    border-style: outset;"
            "    border-color: rgb(50, 50, 50);"
            "}"
            "QPushButton:pressed {"
            "    border-style: inset;"
            "}"
        )


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
