# <center>shortcake</center>
### <center>A Python application for shortening URLs</center>
---

# Features
- [x] Create unique short links (shortened URLs)
- [x] 8-character length short link paths allow for greater than 218 trillion possible short links
- [x] Maintains unique records for original links and short links (i.e. avoids duplication)
- [x] View API example endpoints and basic testing at http://127.0.0.1:8000/docs


# Dependencies
- Docker
- requirements.txt
  - Python 3.9+
  - pip 22.0.3+
  - FastAPI 0.74.1+
  - PostgreSQL 14
  - SQLAlchemy 1.4.31+
  - pydantic 1.9.0+
  - starlette 0.17.1+
  - Uvicorn 0.17.5+


## Getting Started

1. Clone repo
2. Navigate to project root directory
3. Run `docker-compose up`


## Usage

Open Terminal and start the repo's web server implementation:

To view a list of original links, visit:
```bash
http://127.0.0.1:8000
```

or

```bash
http://127.0.0.1:8000/links
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

To view API endpoint documentation, please visit:  http://127.0.0.1:8000/docs


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
- Automating the testing of this service (possibly via an API testing framework, such as pytest with Tavern)
- Purge obsolete links from the database in case original links no longer point to valid pages
- Run automated server monitor and send alert when API or database servers go down
  - Monitor multiple endpoints
  - Run functional checks
    - CRUD operations
    - validate payloads using JSON schema validation
    - identify latency via API response times
  - Test for non HTTP 200 OK status codes for API requests that should fail
  - Test both prod and dev environments
    - Hopefully, identifying and fixing issues in dev will help avoid issues arising in prod

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
