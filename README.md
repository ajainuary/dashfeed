<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Kelly+Slab&text=DashFed&effect=3d">
<h1 align="center"><div class="font-effect-3d">DashFeed</div></h1>

  <p align="center">
    A minimalistic web-based news aggregator
    <br />
    <a href="https://github.com/ajainuary/minic-compiler/issues">Report Bug</a>
    ·
    <a href="https://github.com/ajainuary/minic-compiler/issues">Request Feature</a>
  </p>

![Dashfeed Home](https://user-images.githubusercontent.com/30972152/104807591-16c52900-5806-11eb-8a83-a1c4713cc617.gif)

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#usage">Usage</li>
        <li><a href="#usage">Scraping</li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Dashfeed is a minimalistic news aggregator that allows you to collate news from various popular publishers and read them ad-free without any distractions. You can also bookmark articles for reading later and share on social media.

### Built With

* [Flask](https://flask.palletsprojects.com/)
* [BeautifulSoup](crummy.com/software/BeautifulSoup//)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

#### Flask

```sh
   pip install Flask
   ```

#### Beautiful Soup

We use Beautiful Soup for extracting content from crawled pages.

```sh
   pip install beautifulsoup4
   ```
   
### Usage

1. Clone the repo
   ```sh
   git clone https://github.com/ajainuary/dashfeed.git
   ```
2. Export the Flask App Variable
```sh
   export FLASK_APP=site/index.py
   ``` 
3. Start the app
```sh
   flask run
   ```
<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](license.md) for more information.

## Acknowledgements

This project was built as a part of the IT Workshop Course at IIIT-Hyderabad. I am grateful to Professor Rekha Singhal and the TAs for their guidance and support.
