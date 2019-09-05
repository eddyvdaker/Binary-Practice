# Binary-Practice
A simple application to help students practice binary to decimal and decimal to binary conversions.

![menu](https://media.githubusercontent.com/media/eddyvdaker/Binary-Practice/master/docs/screenshots/menu-screenshot.png)

![question](https://media.githubusercontent.com/media/eddyvdaker/Binary-Practice/master/docs/screenshots/question-screenshot.png)

## Using the application
To run the application:
```bash
python start.py
```

To run the application with a CLI:
```bash
python start.py --cli       # or -c
```

## Generating binaries
To make this application easy to use, it can be distributed as a executable. To create an executable you'll need to install PyInstaller (version 3.5). Then from the project root, run the following command:
```bash
pyinstaller --onefile --name binary-practice start.py
```

The executable is that available from the the dist folder.

## License
Copyright 2019 Eddy van den Aker

MIT License
