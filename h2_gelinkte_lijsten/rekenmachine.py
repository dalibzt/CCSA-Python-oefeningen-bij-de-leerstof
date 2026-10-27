operators = ["+", "-", "*", "/"]

def isOperand(s):
    #check of s is getal
    return s.isnumeric()

def isOperator(s):
    return s in operators

def voerBewerkingUit(operator, getal1, getal2):
    if operator == "+":
        return getal1+getal2
    elif operator == '-':
        return getal1-getal2
    elif operator == "*":
        return getal1*getal2
    elif operator == "/":
        return getal1/getal2
    else :
        raise nietImplementeerbaar()
    
def evalueer_postfix(rijVanStrings):
    # list als een stapel gebruiken 
    # - tijdscomplexiteit constant omdat wijzigingen slecht vanachter
    stack = []
    #arr overlopen
    for s in rijVanStrings:
        if not isOperator(s):
            stack.append(float(s))
        elif isOperator(s):
            getal2 = stack.pop()
            getal1 = stack.pop()
            voerBewerkingUit(s, getal1, getal2)
            stack.append(uitkomst)
    return stack.pop()
# prioriteit(operator)
#  prioriteit v operators instellen

def infix_naar_postfix(expressie):
    # lees s in v links nr rechts
    # als s operand: s appenden aan de uitvoer list
    # als s operator: 
        # met stapel
        # vw; als leeg 
        #   of s is een openend haakje (
        #   of er is laatste el(=peak) met hogere prioriteit
       # dan: s tijdelijk op stapel appenden
    # zolang er een el met hogere prior is:
        # dan
      # append de s
    # check sluitend haakje
        #haal operator vd stapel
        #append uitvoer
    #of als s )
        #zolang stapel open haakje
            # pop stapel
            #voeg toe aan uitvoer
        #haakje pop vd stapel
    #totdat de stapel leeg is (met len)
    #return uitvoer

    pass

def rekenmachine(s):
    #split infixstring
    #
    pass
