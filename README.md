Logs Analysis
===

Python and PostgreSQL
---

---

**Author :** Matheus Willian Machado  
**Date :** July 11, 2019

---

Project Overview
---

> You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
>
> In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.
> 
> (Udacity)

---

## Step-by-Step

### Installing Postgres on Mac

```bash
brew install postgresql
brew services list
brew services start postgresql
```

### Importing database

```bash
curl https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip -o newsdata.zip
unzip newsdata.zip
createdb news
psql -d news -f newsdata.sql
```

### Setting up Python Enviroment on Mac

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
conda create -n logs -f requirements.txt
conda activate logs
```

or

```bash
pip3 install -r requirements.txt
```

### Running

```bash
python3 report.py
```

or

```bash
python3 report.py > report.txt
```

---

References
---

<https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip>
<https://review.udacity.com/#!/rubrics/2239/view>