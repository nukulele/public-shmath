# shmath
math, shmath

A tiny CMS for `markdown` and `mathjax` and `Django` and `Vue`.

## installation

- set up and enter a virtual environment
- do the following from the main directory:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata data/stub.py
npm install
npm run dev
python manage.py runserver
```

If it's gone well, you should see an entry including math notation at `http://127.0.0.1:8000/complex-number/`

