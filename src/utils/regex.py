import re

# Regex for matching a list of sql commands
# sql = 'CREATE TABLE <id> (<id> <tipo>, <id> <tipo>);'
# sql = 'CREATE DATABASE <id>;'
# sql = 'USE <id>;'
# sql = 'INSERT INTO <id> (<id>, <id>) VALUES (<valor>, <valor>);'
# sql = 'SELECT * FROM <id>;'
# sql = 'SELECT (<id>, <id>) FROM <id>;'
# sql = 'SELECT * FROM <id> ORDER BY <id>;'
# sql = 'SELECT * FROM <id> WHERE <id> = <valor>;'
# sql = 'UPDATE <id> SET <id> = <valor> WHERE <id> = <valor>;'
# sql = 'TRUNCATE TABLE <id>;'

# Regex for matching whitespaces
WS = r'\s+'

# Regex for matching numbers
NUMBER = r'\d+(\.\d+)?'

# Regex for matching identifiers
ID = r'[a-zA-Z_]+[a-zA-Z0-9_]*'

# Regex for matching strings
STRING = r'"[a-zA-Z0-9_ ]+"|\'[a-zA-Z0-9_ ]\''

# Regex for matching types
TYPE = r'int|float|string|boolean|date|datetime'

# Regex for matching values
VALUE = rf'{NUMBER}|{STRING}'

# Regex for matching operators
OPERATOR = r'<=|>=|<|>|=|!=|<>'

# Regex for matching some of expected commands

reservedWords = [
  'CREATE',
  'DATABASE',
  'TABLE',
  'USE',
  'INSERT',
  'INTO',
  'VALUES',
  'SELECT',
  'FROM',
  'ORDER',
  'BY',
  'WHERE',
  'UPDATE',
  'SET',
  'DELETE',
  'TRUNCATE',
]

specialChars = [
  ';',
  ',',
  '(',
  ')',
]

def isIdentifier(token: str):
  return re.match(ID, token)

def isType(token: str):
  return re.match(TYPE, token)

def isValue(token: str):
  return re.match(VALUE, token)

def isSpecialChar(token: str):
  return token in specialChars

def isReservedWord(token: str):
  return token in reservedWords

def isWhitespace(token: str):
  return re.match(WS, token)

def isOperator(token: str):
  return re.match(OPERATOR, token)

def isRecognized(token: str):
  if isReservedWord(token) or isSpecialChar(token):
    return True
  elif isOperator(token):
    return True
  elif isType(token):
    return True
  elif isIdentifier(token):
    return True
  elif isValue(token):
    return True
  elif isWhitespace(token):
    return True
  else:
    return Exception(f'Unrecognized token: {token}'	)

tokenTypeIs = {
  'ID': isIdentifier,
  'TYPE': isType,
  'VALUE': isValue,
  'WS': isWhitespace,
}
