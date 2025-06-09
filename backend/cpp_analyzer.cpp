#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <jsoncpp/json/json.h>

using namespace std;

string read_file_header(const string& path, size_t num_bytes = 64) {
    ifstream file(path, ios::binary);
    if (!file.is_open()) return "";

    vector<unsigned char> buffer(num_bytes);
    file.read(reinterpret_cast<char*>(buffer.data()), num_bytes);
    ostringstream oss;

    size_t bytes_read = file.gcount();
    for (size_t i = 0; i < bytes_read; ++i) {
        oss << hex << setw(2) << setfill('0') << static_cast<int>(buffer[i]) << " ";
        if ((i + 1) % 16 == 0) oss << "\n";
    }

    return oss.str();
}

long get_file_size(const string& path) {
    ifstream file(path, ios::binary | ios::ate);
    return file ? static_cast<long>(file.tellg()) : -1;
}

string analyze(const string& path) {
    Json::Value root;

    string header = read_file_header(path);
    long size = get_file_size(path);

    root["header_preview"] = header;
    root["file_size"] = size;

    if (header.find("4d 5a") == 0) {
        root["heuristic"] = "Possibly a PE executable (MZ header)";
    } else {
        root["heuristic"] = "Unknown or non-PE format";
    }

    Json::StreamWriterBuilder writer;
    return Json::writeString(writer, root);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "{\"error\": \"Usage: ./cpp_analyzer <file_path>\"}" << endl;
        return 1;
    }

    string result = analyze(argv[1]);
    cout << result << endl;
    return 0;
}
