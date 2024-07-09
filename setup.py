from setuptools import setup
import sys

# Check if the script is being run on Windows
if sys.platform == 'win32':
    sys.argv.append('pyinstaller')

setup(
    name='Browsify',
    version='1.0',
    console=['main.py'],  # Use 'console' for console applications and 'windows' for GUI applications
    options={
        'pyinstaller': {
            'packages': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'PyQt5.QtWebEngineWidgets'],
            'exclude': ['venv'],  # Exclude virtual environment directory
        }
    },
    entry_points={
        'console_scripts': [
            'browsify = main:main',  # Change 'main' to the actual name of your main module
        ],
    },
)
