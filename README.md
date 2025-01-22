# Oyanami
TODO: Overview

## Build It Yourself!
The Oyanami board is open-source. You can grab the Gerber files from [the Releases page](https://github.com/barbeque/oyanami-msx-megarom/releases) and send those to a fabricator of your choice.

Recommended settings: 

 - ENIG or Hard Gold finishing
 - Beveled or chamfered edge connector

## Known Working Games
 - Contra (MSX2)
 - F1 Spirit
 - Nemesis
 - Nemesis 2
 - Parodius
 - Salamander
 - Spy vs. Spy II (64kB Konami-mapper version)
 - The Fairyland Story
 - The Maze of Galious: Knightmare 2
 - Treasure of USAS (MSX2)
 - Vampire Killer (MSX2)

This is an incomplete list, please submit pull requests for any other games you have tested.

## Bill of Materials

| Position | Component     | Digi-Key link      | Comments  |
|----------|---------------|--------------------|-----------|
| U1       | SST39SF040 DIP EEPROM | | |
| U3       | 74LS670 DIP | | |
| U4       | 74LS02 DIP | | |
| C...     | 0.1µF through-hole ceramic capacitor | | |
| RN1      | 10kΩ x 8 (9-pin SIP) resistor network | | |
| SW1      | 2-pin DIP switch | | |

I also recommend getting a case for the PCB from somewhere like [Retro Game Restore](https://retrogamerestore.com/store/msx_cart_shell).

Beware! Using socketed ICs may not leave enough vertical height for a standard Konami-style cartridge case to close.
