def pawn_check(x1,y1,x2,y2):
    return x1==x2 and y2-y1==1

def rook_check(x1,y1,x2,y2):
    return x1==x2 or y1==y2


def bishop_check(x1,y1,x2,y2):
    return abs(x1-x2)==abs(y1-y2)



def knight_check(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2==5
print(knight_check(4,4,5,6))



def queen_check(x1,y1,x2,y2):
    return abs(x1-x2)==abs(y1-y2)or x1==x2 or y1==y2



def king_check(x1,y1,x2,y2):
    ox = abs(x1-x2)
    oy=abs(y1-y2)

    return (ox==1 and oy==1) or (ox==0 and oy==1) or (ox==1 and oy==0)

print(king_check(2,1,2,2))