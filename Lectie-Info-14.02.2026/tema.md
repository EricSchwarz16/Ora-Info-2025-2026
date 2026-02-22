Trebuie să faci un joc multiplayer în terminal, gen „Bomb Party”, care merge pe rețea, cu socket-uri și broadcast.

Ideea e așa:

Mai mulți jucători se conectează la un server. Serverul alege un „trigger” (o literă sau o combinație de litere, de exemplu „ar”). Apoi, pe rând, fiecare jucător trebuie să scrie un cuvânt care conține acel trigger.

Dacă nu răspunde la timp sau scrie un cuvânt greșit (care nu conține trigger-ul), pierde o viață. Fiecare începe, de exemplu, cu 3 vieți. Când rămâne fără vieți, e eliminat. Ultimul jucător rămas câștigă.

Exemplu de rundă:

Serverul anunță: Trigger-ul este „ar”.
Serverul anunță: Este rândul Anei.

Ana scrie: margine – corect.

Serverul anunță: Este rândul lui Mihai.
Mihai scrie: masa – greșit, nu conține „ar”.
Mihai pierde o viață.

Cerințe obligatorii pentru server:

Să accepte minim 2 jucători conectați.

Să țină evidența jucătorilor și a vieților (ex: 3 vieți fiecare).

Să gestioneze turele (cine e la rând).

Să trimită broadcast către toți jucătorii cu:

trigger-ul curent

al cui este rândul

cine a pierdut o viață

cine a fost eliminat

Să închidă jocul când rămâne un singur jucător și să anunțe câștigătorul.

 asta o sa fie tema, jocul incepe cand sunt MAX_PLAYERS conectati, hardcodezi tu acolo o variabila si pui 2 ca sa testezi mai easy si dupa o bagi si pt mai multi jucatori