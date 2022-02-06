#include<iostream>
#include<vector>
#include<string>

using namespace std;

vector<float> p = {0.2, 0.2, 0.2, 0.2, 0.2};
vector<string> measurements = {"red", "green"};
vector<int> motions = {1,1};
float pHit = 0.6;
float pMiss = 0.2;
float pExact = 0.8;
float pOvershoot = 0.1;
float pUndershoot = 0.1;
vector<string> world = {"green", "red", "red", "green", "green"};

vector<float> sense(vector<float> p, string Z){

    vector<float> q;
    for(int i = 0; i<p.size(); i++){
        bool hit = (Z == world[i]);
        q.push_back(p[i] * (hit * pHit + (1-hit) * pMiss));
        float s = 0;
        for(int i = 0; i<q.size(); i++){
            s += q[i];
            q[i] = q[i] / s;
        }
        
        return q;
    } 
}


vector<float> move(vector<float> p, float U){
    vector<float> q;
    for(int i=0; i<p.size(); i++){
        
        float s = pExact * p[(i-U) % p.size()];
        s = s + pOvershoot * p[(i-U-1) % len(p)];
        s = s + pUndershoot * p[(i-U+1) % len(p)];
        q.push_back(s);
    }        
    return q;
}

int main(){

    for(int i=0;i<measurements.size(); i++){
        p = sense(p, measurements[i]);
        p = move(p, motions[i]);

    } 

    cout << p << endl;

}