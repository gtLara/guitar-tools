import numpy as np

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

class scale():
    
    def __init__(self, mode = 'ionian', note = 'C'):
        
        #Assume que escala será maior/ioniana para depois
        #corrigir se necessário
        
        mode = mode.lower()
        
        translate = {
                    'major':'ionian',
                    'minor':'aeolian'
                    }
                
        modes = {
                'dorian': 1,
                 'phrygian': 2,
                 'lydian': 3,
                 'mixolydian': 4,
                 'aeolian': 5,
                 'locrian': 6
                 }
        
        if mode not in modes:
            mode = translate[mode]
        
        self.intervals = [2, 2, 1, 2, 2, 2, 1]       
        
        chrom = chromatic().scale
        
        self.tonic = note
        self.notes = []
               
        index = chrom.index(note)
                    
        for count in range(7):
            index = index % len(chrom)
            self.notes.append(chrom[index])
            index += self.intervals[count]
        
        if mode != 'ionian': #Correção de modos
            print('entrando')
            intervals = []
            notes = []
            
            index = modes[mode]
            
            for count in range(7):
                index = index % len(self.intervals)
                intervals.append(self.intervals[index])
                notes.append(self.notes[index])
                index += 1
            
            self.intervals = intervals
            self.notes = notes        
    
class fretboard():
    
    def __init__(self, tuning = 'standard', n_frets = 20):
        self.board = np.zeros((6, n_frets))
        c = chromatic()
        self.scale = c.scale
        self.hash = c.hash
        self.inv_hash = c.inv_hash
        self.n_frets = n_frets
        
        if tuning == 'standard': 
            self.open_strings = ['E', 'A', 'D', 'G', 'B', 'E']
        
        for s in range(6):
            base_note = self.open_strings[s]
            base_index = self.scale.index(base_note)
            for n in range(n_frets):
                index = (n + base_index) % chromatic().size
                self.board[s, n] = self.hash[self.scale[index]]
                
    def show_notes(self):
        border = ''
        for n in range(self.n_frets*5):
            border = border + '_'
        
        print(border)
        print('')

        for s, string in enumerate(self.board):
            visual_list = [self.inv_hash[note] for note in string]
            visual_string = ""
            for note in visual_list:
                if '#' not in note:
                    visual_string = visual_string + note + "  | "
                else:
                    visual_string = visual_string + note + " | "

            print(visual_string)
        
        print(border)
    
#fretboard().show_notes()
        
s = scale(mode = 'Major', note = 'F#')

print(s.tonic)
print(s.notes)
print(s.intervals)



