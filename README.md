1. Create virtual env
	```sh
	python -m venv env
	```
2. Activate
	```sh
	env\Scripts\activate
	```

3. Install requirements
	```sh
	pip install -r requirements.txt
	```

4. Run migrations and create superuser
	```sh
	python manage.py migrate
	python manage.py createsuperuser
	```


5.To load district data
    ```sh 
    python manage.py loaddata health_worker/fixtures/district.json
    ```
