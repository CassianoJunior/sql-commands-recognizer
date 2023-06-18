# grammar: S -> SQL_CMD S | ε
# SQL_CMD -> CREATE_STMT
#       |  USE_STMT
#       |  INSERT_STMT
#       |  SELECT_STMT
#       |  UPDATE_STMT
#       |  DELETE_STMT
#       |  TRUNCATE_STMT
# CREATE_STMT -> 'CREATE' 'DATABASE' ID ';' | 'CREATE' 'TABLE' ID '(' COLLUMN ')' ';'
# USE_STMT -> 'USE' ID ';'
# INSERT_STMT -> 'INSERT' 'INTO' ID '(' COLLUMN_NAME ')' 'VALUES' COLLUMN_VALUE ';'
# SELECT_STMT -> 'SELECT' '*' 'FROM' ID ';'
#          |    'SELECT' COLLUMN_NAME 'FROM' ID ';'
#          |    'SELECT' '*' 'FROM' ID 'ORDER' 'BY' ID ';'
#          |    'SELECT' '*' 'FROM' ID 'WHERE' ID '=' VALUES ';'
# UPDATE_STMT -> 'UPDATE' ID 'SET' ID '=' VALUES 'WHERE' ID '=' VALUES ';'
# DELETE_STMT -> 'DELETE' 'FROM' ID 'WHERE' ID '=' VALUES ';'
# TRUNCATE_STMT -> 'TRUNCATE' 'TABLE' ID ';'
# COLLUMN -> ID TIPO ',' COLLUMN | ID TIPO
# COLLUMN_NAME -> ID ',' COLLUMN_NAME | ID
# COLLUMN_VALUE -> '(' VALUES ')' ',' COLLUMN_VALUE | '(' VALUES ')'
# VALUES -> ((STRING | NUM) ',' VALUES) | STRING | NUM
# ID -> [a-zA-Z]+
# TIPO -> 'string' | 'int' | 'float' | 'bool'
# STRING -> '"' [a-zA-Z]+ '"'
# NUM -> [0-9]+('.' [0-9]+)*

from sqlParser import SQLParser

sql = 'INSERT INTO Alunos (nome, idade, CPF) VALUES ("Jose", 30, 08372487328);'

#sql2 = open('cmds2.txt', 'r')

if __name__ == '__main__':

  parser = SQLParser(sql)
  parser.S()
