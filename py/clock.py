import pygame
import time

class Clock:
    def __init__(self, profile: int, turbo: bool, fps: bool):
        self.cycle = 0
        self.frame = 0
        self.profile = profile
        self.turbo = turbo
        self.fps = fps
        self.pyclock = pygame.time.Clock()
        self.last_report = time.time()

    def tick(self) -> bool:
        if self.cycle > 70224:
            self.cycle = 0

            # Sleep if we have time left over
            if not self.turbo:
                self.pyclock.tick(60)

            # Print FPS once per frame
            if self.fps and self.frame % 60 == 0:
                t = time.time()
                fps = 60/(t - self.last_report)
                print(f"{fps:.1f}fps")
                self.last_report = t

            # Exit if we've hit the frame limit
            if self.profile != 0 and self.frame > self.profile:
                return False

            self.frame += 1
        self.cycle += 1
        return True

