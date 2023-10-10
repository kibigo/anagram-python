word = "listen"

array = ['enlists', 'google', 'inlets', 'banana']

class Anagram:

    def __init__(self, word):
        self.word = word.lower()

    def match(self, array):

        expected = []
        for item in array:
            item_lower = item.lower()

            if sorted(item_lower) == sorted(self.word):
                expected.append(item_lower)

            elif item_lower == self.word:
                expected.append(item_lower)
    
listen = Anagram("listen")

result = listen.match(array)

print(result)