# Overpick

**Overpick** is a GUI-based application that assists players in selecting heroes in the game Overwatch. By choosing a hero from the dropdown in the Overpick window and pressing 'M' in-game, the hero is automatically selected, saving the user time and effort.

[Download here](https://github.com/abdualblooshi/Overpick/releases/tag/v1.0.0)

## Features:

- **Category-based Hero Selection**: Choose heroes based on their categories (e.g., Support, DPS, Tank).
- **Hotkey Selection**: After selecting a hero from the dropdown, press 'M' in-game to quickly choose that hero.
- **Stop Selection**: A feature to stop the "M" hotkey functionality when not needed.

### [Sometimes it won't work with full screen, so run it as administrator and this currently only works on 1920x1080]

## Installation:

1. Ensure you have the required libraries installed:

   ```bash
   pip install -r requirements.txt
   ```

2. Clone this repository:

   ```bash
   git clone [your-repo-link]
   cd [your-repo-name]
   ```

3. Run the `select_hero.py` script:

   ```bash
   python select_hero.py
   ```

## Creating Executable File:

```bash
 pyinstaller --onefile --icon=images/Overwatch_circle_logo.ico select_hero.py
```

## Usage:

1. Start the Overpick application.
2. Select a category (Support, DPS, Tank) to filter heroes.
3. Choose your desired hero from the dropdown.
4. In-game, simply press 'M' to select the chosen hero.
5. If you wish to stop the "M" hotkey functionality, click the "Stop Selecting" button in the Overpick window.

## Contribution:

Feel free to fork this project and make your own changes. If you have any ideas or suggestions, please open an issue or submit a pull request.

## License:

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
