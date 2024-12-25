#ifndef MAZE_H
#define MAZE_H

#include <vector>
#include <map>
#include "globals.h"

// Define or include CellType


typedef std::vector<std::vector<Cell>> grid_t;

class Maze {
    private:
        // Direct Representation of game state. 
        grid_t grid;
    public:
        // Constructor with grid to be used for game state
        Maze(const std::vector<std::string>& layout);

        grid_t getGrid() const;
        int getGridWidth() const;
        int getGridHeight() const;
        
        std::vector<Position> getValidPositions(Position pos);
        Cell getCell(Position pos) const; 
        void setCell(Position pos, Cell type); 
        void printGrid();

};

#endif
