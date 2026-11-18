# Library Dual-User Concurrency Simulator

An interactive real-time concurrency and mutex synchronization dashboard demonstrating multi-threaded race conditions vs. thread-safe execution in a library book lending system.

## 🚀 Live Demo
Access the live interactive web dashboard here:
- **Live URL**: https://mothiwarsriharshgoud-dev.github.io/library-concurrency-dashboard/

## 📚 Overview
The application simulates a library catalog where two concurrent users (**User 1 — Alice** and **User 2 — Bob**) search, select, and attempt to borrow books simultaneously.

### Key Features
- **Split-Screen Dual Terminals**: Separate interfaces for User 1 and User 2 with search, catalog browsing, and execution pipelines.
- **Two Execution Modes**:
  - **⚠️ Unsafe (Race Hazard)**: Demonstrates what happens when concurrent threads check availability and update shared data without mutual exclusion, resulting in the duplicate issue bug.
  - **🛡️ Mutex Protected (Safe)**: Utilizes `threading.Lock()` to enforce mutual exclusion on the check-and-decrement critical section.
- **Live Audit Stream**: Real-time timestamped event log capturing thread transitions and lock states.
- **Visual Critical Section Chamber**: Interactive inspection of the shared resource and lock ownership.

## 💻 Tech Stack
- HTML5, CSS3 (Tailwind CSS)
- Vanilla JavaScript Simulation Engine
- Python `threading` module implementation reference

## 🛠️ Local Usage
Open `index.html` directly in any modern web browser (Chrome, Edge, Firefox, Safari).
