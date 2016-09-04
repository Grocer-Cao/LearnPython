class Lexicon(object):
    
    def scan(self, stuff):
        self.stuff = stuff
        words = stuff.split()
        sentence = []
        for i in words:
            try:
                sentence.append(('number', int(i)))
            except ValueError:
                if i in ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']:
                    sentence.append(('direction', i))
                elif i in ['go', 'stop', 'kill', 'eat']:
                    sentence.append(('verb', i))
                elif i in ['the', 'in', 'of', 'from', 'at', 'in']:
                    sentence.append(('stop', i))
                elif i in ['door', 'bear', 'princess', 'cabinet']:
                    sentence.append(('noun', i))
                else:
                    sentence.append(('error', i))

        return sentence
       
lexicon = Lexicon()