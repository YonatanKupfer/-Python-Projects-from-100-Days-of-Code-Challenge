# Internet Speed Tester

This is a Python script for testing your internet speed using the [Speedtest.net](https://www.speedtest.net/) website. It automates the speed test process using the Selenium library and provides you with the download and upload speeds of your internet connection.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Installation

1. Clone the repository or download the ZIP file and extract it to your desired location.

```bash
git clone https://github.com/yourusername/internet-speed-tester.git
```

2. Install the required Python packages using pip.

```bash
pip install selenium
```

3. Download the appropriate ChromeDriver for your operating system from the [official ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to select the version that matches your installed Chrome browser.

4. Move the downloaded ChromeDriver executable to the project directory.

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

```bash
cd /path/to/internet-speed-tester
```

2. Execute the `main.py` script using Python.

```bash
python main.py
```

3. The script will open a Chrome browser window and navigate to the Speedtest.net website.

4. After a brief pause, the script will initiate the speed test by clicking the "Go" button on the website.

5. Wait for the speed test to complete. This may take some time (around 80 seconds).

6. Once the speed test is finished, the script will print the results on the console, displaying your download and upload speeds in Mbps (megabits per second).

## Dependencies

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome web browser
- ChromeDriver (Make sure to download the correct version that matches your Chrome browser)

---

Note: I developed this project as part of the "100 Days of Code" challenge, but has been customized and adapted to meet specific requirements. Happy coding! 🚀
