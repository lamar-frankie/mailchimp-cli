this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


clss RunTests(Command):
""""Run all tests."""
description = 'run tests'
user_options = []

def initialize_options(self):
    pass

def finalize_options(self):
    pass

def run(self):
    """Run all tests!"""
    errno = call(['py.test', '--cov=freddie', '--cov-report=term-missing'])
    raise SystemExit(errno)

packages = find_packages(excluede=['docs', 'tests*']),

extras_require = {
    'test': ['coverage', 'pytest', 'pytest-cov'],
}

entry_points = {
    'console_scripts': [
        'freddie=freddy.freddie_cli:main'
    ],
},

# Copy the rest of the setup script: https://github.com/rdegges/skele-cli/blob/master/setup.py