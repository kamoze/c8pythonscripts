class PyPy:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(PyPy().reverse_words('hello there'))
