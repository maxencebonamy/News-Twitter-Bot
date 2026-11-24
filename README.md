# News Twitter Bot

A Python tool that collects French news headlines and prepares square images from their pictures.

It fetches the latest top headlines for France from NewsAPI, keeps the articles that have a short usable description, and can turn each article picture into a 400x400 image. It is meant as the base of a bot that publishes news on Twitter; the publishing step is not implemented yet.

## Table of contents

- [News Twitter Bot](#news-twitter-bot)
	- [Table of contents](#table-of-contents)
	- [How it works](#how-it-works)
	- [Tech stack](#tech-stack)
	- [Repository structure](#repository-structure)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
	- [Configuration](#configuration)
	- [Running locally](#running-locally)
	- [License](#license)

## How it works

1. **Fetch**: `ArticlesGetter` queries the NewsAPI `top-headlines` endpoint for France, ten articles per page, and goes through the pages until it has the requested number of articles.
2. **Filter**: an article is kept only if its description, source, image URL and link are all present, the description is at most 250 characters long, and it contains neither `-` nor `...`. If too few articles match, an error is raised.
3. **Clean**: non-breaking spaces in descriptions are replaced with regular spaces.
4. **Image**: `ImageGenerator` downloads the article picture, crops it to a centered square and resizes it to 400x400 pixels.
5. **Output**: `main.py` prints the source, description and link of each selected article. `ImageGenerator` is not called from `main.py` yet.

## Tech stack

| Layer | Technologies |
| --- | --- |
| Language | Python 3 (the local virtual environment uses 3.9) |
| HTTP | `requests` |
| Images | Pillow |
| Data source | [NewsAPI](https://newsapi.org/) |

## Repository structure

```
.
├── assets/
│   ├── backgrounds/        28 background images (1.png to 28.png)
│   └── font/               JetBrains font (jetbrains.ttf)
├── sources/
│   ├── articles/           Article model and NewsAPI client
│   ├── images/             Image cropping and resizing
│   ├── utils/              String and random helpers
│   └── main.py             Entry point
└── requirements.txt        Python dependencies
```

Classes use dataclasses with name-mangled private attributes and expose them through getters. Modules are imported as `sources.<package>.<module>`, so the project is run from the repository root.

## Prerequisites

- Python 3
- A [NewsAPI](https://newsapi.org/) API key

## Installation

```bash
git clone git@github.com:maxencebonamy/News-Twitter-Bot.git
cd News-Twitter-Bot
```

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

The API key is read from an environment variable. There is no `.env` file support: export the variable in your shell.

```bash
export NEWS_API_KEY=your_api_key
```

| Variable | Description | Example |
| --- | --- | --- |
| `NEWS_API_KEY` | NewsAPI key used to fetch headlines | `your_api_key` |

## Running locally

From the repository root:

```bash
python -m sources.main
```

The script prints four articles, each as `[source] description` followed by its link. Change the number in `ArticlesGetter(4)` in [`sources/main.py`](sources/main.py) to get more or fewer.

## License

This project is licensed under the [MIT License](LICENSE).
