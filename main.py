import pygame
import math

class Main:

    def __init__(self):
        self.m1 = 3
        self.m2 = 2
        self.l1 = 250
        self.l2 = 200
        self.v1 = 0
        self.v2 = 0
        self.g = 9.81
        self.rub = 0.997
        self.time_step = 0.10
        self.theta1 = math.pi / 2
        self.theta2 = math.pi / 2
        self.display_w = 960
        self.display_h = 480
        self.x0 = self.display_w // 2
        self.y0 = 0
        self.color_thread = (255, 0, 0)
        self.color_ball = (0, 255, 0)
        self.width_thread = 2

        
    def frame(self, display, dt):
        display.fill((0, 0, 0))
        
        z1 = -self.g * (2 * self.m1 + self.m2) * math.sin(self.theta1)
        z2 = -self.m2 * self.g * math.sin(self.theta1 - 2 * self.theta2)
        z3 = -2 * math.sin(self.theta1 - self.theta2) * self.m2
        z4 = self.v2**2 * self.l2 + self.v1**2 * self.l1 * math.cos(self.theta1 - self.theta2)
        z5 = self.l1 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.theta1 - 2 * self.theta2))
        acc1 = (z1 + z2 + z3 * z4) / z5
        z1 = 2 * math.sin(self.theta1 - self.theta2);
        z2 = self.v1**2 * self.l1 * (self.m1 + self.m2);
        z3 = self.g * (self.m1 + self.m2) * math.cos(self.theta1);
        z4 = self.v2**2 * self.l2 * self.m2 * math.cos(self.theta1 - self.theta2);
        z5 = self.l2 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.theta1 - 2 * self.theta2));
        acc2 = (z1 * (z2 + z3 + z4)) / z5

        acc1 *= self.time_step
        acc2 *= self.time_step

        self.v1 += acc1
        self.v2 += acc2
        self.v1 *= self.rub
        self.v2 *= self.rub

        self.theta1 += self.v1
        self.theta2 += self.v2

        self.x1 = self.x0 + self.l1 * math.sin(self.theta1)
        self.y1 = self.y0 + self.l1 * math.cos(self.theta1)
        self.x2 = self.x1 + self.l2 * math.sin(self.theta2)
        self.y2 = self.y1 + self.l2 * math.cos(self.theta2)

        p0 = (int(self.x0), int(self.y0))
        p1 = (int(self.x1), int(self.y1))
        p2 = (int(self.x2), int(self.y2))

        l1 = math.sqrt(self.m1 / math.pi)
        l2 = math.sqrt(self.m2 / math.pi)

        pygame.draw.line(display, self.color_thread, p0, p1, self.width_thread)
        pygame.draw.line(display, self.color_thread, p1, p2, self.width_thread)
        pygame.draw.circle(display, self.color_ball, p1, int(l1 * 20));
        pygame.draw.circle(display, self.color_ball, p2, int(l2 * 20));

    def run(self):
        pygame.init()      

        display = pygame.display.set_mode((self.display_w, self.display_h))

        cl = pygame.time.Clock()

        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break               

            dt = cl.tick(60) 

            self.frame(display, dt)
            pygame.display.flip()

        pygame.quit()



if __name__ == '__main__':
    main = Main()
    main.run()
