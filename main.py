# Test python env
def print_hello():
    animals = ['dog', 'cat', 'hamster', 'tiger'] #in one line
    food = [
        'chicken',
        'Pizza',
        'Pasta'
    ] # w/o trailing comma
    names = [
        'John',
        'Jane',
        'Gil-dong',
        'Hyung-Young',
    ] # w/ trailing comma
    for f_name in names:
        print(f'hello, {f_name}')
if __name__ == '__main__':
    print_hello()
