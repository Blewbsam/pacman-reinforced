
#pragma once

#include "../../game/game.hpp"
#include <SFML/Graphics.hpp>
#include "../../game/globals.hpp"
#include "agentUI.hpp"
#include "../globalsUI.hpp"

class GhostUI : public AgentUI {
    protected:
        GhostType ghostType;
        sf::Sprite * face;
        sf::Color defaultColor;
    public:
        GhostUI(GameState * gameState, sf::Vector2f pos, sf::Color defaultColor, GhostType type);
        
        sf::Sprite getFace();
        
        // Specifications similar to pacmanUI
        virtual void move() override;

        // moves Ghost to dir by set_size
        void move(Direction dir,double step_size);

        // gets speed of ghost given type and speed
        double getGhostSpeed(GhostType type, GhostState state);

        void setOrientationForRendering() override;

        void render(GhostState state, Direction ghostDir);
        void setBodyColorForRendering(GhostState state);
        void setFacePositionForRendering();
        void setFaceOrientationForRendering(GhostState state, Direction ghostDir);


        void nextFrame();
        int getRowIndex(Direction ghostDir);
};




#define AMBUSHER_START_X PIXEL_SIZE * 10
#define AMBUSHER_START_Y PIXEL_SIZE * 9

class AmbusherUI : public GhostUI {
    public:
    AmbusherUI(GameState * gameState);
};


#define CHASER_START_X PIXEL_SIZE * 9
#define CHASER_START_Y PIXEL_SIZE * 7

class ChaserUI : public GhostUI{    
public:
    ChaserUI(GameState * gameState);
};

#define FICKLE_START_X PIXEL_SIZE * 9
#define FICKLE_START_Y PIXEL_SIZE * 9

class FickleUI : public GhostUI{    
    public:
    FickleUI(GameState * gameState);
};

#define STUPID_START_X PIXEL_SIZE * 11
#define STUPID_START_Y PIXEL_SIZE * 9

class StupidUI : public GhostUI{    
    public:
    StupidUI(GameState * gameState);
};




