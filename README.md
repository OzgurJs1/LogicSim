# ⚡ Logic Flow Simulator - 2026

A modular, interactive digital logic circuit simulator built with Python and Pygame. This project enables users to design complex digital circuits using drag-and-drop mechanics with real-time signal propagation.



## 🚀 Key Features

* **Modular Architecture:** Implements a strict separation of concerns between **Logic Engine**, **UI Renderer**, and **Input Handling** layers (Clean Code principles).
* **Professional Dark Mode:** High-contrast, engineering-grade interface designed for modern software environments.
* **Dynamic Wiring System:** Interactive connections that change color (Neon Yellow/Gray) based on the real-time signal state.
* **Full Gate Support:** Includes support for AND, OR, NOT, XOR, and NAND logic gates.
* **Keyboard Shortcuts:** Full `Ctrl + Z` (Undo) support to revert the most recent actions instantly.
* **Real-Time Simulation:** Instant logic calculations; toggle a switch and watch the energy propagate through the entire circuit.

## 🛠️ Technical Specifications

* **Language:** Python 3.x
* **Library:** Pygame
* **Design Pattern:** Object-Oriented Programming (OOP) utilizing Polymorphism for gate logic.
* **Backend Logic:** Stack-based history management for undo operations.
* **Architecture:** Decoupled system design for high maintainability and scalability.
* **Language:** Python 3.x
* **Library:** Pygame-ce
* **Design Pattern:** Object-Oriented Programming (OOP) utilizing Polymorphism for gate logic.
* **Backend Logic:** Stack-based history management for undo operations.

## ⚙️ Installation & Setup

* **Clone The Repository:** [https://github.com/OzgurJs1/LogicSim.git](https://github.com/OzgurJs1/LogicSim.git)
* **Create and Activate Virtual Environment:** python -m venv venv -> **On Windows:** .\venv\Scripts\activate  **On macOS/Linux:** source venv/bin/activate
* **Install Dependencies:** pip install -r requirements.txt
* **Run the Application:** python main.py

## How To Use

* **Add Components:** Use the sidebar buttons to spawn gates (AND, OR, NOT, XOR, NAND) or input switches.
* **Move:** Drag and drop components to organize your workspace.
* **Wire:** Click and drag from an output pin (right side) to an input pin (left side) to establish a connection.
* **Interact:** Click on any SW (Switch) to toggle its state. Neon yellow wires represent an active (True) signal.
* **Undo:** Use the UNDO button or press Ctrl + Z to remove the last action.

## 📁 Project Structure

### Developed by Özgür Ay Computer Programmer

```text
LogicSim/
├── core/
│   ├── engine.py        # Signal transmission and wiring logic
│   └── gates.py         # Definitions of Logic Gates (AND, OR, etc.)
├── ui/
│   ├── input_handler.py # Event management for mouse and keyboard
│   └── renderer.py      # Drawing engine and Dark Mode visual effects
├── main.py              # Application entry point
└── requirements.txt
└── README.md
