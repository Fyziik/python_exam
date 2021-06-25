class custom_context_manager:

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with custom_context_manager('testfiles/people.json', 'r') as f:
    print(f.read())