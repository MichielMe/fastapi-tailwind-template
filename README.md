# FastAPI + Tailwind CSS + DaisyUI Template

A modern, production-ready template for building web applications with FastAPI backend and Tailwind CSS + DaisyUI frontend.

## 🚀 Features

- **FastAPI Backend**: Modern Python web framework with automatic OpenAPI documentation
- **Tailwind CSS**: Utility-first CSS framework for rapid UI development
- **DaisyUI**: Component library built on Tailwind CSS
- **Custom Dark Theme**: Professional dark theme with custom color scheme
- **Jinja2 Templates**: Server-side rendering with component-based architecture
- **Docker Support**: Containerized deployment with multi-stage builds
- **uv Package Manager**: Fast Python package management
- **Modular Architecture**: Clean separation of concerns with organized project structure

## 📁 Project Structure

```
├── app/                    # FastAPI application
│   ├── api/               # API routes
│   ├── core/              # Core configuration and settings
│   ├── models/            # Database models
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   ├── views/             # Frontend view controllers
│   └── main.py            # FastAPI app entry point
├── frontend/              # Frontend assets and templates
│   ├── static/            # Static files (CSS, JS, images)
│   │   ├── css/           # Tailwind CSS files
│   │   ├── js/            # JavaScript files
│   │   └── images/        # Image assets
│   └── templates/         # Jinja2 templates
│       ├── components/    # Reusable components
│       ├── pages/         # Page templates
│       └── base.html      # Base template
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile            # Docker image configuration
├── pyproject.toml        # Python project configuration
└── Makefile             # Development commands
```

## 🛠️ Prerequisites

- Python 3.13+
- Node.js 18+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Docker (optional, for containerized deployment)

## 🚀 Quick Start

### Option 1: Local Development

#### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-name>
```

#### 2. Backend Setup

```bash
# Install Python dependencies
uv sync

# Start the FastAPI development server
uv run fastapi dev --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

#### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start Tailwind CSS watch mode
npm run dev
```

This will watch for changes in your CSS and automatically rebuild the output CSS file.

### Option 2: Docker Development

```bash
# Build and start the application
docker compose up --build

# Or use the Makefile
make run-docker
```

The application will be available at `http://localhost:8000`

## 🎨 Customization

### Tailwind CSS Configuration

The Tailwind CSS configuration is located in `frontend/static/css/input.css`. The template includes:

- **Custom DaisyUI Theme**: A professional dark theme called "broadcast-pro"
- **Google Fonts**: PT Sans font family
- **Custom Color Scheme**: Dark backgrounds with electric blue accents

To customize the theme, modify the `@plugin "daisyui/theme"` section in `input.css`.

### Adding New Pages

1. Create a new template in `frontend/templates/pages/`
2. Add a new route in `app/views/` or create a new router file
3. Include the router in `app/main.py`

Example:

```python
# app/views/about.py
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.core import settings

router = APIRouter()
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)

@router.get('/about', response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
        'pages/about.html',
        {
            'title': 'About',
            'request': request,
        }
    )
```

### Adding Components

Create reusable components in `frontend/templates/components/` and include them in your pages:

```html
<!-- frontend/templates/components/my-component.html -->
<div class="my-component">
  <!-- Component content -->
</div>

<!-- Usage in pages -->
{% include 'components/my-component.html' %}
```

## 🔧 Development Commands

The project includes a Makefile with common development commands:

```bash
# Start development server with uv
make run-uv

# Start with Docker
make run-docker

# Stop Docker containers
make down-docker

# Clean cache files
make clean
```

### Frontend Commands

```bash
# Watch mode for development
npm run dev

# Build for production
npm run build
```

## 🐳 Docker Deployment

The project includes a multi-stage Dockerfile optimized for production:

1. **Builder Stage**: Installs dependencies and builds the application
2. **Runtime Stage**: Minimal image with only the application and runtime dependencies

### Environment Variables

Configure the application using environment variables:

- `PROJECT_NAME`: Application name (default: "FastAPI Project")
- `LOG_LEVEL`: Logging level (default: "INFO")
- `BACKEND_CORS_ORIGINS`: List of allowed CORS origins

Create a `.env` file in the project root:

```env
PROJECT_NAME=My Awesome App
LOG_LEVEL=DEBUG
BACKEND_CORS_ORIGINS=["http://localhost:3000", "https://myapp.com"]
```

## 📝 API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## 📋 Using as a Template

### Method 1: Use GitHub Template (Recommended)

1. **Click "Use this template"** button on the GitHub repository page
2. **Create your new repository** with your desired name
3. **Clone your new repository**:
   ```bash
   git clone https://github.com/yourusername/your-new-project.git
   cd your-new-project
   ```

### Method 2: Manual Setup

1. **Clone this template**:

   ```bash
   git clone https://github.com/original-owner/fastapi-tailwind-template.git
   cd fastapi-tailwind-template
   ```

2. **Remove the original git history**:

   ```bash
   rm -rf .git
   git init
   ```

3. **Create your own repository** on GitHub and add it as origin:

   ```bash
   git remote add origin https://github.com/yourusername/your-new-project.git
   ```

4. **Make your initial commit**:
   ```bash
   git add .
   git commit -m "Initial commit from template"
   git branch -M main
   git push -u origin main
   ```

### After Setup

1. **Update project configuration**:

   - Edit `pyproject.toml` to change the project name and description
   - Update `app/core/config.py` to set your `PROJECT_NAME`
   - Modify the custom theme in `frontend/static/css/input.css` if desired

2. **Follow the Quick Start guide** above to run your new project

## 🚀 Production Deployment

1. **Build the Docker image**:

   ```bash
   docker build -t my-app .
   ```

2. **Run the container**:

   ```bash
   docker run -p 8000:8000 my-app
   ```

3. **Or use Docker Compose**:
   ```bash
   docker compose up --build
   ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework for Python
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [DaisyUI](https://daisyui.com/) - Component library for Tailwind CSS
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

---

**Happy coding! 🎉**
