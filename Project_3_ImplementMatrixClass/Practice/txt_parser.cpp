# include <iostream>
#include <fstream>
#include<vector>
#include<string>
#include <sstream>

using namespace std;

int main()
{
    string line;
    stringstream ss;

    vector <vector <float>> matrix;

    vector <float> row;

    float i;

    ifstream matrixfile ("matrix.txt");

    if(matrixfile.is_open()){
        while(getline (matrixfile, line)){
            ss.clear();
            ss.str("");
            ss.str(line);
            row.clear();


            while(ss >> i){
                row.push_back(i);

                if(ss.peek() == ',' || ss.peek() == ' ' ){

                    ss.ignore();
                }
            }

            matrix.push_back(row);
        }
        matrixfile.close();

        for(int row = 0; row < matrix.size(); row++){
            for(int column = 0; column < matrix[row].size(); column++){
                cout << matrix[row][column] << " ";
            }
            cout << endl;
        }
    }
    else cout << "Unable to open file";


}