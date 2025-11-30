# Task Manager

Simple task manager app built with Django and Vue 3.

## What it does

- View all tasks
- Create new tasks
- Edit tasks
- Mark tasks as complete/incomplete
- Delete tasks

## Tech Used

**Backend:**
- Django 4.2.7
- Django REST Framework
- SQLite

**Frontend:**
- Vue 3
- Axios
- SweetAlert2

## Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs on `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:5173`

## API Endpoints

- `GET /tasks/` - Get all tasks
- `POST /tasks/` - Create task
- `GET /tasks/{id}/` - Get single task
- `PUT /tasks/{id}/` - Update task (title & description)
- `PATCH /tasks/{id}/` - Toggle completed status
- `DELETE /tasks/{id}/` - Delete task

## Task Fields

- `id` - Auto generated
- `title` - Required, max 200 chars
- `description` - Optional
- `completed` - Boolean, default false
- `created_at` - Auto generated timestamp

## Notes

- Uses ViewSet (not ModelViewSet)
- Frontend uses Vue 3 Composition API
- SQLite database for development
- CORS enabled for localhost:5173
"# task-manager" 
"# task-manager" 
