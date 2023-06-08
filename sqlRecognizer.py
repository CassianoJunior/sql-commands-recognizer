#grammar: S -> SQL_CMD S | SQL_CMD
#SQL_CMD -> CREATE_STMT
#       |  USE_STMT
#       |  INSERT_STMT
#       |  SELECT_STMT
#       |  UPDATE_STMT
#       |  DELETE_STMT
#       |  TRUNCATE_STMT
#CREATE_STMT -> 'CREATE' 'DATABASE' '<id>' ';' | 'CREATE' 'TABLE' '<id>' '(' COLLUMN ')' ';'
#USE_STMT -> 'USE' '<id>' ';'
#INSERT_STMT -> 'INSERT' 'INTO' '<id>' '(' COLLUMN_NAME ')' 'VALUES' COLLUMN_VALUES ;
#SELECT_STMT -> 'SELECT' '*' 'FROM' '<id>' ';'
#          |    'SELECT' '(' COLLUMN_NAME ')' 'FROM' '<id>' ';'
#          |    'SELECT' '*' 'FROM' '<id>' 'ORDER' 'BY' '<id>' ';'
#          |    'SELECT' '*' 'FROM' '<id>' 'WHERE' '<id>' '=' '<valor>' ';'
#UPDATE_STMT -> 'UPDATE' '<id>' 'SET' '<id>' '=' '<valor>' 'WHERE' '<id>' '=' '<valor>' ';'
#DELETE_STMT -> 'DELETE' 'FROM' '<id>' 'WHERE' '<id>' '=' '<valor>' ';'
#TRUNCATE_STMT -> 'TRUNCATE' 'TABLE' '<id>' ';'
#COLLUMN -> '<id>' '<tipo>' ',' COLLUMN | '<id>' '<tipo>'
#COLLUMN_NAME -> '<id>' ',' COLLUMN_NAME | '<id>'
#COLLUMN_VALUE -> '(' VALUE ')' ',' COLLUMN_VALUE | '(' VALUE ')'
#VALUE -> '<valor>' ',' VALUE | '<valor>'

sql = 'CREATE TABLE <id> ( <id> <tipo> , <id> <tipo> ) ;'
index = 0

def getNextToken():
    try:
        return sql.split()[index]
    except IndexError:
        return print('final da string alcançado')

def incrementIndex():
    global index
    index += 1

def S():
    if SQL_CMD():
        print("Comando SQL reconhecido com sucesso!!")
        S()

def SQL_CMD():
    token = getNextToken()
    if token == 'CREATE':
        if CREATE_STMT():
            incrementIndex()
            return True
    elif token == 'USE':
        if USE_STMT():
            incrementIndex()
            return True

    return False

def CREATE_STMT():
    incrementIndex()
    token = getNextToken()
    if token == 'DATABASE':
        incrementIndex()
        token = getNextToken()
        if token == '<id>':
            incrementIndex()
            token = getNextToken()
            if token == ';':
                return True
    elif token == 'TABLE':
        incrementIndex()
        token = getNextToken()
        if token == '<id>':
            incrementIndex()
            token = getNextToken()
            if token == '(':
                if COLUMN():
                    token = getNextToken()
                    if token == ')':
                        incrementIndex()
                        token = getNextToken()
                        if token == ';':
                            return True

def COLUMN():
    incrementIndex()
    token = getNextToken()
    if token == '<id>':
        incrementIndex()
        token = getNextToken()
        if token == '<tipo>':
            incrementIndex()
            token = getNextToken()
            if token == ',':
                if COLUMN():
                    return True
            return True
    return False

def USE_STMT():
    incrementIndex()
    token = getNextToken()
    if token == '<id>':
        incrementIndex()
        token = getNextToken()
        if token == ';':
            return True

if __name__ == '__main__':
    S()

        


