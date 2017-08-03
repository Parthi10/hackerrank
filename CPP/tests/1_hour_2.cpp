//g++ -std=c++11 1_hour.cpp && ./a.out
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stdlib.h>
// #include <algorithm>
// #include <cstdlib>
using namespace std;

int addNumbers(int firstNum, int secondNum = 0){
  int sum = firstNum + secondNum;
  return sum;
}
/*you can create two functions with same name
  only condition is parameters should be different

this is called overloading

  */

//pass by reference

void makeMeYoung(int * age){
  cout<<"My current age " << *age << endl;
  *age = 30;
}
int main(){

  //exception handling
  int number = 0;

  try{
    if (number != 0){
      cout<< 2/number<<endl;
    } else throw(number);
  }
  catch(int number){
    cout<< number << " is not valid!" << endl;
  }

  int myAge = 20;
  cout << "My age is located at: " << &myAge <<endl;

  int arr[5] = {4,6,2,9,7};
  int * arrPtr = arr;
  //arrPtr is pointer to first element of arr
  cout << "arr address " << arrPtr << " Value: " << * arrPtr << endl;


  makeMeYoung(&myAge);
  cout<<"My new age " << myAge << endl;


  return 0;
}
