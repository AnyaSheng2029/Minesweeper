Implemented Minesweeper in Python with two AI helpers. Run with python -i final.py then call hostGame(8,8,13).

Probabilistic AI: Opens cells with ≥75% safety, falls back to ≥50% when stuck. 14% solo win rate, but useful as a human decision-support tool.

Constraint-based AI b: Auto-flags cells when remaining unknowns match the bomb count. Best used to skip redundant moves.

See minesweeper.txt for full writeup and gameplay instructions.
