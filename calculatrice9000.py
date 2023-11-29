def addition(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Erreur : Division par zéro")

def calc(expression):
    operandes = []
    operateurs = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (i == 0 and expression[i] == '-'):
            start = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            operandes.append(float(expression[start:i]))
        elif expression[i] in ['+', '-', '*', '/']:
            while (operateurs and operateurs[-1] in ['+', '-'] and
                   (expression[i] in ['*', '/'])):
                operateurs.pop()
                operand2 = operandes.pop()
                operand1 = operandes.pop()
                if operateurs[-1] == '+':
                    operandes.append(addition(operand1, operand2))
                else:
                    operandes.append(soustraction(operand1, operand2))

            operateurs.append(expression[i])
            i += 1
        else:
            raise ValueError("Erreur : Caractère non valide dans l'expression")
    while operateurs:
        operand2 = operandes.pop()
        operand1 = operandes.pop()
        operateur = operateurs.pop()
        if operateur == '+':
            operandes.append(addition(operand1, operand2))
        elif operateur == '-':
            operandes.append(soustraction(operand1, operand2))
        elif operateur == '*':
            operandes.append(multiplication(operand1, operand2))
        elif operateur == '/':
            operandes.append(division(operand1, operand2))
    return operandes[0]

def calculatrice():
    try:
        expression = input("Entrez une expression mathématique : ")
        result = calc(expression)
        print(f"Le résultat de l'expression {expression} est : {result}")

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

calculatrice()