class Pion:
    color = 'b'
    posN = 1
    posA = 1
    def __init__(self, color='b', posN=1, posA=1) -> None:
        self.color = color
        self.posN = posN
        self.posA = posA   

class Grid:
    template = (
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
    )
    def __init__(self) -> None:
        self.template = (
        (None, Pion('b', 2, 1), None, Pion('b', 4, 1), None, Pion('b', 6, 1), None, Pion('b', 8, 1), None, Pion('b', 10, 1)) ,
        (Pion('b', 1, 2), None, Pion('b', 3, 2), None, Pion('b', 5, 2), None, Pion('b', 7, 2), None, Pion('b', 9, 2), None) ,
        (None, Pion('b', 2, 3), None, Pion('b', 4, 3), None, Pion('b', 6, 3), None, Pion('b', 8, 3), None, Pion('b', 10, 3)) ,
        (Pion('b', 1, 4), None, Pion('b', 3, 4), None, Pion('b', 5, 4), None, Pion('b', 7, 4), None, Pion('b', 9, 4), None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, None, None, None, None, None, None, None, None, None) ,
        (None, Pion('a', 2, 7), None, Pion('a', 4, 7), None, Pion('a', 6, 7), None, Pion('a', 8, 7), None, Pion('a', 10, 7)) ,
        (Pion('a', 1, 8), None, Pion('a', 3, 8), None, Pion('a', 5, 8), None, Pion('a', 7, 8), None, Pion('a', 9, 8), None) ,
        (None, Pion('a', 2, 9), None, Pion('a', 4, 9), None, Pion('a', 6, 9), None, Pion('a', 8, 9), None, Pion('a', 10, 9)) ,
        (Pion('a', 1, 10), None, Pion('a', 3, 10), None, Pion('a', 5, 10), None, Pion('a', 7, 10), None, Pion('a', 9, 10), None) ,
    )

    def findByCoord(self, n, a):
        return self.template[a-1][n-1]
    
    def addInCoord(self, pion, n, a):
        pion.posN = n
        pion.posA = a
        self.template[a-1][n-1] = pion

    def displayGrid(self):
        print('-----------------------------------------') 
        for i in range(len(self.template)):
            for y in range(len(self.template[i])):
                display = ' '
                if self.template[i][y] != None:
                    display = self.template[i][y].color
                print(f'| {display} ', end='')
            print('|\n-----------------------------------------') 

if __name__ == "__main__":
    grid = Grid()
    grid.displayGrid()
