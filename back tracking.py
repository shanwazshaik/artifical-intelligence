Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
f(X,0) :- X < 3.              % Rule 1
f(X,2) :- 3 =< X, X < 6.   % Rule 2
f(X,4) :- 6 =< X.             % Rule 3