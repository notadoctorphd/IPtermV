
### IPTermV 
#### a fork and remix of "termv - tv in your terminal" that adds the function (hopefully) for using your own .m3u8 playlists. 

## Dependencies
- `curl`
- `mpv`
- `gawk`
- [`jq`](https://github.com/stedolan/jq)
- [`fzf`](https://github.com/junegunn/fzf)
- `xdo` (optional, for `-s` flag)

## Installation
1) clone
2) create python env
3) install requirements (once you've activated environment)  `pip install -r requirements.txt`
4) run main_parser.py -f path_to_file 
5) mkdir ~/.cache/termv
6) mv data.json ~/.cache/termv/ (newly created data.json) 
7) mv iptermv /usr/local/bin 
## Usage

```console
Usage:   iptermv [OPTIONS] query

Options:
  General Options:
    -h, --help                Print this help text and exit.
    -v, --version             Print program version and exit.
    -u, --update              Update channel list to latest version.

  Player Options:
    -f, --full-screen         Open mpv in fullscreen.
    -s, --swallow             Swallow terminal during playback (X11 only) based on devour; https://github.com/salman-abedin/devour.sh

  Environment variables:  
    TERMV_AUTO_UPDATE         Auto update channel list to latest version. (default: true)
    TERMV_SWALLOW             Always swallow terminal during playback. (default: false)
    TERMV_FULL_SCREEN         Always open mpv in fullscreen. (default: false)
    TERMV_DEFAULT_MPV_FLAGS   Default arguments which are passed to mpv. (default: --no-resume-playback)


Show (https://github.com/Roshan-R/termv some love.)
