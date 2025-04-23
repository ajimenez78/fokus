# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: Fokus

Fokus is a minimalist terminal assistant to help users regain focus through daily routines.

## Commands
- Run the main application: `python fokus.py`
- No formal test framework implemented yet

## Code Style Guidelines
- **Imports**: Group standard library imports first, then third-party, then local
- **Formatting**: Use 4 spaces for indentation
- **Naming**: Use snake_case for functions and variables
- **Documentation**: Use docstrings for functions
- **Error Handling**: Use try/except blocks with specific exceptions
- **Constants**: Uppercase with underscores (e.g., DATA_FILE)
- **Functions**: Keep functions small and focused on a single responsibility
- **String Formatting**: Use f-strings for string interpolation
- **File Handling**: Always use context managers (with statements) for file operations

## Project Structure
- Main functionality in fokus.py
- Utility modules in utils/ directory
- Data stored in data/journal.json