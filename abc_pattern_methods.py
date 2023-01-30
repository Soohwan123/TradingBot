def Get_382_In_B_Wave(startPointOfA, endPointOfA) :
    direction = 'bullish'
    if(startPointOfA - endPointOfA < 0):
        direction = 'bearish'

    if(direction == 'bearish'):
        return endPointOfA - (abs(startPointOfA - endPointOfA) * 0.382)
    else:
        return endPointOfA + (abs(startPointOfA - endPointOfA) * 0.382)

def Get_5_In_B_Wave(startPointOfA, endPointOfA) :
    direction = 'bullish'
    if(startPointOfA - endPointOfA < 0):
        direction = 'bearish'

    if(direction == 'bearish'):
        return endPointOfA - abs(startPointOfA - endPointOfA) * 0.5
    else:
        return endPointOfA + abs(startPointOfA - endPointOfA) * 0.5


def Get_618_In_B_Wave(startPointOfA, endPointOfA) :
    direction = 'bullish'
    if(startPointOfA - endPointOfA < 0):
        direction = 'bearish'

    if(direction == 'bearish'):
        return endPointOfA - abs(startPointOfA - endPointOfA) * 0.618
    else:
        return endPointOfA + abs(startPointOfA - endPointOfA) * 0.618


        
def Get_End_Point_Of_C(startPointOfA, endPointOfA, endPointOfB) :
    direction = 'bullish'
    if(startPointOfA - endPointOfA < 0):
        direction = 'bearish'

    if(direction == 'bearish'):
        return endPointOfB + abs(startPointOfA - endPointOfA)
    else:
        return endPointOfB - abs(startPointOfA - endPointOfA)




    

