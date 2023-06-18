# grammar: S -> SQL_CMD S | ε
# SQL_CMD -> CREATE_STMT
#       |  USE_STMT
#       |  INSERT_STMT
#       |  SELECT_STMT
#       |  UPDATE_STMT
#       |  DELETE_STMT
#       |  TRUNCATE_STMT
# CREATE_STMT -> 'CREATE' 'DATABASE' ID ';' | 'CREATE' 'TABLE' ID '(' COLUMN ')' ';'
# USE_STMT -> 'USE' ID ';'
# INSERT_STMT -> 'INSERT' 'INTO' ID '(' COLUMN_NAME ')' 'VALUES' COLUMN_VALUE ';'
# SELECT_STMT -> 'SELECT' '*' 'FROM' ID ';'
#          |    'SELECT' COLUMN_NAME 'FROM' ID ';'
#          |    'SELECT' '*' 'FROM' ID 'ORDER' 'BY' ID ';'
#          |    'SELECT' '*' 'FROM' ID 'WHERE' ID OPERATOR VALUES ';'
# UPDATE_STMT -> 'UPDATE' ID 'SET' ID OPERATOR VALUES 'WHERE' ID OPERATOR VALUES ';'
# DELETE_STMT -> 'DELETE' 'FROM' ID 'WHERE' ID OPERATOR VALUES ';'
# TRUNCATE_STMT -> 'TRUNCATE' 'TABLE' ID ';'
# COLUMN -> ID TIPO ',' COLUMN | ID TIPO
# COLUMN_NAME -> ID ',' COLUMN_NAME | ID
# COLUMN_VALUE -> '(' VALUES ')' ',' COLUMN_VALUE | '(' VALUES ')'
# VALUES -> ((STRING | NUM) ',' VALUES) | STRING | NUM
# ID -> [a-zA-Z_]+[a-zA-Z0-9_]*
# TIPO -> 'string' | 'int' | 'float' | 'boolean' | 'date' | 'datetime'
# STRING -> '"' [a-zA-Z0-9_ ]+ '"' | ''' [a-zA-Z0-9_ ]+ '''
# NUM -> [0-9]+('.' [0-9]+)?
# OPERATOR -> '<=' | '>=' | '<' | '>' | '=' | '!=' | '<>'

from sqlParser import SQLParser
import time

if __name__ == '__main__':
  while True:
    print('\nPARSER DESCENDENTE RECURSIVO PREDITIVO\n')
    print('1 - Informar comando SQL a ser reconhecido')
    print('2 - Ler Arquivo texto com comandos SQL')
    print('0 - Encerrar aplicação')
    try:
      opcao = int(input('\nEscolha uma opção: '))
    except ValueError:
      print('Digite uma opção válido')
      time.sleep(2)
      continue
    if opcao == 1:
      sql = input('Informe comando SQL a ser reconhecido: ')
      parser = SQLParser(sql)
      parser.S()
      time.sleep(2)
    elif opcao == 2:
      try:
        sql = open(input('Informe o nome do arquivo texto com os comandos SQL(deve estar dentro da pasta do projeto): '), 'r').read()
        parser = SQLParser(sql)
        parser.S()
        time.sleep(2)
      except FileNotFoundError:
        print('Nome incorreto ou arquivo não existe')
        time.sleep(2)
        continue
    else:
      break
