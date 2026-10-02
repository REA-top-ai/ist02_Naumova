#include "bitmap.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

namespace colorizer {
    std::string setRGBColor(unsigned char r, unsigned char g, unsigned char b) {
        return "\033[38;2;" + std::to_string(r) + ";" + std::to_string(g) + ";" + std::to_string(b) + "m";
    }
    std::string setRGBBackground(unsigned char r, unsigned char g, unsigned char b) {
        return "\033[48;2;" + std::to_string(r) + ";" + std::to_string(g) + ";" + std::to_string(b) + "m";
    }
}

#define PRINT_INFO(MESSAGE) std::cout << colorizer::BOLD << colorizer::CYAN << MESSAGE << colorizer::RESET
#define PRINT_ERROR(MESSAGE) std::cerr << colorizer::RED << MESSAGE << colorizer::RESET << std::endl
#define PRINT_HEADER(VAR) std::cout << colorizer::GREEN << sizeof(VAR) << "b "#VAR" : " << colorizer::BLUE << VAR << colorizer::RESET << std::endl
#define PRINT_COLORED_PIXEL(R,G,B) std::cout << colorizer::setRGBColor(R, G, B) << "R:" << static_cast<int>(R) << " G:" << static_cast<int>(G) << " B:" << static_cast<int>(B) << colorizer::RESET << std::endl

constexpr static auto FILE_CANT_OPEN = R"(Error: Could not open file.)";
constexpr static auto FILE_IS_NOT_A_BITMAP = R"(file is not a bitmap)";

#pragma pack(push, 1)
struct BitmapHeaders {
    char bitmap_signature[2]{};
    int bitmap_file_size{ 0 };
    int reserved{ 0 };
    int bitmap_data_offset{ 0 };
    int bitmap_info_header_size{ 0 };
    int bitmap_width{ 0 };
    int bitmap_height{ 0 };
    short bitmap_planes{ 0 };
    short bitmap_bits_per_pixel{ 0 };
    int bitmap_compression{ 0 };
    int bitmap_image_size{ 0 };
    int bitmap_XpixelsPerM{ 0 };
    int bitmap_YpixelsPerM{ 0 };
    int bitmap_ColorsUsed{ 0 };
    int bitmap_ColorsImportant{ 0 };
};
#pragma pack(pop)

struct Pixel24 {
    unsigned char b{};
    unsigned char g{};
    unsigned char r{};
};

struct PaletteEntry {
    unsigned char b, g, r, reserved;
};

static bool load_raw_file_data(const char* path, unsigned char* file_data, const int size, const int pos = 0) {
    std::ifstream file(path, std::ios::binary);
    if (!file) { return false; }
    file.seekg(pos);
    file.read(reinterpret_cast<char*>(file_data), size);
    return true;
}

static void print_bitmap_headers(const BitmapHeaders* h) {
    PRINT_HEADER(h->bitmap_signature);
    PRINT_HEADER(h->bitmap_file_size);
    PRINT_HEADER(h->bitmap_data_offset);
    PRINT_HEADER(h->bitmap_info_header_size);
    PRINT_HEADER(h->bitmap_width);
    PRINT_HEADER(h->bitmap_height);
    PRINT_HEADER(h->bitmap_planes);
    PRINT_HEADER(h->bitmap_bits_per_pixel);
    PRINT_HEADER(h->bitmap_compression);
    PRINT_HEADER(h->bitmap_image_size);
    PRINT_HEADER(h->bitmap_XpixelsPerM);
    PRINT_HEADER(h->bitmap_YpixelsPerM);
    PRINT_HEADER(h->bitmap_ColorsUsed);
    PRINT_HEADER(h->bitmap_ColorsImportant);
}

static Pixel24 get_pixel_color(int x, int y, const std::vector<unsigned char>& data,
    const BitmapHeaders& headers, const std::vector<PaletteEntry>& palette) {
    Pixel24 color = { 0, 0, 0 };
    int bpp = headers.bitmap_bits_per_pixel;
    int row_size = ((headers.bitmap_width * bpp + 31) / 32) * 4;

    int real_y = (headers.bitmap_height > 0) ? (headers.bitmap_height - 1 - y) : y;
    int row_offset = real_y * row_size;

    if (bpp == 24) {
        int off = row_offset + x * 3;
        if (off + 2 < (int)data.size()) {
            color.b = data[off];
            color.g = data[off + 1];
            color.r = data[off + 2];
        }
    }
    else if (bpp == 8) {
        int off = row_offset + x;
        if (off < (int)data.size()) {
            unsigned char idx = data[off];
            if (idx < palette.size()) color = { palette[idx].r, palette[idx].g, palette[idx].b };
        }
    }
    else if (bpp == 4) {
        int off = row_offset + x / 2;
        if (off < (int)data.size()) {
            unsigned char byte = data[off];
            unsigned char idx = (x % 2 == 0) ? (byte >> 4) : (byte & 0x0F);
            if (idx < palette.size()) color = { palette[idx].r, palette[idx].g, palette[idx].b };
        }
    }
    else if (bpp == 1) {
        int off = row_offset + x / 8;
        if (off < (int)data.size()) {
            unsigned char byte = data[off];
            unsigned char idx = (byte >> (7 - (x % 8))) & 0x01;
            if (idx < palette.size()) color = { palette[idx].r, palette[idx].g, palette[idx].b };
        }
    }
    return color;
}

int main(int argc, char** argv) {
    const char* path = (argc > 1) ? argv[1] : "images/image.bmp";

    BitmapHeaders headers{};
    if (!load_raw_file_data(path, reinterpret_cast<unsigned char*>(&headers), sizeof(BitmapHeaders))) {
        PRINT_ERROR(FILE_CANT_OPEN);
        return 1;
    }

    if (headers.bitmap_signature[0] != 'B' || headers.bitmap_signature[1] != 'M') {
        PRINT_ERROR(FILE_IS_NOT_A_BITMAP);
        return 1;
    }

    print_bitmap_headers(&headers);

    std::vector<PaletteEntry> palette;
    int colors_used = headers.bitmap_ColorsUsed;
    if (colors_used == 0 && headers.bitmap_bits_per_pixel <= 8) {
        colors_used = 1 << headers.bitmap_bits_per_pixel;
    }
    if (colors_used > 0 && headers.bitmap_bits_per_pixel <= 8) {
        palette.resize(colors_used);
        int palette_offset = 14 + headers.bitmap_info_header_size;
        load_raw_file_data(path, reinterpret_cast<unsigned char*>(palette.data()),
            colors_used * sizeof(PaletteEntry), palette_offset);
    }

    std::vector<unsigned char> pixels(headers.bitmap_image_size);
    if (!load_raw_file_data(path, pixels.data(), headers.bitmap_image_size, headers.bitmap_data_offset)) {
        PRINT_ERROR(FILE_CANT_OPEN);
        return 1;
    }

    int w = headers.bitmap_width;
    int h = std::abs(headers.bitmap_height);

    auto print_corner = [&](int x, int y, const char* name) {
        Pixel24 p = get_pixel_color(x, y, pixels, headers, palette);
        PRINT_INFO(name);
        PRINT_COLORED_PIXEL(p.r, p.g, p.b);
        };

    print_corner(0, h - 1, "bottom-left: ");
    print_corner(w - 1, h - 1, "bottom-right: ");
    print_corner(0, 0, "upper-left: ");
    print_corner(w - 1, 0, "upper-right: ");

    return 0;
}