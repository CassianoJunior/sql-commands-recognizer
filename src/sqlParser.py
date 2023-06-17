from utils.regex import isRecognized, tokenTypeIs

class SQLParser:
  def __init__(self, command: str):
    command = command.replace('(', ' ( ')
    command = command.replace(')', ' ) ')
    command = command.replace(',', ' , ')
    command = command.replace(';', ' ; ')
    self.tokens = command.split()
    self.current = ''

  def __setCurrent(self, token):
    self.current = token

  def getNextToken(self):
    try:
      token = self.tokens.pop(0)
      if isRecognized(token):
        self.__setCurrent(token)
        return token
    except IndexError:
      return print('final da string alcançado')

  def S(self):
    if self.SQL_CMD():
      print("Comando SQL reconhecido com sucesso!!")
      return self.S()

  def SQL_CMD(self):
    self.getNextToken()
    if self.current == 'CREATE':
      if self.CREATE_STMT():
        return True
    elif self.current == 'USE':
      if self.USE_STMT():
        return True

    return False

  def CREATE_STMT(self):
    self.getNextToken()
    if self.current == 'DATABASE':
      self.getNextToken()
      if tokenTypeIs['ID'](self.current):
        self.getNextToken()
        if self.current == ';':
          return True
    elif self.current == 'TABLE':
      self.getNextToken()
      if tokenTypeIs['ID'](self.current):
        self.getNextToken()
        if self.current == '(':
          if self.COLUMN():
            if self.current == ')':
              self.getNextToken()
              if self.current == ';':
                return True

  def COLUMN(self):
    self.getNextToken()
    if tokenTypeIs['ID'](self.current):
      self.getNextToken()
      if tokenTypeIs['TYPE'](self.current):
        self.getNextToken()
        if self.current == ',':
          if self.COLUMN():
            return True

        return True

      return False

  def USE_STMT(self):
    self.getNextToken()
    if self.current == '<id>':
      self.getNextToken()
      if self.current == ';':
        return True
