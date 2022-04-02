"""Chess game mini project """

"""Constants"""
WHITE = "white"
BLACK = "black"

print("welcome to our chess game!!")


class Game:
    """classes"""
    def __init__(self):
        self.playerturn = BLACK
        self.message = "Prompts"
        print("this is where your moves will go")
        self.chessboard = {}
        self.place_pieces()
        print("chess program. enter moves in algebraic notation separated by space eg a1 a2")
        print("start with black pieces")
        self.main()

    def place_pieces(self):
        """piece's places"""
        for i in range(0, 8):
            self.chessboard[(i, 1)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)
            self.chessboard[(i, 6)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)

        placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(0, 8):
            self.chessboard[(i, 0)] = placers[i](WHITE, uniDict[WHITE][placers[i]])
            self.chessboard[((7 - i), 7)] = placers[i](BLACK, uniDict[BLACK][placers[i]])
        placers.reverse()

    def main(self):
        """main function"""
        while True:
            self.print_board()
            print(self.message)
            self.message = ""
            startpos, endpos = self.false_input()
            try:
                target = self.chessboard[startpos]
            except:# pylint: disable=bare-except
                self.message = "could not find piece; index probably out of range"
                target = None

            if target:
                print("found " + str(target))
                if target.color != self.playerturn:
                    self.message = "you aren't allowed to move that piece this turn"
                    continue
                if target.is_valid(startpos, endpos, target.color, self.chessboard):
                    self.message = "that is a valid move"
                    print("that is a valid move")
                    self.chessboard[endpos] = self.chessboard[startpos]
                    del self.chessboard[startpos]
                    self.is_check()
                    if self.playerturn == BLACK:
                        self.playerturn = WHITE
                    else:
                        self.playerturn = BLACK
                else:
                    self.message = "invalid move"

                self.message = "there is no piece in that space"

    def is_check(self):
        """indicates about-to check"""
        kingdict = {}
        piecedict = {BLACK: [], WHITE: []}
        for position, piece in self.chessboard.items():
            if isinstance(piece) == King:
                kingdict[piece.color] = position
            print(piece)
            piecedict[piece.color].append((piece, position))
        # white
        if self.cansee_king(kingdict[WHITE], piecedict[BLACK]):
            self.message = "White player is in check"
        if self.cansee_king(kingdict[BLACK], piecedict[WHITE]):
            self.message = "Black player is in check"

    def cansee_king(self, kingpos, piecelist):
        """can spot king"""
        for piece, position in piecelist:
            if piece.is_valid(position, kingpos, piece.color, self.chessboard):
                return True

    def false_input(self):
        """false input"""
        try:
            num_1,num_2 = input().split()
            num_1 = ((ord(num_1[0]) - 97), int(num_1[1]) - 1)
            num_2 = (ord(num_2[0]) - 97, int(num_2[1]) - 1)
            print(num_1, num_2)
            return (num_1, num_2)
        except:# pylint: disable=bare-except
            print("error decoding input. please try again")
            return ((-1, -1), (-1, -1))

    def print_board(self):
        """board is printed"""
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0, 8):
            print("-" * 32)
            print(chr(i + 97), end="|")
            for j in range(0, 8):
                item = self.chessboard.get((i, j), " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 32)


class Piece:
    """pieces are defined"""
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.color = color

    def is_valid(self, startpos, endpos, color, chessboard):
        """validity of moves are checked"""
        if endpos in self.available_moves(startpos[0], startpos[1], chessboard, color=color):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def available_moves(self, x, y, chessboard):
        """Moves which are permitted"""
        print("ERROR: no movement for base class")

    def moves_cnt(self, num_3, num_4, chessboard, color, intervals):
        """chess board moves"""
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = num_3 + xint, num_4 + yint
            while self.isin_bounds(xtemp, ytemp):
                # print(str((xtemp,ytemp))+"is in bounds")

                target = chessboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.color != color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers

    def isin_bounds(self, x, y):
        "checks if a position is on the board"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def rules_chk(self, chessboard, firstcolor, x, y):
        "checks the rules of chess"
        if self.isin_bounds(x, y) and (((x, y) not in chessboard) or
                                     chessboard[(x, y)].color != firstcolor):
            return True
        return False
chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def knight_list(num_5, num_6, int1, int2):
    """Knight possible moves"""
    return [(num_5 + int1, num_6 + int2),
            (num_5 - int1, num_6 + int2),
            (num_5 + int1, num_6 - int2),
            (num_5 - int1, num_6 - int2),
            (num_5 + int2, num_6 + int1),
            (num_5 - int2, num_6 + int1),
            (num_5 + int2, num_6 - int1),
            (num_5 - int2, num_6 - int1)]

def kingList(num_7, num_8):
    """king's possibilities"""
    return [(num_7 + 1, num_8),
            (num_7 + 1, num_8 + 1),
            (num_7 + 1, num_8 - 1),
            (num_7, num_8 + 1),
            (num_7, num_8 - 1),
            (num_7 - 1, num_8),
            (num_7 - 1, num_8 + 1),
            (num_7 - 1, num_8 - 1)]
class Knight(Piece):
    """knight piece"""
    def available_moves(self, x, y, chessboard, color=None):
        if color is None: color = self.color
        return [(xx, yy) for xx,
                yy in knight_list(x, y, 2, 1) if self.rules_chk(chessboard,
               color,
               xx,
              yy)]


class Rook(Piece):
    """Rook piece"""
    def available_moves(self, x, y, chessboard, color=None):
        if color is None: color = self.color
        return self.moves_cnt(x, y, chessboard, color, chessCardinals)


class Bishop(Piece):
    """Bishop piece"""
    def available_moves(self, x, y, chessboard, color=None):
        if color is None: color = self.color
        return self.moves_cnt(x, y, chessboard, color, chessDiagonals)


class Queen(Piece):
    """queen piece"""
    def available_moves(self, x, y, chessboard, color=None):
        if color is None:
            color = self.color
        return self.moves_cnt(x, y, chessboard, color, chessCardinals + chessDiagonals)


class King(Piece):
    """King piece"""
    def available_moves(self, x, y, chessboard, color=None):
        if color is None: color = self.color
        return [(xx, yy) for xx,
                yy in kingList(x, y) if self.rules_chk(chessboard,
               color,
                xx,
                yy)]


class Pawn(Piece):
    """pawn piece"""
    def __init__(self, color, name, direction):
        self.name = name
        self.color = color

        self.direction = direction

    def available_moves(self, x, y, chessboard, color=None):
        if color is None:
            color = self.color
        answers = []
        if (x + 1, y + self.direction) in chessboard and self.rules_chk(chessboard,
            color,
            x + 1,
            y + self.direction):
            answers.append(
            (x + 1,
            y + self.direction))
        if (x - 1, y + self.direction) in chessboard and self.rules_chk(chessboard,
            color,
            x - 1,
            y + self.direction):
            answers.append(
            (x - 1, y + self.direction))
        if (x,
            y + self.direction) not in chessboard and color == self.color:
            answers.append((x,
            y + self.direction))
        return answers

uniDict = {WHITE: {Pawn: "WP", Rook: "WR", Knight: "WKn", Bishop: "WB", King: "WK", Queen: "WQ"},
           BLACK: {Pawn: "BP", Rook: "BR", Knight: "BKn", Bishop: "BB", King: "BK", Queen: "BQ"}}



Game()
