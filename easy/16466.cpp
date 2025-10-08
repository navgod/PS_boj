#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.txt", "r", stdin);
    int N;
    cin >> N ;
    vector<int> numbers;
    int tmp;
    for (int i= 0; i < N; ++ i) {
        cin >> tmp;
        numbers.push_back(tmp);
    }
    sort(numbers.begin(), numbers.end());
    int least = 1;
    for (int num : numbers){
        if (num == least) least++;
        else break;
    }
    cout << least;
    return 0;
}