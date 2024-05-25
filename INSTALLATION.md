
# Installation

## Steam + Windows

1. Subscribe to the "Modtools" mod on Steam (if you have not already)
    * Wait for the download to complete
    * Launch the game
    * Verify the "Mods" button has appeared on the main menu
    * Exit the game
2. Subscribe to the "Magmalink" mod on Steam (if you have not already)
    * Wait for the download to complete
    * Launch the game
    * Click "Mods" on the main menu
    * Verify "Magmalink" has been added to the list
    * Exit the game
3. Subscribe to the "Community Resource and Assets Pack (CRAP!)" mod on Steam (if you have not already)
    * Wait for the download to complete
    * Launch the game
    * Click "Mods" on the main menu
    * Verify "Community Resource and Assets Pack" has been added to the list
    * Exit the game
4. Download the BangOk zip from the USERS download link in the README
    * Note: This is the same as if you click the green GitHub "Code" button and select "Download ZIP"
5. Extract the BangOk zip into a folder
    * For most Windows users, you can right click the BangOk zip and select "Extract All..."
6. Verify that when you double click on the BangOk folder, you see files inside like `bangok_four_bryce1.rpy`. (Make sure it isn't a folder inside another folder.)
    * If you see a folder inside the BangOk folder, move the contents of that folder up one level.
7. Install BangOk into the game
    * Open Steam
    * Right click Angels
    * Manage > Browse Local Files
    * Click down into the `game` folder
    * Click down into the `mods` folder
    * Drag the extracted BangOk folder into the `mods` folder, next to `core` and those ones that are a bunch of numbers.
8. Enjoy
    * Launch the game. You should immediately see a NSFW toggle screen and a "BangOk"-specific new player message from System. These only appear on your first boot of the mod.

## Everything Else

The Steam Workshop for Angels with Scaly Wings is only available on Windows. If you are using a different platform, you will need to download the mods from their sources and install them manually. A manual installation of the modtools is required, but not described here. See the [modtools' installation instructions](https://awsw-modding.github.io/AWSW-Modtools/installation.html) for more on getting to that point.

1. Download and install the modtools (Not covered here)
2. Download MagmaLink from the links in our README
    * Extract the zip
        * Ensure the extracted folder contains an `__init__.py` file along with other files and folders. It should not be a single folder inside another folder.
    * Move the extracted folder to the `mods` folder in the game directory, next to the `core` mod.
3. Download CRAP from the links in our README
    * Extract the zip
        * Ensure the extracted folder contains an `__init__.py` file along with other files and folders. It should not be a single folder inside another folder.
    * Move the extracted folder to the `mods` folder in the game directory, next to the `core` mod.
4. Download BangOk from the USERS download link in the README
    * Extract the zip
        * Ensure the extracted folder contains files like `__init__.py`. It should not be a single folder inside another folder.
    * Move the extracted folder to the `mods` folder in the game directory, next to the `core` mod.
5. Enjoy
    * Launch the game. You should immediately see a NSFW toggle screen and a "BangOk"-specific new player message from System. These only appear on your first boot of the mod.

## Troubleshooting

* If the "Mods" button does not appear on the main menu, then the modtools are not installed correctly. No mod will work without this, and installing any mods before the modtools may break the game.
* If upon installing a mod you see a white screen with black text, this means the game crashed during startup. Carefully review the text. Often there will be a line explicitly stating what went wrong.
    * Example: `Failed resolving dependencies of the mod "Mod A": Cannot find a mod "Mod B".`
        * This tells you that Mod A needs Mod B installed for it to work, but Mod B was not found.
        * In this case uninstall Mod A, install Mod B and ensure it is working (that it appears in the Mods menu,) then reinstall Mod A.
* If the "Mods" list does not show the Magmalink or CRAP mods, then they are not installed correctly.
    * First, try restarting the game.
    * If that does not work, try unsubscribing and resubscribing to the mods. Make sure Steam actually begins a download when you do this.
    * If that does not work, see if the mods have been downloaded to `<STEAM INSTALL DIRECTORY>/steamapps/workshop/content/571880`. There you should see numbered folders for each mod you have _subscribed_ to. If you cannot find Magmalink or CRAP among those numbered folders, then Steam has not downloaded them.
    * If the mods are downloaded, but not showing up in the game, you can attempt to manually copy the numbered folders from the workshop directory to the game's `mods` directory.
        * This is not recommended, as it bypasses mod signature verification and may allow malicious mods to run.
* If a "NSFW Toggle" button does not appear on the main menu after installing BangOk, then you do not have any NSFW mods installed in the game. This means BangOk is not properly installed. Ensure it is in the correct location and is not in a folder inside a folder.

# Uninstallation

To uninstall any mod, simply delete the mod's folder from the `mods` directory. If the mod's files are present anywhere under the `game` directory, the game will attempt to load them, even if the mod is not present in the `mods` directory. This can cause crashes or other issues. If you are experiencing issues with a mod you have uninstalled, ensure all of its files are removed from the `game` directory.

# Updating

* If a mod installed through the Steam Workshop has been updated, the game will automatically spot, validate, and install the new version whenever Steam deigns to download it.
* If a mod installed manually has been updated, you will need to download the new version and install it manually. To update a mod, simply delete the mod's folder from the `mods` directory and follow the installation instructions again.

# Compatibility

Mods generally do not conflict with each other. When they do, frequently one author or the other will add a note to their `__init__.py` that will cause the game to crash and display a message explaining the conflict. Unless you encounter such a message, you can assume that BangOk and its dependencies are compatible with any other mods you may wish to install.

# Development Installation

If you wish to install BangOk for development purposes, simply clone the repository into the `game/mods` directory. The game should safely ignore the `.git` folder and load the mod as normal. If you are developing a mod that depends on BangOk, you should add BangOk as a dependency in your mod's `__init__.py` file. This will ensure that the game will not attempt to load your mod until BangOk is loaded. (Do note that none of BangOk's API is stable, though, so try to focus on the modtools' NSFW toggle instead.)