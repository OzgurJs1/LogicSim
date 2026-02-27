import pygame
from core.gates import AndGate, OrGate, NotGate, XorGate, NandGate
from core.engine import Wire
from ui.renderer import Renderer, DraggableGate, InputSwitch 
from ui.input_handler import InputHandler

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Logic Flow Simulator - Ozgur Ay Edition")
    
    renderer = Renderer(screen, 130)
    handler = InputHandler(130)
    
    BACKGROUND_COLOR = (30, 30, 30)
    
    ui_buttons = [
        (pygame.Rect(15, 40, 100, 30), "ADD AND"),
        (pygame.Rect(15, 80, 100, 30), "ADD OR"),
        (pygame.Rect(15, 120, 100, 30), "ADD NOT"),
        (pygame.Rect(15, 160, 100, 30), "ADD XOR"),
        (pygame.Rect(15, 200, 100, 30), "ADD NAND"),
        (pygame.Rect(15, 240, 100, 30), "ADD SW"),
        (pygame.Rect(15, 300, 100, 35), "UNDO")
    ]

    gates, switches, wires, history = [], [], [], []
    active_obj, drawing_wire, wire_start_node = None, False, None

    # Undo Fonksiyonu (DRY Prensiplerine Uygun - Backend Disiplini)
    def perform_undo():
        if history:
            last_action = history.pop()
            action_type, obj = last_action
            if action_type == "gate" and obj in gates: gates.remove(obj)
            elif action_type == "switch" and obj in switches: switches.remove(obj)
            elif action_type == "wire" and obj in wires: wires.remove(obj)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- KEYBOARD CONTROL (Ctrl + Z) ---
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    perform_undo()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                btn_label = handler.get_clicked_button(event.pos, ui_buttons)
                
                if btn_label == "ADD AND":
                    new_gate = DraggableGate(200, 100, AndGate(f"AND_{len(gates)+1}"))
                    gates.append(new_gate); history.append(("gate", new_gate))
                
                elif btn_label == "ADD OR":
                    new_gate = DraggableGate(200, 150, OrGate(f"OR_{len(gates)+1}"))
                    gates.append(new_gate); history.append(("gate", new_gate))

                elif btn_label == "ADD NOT":
                    new_gate = DraggableGate(200, 200, NotGate(f"NOT_{len(gates)+1}"))
                    gates.append(new_gate); history.append(("gate", new_gate))

                elif btn_label == "ADD XOR":
                    new_gate = DraggableGate(200, 250, XorGate(f"XOR_{len(gates)+1}"))
                    gates.append(new_gate); history.append(("gate", new_gate))

                elif btn_label == "ADD NAND":
                    new_gate = DraggableGate(200, 300, NandGate(f"NAND_{len(gates)+1}"))
                    gates.append(new_gate); history.append(("gate", new_gate))

                elif btn_label == "ADD SW":
                    new_sw = InputSwitch(200, 350, f"SW_{len(switches)+1}")
                    switches.append(new_sw); history.append(("switch", new_sw))

                elif btn_label == "UNDO":
                    perform_undo()
                
                else:
                    pin_data = handler.get_pin_at_pos(event.pos, gates, switches)
                    if pin_data and pin_data[1] == "OUT":
                        drawing_wire, wire_start_node = True, pin_data[0]
                    else:
                        obj, obj_type = handler.check_object_click(event.pos, gates, switches)
                        if obj:
                            if obj_type == "switch": obj.toggle()
                            active_obj, obj.dragging = obj, True

            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing_wire:
                    pin_data = handler.get_pin_at_pos(event.pos, gates, switches)
                    if pin_data and pin_data[1] == "IN":
                        new_wire = Wire(wire_start_node, pin_data[0], pin_data[2])
                        wires.append(new_wire); history.append(("wire", new_wire))
                drawing_wire = False
                if active_obj: active_obj.dragging = False
                active_obj = None

            elif event.type == pygame.MOUSEMOTION:
                if active_obj and active_obj.dragging:
                    active_obj.rect.x = max(140, active_obj.rect.x + event.rel[0])
                    active_obj.rect.y += event.rel[1]

        # --- SIMULATION AND DRAWING ---
        for w in wires: w.transmit()
        for g in gates: g.logic_gate.update()

        screen.fill(BACKGROUND_COLOR)
        renderer.draw_toolbox(ui_buttons)
        renderer.draw_wires(wires, drawing_wire, wire_start_node, mouse_pos)
        renderer.draw_objects(gates, switches)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()