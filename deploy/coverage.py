﻿"""Measures code coverage by test suite."""

from subprocess import run
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parent
file = here/'coverage.sqlite'

print('Running test suite.')
run(['python', '-m', 'pytest', '--cov'], cwd=root)

print('Exporting coverage report.')
folder = (here/'coverage').relative_to(root)
run(['coverage', 'html', f'--directory={folder}'], cwd=root)
