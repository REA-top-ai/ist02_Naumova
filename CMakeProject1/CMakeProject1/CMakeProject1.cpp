#include "CMakeProject1.h"   
#include <iostream>
#include <fstream>

#define ERR_IF_FALSE(check, err_message, arg) if (!(check)) { std::cout << err_message << arg << std::endl; return 1;}

constexpr auto ERR_CANT_READ_FILE{ "Failed to load file\n: " };

#pragma pack(push, 1) 
struct BMPHeader {
    char sign[2];
    int filesize;
    int reserved;
    int dataoffset;
    int size;
    int width;
    int height;
    short planes;
    short bitcount;
    int compression;
    int imagesize;
    int xpixelsperm;
    int ypixelsperm;
    int colorused;
    int colorsimportant;
};

struct Pixel {
    unsigned char blue;
    unsigned char green;
    unsigned char red;
};
#pragma pack(pop)

static const Pixel* get_pixel(const Pixel* pixels, const int x, const int y, const int width) {
    return pixels + y * width + x;
}

static bool load_file_bytes(const char* path, unsigned char* headers, const int size, int offset = 0) {
    std::ifstream file(path, std::ios::binary);

    if (!file) {
        return false;
    }

    file.seekg(offset, std::ios::beg);
    file.read(reinterpret_cast<char*>(headers), size);
    return true;
}

static bool check_bmp_header(const unsigned char* file) {
    return *file == 'B' && *(file + 1) == 'M';
}

int main(const int argc, char** argv)
{
    
    const char* path = argc > 1 ? argv[1] : "lena.bmp";
    std::cout << path << std::endl;

    BMPHeader* header = new BMPHeader();

    ERR_IF_FALSE(load_file_bytes(path, reinterpret_cast<unsigned char*>(header), sizeof(BMPHeader)), ERR_CANT_READ_FILE, path)
        ERR_IF_FALSE(check_bmp_header(reinterpret_cast<unsigned char*>(header)), ERR_CANT_READ_FILE, path)

        std::cout << "filesize " << header->filesize << std::endl;
    std::cout << "reserved " << header->reserved << std::endl;
    std::cout << "dataoffsets " << header->dataoffset << std::endl;
    std::cout << "sizes " << header->size << std::endl;
    std::cout << "width " << header->width << std::endl;
    std::cout << "height " << header->height << std::endl;
    std::cout << "planes " << header->planes << std::endl;
    std::cout << "bitcount " << header->bitcount << std::endl;
    std::cout << "compression " << header->compression << std::endl;
    std::cout << "imgsize " << header->imagesize << std::endl;
    std::cout << "x " << header->xpixelsperm << std::endl;
    std::cout << "y " << header->ypixelsperm << std::endl;
    std::cout << "colorused " << header->colorused << std::endl;
    std::cout << "colorsimp " << header->colorsimportant << std::endl;

    const auto pixels = new Pixel[header->height * header->width];

    load_file_bytes(path, reinterpret_cast<unsigned char*>(pixels), header->imagesize, header->dataoffset);

    auto pix_l_t = get_pixel(pixels, 0, 0, header->width);
    auto pix_r_t = get_pixel(pixels, header->width - 1, 0, header->width);

    auto pix_l_b = get_pixel(pixels, 0, header->height - 1, header->width);
    auto pix_r_b = get_pixel(pixels, header->width - 1, header->height - 1, header->width);

    std::cout << "Pixel left bottom: " << (int)pix_l_b->red << " "
        << (int)pix_l_b->green << " "
        << (int)pix_l_b->blue << " "
        << std::endl;

    std::cout << "Pixel right bottom: " << (int)pix_r_b->red << " "
        << (int)pix_r_b->green << " "
        << (int)pix_r_b->blue << " "
        << std::endl;

    std::cout << "Pixel left top: " << (int)pix_l_t->red << " "
        << (int)pix_l_t->green << " "
        << (int)pix_l_t->blue << " "
        << std::endl;

    std::cout << "Pixel right top: " << (int)pix_r_t->red << " "
        << (int)pix_r_t->green << " "
        << (int)pix_r_t->blue << " "
        << std::endl;

    delete[] pixels;
    delete header; 

    return 0;
}