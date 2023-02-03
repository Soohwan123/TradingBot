class AbcPatternMethods :
    def Get_382_In_B_Wave(startPointOfA, endPointOfA) :
        diff = abs(startPointOfA - endPointOfA)
        direction = 'bullish' if startPointOfA - endPointOfA >= 0 else 'bearish'

        return endPointOfA + diff * (-0.382 if direction == 'bearish' else 0.382)


    def Get_5_In_B_Wave(startPointOfA, endPointOfA) :
        diff = abs(startPointOfA - endPointOfA)
        direction = 'bullish' if startPointOfA - endPointOfA >= 0 else 'bearish'

        return endPointOfA + diff * (-0.5 if direction == 'bearish' else 0.5)


    def Get_618_In_B_Wave(startPointOfA, endPointOfA) :
        diff = abs(startPointOfA - endPointOfA)
        direction = 'bullish' if startPointOfA - endPointOfA >= 0 else 'bearish'

        return endPointOfA + diff * (-0.618 if direction == 'bearish' else 0.618)


    def Get_End_Point_Of_C(startPointOfA, endPointOfA, endPointOfB) :
        diff = abs(startPointOfA - endPointOfA)
        direction = 'bullish' if startPointOfA - endPointOfA >= 0 else 'bearish'

        return endPointOfB + diff * (-1 if direction == 'bearish' else 1)


    def Get_Recommended_Price(startPointOfA, endPointOfA, wave_percentage):
        direction = 'bullish'
        if(startPointOfA - endPointOfA < 0):
            direction = 'bearish'

        if(direction == 'bearish'):
            return endPointOfA - abs(startPointOfA - endPointOfA) * wave_percentage
        else:
            return endPointOfA + abs(startPointOfA - endPointOfA) * wave_percentage
        



