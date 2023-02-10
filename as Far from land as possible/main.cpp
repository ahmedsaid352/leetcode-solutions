class Solution {
    public:
        int maxDistance(vector<vector<int>>& grid) {
            vector<pair<int,int>> zeros;
            vector<pair<int,int>> ones;
            int mn = 99999999999;
            int mx = 0;
            for(int i = 0; i < grid.size(); i++){
                for(int j = 0; j < grid[i].size(); j++){
                    if(grid[i][j] == 0){
                        zeros.push_back(make_pair(i,j));
                    }
                    else{
                        ones.push_back(make_pair(i,j));
                    }
                }
            }
            if(ones.size() == 0 || zeros.size() == 0){
                return -1;
            }
            else{
                for(auto zero : zeros){
                    for(auto one : ones){
                        if(mn > (abs(zero.first-one.first)+abs(zero.second-one.second))){
                            mn = (abs(zero.first-one.first)+abs(zero.second-one.second));
                        }
                    }
                    if(mx < mn){
                        mx = mn;
                    }
                    mn = 99999999999;
                }
                return mx;
            }
        }
    };