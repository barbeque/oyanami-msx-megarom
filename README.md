# Oyanami
TODO: Overview

This project was built as part of a [Leaded Solder blog](https://www.leadedsolder.com/) entry.

Articles so far about this project:
 - [Oya, I've heard of Mega-ROMs](https://www.leadedsolder.com/2024/09/03/msx-megarom-oyanami.html)

If it's useful to you, please consider supporting the blog through Patreon or Ko-Fi. All money goes directly to future projects like this.

## Build It Yourself!
The Oyanami board is open-source. You can grab the Gerber files from [the Releases page](https://github.com/barbeque/oyanami-msx-megarom/releases) and send those to a fabricator of your choice.

Recommended settings: 

 - ENIG or Hard Gold finishing
 - Beveled or chamfered edge connector

## Known Working Games
 - 1942 (MSX2 version only)
 - Arkanoid 2 - Revenge of DOH
 - Ashguine Story I
 - Bubble Bobble
 - Contra (MSX2; CRC32: 4e82660d)
 - Cyborg Z
 - Digital Devil Story
 - Dragon Buster
 - Dragon Quest 1 (both MSX1, MSX2 versions)
 - Druid
 - F1 Spirit
 - Family Billiards
 - Fantasy Zone 1
 - Final Zone Wolf
 - Ganbare Goemon
 - Gangjeol Robocop
 - Genesis - Dawn of a New Day
 - Hai No Majutsushi
 - Hinotori
 - King Kong 2
 - King's Valley 2 Edit Contest Edition
 - King's Valley 2 (MSX2 only)
 - Metal Gear (CRC32: e85c5731)
 - Mr. Ninja Ashura's Chapter
 - Nemesis (CRC32: 4dfcc009)
 - Nemesis 2
 - Parodius
 - Pengo
 - Penguin Adventure
 - Pennant Race
 - Return of Jelda
 - Salamander
 - Spy vs. Spy II (64kB Konami-mapper version)
 - Seikima 2 Special - Tetsuji
 - Street Master
 - Super Bioman 4
 - Super Boy 3
 - Super Runner
 - Tengoku Yoitoko - Heaven
 - The Fairyland Story
 - The Fantasm Soldier Valis
 - The Maze of Galious: Knightmare 2
 - Topple Zip MSX2
 - Treasure of USAS (MSX2)
 - Vampire Killer (MSX2)
 - Wonsiin
 - Young Sherlock: Legacy of Doyle

This is an incomplete list, please submit pull requests for any other games you have tested.

## Bill of Materials

| Position | Component     | Digi-Key link      | Comments  |
|----------|---------------|--------------------|-----------|
| U1       | SST39SF040 DIP EEPROM | | |
| U3       | 74LS670 DIP | | Do not use ALS, see below |
| U4       | 74LS02 DIP | | |
| C...     | 0.1µF through-hole ceramic capacitor | | |
| RN1      | 10kΩ x 8 (9-pin SIP) resistor network | | |
| SW1      | 2-pin DIP switch | | |

I also recommend getting a case for the PCB from somewhere like [Retro Game Restore](https://retrogamerestore.com/store/msx_cart_shell).

Beware! Using socketed ICs may not leave enough vertical height for a standard Konami-style cartridge case to close.

74ALS670 has been reported not to work with MSX Turbo-R systems. Please use only the LS variant.

## Version History
### v1.2: In development
Still in development. Adds write-enable pin to ROM to support in-MSX reflashing.

### v1.1: July 2024
Initial working version. Supports read-only games.

## Special Thanks
 - bsittler for the help and inspiration to get this figured out;
 - Pax for CRC32s;
 - Annual_Bottle_4639 on Reddit for testing additional games
