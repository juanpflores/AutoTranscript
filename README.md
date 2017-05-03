# AutoTranscript
A python script that uses GDocs to transcript audio files.

## Prerequisites
AutoTranscript needs some previous configurations to work properly.

 - Google Account
 - Python 2
 - Pip
 - Install Selenium using `pip`:
```python
pip install selenium
```

For OSX:
 - Download and install [Soundflower](https://github.com/mattingalls/Soundflower/releases).
 - Download the [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.29/) or use `brew install chromedriver`.
 - In case you downloaded chromedrive, properly [configure it](http://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/).

For Ubuntu:
 - Install PavuContol  via terminal `sudo apt-get install pavucontrol` or Software Center.
 - Download the [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.29/).
 - Add chromedrive to you `PATH` or `local/bin`.

## Getting Started
 - First configure the audio preferences of your OS:
    - Set the audio input to be the software you previously installed.
    - Set the audio output to be the software as well.
 - Add your Google Account login and password information in the `settings.py` file.
 - Run the main file (`python main.py`).
 - Play the audio you want to transcribe.

## How it works
What this project does it connects the audio output of your computer with the audio input internally, 
then it runs a chrome browser and opens a new GDoc file in which we use the speech to text tool to start transcribing the text. 
When your video is done you just need to stop the srcipt.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
This projects uses a GNU GENERAL PUBLIC. You'll find more in the LICENSE file.
