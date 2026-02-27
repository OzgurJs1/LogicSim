import pygame

class InputHandler:
    def __init__(self, toolbox_width):
        self.toolbox_width = toolbox_width

    def get_clicked_button(self, pos, buttons):
        """Returns which button was clicked."""
        for btn, label in buttons:
            if btn.collidepoint(pos):
                return label
        return None

    def get_pin_at_pos(self, pos, gates, switches):
        """Checks whether there is a pin (black dot) at the clicked coordinate."""
        # Output pins (Where the connection begins)
        for s in switches:
            if pygame.Vector2(s.rect.right, s.rect.centery).distance_to(pos) < 12:
                return s, "OUT", 0
        for g in gates:
            if pygame.Vector2(g.rect.right, g.rect.centery).distance_to(pos) < 12:
                return g, "OUT", 0
            
        # Input pins (Where the connection ends)
        for g in gates:
            for i in range(len(g.logic_gate.inputs)):
                pin_y = g.rect.y + (i + 1) * (g.rect.height / (len(g.logic_gate.inputs) + 1))
                if pygame.Vector2(g.rect.x, pin_y).distance_to(pos) < 12:
                    return g, "IN", i
        return None

    def check_object_click(self, pos, gates, switches):
        """Checks whether a gate or switch was clicked."""
        for s in switches:
            if s.rect.collidepoint(pos):
                return s, "switch"
        for g in gates:
            if g.rect.collidepoint(pos):
                return g, "gate"
        return None, None