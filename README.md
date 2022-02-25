# <center>shortcake</center>
### <center>A Python application for shortening URLs</center>
---

# Features
- [x] Create unique short links (shortened URLs)
- [x] 8-character length short link paths allow for greater than 218 trillion possible short links
- [x] Maintains unique records for original links and short links (i.e. avoids duplication)
- [x] Visit API example endpoints and basic testing at http://127.0.0.1:8000/docs


# Dependencies
- Visual Studio Code
- Docker
- requirements.txt
  - Python 3.10+
  - pip 22.0.3+
  - FastAPI 0.74.1+
  - PostgreSQL 14
  - SQLAlchemy 1.4.31+
  - pydantic 1.9.0+
  - starlette 0.17.1+
  - Uvicorn 0.17.5+


## Getting Started

1. Clone repo
2. Open repo directory in VSCode
3. Using vscode Remote-Containers Extension: Rebuild and Reopen in Container


## Usage

Open Terminal and start the repo's web server implementation:

```bash
cd shortcake && uvicorn main:app --reload --host 0.0.0.0
```

To view a list of original links, visit:
```bash
http://127.0.0.1:8000
```

To view a list of short links, visit:
```bash
http://127.0.0.1:8000/short-links
```

To shorten a link, input original link as value of `long_link`:
```bash
curl --location --request POST '127.0.0.1:8000/add-link' \
    --header 'Content-Type: application/json' \
    --data-raw '{"long_link": "https://www.youtube.com/watch?v=vjcWToSAlZ8"}'
```

Visit a short link to get redirected by API to original link.

## Future plans and ideas
Features to add:
- Add column `date_created` for short links
- Count `times_accessed` for short links
- Augment frontend to allow users to interact with API more smoothly
- Add column `email` associated to creator of each short link
- Add unit tests
- Create a dashboard to manage short links and original links
- Implement reporting features (such as most accessed links, most popular domains, most frequent users etc.)

## Maintenance
- Automating the testing of this service (possibly via a API testing framework, such as pytest with Tavern)
- Purge obsolete links from the database in case original links no longer point to valid pages


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
