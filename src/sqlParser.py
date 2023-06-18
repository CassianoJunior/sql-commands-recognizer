from utils.regex import isRecognized, tokenTypeIs

class SQLParser:
  def __init__(self, command: str):
    command = command.replace('(', ' ( ')
    command = command.replace(')', ' ) ')
    #command = command.replace('"', ' " ')
    command = command.replace(',', ' , ')
    command = command.replace(';', ' ; ')
    self.tokens = command.split()
    self.current = ''
    self.end = False

  def __setCurrent(self, token):
    self.current = token

  def getNextToken(self):
    try:
      token = self.tokens.pop(0)
      if isRecognized(token):
        self.__setCurrent(token)
        return token
    except IndexError:
      self.end = True


  def S(self):
    RED = '\033[91m'
    GREEN = '\033[92m'
    CIAN = '\033[96m'
    RESET = '\033[0m'
    if self.SQL_CMD():
      print(GREEN + 'Comando SQL reconhecido com sucesso!!' + RESET)
      self.S()
    else:
      if self.end:
        print(CIAN + 'Final da String alcançado' + RESET)
      else:
        print(RED + 'Comando SQL não reconhecido' + RESET)


  def SQL_CMD(self):
    self.getNextToken()
    if self.current == 'CREATE':
      if self.CREATE_STMT():
        return True
    elif self.current == 'USE':
      if self.USE_STMT():
        return True
    elif self.current == 'INSERT':
      if self.INSERT_STMT():
        return True
    elif self.current == 'SELECT':
      if self.SELECT_STMT():
        return True
    elif self.current == 'UPDATE':
      if self.UPDATE_STMT():
        return True
    elif self.current == 'DELETE':
      if self.DELETE_STMT():
        return True
    elif self.current == 'TRUNCATE':
      if self.TRUNCATE_STMT():
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

  def USE_STMT(self):
    self.getNextToken()
    if tokenTypeIs['ID'](self.current):
      self.getNextToken()
      if self.current == ';':
        return True

  def INSERT_STMT(self):
    self.getNextToken()
    if self.current == 'INTO':
      self.getNextToken()
      if tokenTypeIs['ID'](self.current):
        self.getNextToken()
        if self.current == '(':
          if self.COLLUMN_NAME():
            if self.current == ')':
              self.getNextToken()
              if self.current == 'VALUES':
                if self.COLLUMN_VALUE():
                  if self.current == ';':
                    return True

  def SELECT_STMT(self):
    if self.COLLUMN_NAME():
      if self.current == 'FROM':
        self.getNextToken()
        if tokenTypeIs['ID'](self.current):
          self.getNextToken()
          if self.current == ';':
            return True
    if self.current == '*':
      self.getNextToken()
      if self.current == 'FROM':
        self.getNextToken()
        if tokenTypeIs['ID'](self.current):
          self.getNextToken()
          if self.current == ';':
            return True
          elif self.current == 'ORDER':
            self.getNextToken()
            if self.current == 'BY':
              self.getNextToken()
              if tokenTypeIs['ID'](self.current):
                self.getNextToken()
                if self.current == ';':
                  return True
          elif self.current == 'WHERE':
            self.getNextToken()
            if tokenTypeIs['ID'](self.current):
              self.getNextToken()
              if tokenTypeIs['OPERATOR'](self.current):
                self.getNextToken()
                if tokenTypeIs['VALUE'](self.current):
                  self.getNextToken()
                  if self.current == ';':
                    return True
          else:
            return False

  def UPDATE_STMT(self):
    self.getNextToken()
    if tokenTypeIs['ID'](self.current):
      self.getNextToken()
      if self.current == 'SET':
        self.getNextToken()
        if tokenTypeIs['ID'](self.current):
          self.getNextToken()
          if tokenTypeIs['OPERATOR'](self.current):
            self.getNextToken()
            if tokenTypeIs['VALUE'](self.current):
              self.getNextToken()
              if self.current == 'WHERE':
                self.getNextToken()
                if tokenTypeIs['ID'](self.current):
                  self.getNextToken()
                  if tokenTypeIs['OPERATOR'](self.current):
                    self.getNextToken()
                    if tokenTypeIs['VALUE'](self.current):
                      self.getNextToken()
                      if self.current == ';':
                        return True

  def DELETE_STMT(self):
    self.getNextToken()
    if self.current == 'FROM':
      self.getNextToken()
      if tokenTypeIs['ID'](self.current):
        self.getNextToken()
        if self.current == 'WHERE':
          self.getNextToken()
          if tokenTypeIs['ID'](self.current):
            self.getNextToken()
            if tokenTypeIs['OPERATOR'](self.current):
              self.getNextToken()
              if tokenTypeIs['VALUE'](self.current):
                self.getNextToken()
                if self.current == ';':
                  return True

  def TRUNCATE_STMT(self):
    self.getNextToken()
    if self.current == 'TABLE':
      self.getNextToken()
      if tokenTypeIs['ID'](self.current):
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

  def COLLUMN_NAME(self):
    self.getNextToken()
    if tokenTypeIs['ID'](self.current):
      self.getNextToken()
      if self.current == ',':
        if self.COLLUMN_NAME():
          return True

      return True

    return False

  def COLLUMN_VALUE(self):
    self.getNextToken()
    if self.current == '(':
      if self.VALUES():
        if self.current == ')':
          self.getNextToken()
          if self.current == ',':
            if self.COLLUMN_VALUE():
              return True

            return False

          return True

        return False

      return False

    return False

  def VALUES(self):
    self.getNextToken()
    if tokenTypeIs['VALUE'](self.current):
      self.getNextToken()
      if self.current == ',':
        if self.VALUES():
          return True

        return False

      return True

    return False