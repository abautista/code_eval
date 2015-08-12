#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

vector <vector<int> > table;

void create_table(int m)
{
  vector<int> *row;
  for (int i = 0; i < m; i++) {
    row = new vector<int>();
    for (int j = 0; j <= i; j++) {
      if (i == j || j == 0) {
	row->push_back(1);
      } else {
	row->push_back(table[i-1][j-1] + table[i-1][j]);
      }
    }
    table.push_back(*row);
  }
}

void print_triangle(int m)
{
  for (int i = 0; i < m; i++) {
    for (int j = 0; j <= i; j++) {
      cout << table[i][j] << " ";
    }
  }
  cout << endl;
}

int main(int argc, char *argv[])
{
  int max_depth = 0;
  FILE *fp = fopen(argv[1], "r");
  char line[200];
  vector<int> depths;
  
  while (fgets(line, sizeof(line), fp)) {
    int depth;
    sscanf(line, "%d", &depth);
    depths.push_back(depth);
    if (depth > max_depth) {
      max_depth = depth;
    }
  }

  create_table(max_depth);
  vector<int>::iterator it;
  
  for (it = depths.begin(); it != depths.end(); it++) {
    print_triangle(*it);
  }
}
