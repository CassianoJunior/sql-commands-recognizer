grammar grammarSql;

command: ('CREATE' | 'DATABASE' | 'INTO' | 'USE' | 'TABLE' | 'INSERT' | 'SELECT' | 'FROM' | 'ORDER' | 'BY' | 'WHERE' | 'UPDATE'
| 'SET' | 'DELETE' | 'TRUNCATE' | '(' | ')' | '<=' | '>=' | '=' | '>' | '<' | ',' | '*' | ';' | TYPE | VALUE | ID)*;

TYPE: 'int' | 'string' | 'double' | 'boolean' | 'date' | 'date_time';

VALUE: NUM | STRING;

ID: [a-zA-Z]+[a-zA-Z0-9_]*;

STRING: '"'ID'"' | '"''"';

NUM: DIGIT+ | FLOAT;

DIGIT: [0-9];

FLOAT: DIGIT'.'DIGIT;

WS: [ \t\n\r] -> skip;
