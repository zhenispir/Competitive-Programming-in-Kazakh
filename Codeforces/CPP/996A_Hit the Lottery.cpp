// https://codeforces.com/problemset/problem/996/A

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, n100, n20, n10, n5, n1;
    cin >> n;

    n100 = n / 100;
    n20 = (n - n100 * 100) / 20;
    n10 = ((n - n100 * 100) - n20 * 20) / 10;
    n5 = (((n - n100 * 100) - n20 * 20) - n10 * 10) / 5;
    n1 = ((((n - n100 * 100) - n20 * 20) - n10 * 10) - n5 * 5) / 1;

    cout << n100 + n20 + n10 + n5 + n1;
    return 0;
}