import pygame

class ScoreTable():
    def __init__(self):
        self.initial_dir = 'hiscore/initials.txt'
        self.score_dir = 'hiscore/scores.txt'
        self.initial_string_list = []
        self.score_string_list = []
        self.initial_group = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()

    def populate(self):
        # Populate string lists from file system
        self.initial_string_list = self.getStringsFromFile(self.initial_dir)
        self.score_string_list = self.getStringsFromFile(self.score_dir)

        # Empty sprite groups
        self.initial_group.empty()
        self.score_group.empty()

        # Create new sprites using string lists
        vert_space = 75
        for entry in self.initial_string_list:
            initial = InitialEntry(entry, 300, vert_space)
            self.initial_group.add(initial)
            vert_space += 30

        vert_space = 75
        for entry in self.score_string_list:
            score = ScoreEntry(entry, 600, vert_space)
            self.score_group.add(score)
            vert_space += 30
    
    def draw(self, screen):
        self.initial_group.draw(screen)
        self.score_group.draw(screen)
    
    def isHiscore(self, score):
        hiscores = self.getStringsFromFile(self.score_dir)
        for hiscore in hiscores:
            hiscoreInt = int(hiscore)
            if score >= hiscoreInt:
                return True
        return False

    def insertNewScore(self, initial, score):
        # Read table info from file system
        hiscores = self.getStringsFromFile(self.score_dir)
        initials = self.getStringsFromFile(self.initial_dir)
        # Insert new info into appropriate point in list, pop last place
        for hiscore in hiscores:
            hiscoreInt = int(hiscore)
            if score >= hiscoreInt:
                index = hiscores.index(hiscore)
                hiscores.insert(index, score)
                hiscores.pop()
                initials.insert(index, initial)
                initials.pop()
                break
        # Write modified tables to file system
        self.writeStringsToFile(self.score_dir, hiscores)
        self.writeStringsToFile(self.initial_dir, initials)

    def getStringsFromFile(self, dir):
        infile = open(dir, 'rt')
        strings = []
        for line in infile:
            strings.append(line.rstrip())
        infile.close()
        return strings

    def writeStringsToFile(self, dir, strings):
        outfile = open(dir, 'wt')
        for string in strings:
            print(string, file=outfile)
        outfile.close()

class InitialEntry(pygame.sprite.Sprite):
    def __init__(self, entry, x, y):
        super().__init__()
        self.font = pygame.font.Font('fonts/AGENCYB.ttf', 24)
        self.image = self.font.render(entry, False, (99,155,255))
        self.rect = self.image.get_rect(topleft = (x, y))

class ScoreEntry(pygame.sprite.Sprite):
    def __init__(self, entry, x, y):
        super().__init__()
        self.font = pygame.font.Font('fonts/AGENCYB.ttf', 24)
        self.image = self.font.render(f'{str(entry).zfill(8)}', False, (99,155,255))
        self.rect = self.image.get_rect(topright = (x, y))