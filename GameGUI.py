import tkinter as tk
from visualization import visualize_game
import random


class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Гра Nim")
        self.root.geometry("800x600")

        self.bg_color = "#4CAF50"
        self.button_color = "#2E7D32"
        self.button_active_color = "#1B5E20"
        self.text_color = "white"

        self.root.configure(bg=self.bg_color)

        self.player1_name = ""
        self.player2_name = ""
        self.is_bot = False

        self.state = [5, 5, 5, 5]
        self.current_player = 1
        self.current_frame = None

        self.move_log = []
        self.previous_states = []

    def start_game(self):
        self.show_main_menu()
        self.root.mainloop()

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill="both", expand=True)

        title = tk.Label(
            self.current_frame, text="Гра Nim", font=("Arial", 24),
            bg=self.bg_color, fg=self.text_color
        )
        title.pack(pady=20)

        play_button = tk.Button(
            self.current_frame, text="Грати", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=self.show_player_selection
        )
        play_button.pack(pady=10)

        rules_button = tk.Button(
            self.current_frame, text="Правила", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=self.show_rules
        )
        rules_button.pack(pady=10)

        exit_button = tk.Button(
            self.current_frame, text="Вийти", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=self.root.destroy
        )
        exit_button.pack(pady=10)

    def show_rules(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill="both", expand=True)

        rules = (
            "Правила гри Nim:\n"
            "1. У грі є кілька куп сірників.\n"
            "2. Кожен гравець по черзі видаляє будь-яку кількість сірників з однієї купи.\n"
            "3. Можна видалити від 1 до максимального числа сірників у купі.\n"
            "4. Гравець, який не може зробити хід, програє."
        )

        tk.Label(
            self.current_frame, text="Правила гри", font=("Arial", 20),
            bg=self.bg_color, fg=self.text_color
        ).pack(pady=20)

        tk.Label(
            self.current_frame, text=rules, font=("Arial", 14),
            bg=self.bg_color, fg=self.text_color, justify="left"
        ).pack(pady=10)

        back_button = tk.Button(
            self.current_frame, text="Назад", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=self.show_main_menu
        )
        back_button.pack(pady=20)

    def show_player_selection(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill="both", expand=True)

        title = tk.Label(
            self.current_frame, text="Введіть імена гравців", font=("Arial", 20),
            bg=self.bg_color, fg=self.text_color
        )
        title.pack(pady=20)

        tk.Label(self.current_frame, text="Гравець 1:", bg=self.bg_color, fg=self.text_color).pack(pady=5)
        player1_entry = tk.Entry(self.current_frame, bg="#81C784", fg="black")
        player1_entry.pack(pady=5)

        tk.Label(self.current_frame, text="Гравець 2:", bg=self.bg_color, fg=self.text_color).pack(pady=5)
        player2_entry = tk.Entry(self.current_frame, bg="#81C784", fg="black")
        player2_entry.pack(pady=5)

        is_bot_var = tk.BooleanVar()
        bot_checkbox = tk.Checkbutton(
            self.current_frame, text="Другий гравець - бот", variable=is_bot_var,
            bg=self.bg_color, fg=self.text_color, selectcolor=self.bg_color
        )
        bot_checkbox.pack(pady=10)

        play_button = tk.Button(
            self.current_frame, text="Грати", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=lambda: self.start_nim_game(player1_entry.get(), player2_entry.get(), is_bot_var.get())
        )
        play_button.pack(pady=20)

        # Кнопка "Назад"
        back_button = tk.Button(
            self.current_frame, text="Назад", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=self.show_main_menu
        )
        back_button.pack(pady=10)

    def start_nim_game(self, player1_name, player2_name, is_bot):
        self.player1_name = player1_name or "Гравець 1"
        self.player2_name = player2_name or "Гравець 2"
        self.is_bot = is_bot
        self.state = [5, 5, 5, 5]
        self.current_player = random.choice([1, 2])  # Випадковий вибір першого гравця
        self.move_log = []
        self.previous_states = []
        self.show_game_window()

    def show_game_window(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill="both", expand=True)

        visualize_game(self.state, self.current_frame, self)

    def make_move(self, pile, stones):
        if 0 <= pile < len(self.state) and 1 <= stones <= self.state[pile]:
            self.previous_states.append((self.state[:], self.current_player))
            self.state[pile] -= stones

            self.move_log.append(f"Гравець {self.current_player}: {stones} з купи {pile + 1}")

            if all(p == 0 for p in self.state):
                self.show_winner()
                return

            self.current_player = 2 if self.current_player == 1 else 1

            if self.is_bot and self.current_player == 2:
                self.bot_move()
            else:
                self.show_game_window()

    def undo_move(self):
        if self.previous_states:
            self.state, self.current_player = self.previous_states.pop()
            self.move_log.pop()
            self.show_game_window()

    def bot_move(self):
        non_empty_piles = [i for i, p in enumerate(self.state) if p > 0]
        if non_empty_piles:
            pile = random.choice(non_empty_piles)
            stones = random.randint(1, self.state[pile])
            self.make_move(pile, stones)

    def show_winner(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root, bg=self.bg_color)
        self.current_frame.pack(fill="both", expand=True)

        winner = self.player1_name if self.current_player == 1 else self.player2_name
        tk.Label(
            self.current_frame, text=f"Переможець: {winner}!", font=("Arial", 24),
            bg=self.bg_color, fg=self.text_color
        ).pack(pady=20)

        back_button = tk.Button(
            self.current_frame, text="Назад до меню", font=("Arial", 16),
            bg=self.button_color, fg=self.text_color,
            activebackground=self.button_active_color, activeforeground=self.text_color,
            command=self.show_main_menu
        )
        back_button.pack(pady=10)


if __name__ == "__main__":
    game = GameGUI()
    game.start_game()
