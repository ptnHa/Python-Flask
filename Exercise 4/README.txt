Run these commands to check the website:

1. Activate virtual environment
    For cmd:        venv\Scripts\activate.bat
    For bash:       venv/bin/activate

2. Install environment
    pip install -e .

3. Run Flask
    For cmd:        set FLASK_APP=flaskr
                    set FLASK_ENV=development
                    flask run

    For bash:       export FLASK_APP=flaskr
                    export FLASH_ENV=development
                    flask run