/*
Name: Pangram
Link: https://codeforces.com/problemset/problem/520/A
Categories: string
*/
#include <bits/stdc++.h>

using namespace std;

int main()
{
    // n int, a string input
    int n;
    string a, b;
    set<string> string_set;
    cin >> n >> a;

    // lowercase given string and make it set
    int tolower(int a);
    for (char c : a)
    {
        string_set.insert(string{c});
    }

    // checking alphabet
    if (string_set.size() == 26)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}
