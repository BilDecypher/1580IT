def read_string(filename):
    with open(filename) as input_file:
        string = input_file.readline()
        return string

def solve(s):
    data = [i for i in s.split('AA') if len(i) == 34 and i[1] == 'E']
    return len(data)
s = read_string('m9-1.txt')
print(solve(s))