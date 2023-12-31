# 0x00. Python - Hello, World

## [0-run](./0-run)
> Shell script that runs a Python script.
> Python file name will be saved in the environment variable `$PYFILE`.
Test:
```bash
export PYFILE=test/main.py
./0-run
```

## [1-run_inline](./1-run_inline)
> Shell script that runs Python code.
> Python code will be saved in the environment variable `$PYCODE`.
Test:
```bash
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
```

## [2-print.py](./2-print.py)
> Python script that prints exactly `"Programming is like building a multilingual puzzle` using the `print` function.
Test:
```bash
./2-print.py
```

## [3-print_number.py](./3-print_number.py)
> Print 98 Battery street
Test:
```bash
./3-print_number.py
```

## [4-print_float.py](./4-print_float.py)
> print the float stored in the variable number with a precision of 2 digits.
Test:
```bash
./4-print_float.py
```

## [5-print_string.py](./5-print_string.py)
> print 3 times a string stored in the variable str, followed by its first 9 characters.
Test:
```bash
./5-print_string.py
```

## [6-concat.py](./6-concat.py)
> Concatenate and print a string
Test:
```bash
./6-concat.py
```

## [7-edges.py](./7-edges.py)
> Implementation string slicing
Test:
```bash
./7-edges.py
```

## [8-concat_edges.py](./8-concat_edges.py)
> More slicing
Test:
```bash
./8-concat_edges.py
```

## [9-easter_egg.py](./9-easter_egg.py)
> Python script that prints “The Zen of Python”, by TimPeters. `import this`
Test:
```bash
./9-easter_egg.py
```

## [10-check_cycle.c](./10-check_cycle.c)
>

### [100-write.py](./100-write.py)
> Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`.
	- Use the function `write` from the `sys` module
	- exit with the status code `1`
Test:
```bash
./100-write.py
echo $?
```
