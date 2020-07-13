// https://www.hackerrank.com/contests/university-codesprint-5/challenges/exceeding-speed-limit/problem

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

// Complete the solve function below.
void solve(int s) {
    if(s<91)
        cout<<0<<" No punishment"<<endl;
    else if(s<111)
        cout<<(s-90)*300<<" Warning"<<endl;
    else
        cout<<(s-90)*500<<" License removed"<<endl;
}

int main()
{
    string s_temp;
    getline(cin, s_temp);

    int s = stoi(ltrim(rtrim(s_temp)));

    solve(s);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
