# Inventroy Tracking Web Application

This is an inventory tracking web application that satisfies basic CRUD Functionality and ability to Push a button export product data to a CSV.  

Backend is written in Python using [Django](https://www.djangoproject.com/) Framework. Frontend is developed using [this](https://github.com/KenBroTech/Bootstrap-Dashboard-Interface-Design) template and [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/theming/) Framework.  

## If you encountered any problems while trying to run the app, please reach out to me at [ruidih2@illinois.edu](mailto:ruidih2@illinois.edu)

Before we can run the app, we need to install some dependencies:  

Follow this if you have **macOS**:
1. If you don't have python3 downloaded, download python3 [here](https://www.python.org/downloads/)
3. Run `python --version` and `pip --version` to make sure they are installed. **Make sure you have python3 in this step. If not, add 3 after python and pip when running the following steps: `python` -> `python3`, `pip` -> `pip3`**
4. Run `pip install django`.
12. Run `pip install django-crispy-forms`.
5. Clone the repo `git clone https://github.com/ruidi-huang/Inventory-Tracking-App.git`
6. Change the directory to `Inventory-Tracking-App`.
7. Run `python manage.py runserver`.
8. Follow the instructions or go to [localhost:8000](http://localhost:8000/) (make sure you are not using the port [localhost:8000](http://localhost:8000/) first)

Follow this if you have **Windows**:  

1. I would suggest to use [Git Bash](https://git-scm.com/downloads) to interface with the OS.
2. Download python3 from [here](https://www.python.org/downloads/).
3. Run `python --version` and `pip --version` in bash shell to make sure they are installed. **Make sure you have python3 in this step. If not, add 3 after python and pip when running the following steps: `python` -> `python3`, `pip` -> `pip3`**
4. Run `pip install django`.
12. Run `pip install django-crispy-forms`.
5. Clone the repo `git clone https://github.com/ruidi-huang/Inventory-Tracking-App.git`
6. Change the directory to `Inventory-Tracking-App`.
13. Run `python manage.py runserver`.
14. Follow the instructions or go to [localhost:8000](http://localhost:8000/) (make sure you are not using the port [localhost:8000](http://localhost:8000/) first)



Project Demo:
1. Home Page:  
![home page](Demo_1.png)  
2. Product Page:  
![product page](Demo_2.png)  
3. Edit Page:  
![edit page](Demo_3.png)  
4. Delete Page:  
![delete page](Demo_4.png)
