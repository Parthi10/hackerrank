#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
    public:
        string name;
        int age;

        virtual void getdata(){};
        virtual void putdata(){};
};

class Professor : public Person{
    public:
        int publications;
        int id;
        static int cur_id;

        void getdata(){
            cin>>name>>age>>publications;
            id=cur_id;
        }
        void putdata(){
            cout<<name<<" "<<age<<" "<<publications<<" " <<id<<endl;
        }

    Professor(){
        cur_id++;
    }
};
int Professor::cur_id=0;

class Student : public Person{
    public:
        int marks[6];
        int id;
        static int cur_id;

    void getdata(){
        cin>>name>>age;
        for(int x=0; x<6; x++){
            cin>>marks[x];
        }
        id=cur_id;

    }
    void putdata(){
        int sum = 0;
        for(int x=0; x<6; x++){
            sum += marks[x];
        }
        cout<<name<<" "<<age<<" "<<sum<<" "<<id<<endl;
    }

    Student(){
        cur_id++;
    }
};
int Student::cur_id=0;
int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
