
#ifndef PACMANUI
#define PACMANUI

#include <SFML/Graphics.hpp>
#include "../game/globals.h"
#include "../game/game.h"
#include "globalsUI.h"
#include "ghosts/agentUI.h"





class PacmanUI : public AgentUI {
    private:
        Direction pacmanDir;
        Direction nextDir;

    public:
        PacmanUI(GameState * gamestate);

        bool validPacmanMove(Direction dir);

        void move() override;

        // changes direction of pacman to specified dir
        void setNextDir(Direction dir);     

        // sets pacmanDir to nextDir
        void switchDirection();


        // returns row index of image to be used for pacman. 
        int getRowIndex();

        // increases frame by one or resets it.
        void nextFrame();


        void setOrientationForRendering() override;
        void setPositionForRendering() override;
};



#endif