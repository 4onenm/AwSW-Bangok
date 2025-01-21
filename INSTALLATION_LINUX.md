Mod installation on Linux requires significantly more manual effort. This guide will start with an overview of concepts, then drill down into the specific install procedure necessary to get BangOk working with all requirements.

# Concepts

## Steam Workshop and the AwSW Modtools

The Steam Workshop is a platform for distributing mods for games on Steam. It is integrated into the Steam client, and allows users to subscribe to mods for games they own. When a user subscribes to a mod, the mod is downloaded to the user's computer and automatically updated when the mod author releases a new version.

One condition of the author of AwSW allowing a Steam Workshop for AwSW is that the mods are validated by a leader of the modding community for safety and prohibited content. This validation comes in the form of an invisible "signature" attached to mods that have been checked. The Windows copy of the modtools will only install Steam Workshop mods that have been signed in this way.

The Linux modtools have no ability to validate this signature, so do not automatically install Steam Workshop mods. Instead, the user must manually copy the mod files from the Steam Workshop directory to the game's `mods` directory. The user must also manually install the modloader, and manually install mod updates.

**Safety and content of Steam Workshop mods is not guaranteed by the modtools when operating on Linux.** The user must take care to only install mods from authors they trust, as unsigned updates may be downloaded from the Steam Workshop automatically and may contain malicious code.

## Mod Installations

To install a mod, it must be placed in the `game/mods` directory of the game. This directory is created by the modloader installation process, and is where the modloader looks for mods to load. Each mod _must_ have an `__init__.py` file in its root directory, which is used by the modloader to load the mod. If upon opening a mod you don't see that file, the mod may have been unpacked as a folder inside a folder. Move the contents of the inner folder to the outer folder to fix this.

## AwSW App ID

Every game and software on Steam has a unique numeric identifier, called an "App ID". This is a number that is used by the Steam client to identify the game. The App ID for Angels with Scaly Wings is `571880`. This number is used in the directory structure of the Steam Workshop directory, and is also used in the URL of the game's page on the Steam store.

## Steam Mod IDs

Every mod on the Steam Workshop has a unique numeric identifier, which this guide will refer to as a "Mod ID". This is a number that is used by the Steam client to identify the mod. The mod ID is used as the name of the directory where the mod is stored in the Steam Workshop directory. The mod ID is also part of the URL of the mod's page on the Steam Workshop.

## Relevant Locations

The default installation location of Steam on Linux distributions with which I have familiarity is `~/.local/share/Steam`. This guide will assume this is the root directory where the Steam client is installed. For alternative setups, replace this part with the path to your Steam installation.

The `steamapps` directory inside this is where all game data is stored. For our purposes modding Angels with Scaly Wings, 4 directories will be relevant:

* `~/.local/share/Steam/steamapps/workshop/content/571880` (henceforth "the Workshop directory") - This is the root directory of all mods downloaded from the Steam Workshop. Each mod is stored in a separate directory here, numbered by their "Mod ID"
* `~/.local/share/Steam/steamapps/common/Angels with Scaly Wings` (henceforth "the Install directory") - This is the root directory of the game. **You can get here with the "Browse Local Files" button in the Steam client.** If you do not know where your Steam installation is located, you can find it by right-clicking the game in the Steam client, selecting "Properties", then "Local Files", then "Browse Local Files" to get here, then figure out the rest of the paths from here.
* `~/.local/share/Steam/steamapps/common/Angels with Scaly Wings/game` (henceforth "the `game` directory") - This is the directory where the modloader and mods must be installed. **This is the most important directory for modding the game.** Installing the modloader a directory above this will not work.

# Installation

## Modloader

### Choose your modloader

There are two ways to get the modloader for Angels with Scaly Wings on Linux. The first is to download the modtools from the [installation instructions](https://awsw-modding.github.io/AWSW-Modtools/installation.html) and extract them. The second is to subscribe to the [Modtools mod](https://steamcommunity.com/sharedfiles/filedetails/?id=1305731599) (Mod ID `1305731599`) mod on the Steam Workshop, which will download the modloader to your computer. The second method should be easier, as it will help prepare you for installing other Steam Workshop mods.

#### Downloaded modtools

If you downloaded the modtools from the website, extract the contents of the archive to a directory of your choice. Inside the extracted directory will be the two folders and one file that you will need to copy to the `game` directory to install, along with some auxiliary files that you can ignore.

#### Subscribed modtools

If you subscribed to the Modtools mod, the modloader will be downloaded to the Workshop directory. The modloader will be in a directory named `1305731599`. This method should not have any auxiliary files, just the two folders and one file that you need to copy to the `game` directory to install. 
Copy the contents of this directory to the `game` directory.

### Install the modloader

From your chosen source, copy the following files and directories to the `game` directory:

* `modloader` - This is the modloader itself. Copy this to the `game` directory.
* `mods` - This is the directory where mods are stored. Copy this to the `game` directory. It should already have one mod inside, named `core`.
* `modloader_error_handling.rpe` - This is a file that helps the modloader display error messages for you instead of silently crashing. Copy this to the `game` directory.

You should now be able to run the game with the modloader installed. On the main menu, there should be a new button in the lower left corner that says "MODS." If you click this button, you should see a list of mods that are installed, which for now is just the `core` mod. If you see this, the modloader is installed correctly.

## Steam Workshop Mods

This guide will describe installing Steam Workshop mods in general and leave it to you to select the requirements for BangOk you would like to install through this method and which you would like to download and install from external sources.

### Subscribe

To install a Steam Workshop mod, you must first subscribe to it on the Steam Workshop. To do this, go to the mod's page on the Steam Workshop and click the "Subscribe" button. This should start the download of the mod to your computer. If it doesn't, try launching and closing the game or unsubscribing and resubscribing to the mod.

### Find the mod

The mod will be downloaded to the Workshop directory. The mod will be in a directory named by its Mod ID. You can find the Mod ID by looking at the URL of the mod's page on the Steam Workshop. For example, the URL `https://steamcommunity.com/sharedfiles/filedetails/?id=1234567890` has a Mod ID of `1234567890`.

### Install the mod

For any mod EXCEPT THE MODTOOLS (Mod ID `1305731599`): Copy the directory of the mod from the Workshop directory to the `game/mods` directory, which should have been created when you installed the modtools. The mod should have an `__init__.py` file in its root directory. If it does not, the mod may have been unpacked as a folder inside a folder. Move the contents of the inner folder to the outer folder to fix this.

For the modtools, see the section on installing the modtools.

## External Mods

For mods that are not on the Steam Workshop, you will need to download the mod from the mod author's website or another source. The mod should be distributed as a `.zip` or `.rar` archive. Extract the contents of the archive to a directory of your choice. The mod should have an `__init__.py` file in its root directory. If it does not, the mod may have been unpacked as a folder inside a folder. Move the contents of the inner folder to the outer folder to fix this.

Copy the directory of the mod to the `game/mods` directory, which should have been created when you installed the modtools. Once in the `mods` directory, check again for the `__init__.py` file inside to make sure the mod is installed correctly.

BangOk is an external mod, so you will need to download it from the [BangOk GitHub page](./README.md) and install it manually through this method.

# Updating Mods

When an update to a mod is released, simply delete the old version of the mod from the `game/mods` directory and install the new version in its place. The modloader will then load the new version of the mod when you start the game.

Note that the modloader will not automatically update mods for you. You must manually download and install updates to mods.

Individual playthroughs' save files may become incompatible and fail to load when a mod is installed, removed, or updated. If this happens, you may need to start a new game to continue playing. Your "persistent" save data (between playthroughs) should _not_ be affected by this effect (though any changes to persistent data performed by a mod will persist.)

# Assorted additional notes

* <https://youtu.be/zqYgPf4u2yc> this tutorial tells you how to get Windows-like save data on SteamOS. Instead of going into the folder `compatdata`, at that point go to the folder `common`, then `Angels with Scaly Wings`. This is your Installation directory, which should have the `game` directory inside it. You are now ready to perform the rest of the steps in this guide.
* If you have any issues with the modloader, you can try running the game from the terminal to see any error messages that are printed but not captured by the modloader's error screen. To do this, open a terminal and navigate to the Installation directory. Then run `./lib/linux-x86_64/python -O "Angels with Scaly Wings.py"` to start the game.
  * Command breakdown:
    * `./lib/linux-x86_64/python` is the specific Python 2.7 binary that the Angels with Scaly Wings game engine requires. If you have a different Python 2.7 binary installed on your system, you may attempt to use it instead, but it will need to know where to get the `renpy` module from the folder above. This version of the `renpy` engine is not equipped to work with Python 3.
    * `-O` is a flag that tells Python to run the game in "optimized" mode, which may improve performance slightly. Some parts of the Ren'Py engine have been observed to misbehave without this flag.
    * `"Angels with Scaly Wings.py"` is the main game script, which loads and runs the game.
  * This launch method may not work on ARM-based systems that require additional commands to launch x86_64 applications under emulation. If you are in that situation, may God have mercy on your soul, because I can't help you.
* Not all mods are compatible with each other. Mod authors do their best to specify this in a way the modloader understands. If you encounter an error message the moment the game window appears, take a moment to read what it says. It may indicate a mod dependency is missing or that two mods cannot be loaded together.