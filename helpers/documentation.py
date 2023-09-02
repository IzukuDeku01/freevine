from helpers import __version__

main_help = f"""
    \b
    Freevine v{__version__}
    Author: stabbedbybrick

    \b
    Requirements:
        Python 3.7+
        Working CDM(blob and key)
        N_m3u8DL-RE
        ffmpeg
        mkvmerge
        mp4decrypt

    \b
    Python packages installation:
        pip install -r requirements.txt

    \b
    Settings:
        Open config.yaml in your favorite text editor to change settings like
        download path, folder structure, file names, subtitle options etc.
    \b
    Instructions:
        Place blob and key file in pywidevine/L3/cdm/devices/android_generic to use local CDM
        Use --remote option if you don't have a CDM (ALL4 not supported)
    \b
        Use dl.py to call on the streaming service you want to download from
        by using the service alias: ALL4, CTV, ITV, UKTV, STV, ROKU, TUBI, PLUTO
        Add options and a URL to series or movie to specify what you want to download
        See examples at the bottom
    \b
        Always use main page URL of series or movie, not specific episode URLs
        Use the "S01E01" format (Season 1, Episode 1) to request episodes
        Use --episode S01E01-S01E10 to request a range of episodes (from the same season)
        Use --episode S01E01,S03E07,S10E12 (no spaces!) to request a mix of episodes
    \b
        --remote to get decryption keys remotely (default: local CDM)
        --titles to list all available episodes from a series
        --quality to specify video quality (default: Best)
        --all-audio to include all audio tracks (default: Best)
    \b
    Information:
        ROKU:  1080p, DD5.1, premium content is not supported
        CTV:   1080p, DD5.1, TV provider-required content is (probably) not supported
        ALL4:  1080p, AAC2.0
        UKTV:  1080p, AAC2.0
        STV:   1080p, AAC2.0 Some titles have DRM, some do not. Both are supported
        ITV:   720p,  AAC2.0
        TUBI:  720p,  AAC2.0 Some titles have DRM, some do not. Both are supported
        PLUTO: 720p,  AAC2.0 
    \b
        Default file names follow the current P2P standard: 
        "Title.S01E01.Name.1080p.SERVICE.WEB-DL.AUDIO.CODEC"
    \b
        If you request a quality that's not available,
        the closest match is downloaded instead
    \b
        Default download path is /downloads folder
        Series are organized in respective season folder
        Subtitles(if available) are muxed in with the final file

    \b
    Examples:
        python dl.py CTV  --episode S01E01 URL
        python dl.py ALL4 --episode S01E01-S01E10 URL
        python dl.py ITV  --quality 720p --season S01 URL
        python dl.py ROKU --remote --season S01 URL
        python dl.py UKTV --titles URL
    """
