class SQLParser:
  def __init__(self, command: str):
    command = command.replace('(', ' ( ')
    command = command.replace(')', ' ) ')
    command = command.replace('"', ' " ')
    command = command.replace(',', ' , ')
    command = command.replace(';', ' ; ')
    self.tokens = command.split()
    self.current = None
    self.end = False

  def __setCurrent(self, token):
    self.current = token

  def getNextToken(self):
    try:
      token = self.tokens.pop(0)
      self.__setCurrent(token)
      return token
    except IndexError:
      self.end = True

  def ID(self):
    for letter in self.current:
        if letter.isalpha():
          continue
        else:
          return False
    return True

  def TIPO(self):
    if self.current == 'string' or self.current == 'int' or self.current == 'float' or self.current == 'bool':
      return True
    return False
      

  def S(self):
    if self.SQL_CMD():
      print('Comando SQL reconhecido com sucesso!!')
      self.S()
    else:
      if self.end:
        print('Final da String alcançado')
      else:
        print('Comando sql não reconhecido')
      

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
      if self.ID():
        self.getNextToken()
        if self.current == ';':
          return True
    elif self.current == 'TABLE':
      self.getNextToken()
      if self.ID():
        self.getNextToken()
        if self.current == '(':
          if self.COLUMN():
            if self.current == ')':
              self.getNextToken()
              if self.current == ';':
                return True

  def USE_STMT(self):
    self.getNextToken()
    if self.ID():
      self.getNextToken()
      if self.current == ';':
        return True

  def INSERT_STMT(self):
    self.getNextToken()
    if self.current == 'INTO':
      self.getNextToken()
      if self.ID():
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
        if self.ID():
          self.getNextToken()
          if self.current == ';':
            return True
    if self.current == '*':
      self.getNextToken()
      if self.current == 'FROM':
        self.getNextToken()
        if self.ID():
          self.getNextToken()
          if self.current == ';':
            return True
          elif self.current == 'ORDER':
            self.getNextToken()
            if self.current == 'BY':
              self.getNextToken()
              if self.ID():
                self.getNextToken()
                if self.current == ';':
                  return True
          elif self.current == 'WHERE':
            self.getNextToken()
            if self.ID():
              self.getNextToken()
              if self.current == '=':
                if self.VALUES():
                  if self.current == ';':
                    return True
          else:
            return False

  def UPDATE_STMT(self):
    self.getNextToken()
    if self.ID():
      self.getNextToken()
      if self.current == 'SET':
        self.getNextToken()
        if self.ID():
          self.getNextToken()
          if self.current == '=':
            if self.VALUES():
              if self.current == 'WHERE':
                self.getNextToken()
                if self.ID():
                  self.getNextToken()
                  if self.current == '=':
                    if self.VALUES():
                      if self.current == ';':
                        return True

  def DELETE_STMT(self):
    self.getNextToken()
    if self.current == 'FROM':
      self.getNextToken()
      if self.ID():
        self.getNextToken()
        if self.current == 'WHERE':
          self.getNextToken()
          if self.ID():
            self.getNextToken()
            if self.current == '=':
              if self.VALUES():
                if self.current == ';':
                  return True

  def TRUNCATE_STMT(self):
    self.getNextToken()
    if self.current == 'TABLE':
      self.getNextToken()
      if self.ID():
        self.getNextToken()
        if self.current == ';':
          return True

  def COLUMN(self):
    self.getNextToken()
    if self.ID():
      self.getNextToken()
      if self.TIPO():
        self.getNextToken()
        if self.current == ',':
          if self.COLUMN():
            return True
        
        return True

      return False

  def COLLUMN_NAME(self):
    self.getNextToken()
    if self.ID():
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
    if self.STRING() or self.NUM():
      self.getNextToken()
      if self.current == ',':
        if self.VALUES():
          return True

        return False

      return True

    return False


  def STRING(self):
    if self.current == '"':
      self.getNextToken()
      for letter in self.current:
        if letter.isalpha():
          continue
        else:
          return False
      self.getNextToken()
      if self.current == '"':
        return True
        
    return False

  def NUM(self):
    if self.current.isdigit or self.current.isdecimal:
      return True

    return False
    
    






