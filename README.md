<br>
<p align="center">
  <img alt="SearchLy" src="src/searchly/static/img/og.png" width="50%"/>
</p>
<br>

[![HitCount](http://hits.dwyl.io/AlbertSuarez/searchly.svg)](http://hits.dwyl.io/AlbertSuarez/searchly)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/searchly.svg)](https://GitHub.com/AlbertSuarez/searchly/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/searchly.svg)](https://GitHub.com/AlbertSuarez/searchly/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AlbertSuarez/searchly.svg)](https://github.com/AlbertSuarez/searchly)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/searchly.svg)](https://GitHub.com/AlbertSuarez/searchly/graphs/contributors/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/searchly.svg)](https://github.com/AlbertSuarez/searchly/blob/master/LICENSE)

🎶 Song similarity search API based on lyrics

[Demo](https://searchly.asuarez.dev) | [API Endpoint](https://searchly.asuarez.dev/api/v1) | [API Documentation](https://searchly.asuarez.dev/docs/v1) 

## Contents

1. [Requirements](#requirements)
2. [Recommendations](#recommendations)
3. [Usage](#usage)
4. [Run tests](#run-tests)
5. [Development](#development)
   1. [Development mode](#development-mode)
   5. [Logging](#logging)
   6. [Scripts](#scripts)
   6. [How to add a new test](#how-to-add-a-new-test)
10. [Authors](#authors)
7. [License](#license)

## Requirements

1. Python 3.7+
2. docker-ce (as provided by docker package repos)
3. docker-compose (as provided by PyPI)

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run the API, please execute the following commands from the root directory:

1. Setup virtual environment

2. Install dependencies

  ```bash
  pip3 install -r requirements.lock
  ```

3. Initialize database (if is not initialized)

    ```bash
    source db/deploy.sh
    ```

4. Run the server as a docker container with docker-compose

    ```bash
    docker-compose up -d --build
    ```

    or as a Python module (after enabling the [Development mode](#development-mode))

    ```bash
    python3 -m src.searchly
    ```

## Run tests

1. Run Searchly locally with the [Development mode](#development-mode) enabled.

2. Run tests

   ```
   python3 -m unittest discover -v
   ```

## Development

### Development mode

Edit `src/searchly/__init__.py` and switch `DEVELOPMENT_MODE` flag from `False` to `True` for enabling development mode.

```python
# DEVELOPMENT_MODE = False
DEVELOPMENT_MODE = True
```

### Logging

For checking the logs of the whole stack in real time, the following command is recommend it:

```bash
docker-compose logs -f
```

### Scripts

The module `src/searchly/scripts` contains a bunch of scripts whose allow to create and build the needed index for searching the similarity between song lyrics. It's needed to have the [Development mode](#development-mode) enabled for using the scripts.

1. **Fill database** (`fill_database.py`): from a zip file extracted from the AZLyrics scraper, found on [this repository](https://github.com/AlbertSuarez/azlyrics-scraper), fills the database with all the data on it.
2. **Train** (`train.py`): given the data of the database, extracts all the features from the song lyrics and trains a word2vec model. The results will be saved on the `data`folder.
3. **Build** (`build.py`): given the trained word2vec model, builds an NMSLIB index for allowing searchs on the API. The index file will be saved on the `data` folder.
4. **Extract maximum distance** (`extract_maximum_distance.py`): given the trained word2vec model and the built index, searchs across all the database for getting the maximum distance between two points. This is needed for computing the percentage of similarity instead of returning a raw distance on the API response. The result will be saved on the `data` folder.

### How to add a new test

Create a new Python file called `test_*.py` in `test.searchly` with the following structure:

```python
import unittest


class NewTest(unittest.TestCase):
    
    def test_v0(self):
        expected = 5
        result = 2 + 3
        self.assertEqual(expected, result)

# ...

if __name__ == '__main__':
    unittest.main()
```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © SearchLy
