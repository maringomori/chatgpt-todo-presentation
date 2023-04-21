### This whole project was made with ChatGPT-4 while I hold a presentation about it. Even the readme :)

### You can see the whole conversation in the the chat.openai.com_x.png files

### Feel free to reach me out on [LinkedIn](https://www.linkedin.com/in/marin-g%C3%B6m%C3%B6ri/) if you have any questions or just want to talk about the topic :)

# Django Todo App with Subtasks


This is a simple Todo App built using Django and Django REST framework. The app allows you to create, update, and delete todo items with support for subtasks. It also provides endpoints to list all todos, finished todos, unfinished todos, and subtasks for a given task.

## Features

- Create, update, and delete todos
- Subtasks support
- List all todos, finished todos, and unfinished todos
- List subtasks for a given task

## Installation

1. Clone this repository:

```
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app
```

2. Create a virtual environment and install the required packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Apply migrations:

```
python manage.py migrate
```

4. Run the Django development server:

```
python manage.py runserver
```

The server will start at http://127.0.0.1:8000/

## API Endpoints

1. List/Create todos: `/api/todos/`
2. Retrieve/Update/Delete a specific todo: `/api/todos/<id>/`
3. List unfinished todos: `/api/todos/unfinished/`
4. List finished todos: `/api/todos/finished/`
5. List subtasks for a given task: `/api/todos/<parent_task_id>/subtasks/`

## License

This project is licensed under the MIT License
