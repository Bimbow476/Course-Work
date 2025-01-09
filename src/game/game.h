#ifndef GAME_H
#define GAME_H

#include <vector>

class NimGame {
public:
    NimGame(int piles, int max_removal);
    void make_move(int pile, int stones);
    bool is_game_over() const;
    int get_winner() const;
    std::vector<int> get_piles() const;

private:
    std::vector<int> piles;
    int current_player;
    int max_removal;
    int winner;

    bool is_valid_move(int pile, int stones) const;
};

#endif // GAME_H
    