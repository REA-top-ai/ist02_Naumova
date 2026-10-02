#pragma once
#include <string>

namespace colorizer {
    constexpr auto RESET{ "\033[0m" };
    constexpr auto BOLD{ "\033[1m" };
    constexpr auto RED{ "\033[31m" };
    constexpr auto GREEN{ "\033[32m" };
    constexpr auto BLUE{ "\033[34m" };
    constexpr auto CYAN{ "\033[36m" };

    std::string setRGBColor(unsigned char r, unsigned char g, unsigned char b);
    std::string setRGBBackground(unsigned char r, unsigned char g, unsigned char b);
}
