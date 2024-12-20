# Django Book Management System

A comprehensive book management system built with Django that allows users to perform CRUD (Create, Read, Update, Delete) operations on a book collection. This project implements best practices for Django development and includes a responsive Bootstrap-based UI.

## Features

- **Complete CRUD Operations:**
  - Create new books with title, author, description, publication year, and price
  - View a list of all books in a responsive grid layout
  - View detailed information about each book
  - Update existing book information
  - Delete books with confirmation

- **Form Validation:**
  - Custom validation for book titles
  - Publication year validation (between 1000 and current year)
  - Price validation (must be positive)
  - User-friendly error messages

- **User Interface:**
  - Responsive Bootstrap 5 design
  - Card-based book display with hover effects
  - Flash messages for user feedback
  - Clean and intuitive navigation

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd book-management-system
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up the database**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Collect static files**
```bash
python manage.py collectstatic
```

7. **Run the development server**
```bash
python manage.py runserver
```

## Usage

1. **Access the application**
   - Open your web browser and navigate to `http://127.0.0.1:8000/`
   - For admin interface, go to `http://127.0.0.1:8000/admin/`

2. **Managing Books**
   - Click "Add New Book" to create a new book entry
   - View all books on the home page
   - Click "View" to see detailed information about a book
   - Click "Edit" to modify book information
   - Click "Delete" to remove a book (requires confirmation)

## Project Structure

```
book_management/
├── config/                 # Project configuration
├── books/                  # Main application
│   ├── templatetags/      # Custom template filters
│   └── templates/         # HTML templates
├── static/                # Static files
├── staticfiles/           # Collected static files
├── venv/                  # Virtual environment
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Forms and Models

### Book Model
- Title (CharField)
- Author (CharField)
- Description (TextField)
- Publication Year (IntegerField with validation)
- Price (DecimalField with validation)
- Created/Updated timestamps

### BookForm
- Custom validation for title length
- Bootstrap-styled form fields
- Proper error handling and display

## Styling and UI Features

- Bootstrap 5 framework
- Responsive grid layout
- Card-based design with hover effects
- Clean and intuitive navigation
- Flash messages for user feedback

## Development

1. **Making Changes**
   - Activate the virtual environment
   - Make your changes
   - Run tests if available
   - Commit your changes

2. **Adding Features**
   - Create new models in `models.py`
   - Add forms in `forms.py`
   - Create views in `views.py`
   - Add templates in `templates/`
   - Update URLs in `urls.py`

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Common Issues and Solutions

1. **Static files not loading**
```bash
python manage.py collectstatic --clear --no-input
```

2. **Database migration issues**
```bash
python manage.py makemigrations --dry-run  # Check migrations
python manage.py showmigrations  # List migrations
python manage.py migrate --plan  # Show migration plan
```

3. **Permission errors**
```bash
sudo chown -R $USER:$USER .
chmod -R 755 .
```

## Security Considerations

- CSRF protection enabled
- Form validation implementation
- Secure password storage for admin users
- XSS protection through template escaping

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Python Community

## Contact

For questions and support, please open an issue in the GitHub repository.
