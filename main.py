#!/usr/bin/env python3
# ── Gorillas 3000 – main.py ────────────────────────────────────────────────────

import sys
import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from core.game import new_game, GameState
from ui.renderer import Renderer
from ui.input_handler import InputHandler


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    renderer = Renderer(screen)
    handler  = InputHandler()
    session  = new_game()

    while True:
        # ── Events / Input ─────────────────────────────────────────────────────
        handler.process_events()
        inp = handler.state

        if inp.quit_requested:
            break

        if inp.restart_requested:
            session.restart()
            handler.state.angle = 45.0
            handler.state.speed = 50.0

        # ── Spiellogik ─────────────────────────────────────────────────────────
        if session.state == GameState.INPUT and inp.throw_requested:
            session.throw(angle=inp.angle, speed=inp.speed)

        if session.state == GameState.ANIMATING:
            session.tick()
            # Explosion bei Treffer
            if session.state == GameState.GAME_OVER and session.projectile:
                renderer.add_explosion(session.projectile.x, session.projectile.y)

        # ── Zeichnen ───────────────────────────────────────────────────────────
        renderer.draw(session, handler.as_dict())
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
