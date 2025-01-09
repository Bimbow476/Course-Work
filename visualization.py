import tkinter as tk

def visualize_game(state, root, gui):
    """
    Візуалізація стану гри у вигляді сірників.
    """
    root.configure(bg="#4CAF50")


    for widget in root.winfo_children():
        widget.destroy()

    # Рахунок гравців
    score_frame = tk.Frame(root, bg="#4CAF50")
    score_frame.pack(pady=10)

    tk.Label(
        score_frame, text=f"{gui.player1_name}: {gui.current_player == 1}",
        font=("Arial", 14), bg="#4CAF50", fg="white"
    ).pack(side="left", padx=10)

    tk.Label(
        score_frame, text=f"{gui.player2_name}: {gui.current_player == 2}",
        font=("Arial", 14), bg="#4CAF50", fg="white"
    ).pack(side="left", padx=10)

    # Відображення сірників для кожної купи
    match_frame = tk.Frame(root, bg="#4CAF50")
    match_frame.pack(pady=20)

    for i, pile in enumerate(state):
        pile_frame = tk.Frame(match_frame, bg="#4CAF50")
        pile_frame.pack(pady=5)

        tk.Label(
            pile_frame, text=f"Купа {i + 1}:", font=("Arial", 14), bg="#4CAF50", fg="white"
        ).pack(side="left", padx=10)

        matches = " | " * pile
        match_label = tk.Label(
            pile_frame, text=matches, font=("Arial", 14), fg="#0178d6", bg="#4CAF50"
        )
        match_label.pack(side="left", padx=10)

        entry = tk.Entry(pile_frame, width=5, font=("Arial", 14), bg="#81C784", fg="black")
        entry.pack(side="left", padx=5)

        move_button = tk.Button(
            pile_frame, text="Видалити", font=("Arial", 12),
            bg="#2E7D32", fg="white", activebackground="#1B5E20", activeforeground="white",
            command=lambda p=i, e=entry: gui.make_move(p, int(e.get()) if e.get().isdigit() else 0)
        )
        move_button.pack(side="left", padx=10)


    log_frame = tk.Frame(root, bg="#4CAF50")
    log_frame.pack(pady=10, fill="both")

    tk.Label(log_frame, text="Журнал ходів:", font=("Arial", 16), bg="#4CAF50", fg="white").pack(anchor="w", padx=10)
    log_text = tk.Text(log_frame, height=8, font=("Arial", 12), bg="#81C784", fg="black", state="normal")
    log_text.pack(fill="both", padx=10, pady=5)
    log_text.insert("1.0", "\n".join(gui.move_log))
    log_text.config(state="disabled")


    undo_button = tk.Button(
        root, text="Скасувати хід", font=("Arial", 16),
        bg="#2E7D32", fg="white", activebackground="#1B5E20", activeforeground="white",
        command=gui.undo_move
    )
    undo_button.pack(pady=10)


    menu_button = tk.Button(
        root, text="Головне меню", font=("Arial", 16),
        bg="#2E7D32", fg="white", activebackground="#1B5E20", activeforeground="white",
        command=gui.show_main_menu
    )
    menu_button.pack(pady=10)
