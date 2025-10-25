def get_lines(string,strip=True):
    lines = string.split('\n')
    if strip:
        lines = [line for line in lines if line]
    return lines
def get_alpha():
    return 'abcdefghijklmnopqrstuvwxyz'
def is_alpha(char,case_sensative=False):
    alphas = get_alpha()
    if not case_sensative:
        alphas+=alphas.upper()
    return char in alphas
