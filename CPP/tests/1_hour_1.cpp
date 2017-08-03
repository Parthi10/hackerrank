//http://www.newthinktank.com/2014/11/c-programming-tutorial/
//g++ -std=c++11 1_hour.cpp && ./a.out
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stdlib.h>
// #include <algorithm>
// #include <cstdlib>
using namespace std;

int main(){
  cout<<"hello world"<<endl;

  const double PI = 3.1415926535;

  char myChar = 'A'; //1 byte
  bool isHappy = false; //or true

  int myAge = 34;
  float favNum = 3.121233; //6 decimal places
  double otherFavNum = 3.123423453456323; //15 decimal places

  cout<< "favNum "<< favNum<<endl;
  cout<<PI<<endl;

  // short int: At least 16 bits
  // long int: At least 32 bits
  // long long int: At least 64 bits
  // unsigned int: same size as signed version
  // long double: not less than double

  cout << "Size of int " << sizeof(myAge)<<endl;
  //syzeof gives size in bytes

  cout<< 4 / 5<<endl;
  cout<< (float) 4 / 5 <<endl;


  int lol=1;
  switch (lol) {

    case 1:
    cout<<"lol is 1"<<endl;
    break;

    case 2:
    cout<<"Lol is 3"<<endl;
    break;

    default:
    cout<<"default ran"<<endl;
  }
    //ternary operator
    //variable = (condition) ? true: false
    int largestNum = (5>2) ? 5 : 2;

    //arrays

    int myNums[5];

    char myName[2][9] = {
      {'r','i','s','h','a','b','h'},//notice it's 7 chars in row 1
      {'a','g','r','a','h','a','r','i'},
    };
    cout<<"firstname "<<myName[0]<<endl;
    cout<<"lastName "<<myName[1]<<endl;

    cout<<"see what's here "<<myName[0][7]<<myName[0][8]<<endl;
    myName[0][7]='z';
    cout<<"see what's here "<<myName[0][7]<<myName[0][8]<<endl;


    //random number

    int randNum = (rand() % 100) + 1;
    while (randNum!=67){
      cout<< randNum << ", ";
      randNum = rand() % 100;
    }


    //do while
    string numGuessed;
    int intNumGuessed=0;

    do {
      cout<<"Guess a num between 1 and 10: ";
      getline(cin, numGuessed);
      intNumGuessed = stoi(numGuessed);
      cout<<intNumGuessed<<endl;
    }while(intNumGuessed!=4);
    cout<<"You win"<<endl;

    //strings
    string Bday = "happy birthday";
    cout<<Bday<<endl;
    cout<<Bday.size()<<endl;
    cout<<Bday.empty()<<endl;
    cout<<Bday.append(" lol")<<endl;
    cout<<Bday<<endl;

    string dogString = "dog";
    string catString = "cat";

    //lexicographical comparision
    cout<<dogString.compare(catString)<<endl;
    cout<<catString.compare(dogString)<<endl;
    cout<<dogString.compare(dogString)<<endl;

    string yourName = "Rishabh Agrahari";
    cout<<"yourName "<<yourName<<endl;
    string wholeName = yourName.assign(yourName);//str, starting index, no. of chars
    cout<< "wholeName " << wholeName << endl;
    string firstName = yourName.assign(yourName, 0, 7);//yourName is modified in this
    cout<< "firstName "<<firstName << endl;
    cout<<"yourName " << yourName<<endl;
    int lastNameIndex = wholeName.find("Agra", 0);//(substr, which index to start from)
    cout << "Ind3x of lastName " << lastNameIndex << endl;
    wholeName.insert(6, "LOL");
    cout<<"wholeName "<<wholeName<<endl;
    yourName.erase(3, 2);//3 chars to be del, starting at 2
    cout<<"yourName "<<yourName<<endl;
    yourName.replace(1, 3, "LLL");//strating at 1, replace 3 chars with "LLL"
    cout<<"yourName "<<yourName<<endl;

    //Vectors
    vector <int> myVector(10);
    int arr[5] = {34,56,78,32,12};

    myVector.insert(myVector.begin(), arr, arr+4);//start index, array, number of elements
    cout<<myVector.at(3)<<endl;

    myVector.insert(myVector.begin()+5, 99);
    cout<<myVector.at(5)<<endl;

    myVector.push_back(100);
    cout<<"Last value "<< myVector.back()<<endl;
    cout<<"Front Value "<< myVector.front()<<endl;

    myVector.pop_back();
    myVector.push_back(66);
    cout<<"Last value after push_back "<< myVector.back()<<endl;
    cout<<"Last value after push_back "<< myVector.at(6)<<endl;

    cout<<"Front Value "<< myVector.front()<<endl;
    cout<<"Check if empty "<<myVector.empty()<<endl;
    cout<<"Get size or num of elements "<<myVector.size()<<endl;



  return 0;
}
