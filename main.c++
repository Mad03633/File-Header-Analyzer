#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <string>
#include <cctype>

using namespace std;

string toLower(const string &str) {
    string result = str;
    transform(result.begin(), result.end(), result.begin(), ::tolower);
    return result;
}

struct FileInfo {
    string filename;
    string header;
};

vector<FileInfo> readFilenamesCSV(const string& filepath) {
    vector<FileInfo> files;
    ifstream file(filepath);
    if (!file.is_open()) {
        cerr << "Error: Could not open " << filepath << endl;
        return files;
    }
    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string filename, header;
        if (getline(ss, filename, ',') && getline(ss, header, ',')) {
            files.push_back({filename, header});
        }
    }
    file.close();
    return files;
}

unordered_set<string> readVirusHeadersCSV(const string& filepath) {
    unordered_set<string> virusHeaders;
    ifstream file(filepath);
    if (!file.is_open()) {
        cerr << "Error: Could not open " << filepath << endl;
        return virusHeaders;
    }
    string line;
    while (getline(file, line)) {
        virusHeaders.insert(toLower(line));
    }
    file.close();
    return virusHeaders;
}

void sortFilesByHeader(vector<FileInfo>& files) {
    sort(files.begin(), files.end(), [](const FileInfo& a, const FileInfo& b) {
        return a.header < b.header;
    });
}

void checkForViruses(const vector<FileInfo>& files, const unordered_set<string>& virusHeaders) {
    for (const auto& file : files) {
        string headerLower = toLower(file.header);
        for (const auto& virusSig : virusHeaders) {
            if (headerLower.find(virusSig) != string::npos) {
                cout << "[WARNING] File '" << file.filename 
                     << "' has a header indicating a potential virus: " << file.header << endl;
                break;
            }
        }
    }
}

int main() {
    string filenamesCSV = "data-files\\filenames.csv";
    string virusnamesCSV = "data-files\\virusenames.csv";

    // Read data from CSV files
    vector<FileInfo> files = readFilenamesCSV(filenamesCSV);
    unordered_set<string> virusHeaders = readVirusHeadersCSV(virusnamesCSV);

    // Sort files by header
    sortFilesByHeader(files);

    // Check for viruses using substring matching
    checkForViruses(files, virusHeaders);

    return 0;
}
