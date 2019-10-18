#include <stdio.h>
#include <string>
class Test {
    int age;
    std::string name;
};
int main() {
    Test* t = new Test();
    delete t;
    Test* t2 = new Test();
    printf("%p - %p\n", t, t2);
    delete t2;
}