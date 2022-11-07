first = 0
second = 0
result = 0

# charO=''

listOperator = {'*': lambda x, y: int(x) * int(y),
                '/': lambda x, y: int(x) / int(y),
                '+': lambda x, y: int(x) + int(y),
                '-': lambda x, y: int(x) - int(y)}


def set_first(number: int):
    global first
    first = number


def set_second(number: int):
    global second
    second = number


def set_result(oper: str):
    global result
    global second
    # if second != 0 and oper == '/':
    result = listOperator.get(oper)(first, second)
   # else:
    #result == None


def get_first():
    global first
    return first


def get_second():
    global second
    return second


def get_result():
    global result
    return result


# def InitChar0(charOp: str):
 #   global charO
 #   charO = charOp

# def GetA():
#    global a
 #   return a

# def GetB():
 #   global b
 #   return b


# def OperatorChoice():
  #  global a
   # global b
  #  global charO
    # for key,value in listOperator:
    # if key == char0:
    #     operand=value
    # else: print
   # functionName=listOperator[charO]
