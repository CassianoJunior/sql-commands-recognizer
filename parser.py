index = 0

def getNextToken(command: str):
  try:
    return command.split()[index]
  except IndexError:
    return print('final da string alcançado')

def incrementIndex():
  global index
  index += 1

def S(command: str):
  if SQL_CMD(command):
    print("Comando SQL reconhecido com sucesso!!")
    S(command)

def SQL_CMD(command: str):
  token = getNextToken(command)
  if token == 'CREATE':
    if CREATE_STMT(command):
      incrementIndex()
      return True
  elif token == 'USE':
    if USE_STMT(command):
      incrementIndex()
      return True

  return False

def CREATE_STMT(command: str):
  incrementIndex()
  token = getNextToken(command)
  if token == 'DATABASE':
    incrementIndex()
    token = getNextToken(command)
    if token == '<id>':
      incrementIndex()
      token = getNextToken(command)
      if token == ';':
        return True
  elif token == 'TABLE':
    incrementIndex()
    token = getNextToken(command)
    if token == '<id>':
      incrementIndex()
      token = getNextToken(command)
      if token == '(':
        if COLUMN(command):
          token = getNextToken(command)
          if token == ')':
            incrementIndex()
            token = getNextToken(command)
            if token == ';':
              return True

def COLUMN(command: str):
  incrementIndex()
  token = getNextToken(command)
  if token == '<id>':
    incrementIndex()
    token = getNextToken(command)
    if token == '<tipo>':
      incrementIndex()
      token = getNextToken(command)
      if token == ',':
        if COLUMN(command):
          return True

      return True

    return False

def USE_STMT(command: str):
  incrementIndex()
  token = getNextToken(command)
  if token == '<id>':
    incrementIndex()
    token = getNextToken()
    if token == ';':
      return True

statements = {
  'CREATE': CREATE_STMT,
  'USE': USE_STMT
}

parser = {
  'initial': S,
  'statements': statements
}
