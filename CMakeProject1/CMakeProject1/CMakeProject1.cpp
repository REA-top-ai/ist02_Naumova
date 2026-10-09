#include <iostream>
#include <fstream>

using namespace std;

static bool load_file_bytes(const char* path, unsigned char* headers, const int size) {
    std::ifstream file(path, std::ios::binary);

    if (!file) { return false; }

    file.read(reinterpret_cast<char*>(headers), size);
    return true;
}

static bool check_bmp_header(const unsigned char* file) {
    return *file == 'B' && *(file + 1) == 'M';
}

int main(const int argc, char** argv)
{
    const char* path = argc > 1 ? argv[1] : "lena.bmp";

    unsigned char buffer[54]{};

    if (!load_file_bytes(path, buffer, 54)) {
        std::cout << "Failed to load file\n: " << path << std::endl;
    }

    if (!check_bmp_header(buffer)) {
        std::cout << "Failed to load file\n: " << path << std::endl;
    }

    int* filesize = (int*)(buffer + 2);
    int* reserved = (int*)(buffer + 6);
    int* dataoffsets = (int*)(buffer + 10);
    int* sizes = (int*)(buffer + 14);
    int* width = (int*)(buffer + 18);
    int* height = (int*)(buffer + 22);
    short* planes = (short*)(buffer + 26);
    short* bitcount = (short*)(buffer + 28);
    int* compression = (int*)(buffer + 30);
    int* imagesize = (int*)(buffer + 34);
    int* xpixelsperm = (int*)(buffer + 38);
    int* ypixelsperm = (int*)(buffer + 42);
    int* colorused = (int*)(buffer + 46);
    int* colorsimportant = (int*)(buffer + 50);

    std::cout << "filesize " << *filesize << std::endl;
    std::cout << "reserved " << *reserved << std::endl;
    std::cout << "dataoffsets " << *dataoffsets << std::endl;
    std::cout << "sizes " << *sizes << std::endl;
    std::cout << "width " << *width << std::endl;
    std::cout << "height " << *height << std::endl;
    std::cout << "planes " << *planes << std::endl;
    std::cout << "bitcount " << *bitcount << std::endl;
    std::cout << "compression " << *compression << std::endl;
    std::cout << "imgsize " << *imagesize << std::endl;
    std::cout << "x " << *xpixelsperm << std::endl;
    std::cout << "y " << *ypixelsperm << std::endl;
    std::cout << "colorused " << *colorused << std::endl;
    std::cout << "colorsimp " << *colorsimportant << std::endl;

    return 0;
}