#include "iostream"
#include "fstream"
#include "sstream"
#include "vector"

using namespace std;

string readLine(string &line) {
  stringstream ss(line);
  string token, lastToken;
  vector<string> tokens;

  while (getline(ss, token, ',')) {
    if (lastToken.empty() || token != lastToken) {
      tokens.push_back(token);
    }
    lastToken = token;
  }

  vector<string>::iterator tokensIter;
  ostringstream result;
  for (tokensIter = tokens.begin(); tokensIter != tokens.end(); ++tokensIter) {
    if (tokensIter != tokens.begin()) result << ",";
    result << *tokensIter;
  }
  result << endl;
  return result.str();
}

int main(int argc, char *argv[]) {
  string line;
  ifstream ifs(argv[1]);

  while (getline(ifs, line)) {
    cout << readLine(line);
  }
}