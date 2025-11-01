#include <fstream>
#include <vector>
#include <stack>
#include <cstring>  // pentru a utiliza functia strlen

using namespace std;
ifstream fin ("librarie.in");
ofstream fout ("librarie.out");

int n, Q, t;
char op[100000];
vector <long long> Preturi;

struct operatie {
    char tip; 
    int st, dr;
    int val;
};

stack<operatie> undo;
stack<operatie> redo;

void Operatie(operatie& oper, int semn) {
    for (int i = oper.st; i <= oper.dr; i++) {
        if (oper.tip == '+') 
            Preturi[i] += oper.val * semn;
        
        else 
            Preturi[i] -= oper.val * semn;
        
    }
}

int main()
{
    fin >> n;

    Preturi.resize(n + 1);
    for (int i = 1; i <= n; i++) 
        fin >> Preturi[i];

    fin >> Q;
    while(Q--) {
        fin >> t;
        int cnt_op = 0;
        // Vector pentru operațiile tip "+" sau "-"
        // O vom folosi împreună cu stivele undo/redo

        // Iterare prin operații pentru această zi
        int index_Op_curent = 1;
        while(index_Op_curent <= t) {
            char c;
            fin >> c;

            if (c == '+' || c == '-') {
                int st, dr, val;
                fin >> st >> dr >> val;
                operatie oper = {c, st, dr, val};
                Operatie(oper, 1);
                undo.push(oper);
            }
            else if (c == 'u') {
                // Undo: ultima operație neanulată
                if (!undo.empty()) {
                    operatie ultim_Oper = undo.top();
                    undo.pop();
                    Operatie(ultim_Oper, -1);
                    redo.push(ultim_Oper);
                }
            }
            else if (c == 'r') {
                // Redo: ultima operație anulată
                if (!redo.empty()) {
                    operatie ultim_Undo = redo.top();
                    redo.pop();
                    Operatie(ultim_Undo, 1);
                    undo.push(ultim_Undo);
                }
            }
            index_Op_curent++;
        }

        // La finalul zilei, printăm prețurile
        for (int i = 1; i <= n; i++) {
            fout << Preturi[i] << " ";
        }
        fout << "\n";
    }
    return 0;
}
