# wsulib_photobooth
Repository to support WSU Library Photobooth kiosk


## Installation

  * install [homebrew](https://brew.sh/) on Mac
    * `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
  * install [fswatch](https://github.com/emcrisostomo/fswatch)
    * `brew install fswatch`


## To Run

From any directory, run the following command, replacing `INPUT_FOLDER` with where Movies and Pictures are automatically stored, and `OUTPUT_FOLDER` with where they should be copied:

```
fswatch -0 INPUT_FOLDER | xargs -0 -n1 -I {} cp {$1} OUTPUT_FOLDER
```

e.g.
```
fswatch -0 /Users/amazing_username/Pictures/Photo\ Booth\ Library/Pictures | xargs -0 -n1 -I {} cp {$1} /Users/amazing_username/never/delete/me/photobooth_output
```

*Note the forward slashes for escaping possible blank spaces in paths*

Alternatively, run the included python script `photobooth_file_copier.py` with input and output folders as first and second arguments:

```
python photobooth_file_copier.py /Users/amazing_username/Pictures/Photo\ Booth\ Library/Pictures /Users/amazing_username/never/delete/me/photobooth_output
```

*Note the forward slashes required for escaping blank spaces, or enclose input or output folder in quotes*

## Notes

In the cases where photos are deleted from the Pictures directory, `fswatch` will still notices that that file has changed and will attempt to copy it, resulting in an error like this:

```
cp: /Users/amazing_username/Pictures/Photo Booth Library/Pictures/Photo on 8-23-18 at 12.41 PM.jpg: No such file or directory
```

But the error is harmless, will not stop `fswatch`, and can just be ignored.  Very likely possible to parse what the operation on the file was, but this just ignoring the error makes for a fairly straightforward approach.
