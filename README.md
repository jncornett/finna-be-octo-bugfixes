Some scripts to get flickr interestingness photos onto your Mac as desktop wallpaper.

# downloader.py
Fetches the first `N` photos from Flickr's interestingness gallery. Set the `api_key`, `OUTPUT_DIRECTORY` and `N` variables to use.

# setter.py
Uses `osascript` to set the current desktop background to a random image from `PHOTO_DIRECTORY`.

_NOTE: The setter only works for Mac OS X as of now. I may write scripts/binaries for other OSes in the future._

# Implementation
I use `cron` to schedule the setter to run every 20 minutes and the getter to run once a day. Don't forget to `chmod +x` the python scripts.
