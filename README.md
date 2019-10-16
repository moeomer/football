# Football
A Docker image for converting HTML to PDF using wkhtmltopdf

## Quickstart
* `docker-compose build`

* `docker-compose up`

* `POST` to `localhost:5000` with following form-data body:
  * `file` : _required_ HTML binary file for conversion to PDF
  * `toc` : _optional_  true | false bool indicating whether to include a Table of Contents - default `false`
  * `pagenumbers` : _optional_ true | false bool indicating whether to include page numbers - default `false`
  * `cover` : _optional_  HTML binary file for cover page - default `None`
  * `filename` : _optional_  Filename for the converted PDF - default `tmp.pdf`

## Development
- install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
- `mkvirtualenv football`
- `workon football`
- `pip install -r requirements.txt`
- `python app.py`

## TODO
- [ ] Input validation
- [ ] Avoid writing `cover` to temp file
- [ ] Use a production server instead of Flask's dev server
- [ ] More pythonic code :rocket:
