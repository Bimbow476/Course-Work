#include "game.h"
#include <stdexcept>

NimGame::NimGame(int piles, int max_removal) 
    : current_player(0), max_removal(max_removal), winner(-1) {
    this->piles.resize(piles, 5); 
}

void NimGame::make_move(int pile, int stones) {
    if (!is_valid_move(pile, stones)) {
        throw std::invalid_argument("Неприпустимий хід");
    }

    piles[pile] -= stones;

    if (is_game_over()) {
        winner = current_player;
    } else {
        current_player = 1 - current_player; 
    }
}

bool NimGame::is_game_over() const {
    for (int pile : piles) {
        if (pile > 0) return false;
    }
    return true;
}

int NimGame::get_winner() const {
    return winner;
}

std::vector<int> NimGame::get_piles() const {
    return piles;
}

bool NimGame::is_valid_move(int pile, int stones) const {
    return pile >= 0 && pile < piles.size() && stones > 0 && stones <= piles[pile] && stones <= max_removal;
}
