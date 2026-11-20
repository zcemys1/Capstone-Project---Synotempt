# Hello there, welcome to SYNO-TEMPT

**Directory**

└── Capstone Project
  ├──  .git
  ├──  notes.txt                  -> Some notes regarding the code including some issues that were found and "resolved"
  ├──  README.md                  -> Game overview and instructions
  └────  src
    ├──  requirements.txt         -> Imports needed for game
    ├──  functions.py             -> Contains the functions required for game.py to run
    ├──  game.py                  -> Contains the code to run the game
    ├──  __pycache__
    │    └──    functions.cpython-315.pyc
    └──  .venv                    -> Instance of virtual environment

_How to run code:_

1. Create and activate virtual environment in terminal:
   
    `python -m venv .venv`
    `.venv\Scripts\activate`
    (For Mac/Linux)
    `python3 -m venv .venv && source .venv/bin/activate`

2. Install the code module required:
   
   `pip install -r requirements.txt`

3. Play the game!:
   
   `python3 game.py`
