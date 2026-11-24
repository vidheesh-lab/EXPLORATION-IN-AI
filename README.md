# Exploration in Artificial Intelligence - Lab Experiments

This folder contains the 13 experiments listed in the CS6102 lab manual. Each `expNN` folder contains its Python program and, where the manual uses external input, a small input file.

## Open and run in VS Code

1. Open this folder in VS Code.
2. Install Python 3.10 or newer.
3. In the VS Code terminal, install the libraries with `python -m pip install -r requirements.txt`.
4. Open the experiment folder you want to run in the terminal, then run its `.py` file with `python expNN_....py`.

For experiments 1-3 and 13, enter the short sample input shown in that experiment's `input.txt` (experiment 13's query is `neural networks`). Experiments 8-13 use `google.colab.files` in the manual. Each of those folders includes a tiny local compatibility helper for VS Code; it keeps the manual's experiment script unchanged and lets it use the CSV beside the script without opening an upload dialog. In Google Colab, the normal Colab upload helper is used instead. Experiments 1-3 are interactive and do not read their `input.txt` automatically; use it as the short input sequence when prompted.

Experiment 4 writes `students.csv` and `students.txt` when run. These are generated outputs, not input datasets.

## Manual fidelity note

The experiment scripts preserve the manual's code and logic. Only input data is shortened: embedded data values and external CSV rows are reduced while retaining the relevant fields and missing-value examples. The manual's experiment 1 has its performance assignment under the `else` branch, so the program reports `Needs Improvement` even for a passing mark; it is retained as printed.

