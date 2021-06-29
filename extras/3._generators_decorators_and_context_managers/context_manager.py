class my_context_manager:

    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

with my_context_manager('test.txt', 'w') as f:
    f.write('Testing')

with my_context_manager('test.txt', 'r') as f:
    print(f.read())