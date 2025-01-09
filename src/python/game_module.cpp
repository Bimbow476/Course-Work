#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "game.h"

namespace py = pybind11;

PYBIND11_MODULE(game_module, m) {
    py::class_<NimGame>(m, "NimGame")
        .def(py::init<int, int>(), py::arg("piles"), py::arg("max_removal"))  
        .def("make_move", &NimGame::make_move, py::arg("pile"), py::arg("stones")) 
        .def("is_game_over", &NimGame::is_game_over) 
        .def("get_winner", &NimGame::get_winner) 
        .def("get_piles", &NimGame::get_piles) 
        ;
}
