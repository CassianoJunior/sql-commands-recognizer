# grammar: S -> SQL_CMD S | SQL_CMD
# SQL_CMD -> CREATE_STMT
#       |  USE_STMT
#       |  INSERT_STMT
#       |  SELECT_STMT
#       |  UPDATE_STMT
#       |  DELETE_STMT
#       |  TRUNCATE_STMT
# CREATE_STMT -> 'CREATE' 'DATABASE' '<id>' ';' | 'CREATE' 'TABLE' '<id>' '(' COLLUMN ')' ';'
# USE_STMT -> 'USE' '<id>' ';'
# INSERT_STMT -> 'INSERT' 'INTO' '<id>' '(' COLLUMN_NAME ')' 'VALUES' COLLUMN_VALUES ;
# SELECT_STMT -> 'SELECT' '*' 'FROM' '<id>' ';'
#          |    'SELECT' '(' COLLUMN_NAME ')' 'FROM' '<id>' ';'
#          |    'SELECT' '*' 'FROM' '<id>' 'ORDER' 'BY' '<id>' ';'
#          |    'SELECT' '*' 'FROM' '<id>' 'WHERE' '<id>' '=' '<valor>' ';'
# UPDATE_STMT -> 'UPDATE' '<id>' 'SET' '<id>' '=' '<valor>' 'WHERE' '<id>' '=' '<valor>' ';'
# DELETE_STMT -> 'DELETE' 'FROM' '<id>' 'WHERE' '<id>' '=' '<valor>' ';'
# TRUNCATE_STMT -> 'TRUNCATE' 'TABLE' '<id>' ';'
# COLLUMN -> '<id>' '<tipo>' ',' COLLUMN | '<id>' '<tipo>'
# COLLUMN_NAME -> '<id>' ',' COLLUMN_NAME | '<id>'
# COLLUMN_VALUE -> '(' VALUE ')' ',' COLLUMN_VALUE | '(' VALUE ')'
# VALUE -> '<valor>' ',' VALUE | '<valor>'

from sqlParser import SQLParser

sql = 'CREATE TABLE users (name string, age int);'

if __name__ == '__main__':
  # sqlParser.parser['initial'](sql)

  parser = SQLParser(sql)
  print(parser.S())
