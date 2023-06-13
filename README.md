# nytimes-digits

## Installation

1. Install Python from [python.org](https://www.python.org).

2. Clone the repository:

```shell
git clone https://github.com/orielsanchez/nytimes-digits.git
```

3. Change the project directory:

```shell
cd nytimes-digits
```

4. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

To use the nytimes-digits tool, run the nytimes-digits.py script with the appropriate command-line arguments.
```shell
python nytimes-digits.py -n [NUMBERS] -t [TARGET] [-s [SOLUTIONS]]
```

Arguments:

-n or --numbers: Input numbers separated by spaces.
-t or --target: Target number.
-s or --solutions (optional): Number of solutions to display (default: 10).

Example usage:
```shell
python nytimes-digits.py -n 1 2 3 4 5 10 -t 65 -s 5
```

This will find the order of operations to reach the target number 65 using the input numbers 1, 2, 3, 4, 5, and 10. It will display the first 5 solutions, if available.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
