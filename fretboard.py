import numpy as np 

#TODO: use translate tables instead of messy multiple dictionaries
#TODO: make show function prettier
#TODO: start creating scales
#TODO: start mapping scales on board

class chromatic():
    def __init__(self, tempered=True):
        
        if tempered:
            
            C = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            
            chrom = []
            
            for note in C:
                chrom.append(note)
                if note != 'E' and note != 'B':
                    chrom.append(note+'#')
                    
            self.scale = chrom
            
            self.size = len(chrom)
        
        else:
            print('No options for natural scale yet')
            
        self.hash = {}
        self.inv_hash = {}
        
        for n, note in enumerate(self.scale):
            self.hash[note] = n
            self.inv_hash[n] = note
        
        
class fretboard():
    
    def __init__(self, tuning = 'standard', n_frets = 20):
        self.board = np.zeros((6, n_frets))
        c = chromatic()
        self.scale = c.scale
        self.hash = c.hash
        self.inv_hash = c.inv_hash
        
        if tuning == 'standard': 
            self.open_strings = ['E', 'A', 'D', 'G', 'B', 'E']
        
        for s in range(6):
            base_note = self.open_strings[s]
            base_index = self.scale.index(base_note)
            for n in range(n_frets):
                index = (n + base_index) % chromatic().size
                self.board[s, n] = self.hash[self.scale[index]]
                
    def show(self):
        for s, string in enumerate(self.board):
            visual_string = [self.inv_hash[note] for note in string]
            print(visual_string)
        
fretboard().show()



