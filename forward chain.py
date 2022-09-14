Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dd_but_fail_if_exists(Fact,KB,[Fact|KB]) :- \+member(Fact,KB).
   
fwd_chain(KB,KBFinal,"forall x: man(x) -> mortal(x)") :-
   member(man(X),KB),
   add_but_fail_if_exists(mortal(X),KB,KB2),
   !,
   fwd_chain(KB2,KBFinal,_).

fwd_chain(KB,KBFinal,"forall x: man(x),woman(y),(married(x,y);married(y,x)) -> needles(y,x)") :-
   member(man(X),KB),
   member(woman(Y),KB),
   (member(married(X,Y),KB);member(married(Y,X),KB)),
   add_but_fail_if_exists(needles(Y,X),KB,KB2),
   !,   
   fwd_chain(KB2,KBFinal,_).
      
fwd_chain(KB,KB,"nothing to deduce anymore").

rt(KBin,KBout) :- fwd_chain(KBin,KBout,_)