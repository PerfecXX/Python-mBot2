#!/bin/bash
# Clone Pixy2 repository and build PixyMon

cd ~
git clone https://github.com/charmedlabs/pixy2.git
cd pixy2/scripts
./build_pixymon_src.sh
