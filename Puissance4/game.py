import pygame
from button import Button
import math
class Menu_Puissance4:
    def __init__(self, screen, font, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = screen
        self.title = font.render("Puissance 4", True, "white")
        self.diagonale = math.hypot(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.game = Puissance4(screen)
        self.font = font
        button_quit = Button(screen, SCREEN_WIDTH - SCREEN_WIDTH / 5, 0, SCREEN_WIDTH / 5, SCREEN_HEIGHT / 15, "white", "Quitter", (0, 0, 0))
        self.buttons = [*[Button(self.game.board_surface,j*(self.screen.get_width()/10)+self.screen.get_width()/2-SCREEN_WIDTH/3+SCREEN_WIDTH/30, i*(SCREEN_HEIGHT/7)+self.screen.get_height()/8, SCREEN_WIDTH / 20, SCREEN_WIDTH / 20,(0,0,0,0),shape = "circle",radius=self.diagonale/35,action=str(j)) for i in range(6) for j in range(7)],button_quit]
        self.button_restart = Button(screen, SCREEN_WIDTH / 2 - SCREEN_WIDTH / 10, SCREEN_HEIGHT * 0.9, SCREEN_WIDTH / 5, SCREEN_HEIGHT / 15, "white", "Recommencer", (0, 0, 0))
        self.menu = "self"
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.title, (self.screen.get_width() / 2 - self.title.get_width() / 2, 0))
        pygame.draw.rect(self.screen, (255,255,255), (self.screen.get_width() / 2-self.screen.get_width()/3, self.screen.get_height()/15, self.screen.get_width()/1.5, self.screen.get_height()/1.2))

        for button in self.game.Button: #Change color of the buttons that have fallen
            self.buttons[button[0]].color = button[1]
            self.game.Button.remove(button)

        
        if self.clock.get_time() < 1000: # Wait for 1 second before starting the animation
            self.game.animate_drop()
            self.clock = pygame.time.Clock()

        
        self.game.create_grid() # Draw the grid
        for button in self.buttons: # Draw the buttons
            button.draw()
        self.screen.blit(self.game.board_surface, (0, 0))
        if self.game.winner is not None and self.game.buttons_drop == []:
            winner_text = self.font.render(f"Player {self.game.winner} wins!", True, "white")
            self.screen.blit(winner_text, (0,0))
            self.button_restart.draw()
        self.preview() # Preview the buttons
        for event in pygame.event.get():
            self.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    def preview(self):
        if self.game.buttons_drop == []: # Only show the preview if no pieces are falling
            for button in self.buttons:
                if button.shape == "circle" and button.is_clicked(pygame.mouse.get_pos()):
                    for i in range(5,-1,-1):
                        if self.game.grid[i][int(button.action())] == 0:
                            color = "yellow" if self.game.current_player == 1 else "red"
                            pygame.draw.circle(self.screen, color, (button.player_pos.x, self.buttons[int(button.action())+i*7].player_pos.y ), button.radius)
                            
                            break
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in self.buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        action = button.action()
                        if action == "Quitter":
                            self.menu = "main"
                        if action.isdigit():
                            self.game.drop_piece(int(action))
                            #if play is not False:
                             #   self.buttons[play*7+int(action)].color = "red" if self.game.current_player == 1 else "yellow"

                        else:
                            print(f"Player {self.game.current_player}'s turn")
                        # Here you can add code to update the display or switch to another menu
                if self.game.winner is not None:
                    if self.button_restart.is_clicked(pygame.mouse.get_pos()):
                        self.game.reset_game()
                        for button in self.buttons:
                            button.color = (0,0,0,0) # Reset the color of the buttons to transparent
                        self.buttons[-1].color = "white" # Reset the color of the quit button to white
        return None
class Puissance4:
    def __init__(self,screen):
        self.screen = screen
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.winner = None
        self.buttons_drop = []  # List to store the buttons for dropping pieces
        self.Button = [] #Buttons that has Fallen
        self.diagonale = math.hypot(self.screen.get_width(),self.screen.get_height())
        self.board_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()),pygame.SRCALPHA)
        pygame.draw.rect(self.board_surface, (0, 0, 255), (self.screen.get_width() / 2-self.screen.get_width()/3, self.screen.get_height()/15, self.screen.get_width()/1.5, self.screen.get_height()/1.2))
        for i in range(6):
            for j in range(7):
                cx = j*(self.screen.get_width()/10) + self.screen.get_width()/2 - self.screen.get_width()/3 + self.screen.get_width()/30
                cy = i*(self.screen.get_height()/7) + self.screen.get_height()/8
                pygame.draw.circle(
                    self.board_surface ,
                    (0,0,0,0),         # entièrement transparent
                    (int(cx), int(cy)),
                    int(self.diagonale/35)
                )
    def create_grid(self):
        pygame.draw.rect(self.board_surface, (0, 0, 255), (self.screen.get_width() / 2-self.screen.get_width()/3, self.screen.get_height()/15, self.screen.get_width()/1.5, self.screen.get_height()/1.2))
        for i in range(6):
            for j in range(7):
                cx = j*(self.screen.get_width()/10) + self.screen.get_width()/2 - self.screen.get_width()/3 + self.screen.get_width()/30
                cy = i*(self.screen.get_height()/7) + self.screen.get_height()/8
                pygame.draw.circle(
                    self.board_surface ,
                    (0,0,0,0),         # entièrement transparent
                    (int(cx), int(cy)),
                    int(self.diagonale/35)
                )

    def drop_piece(self, column):
        if self.winner is not None or self.buttons_drop != []:
            return False
        for row in range(5, -1, -1):
            if self.grid[row][column] == 0:
                self.grid[row][column] = self.current_player
                self.buttons_drop.append([self.screen.get_height()/8,column*(self.screen.get_width()/10)+self.screen.get_width()/2-self.screen.get_width()/3+self.screen.get_width()/30,"yellow" if self.current_player == 1 else "red",row,column])
                if self.check_winner(row, column):
                    self.winner = self.current_player
                self.current_player = 3 - self.current_player  # Switch player
                return row
        return False
    
    def animate_drop(self):
        # Animation logic for dropping the piece
        for button in self.buttons_drop:
            button[0] += 1
            pygame.draw.circle(self.screen,button[2], (button[1], button[0]), self.diagonale/35)
            if button[0] >= button[3]*(self.screen.get_height()/7)+self.screen.get_height()/8:
                # Remove the button from the list if it has reached its final position
                self.Button.append([button[3]*7+button[4],button[2]])
                self.buttons_drop.remove(button)
        
    def check_winner(self, row, column):
        # Check horizontal, vertical and diagonal directions for a win
        return (self.check_direction(row, column, 1, 0) or  # Horizontal
                self.check_direction(row, column, 0, 1) or  # Vertical
                self.check_direction(row, column, 1, 1) or  # Diagonal /
                self.check_direction(row, column, 1, -1)) # Diagonal \

    def check_direction(self, row, column, delta_row, delta_col):
        count = 0
        for i in range(2):
            for j in range(1, 4):
                if 0 <= row + delta_row*j <6 and 0<= column + delta_col*j <=6 and self.grid[row + delta_row * j][column + delta_col * j] == self.current_player:
                    count += 1
                else:
                    delta_row = -delta_row
                    delta_col = -delta_col
                    break
                if count == 3:
                    return True
        return False

    def reset_game(self):
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.winner = None
        