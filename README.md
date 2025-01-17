# TaskKiller

TaskKiller is a simple Python application that provides an interface to monitor and terminate unresponsive processes on Windows. It uses the `psutil` library to interact with system processes and a graphical user interface built with `tkinter`.

## Features

- List all running processes with their PID, Name, and Status.
- Refresh process list to ensure the latest information.
- Terminate unresponsive or unwanted processes with a single click.

## Requirements

- Python 3.x
- `psutil` library (Install via `pip install psutil`)
- Windows Operating System

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/taskkiller.git
   ```

2. Navigate to the directory:

   ```bash
   cd taskkiller
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using Python:

```bash
python task_killer.py
```

- The application window will list all running processes.
- Select a process from the list and click "Kill Process" to terminate it.
- Use the "Refresh" button to update the process list.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to your fork.
5. Create a pull request.

## Acknowledgements

- [psutil](https://github.com/giampaolo/psutil) library for process management.
- Python's `tkinter` for the graphical user interface.