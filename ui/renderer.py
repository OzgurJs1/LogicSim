import pygame

# Dark Mode Color Palette
BACKGROUND = (30, 30, 30)
WHITE = (220, 220, 220)
BLACK = (10, 10, 10)
BLUE = (0, 120, 215)
YELLOW = (255, 200, 0)
GREEN = (50, 200, 50)
GRAY = (70, 70, 70)
PANEL_DARK = (45, 45, 48)

class InputSwitch:
    def __init__(self, x, y, name):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.logic_gate = type('obj', (object,), {'output': False, 'name': name})()
        self.name = name
        self.dragging = False

    def toggle(self):
        self.logic_gate.output = not self.logic_gate.output

    def draw(self, screen):
        # Background of the switch
        color = GREEN if self.logic_gate.output else GRAY
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        pygame.draw.rect(screen, WHITE, self.rect, 1, border_radius=5) # Thin border
        
        # Output pin
        pygame.draw.circle(screen, BLACK, (self.rect.right, self.rect.centery), 7)
        
        # Label
        font = pygame.font.SysFont("Arial", 11, bold=True)
        label_surf = font.render(self.name, True, WHITE)
        screen.blit(label_surf, (self.rect.x, self.rect.y - 18))

class DraggableGate:
    def __init__(self, x, y, logic_gate):
        self.rect = pygame.Rect(x, y, 110, 50)
        self.logic_gate = logic_gate
        self.dragging = False

    def draw(self, screen):
        # Main gate body
        pygame.draw.rect(screen, BLUE, self.rect, border_radius=8)
        pygame.draw.rect(screen, WHITE, self.rect, 1, border_radius=8) # Professional border
        
        # Gate name
        font = pygame.font.SysFont("Arial", 12, bold=True)
        text = font.render(self.logic_gate.name, True, WHITE)
        screen.blit(text, (self.rect.x + 10, self.rect.y + 18))

        # Input pins (Left side)
        for i in range(len(self.logic_gate.inputs)):
            pin_y = self.rect.y + (i + 1) * (self.rect.height / (len(self.logic_gate.inputs) + 1))
            pygame.draw.circle(screen, BLACK, (self.rect.x, int(pin_y)), 7)
            if self.logic_gate.inputs[i]: 
                pygame.draw.circle(screen, YELLOW, (self.rect.x, int(pin_y)), 4)

        # Output pin (Right side)
        out_pin_y = self.rect.y + self.rect.height / 2
        pygame.draw.circle(screen, BLACK, (self.rect.right, int(out_pin_y)), 7)
        if self.logic_gate.output: 
            pygame.draw.circle(screen, YELLOW, (self.rect.right, int(out_pin_y)), 4)

class Renderer:
    def __init__(self, screen, toolbox_width):
        self.screen = screen
        self.toolbox_width = toolbox_width
        self.font = pygame.font.SysFont("Arial", 11, bold=True)

    def draw_toolbox(self, buttons):
        """Draws the professional dark-themed sidebar."""
        pygame.draw.rect(self.screen, PANEL_DARK, (0, 0, self.toolbox_width, self.screen.get_height()))
        pygame.draw.line(self.screen, GRAY, (self.toolbox_width, 0), (self.toolbox_width, self.screen.get_height()), 1)
        
        for btn, label in buttons:
            # Color logic for specialized buttons
            btn_color = (180, 40, 40) if "UNDO" in label else BLUE
            
            pygame.draw.rect(self.screen, btn_color, btn, border_radius=4)
            text_surf = self.font.render(label, True, WHITE)
            text_rect = text_surf.get_rect(center=btn.center)
            self.screen.blit(text_surf, text_rect)

    def draw_wires(self, wires, drawing_wire, wire_start_node, mouse_pos):
        """Cable visuals shining in a dark theme."""
        # Newly pulled cable (Not yet connected)
        if drawing_wire and wire_start_node:
            start_p = (wire_start_node.rect.right, wire_start_node.rect.centery)
            # It leaves a bright blue 'trace' as you drag it around
            pygame.draw.line(self.screen, (0, 191, 255), start_p, mouse_pos, 2)

        # Mevcut bağlantılar
        for w in wires:
            start_p = (w.start_gate.rect.right, w.start_gate.rect.centery)
            # Calculate the input pin position
            pin_spacing = w.end_gate.rect.height / (len(w.end_gate.logic_gate.inputs) + 1)
            end_y = w.end_gate.rect.y + (w.input_index + 1) * pin_spacing
            end_p = (w.end_gate.rect.x, int(end_y))
            
            # IF SIGNAL IS PRESENT: Bright Neon Yellow
            # NO SIGNAL: Dark Gray/White (Dim)
            if w.start_gate.logic_gate.output:
                # Main line (Yellow)
                pygame.draw.line(self.screen, (255, 255, 0), start_p, end_p, 3)
                # Slight shimmer effect (Optional: Thicker and more translucent line)
                pygame.draw.line(self.screen, (255, 255, 100), start_p, end_p, 1)
            else:
                pygame.draw.line(self.screen, (100, 100, 100), start_p, end_p, 2)

    def draw_objects(self, gates, switches):
        for s in switches: s.draw(self.screen)
        for g in gates: g.draw(self.screen)