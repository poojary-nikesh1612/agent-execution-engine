# Agent Execution Engine

A lightweight, foundational execution routing engine built in pure Python. 

While industry-standard frameworks like LangChain or CrewAI provide heavy abstractions for AI agents, this project reconstructs the core autonomous architecture from first principles. It is designed to demonstrate how an AI "brain" interacts with the physical computing environment securely and dynamically.

## Core Architecture
* **Dynamic Tool Registry:** A custom `@tool` decorator that automatically registers functions and their docstrings via Python introspection.
* **Autonomous Routing:** An `Executor` class that safely parses string commands, maps them to the registry, and executes functions dynamically with strict error handling.
* **Persistent State Management:** A built-in JSON logging system that records tool execution history, inputs, and outputs to act as the agent's memory stream.
* **Zero AI Wrappers:** Built entirely without external AI framework dependencies to ensure absolute control over the routing logic.