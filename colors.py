class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def header():
    print(bcolors.HEADER, end='')


def okblue():
    print(bcolors.OKBLUE, end='')

def okgreen():
    print(bcolors.OKGREEN, end='')

def warning():
    print(bcolors.WARNING, end='')

def fail():
    print(bcolors.FAIL, end='')

def endc():
    print(bcolors.ENDC, end='')
