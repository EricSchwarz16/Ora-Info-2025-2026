^ -> inceputul linie
^andrei -> andrei care sa fie neaparat la inceputul liniei!!!!!!
$ -> sfarsitul liniei
 
andrei$
 
[abcdef] -> orice litera dintre a, b, c, d, e 
[a-z] -> orice litera de la a la z
[A-Z] -> orice litera de la A la Z
 
[aA-zZ] -> orice litera de la a la z sau de la A la Z
	|
	|
	|
{a,b,c,d ... z, A,B,C, ... Z}
[1-9] -> orice numar de la 1 la 9
[0-9] -> orice numar de la 0 la 9
 
operatori de multiplicare:
 
[1-9]{3} -> orice numar de la 1 la 9 de 3 ori
[1-9]{3,5} -> orice numar de la 1 la 9 intre de 3 sau 5 ori
[1-9]* -> orice numar de la 1 la 9 de 0 sau mai multe ori, ar fi echivalentul lui {0, oo} -> asta nu exista in regex {0,}
[1-9]+ -> orice numar de la 1 la 9 de 1 sau mai multe ori, ar fi echivalentul lui {1, oo} -> asta nu exista in regex {1,}
. -> poate inseamna orice element
 
? -> caracterul de dinainte poate sau nu poate sa fie prezent(sa apara o data sau de 0 ori){0,1}
 
hell?o would match hello or helo
hell{0,1}o would match hello or helo