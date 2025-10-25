def get_lines(string,strip=True):
    lines = string.split('\n')
    if strip:
        lines = [line for line in lines if line]
    return lines
