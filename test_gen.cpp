#include <iostream>
#include <string>
#include <sstream>

template<typename TData>
class Foo
{
public:
  typedef Foo Self;
  typedef TData Data;
  Foo();
  // just a comment
  Data getData(int i, char const* s);
private:
  /// my precious data
  Data m_data;
};

typedef Foo<int> IntFoo;
using Steve = Foo<float>;

using namespace std;

void add(int a, int b) {
	std::stringstream ss;
	ss << a << " + " << b << " = " << (a+b) << "!\n";
	std::string m(ss.str());
	std::cout << m << "\n";
}

int main() {
	add(3,5);
}
