% Gioi tinh
female(elizabeth_ii).
female(diana).
female(camilla_Parker_Bowles).
female(sarah_Ferguson).
female(kate_Middleton).
female(meghan_Markle).
female(ps_Eugenie).
female(ps_Beatrice).
female(ps_Charlotte).
female(ps_Anne).
female(sophie_RhysJones).
female(autumn_Phillips).
female(zara_Tindall).
female(lady_Louise_Windsor).

male(p_Phillip).
male(charles).
male(p_Andrew).
male(p_William).
male(p_Harry).
male(p_George).
male(p_Louis).
male(archie_Harrison).
male(mark_Phillips).
male(timothy_Laurence).
male(p_Edward).
male(peter_Phillips).
male(mike_Tindall).
male(james_ViscountSevern).

% Quan he gia dinh
married(elizabeth_ii,p_Phillip).
married(p_Phillip,elizabeth_ii).

married(charles,camilla_Parker_Bowles).
married(camilla_Parker_Bowles,charles).

married(p_Andrew,sarah_Ferguson).
married(sarah_Ferguson, p_Andrew).

married(kate_Middleton,p_William).
married(p_William, kate_Middleton).

married(p_Harry,meghan_Markle).
married(meghan_Markle,p_Harry).

married(ps_Anne,timothy_Laurence).
married(timothy_Laurence,ps_Anne).

married(p_Edward,sophie_RhysJones).
married(sophie_RhysJones,p_Edward).

married(peter_Phillips,autumn_Phillips).
married(autumn_Phillips, peter_Phillips).

married(zara_Tindall,mike_Tindall).
married(mike_Tindall, zara_Tindall).

divorced(diana,charles).
divorced(charles, diana).
divorced(ps_Anne,mark_Phillips_Cap).
divorced(mark_Phillips_Cap,ps_Anne).

parent(elizabeth_ii,charles).
parent(elizabeth_ii,p_Andrew).
parent(elizabeth_ii,ps_Anne).
parent(elizabeth_ii,p_Edward).
parent(p_Phillip,charles).
parent(p_Phillip,p_Andrew).
parent(p_Phillip,ps_Anne).
parent(p_Phillip,p_Edward).

parent(diana,p_William).
parent(diana,p_Harry).
parent(charles,p_William).
parent(charles,p_Harry).

parent(p_Andrew,ps_Eugenie).
parent(p_Andrew,ps_Beatrice).
parent(sarah_Ferguson,ps_Eugenie).
parent(sarah_Ferguson,ps_Beatrice).

parent(kate_Middleton,p_George).
parent(kate_Middleton,ps_Charlotte).
parent(kate_Middleton,p_Louis).
parent(p_William,p_George).
parent(p_William,ps_Charlotte).
parent(p_William,p_Louis).

parent(p_Harry,archie_Harrison).
parent(meghan_Markle,archie_Harrion).

parent(mark_Phillips,peter_Phillips).
parent(mark_Phillips,zara_Tindall).
parent(ps_Anne,peter_Phillips).
parent(ps_Anne,zara_Tindall).

parent(p_Edward,james_ViscountSevern).
parent(p_Edward,lady_Louise_Windsor).
parent(sophie_RhysJones,james_VS).
parent(sophie_RhysJones,lady_Louise_Windsor).

%Cac moi quan he phuc tap hon
husband(Person, Wife) :-
    married(Person, Wife),
    male(Person),
    Person \= Wife.

wife(Wife, Husband) :-
    married(Husband, Wife),
    female(Wife),
    Husband \= Wife.

father(Parent, Child) :-
    parent(Parent, Child),
    male(Parent).

mother(Parent, Child) :-
    parent(Parent, Child),
    female(Parent).

child(Child, Parent) :-
    parent(Parent, Child).

son(Child, Parent) :-
    child(Child, Parent),
    male(Child).

daughter(Child, Parent) :-
    child(Child, Parent),
    female(Child).

grandparent(GP, GC) :-
    parent(GP, Parent),
    parent(Parent, GC).

grandmother(GM, GC) :-
    grandparent(GM, GC),
    female(GM).

grandfather(GF, GC) :-
    grandparent(GF, GC),
    male(GF).

grandchild(GC, GP) :-
    parent(GP, Parent),
    parent(Parent, GC).

grandson(GS, GP) :-
    grandchild(GS, GP),
    male(GS).

granddaughter(GD, GP) :-
    grandchild(GD, GP),
    female(GD).

sibling(Person1, Person2) :-
    father(Parent, Person1),
    father(Parent, Person2),
    Person1 \= Person2.

brother(Person, Sibling) :-
    sibling(Person, Sibling),
    male(Person).

sister(Person, Sibling) :-
    sibling(Person, Sibling),
    female(Person).

aunt(Aunt, NieceNephew) :-
    parent(Parent, NieceNephew),
    sibling(Parent, Aunt),
    female(Aunt).

uncle(Uncle, NieceNephew) :-
    parent(Parent, NieceNephew),
    sibling(Parent, Uncle),
    male(Uncle).

niece(Niece, AuntUncle) :-
    (aunt(AuntUncle, Niece); uncle(AuntUncle, Niece)),
    female(Niece).

nephew(Nephew, AuntUncle) :-
    (aunt(AuntUncle, Nephew); uncle(AuntUncle, Nephew)),
    male(Nephew).

test :-
    % Câu hỏi 1: Ai là mẹ của Prince Andrew?
    mother(X1, p_Andrew),
    write('1.Mother of Prince Andrew is: '), write(X1), nl,

    % Câu hỏi 2: Nữ hoàng Elizabeth có phải là vợ của Mia Grace Tindall không?
    married(elizabeth_ii, mia_Grace_Tindall),
    write('2.Is Queen Elizabeth II married to Mia Grace Tindall? Yes.'), nl;
    write('2.Is Queen Elizabeth II married to Mia Grace Tindall? No.'), nl,

    % Câu hỏi 3: Ai là cha của Peter Phillips?
    father(X3, peter_Phillips),
    write('3.Father of Peter Phillips is: '), write(X3), nl,

    % Câu hỏi 4: Ai là con của Camilla Parker Bowles và Charles?
    (child(X4, camilla_Parker_Bowles), child(X4, charles)) ->
    (write('4. Child of Camilla Parker Bowles and Charles is: '), write(X4), nl);
    (write('4. There is no child of Camilla Parker Bowles and Charles.'), nl),

    %Câu hỏi 5: Ai là chồng của Sarah Ferguson?
    husband(X5, sarah_Ferguson),
    write('5. Husband of Sarah Ferguson is: '), write(X5), nl,

    %Câu hỏi 6: Sarah Ferguson là mẹ của ai?
    setof(Child6, mother(sarah_Ferguson, Child6), Childs6),
    write('6. Sarah Ferguson is the mother of: '), write(Childs6), nl,

    %Câu hỏi 7: Charles đã kết hôn bao nhiêu lần?
    findall(Marriage7, married(charles, Marriage7), Marriages7),
    length(Marriages7, Count7),
    write('7. How many times has Prince Charles been married? '),
    write(Count7), nl,

    %Câu hỏi 8: Ai là con gái của Prince William và Kate Middleton?
    (   setof(X8, daughter(X8, p_William), Daughters8)
    ->  write('8. Daughter of Prince William and Kate Middleton: '), write(Daughters8), nl
    ;   write(8.'There is no daughter of Prince William and Kate Middleton.'), nl
    ),

    %Câu hỏi 9: Meghan Markle là vợ của ai?
    husband(Husband9, meghan_Markle),
    write('9. Meghan Markle is the wife of: '), write(Husband9), nl,

    %Câu hỏi 10: Ai là ông nội của Prince George?
    grandfather(X10, p_George),
    write('10. Grandfather of Prince George is: '), write(X10), nl,

    %Câu hỏi 11: Ai là bà nội của Archie Harrison?
    grandmother(GM11, archie_Harrison),
    write('11. Grandmother of Archie Harrison is: '), write(GM11), nl,

    %Câu hỏi 12: Ai là em gái của Prince William?
    (   sister(X12, p_William)
    ->  write('12. Sister of Prince William is: '), write(X12), nl
    ;   write('12. There is no sister of Prince William.'), nl
    ),

    %Câu hỏi 13: Ai là chồng của Princess Charlotte?
    (   husband(X13, ps_Charlotte)
    ->  write('13. Husband of Princess Charlotte is: '), write(X13), nl
    ;   write('13. There is no Husband of Princess Charlotte.'), nl
    ),

    %Câu hỏi 14: Ai là vợ của Prince Harry?
    wife(meghan_Markle, p_Harry),
    write('14. Wife of Prince Harry is: '), write(meghan_Markle), nl,

    %Câu hỏi 15: Ai là cháu của Queen Elizabeth II?
    setof(X15, grandchild(X15, elizabeth_ii), GCs15),
    write('15. Grandchild of Queen Elizabeth II is: '), write(GCs15), nl,

    %Câu hỏi 16: Ai là ông của Lady Louise Windsor?
    grandfather(X16, lady_Louise_Windsor),
    write('16. Grandfather of Lady Louise Windsor is: '), write(X16), nl,

    %Câu hỏi 17: Ai là mẹ của Zara Tindall?
    mother(X17, zara_Tindall),
    write('17. Mother of Zara Tindall is: '), write(X17), nl,

    %Câu hỏi 18: Ai là anh trai của Princess Beatrice?
    (   brother(X18, ps_Beatrice) ->
        write('18. Brother of Princess Beatrice is: '), write(X18), nl
    ;   write('18. There is no brother of Princess Beatrice.'), nl
    ),

    %Câu hỏi 19: Ai là cháu trai của Prince Philip?
    (   setof(X19, grandson(X19, p_Phillip), GSs19) ->
        write('19. Grandson of Prince Philip is: '), write(GSs19), nl
    ;   write('19. There is no grandson of Prince Philip.'), nl
    ),

    %Câu hỏi 20: Ai là con của Princess Anne và Mark Phillips?
    (   setof(X20, parent(ps_Anne, X20), Childs)
    ->  write('20. Child of Princess Anne and Mark Phillips is: '), write(Childs), nl
    ;   write('20. There is no child of Princess Anne and Mark Phillips.'), nl
    ).


