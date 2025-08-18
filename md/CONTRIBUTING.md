`run.sh` script is only built to run on linux, needs to be run in a vm container or an equivalnt `run.bat` needs to be made for windows testing. 

Another solution is to use [cygwin](https://cygwin.com/) or Windows Subsystem for Linux if you're upgraded to Windows 11.

Windows did not allow easy venv use for Python and this is hosted on a Linux Server anyway.


- [git-readme](../README.md)
    - back home
- [digital-ocean](./md//digital-ocean-readme.md)
    - the basis to allow hosting as an app on digital ocean
    - eases the dev load a little

# Running
- most precursor actions (dependecy install/ server startup) are built into the `run.sh` file
- a `.venv` file is created to keep python from breaking the Operating Sytem
    - in case of strange err, usually after depenency install, delete `.venv` folder to renew python environment.
- additional bash defintions is contained in the `./bash/` folder

the script starts a Univcorn instance (favored with FastAPI for uptime) which will reflect any static site changes once saved to disk and browser refreshed.


most top level routes are split off into `./routes/` with `html` serving the home and most of the `./templates/` directory.



# Dependecies

- OS: Linux (debian/ubuntu tested)
- Python 3.x


## System
[*FILE](../bash/depends.txt) - contained in `./bash/depends.txt`


    These have to be installed manually until we create a "install" process to keep app from running in root mode
- python-venv
- something for pdf generator.
## Python


[*FILE](../requirements.txt) - contained in `./requirements.txt`

    we try to include links to documentation/formating for each module.
- [fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)
    - handles web serving as an app, from `server.py`
    - [python-multipart](https://multipart.fastapiexpert.com/)
        - allows parsing of data streams.
        - useful for video feeds and large files
- [jinja2](https://jinja.palletsprojects.com/en/stable/)
    - templating engine to allow HTML to have dynamic information from data sources.
- [uvicorn](https://www.uvicorn.org/)
    - listens to changes in the app folder
    - needs killed and rebooted if the Python logic changes, html stuff is fine
- [httpx](https://www.python-httpx.org/)
    - not sucessfully used just yet but will be for further web scraping/local testing/post/get needs.
    - attempting to check/pull current git, requires an SSH key to auth the call. (***NOTE:*** keys need to be managed better)


