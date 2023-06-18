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
# ID -> [a-zA-Z]+[a-zA-Z0-9]*
# TIPO -> 'string' | 'int' | 'float' | 'boolean' | 'date' | 'datetime'
# STRING -> '"' [a-zA-Z0-9]+ '"' | ''' [a-zA-Z0-9]+ '''
# NUM -> [0-9]+('.' [0-9]+)?

from sqlParser import SQLParser
import time

if __name__ == '__main__':
  while True:
    print('\nPARSER DESCENDENTE RECURSIVO PREDITIVO\n')
    print('1 - Informar comando SQL a ser reconhecido')
    print('2 - Ler Arquivo texto com comandos SQL')
    print('0 - Encerrar aplicação')
    opcao = int(input('\nEscolha uma opção: '))
    if opcao == 1:
      sql = input('Informe comando SQL a ser reconhecido: ')
      parser = SQLParser(sql)
      parser.S()
      time.sleep(2)
    elif opcao == 2:
      sql = open(input('Informe o nome do arquivo texto com os comandos SQL(deve estar dentro da pasta do projeto): '), 'r').read()
      parser = SQLParser(sql)
      parser.S()
      time.sleep(2)
    else:
      break