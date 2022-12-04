#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

int main() {
    ifstream infile("input_3_2022.txt");
    string s;
    vector<string> strings;
    int ans1 = 0;
    while (infile >> s) {
        strings.push_back(s);
        int n = s.size();
        set<char> elem;
        for (int i = 0; i < n / 2; i++) {
            elem.insert(s[i]);
        }
        for (int i = n/2; i < n; i++) {
            if (elem.count(s[i])) {
                if (s[i] >= 'A' && s[i] <= 'Z') {
                    ans1 += s[i] - 'A' + 27;
                }
                else {
                    ans1 += s[i] - 'a' + 1;
                }
                break;
            }
        }
    }
    printf("%d\n", ans1);
    int ans2 = 0;
    for (int i = 0; i < strings.size()/3; i++) {
        set<char> elem;
        set<char> commons;
        for (int j = 0; j < strings[i*3].size(); j++) {
            elem.insert(strings[i*3][j]);
        }
        for (int j = 0; j < strings[i*3+1].size(); j++) {
            if (elem.count(strings[i*3+1][j])) {
                commons.insert(strings[i*3+1][j]);
            }
        }
        for (int j = 0; j < strings[i*3+2].size(); j++) {
            if (commons.count(strings[i*3+2][j])) {
                if (strings[i*3+2][j] >= 'A' && strings[i*3+2][j] <= 'Z') {
                    ans2 += strings[i*3+2][j] - 'A' + 27;
                }
                else {
                    ans2 += strings[i*3+2][j] - 'a' + 1;
                }
                break;
            }
        }
    }
    printf("%d\n", ans2);
}
