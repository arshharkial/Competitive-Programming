// https://www.hackerrank.com/challenges/manasa-and-stones/problem

#include <bits/stdc++.h>

using namespace std;

// Complete the stones function below.
vector<int> stones(int n, int a, int b) {
    vector<int> stone;
    n=n-1;
    if(b==a) {
        stone.push_back(n*a);
        return stone;
    }
    if(b<a) swap(a,b);
    for(int i=0;i<=n;i++)
        stone.push_back(((n-i)*a)+(i*b));
    return stone;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int T;
    cin >> T;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int T_itr = 0; T_itr < T; T_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int a;
        cin >> a;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int b;
        cin >> b;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        vector<int> result = stones(n, a, b);

        for (int i = 0; i < result.size(); i++) {
            fout << result[i];

            if (i != result.size() - 1) {
                fout << " ";
            }
        }

        fout << "\n";
    }

    fout.close();

    return 0;
}
