#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <utility>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.txt", "r", stdin);
    int N, M;
    cin >> N >> M;
    char temp;
    vector<pair<int,string> > players;
    for (int i = 0 ; i< N ; ++i){
        int streak{0};
        int max_streak{0};
        string name;
        for (int j = 0 ; j < M ; ++j){
            cin >> temp;
            if (temp == '*'){
                max_streak = max(max_streak, streak);
                streak = 0;
            }
            else ++streak;
        }
        cin >> name;
        max_streak = max(max_streak, streak);
        players.push_back({max_streak,name});
    }
    set<int> unique_set;
    for (const auto& p : players){
        unique_set.insert(p.first);
    }
    cout << unique_set.size() << '\n';
    for (const auto& p : players){
        cout << p.first << " " << p.second << '\n';
    }
    return 0;
}