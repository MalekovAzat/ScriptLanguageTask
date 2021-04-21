from scriptLanguagesTask import polynomial

class Polynomial:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.__termsList = [arg]
        elif isinstance(arg, (list, tuple)):
            if len(arg) == 0:
                raise Exception(
                    'List or tuple should contain at least one int element.')
            elif False in [isinstance(item, int) for item in arg]:
                raise Exception('List or tuple should contain int args only.')
            else:
                self.__termsList = self.__preprocessTermList(list(arg)[::-1])
        elif isinstance(arg, Polynomial):
            self.__termsList = arg.getTermList().copy()
        else:
            raise Exception('Incorrect arg in constructor Polynomial')

    def __preprocessTermList(self, termList) -> list:
        maxValidDegreeIndex = 0
        for (index, val) in enumerate(termList):
            if val != 0:
                maxValidDegreeIndex = index

        return termList[:maxValidDegreeIndex + 1]

    def __getattribute__(self, name: str):
        if name == 'coeffs':
            return self.getTermList()[::-1]
        else:
            return super().__getattribute__(name)

    def __setattr__(self, name: str, value) -> None:
        if name == 'coeffs' and isinstance(value, (tuple, list)):
            self.__termsList = self.__preprocessTermList(list(value)[::-1])
        else:
            super().__setattr__(name, value)

    def getTermList(self)->list:
        return self.__termsList

    def __repr__(self) -> str:
        return f'Polinomial({self.__termsList[::-1]})'

    def __str__(self) -> str:
        degrees = range(len(self.__termsList))[::-1]
        maxDegree = degrees[0]
        termList = self.__termsList[::-1]
        termStrList = []

        for (degree, termCoeff) in zip(degrees, termList):
            if termCoeff != 0 and maxDegree != 0:
                if not degree:
                    termStrList.append(
                        f'+{termCoeff}' if termCoeff > 0 else f'{termCoeff}')
                elif degree == 1:
                    if maxDegree == 1:
                        termStrList.append(f'{termCoeff}x')
                    else:
                        termStrList.append(
                            f'+{termCoeff}x' if termCoeff > 0 else f'{termCoeff}x')
                elif degree == maxDegree:
                    termStrList.append(f'{termCoeff}x^{degree}')
                else:
                    termStrList.append(
                        f'+{termCoeff}x^{degree}' if termCoeff > 0 else f'{termCoeff}x^{degree}')
            elif maxDegree == 0:
                termStrList.append(f'{termCoeff}')

        return ''.join(termStrList)

    def __add__(self, elem):
        if isinstance(elem, int):
            return self.__addForConst__(elem)
        elif isinstance(elem, Polynomial):
            return self.__addForPolynomial___(elem)
        else:
            raise Exception('Provided incorrect type for second arg in __add__.')

    def __addForPolynomial___(self, elem):
        termList1 = self.getTermList()
        termList2 = elem.getTermList()

        resultList = self.__listAdd__(termList1, termList2)

        return Polynomial(resultList[::-1])

    def __addForConst__(self, elem):
        termList = self.getTermList().copy()
        termList[0] += elem
        
        return Polynomial(termList[::-1])

    def __listAdd__(self, firstList: list, secondList: list) -> list:
        resultList = []
        minListSize = min(len(firstList), len(secondList))
        maxTermList = firstList if len(
            firstList) > len(secondList) else secondList

        for index in range(minListSize):
            resultList.append(firstList[index] + secondList[index])

        resultList.extend(maxTermList[minListSize:])

        return resultList

    def __radd__(self, elem):
        if isinstance(elem, int):
            return self.__addForConst__(elem)
        else:
            raise Exception('Provided incorrect type for second arg in __radd__.')

    def __invertTerms__(self)->list:
        return list(map(lambda x: -x, self.getTermList()))

    def __sub__(self, elem):
        if isinstance(elem, int):
            return self.__addForConst__(-elem)
        elif isinstance(elem, Polynomial):
            termList = self.getTermList()
            invertedList = elem.__invertTerms__()
            resultList = self.__listAdd__(termList, invertedList)
            return Polynomial(resultList[::-1])
        else:
            raise Exception('Provided incorrect type for second arg in __sub__.')

    def __rsub__(self, elem):
        if isinstance(elem, int):
            invertedList = self.__invertTerms__()
            invertedList[0] += elem
            return Polynomial(invertedList[::-1])
        else:
            raise Exception('Provided incorrect type for second arg in __rsub__.')

    def __mul__(self, elem):
        if isinstance(elem, int):
            return Polynomial(list(map(lambda x:x * elem, self.getTermList()))[::-1])
        if isinstance(elem, Polynomial):
            termList1 = self.getTermList()
            termList2 = elem.getTermList()

            resultList = self.__mulList__(termList1, termList2)
            return Polynomial(resultList[::-1])
        else:
            raise Exception('Provided incorrect type for second arg in __mul__.')

    def __mulList__(self, firstList:list, secondList:list)->list:
        sizeOfList = len(firstList) + len(secondList) + 1
        resultList = [0] * sizeOfList

        for (iFirst, eFirst) in enumerate(firstList):
            for (iSecond, eSecond) in enumerate(secondList):
                currentIndex = iFirst + iSecond
                resultList[currentIndex] += eFirst * eSecond

        return resultList

    def __rmul__(self, elem):
        if isinstance(elem, int):
            return self.__mul__(elem)
        else:
            raise Exception('Provided incorrect type for second arg in __rmul__.')

    def __eq__(self, elem) -> bool:
        if isinstance(elem, int):
            termList = self.getTermList()
            return len(termList) == 1 and termList[0] == elem
        elif (isinstance(elem, Polynomial)):
            return self.getTermList() == elem.getTermList()
        else:
            raise Exception('Provided incorrect type for second arg in __eq__.')

if __name__ == '__name__':
    pass
