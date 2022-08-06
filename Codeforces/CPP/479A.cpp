/*
Name: Expression
Link: https://codeforces.com/problemset/problem/479/A
Categories: math, max
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    // inputs as integer
    int a, b, c, r1, r2, r3, r4, r5;
    cin >> a >> b >> c;

    // g1 vector is for dynamic array
    vector<unsigned int> array;

    // all possibilities
    r1 = a + b * c;
    r2 = a * (b + c);
    r3 = a * b * c;
    r4 = (a + b) * c;
    r5 = a + b + c;

    // inserting multiple elements to dynamic array
    array.insert(array.end(), {r1, r2, r3, r4, r5});

    // sorting an array
    sort(array.begin(), array.end());
    cout << array[0];
    return 0;
}