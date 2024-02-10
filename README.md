# FastAPI Human Age API

This project implements a FastAPI-based REST API for calculating the age of a human based on their name.

## Features

- Calculates the age of a human based on their name using an external age API.
- Caches age data to improve performance and reduce external API calls.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/fastapi-human-age-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fastapi-human-age-api
    ```

3. Build the Docker containers:

    ```bash
    docker-compose build
    ```

### Usage

1. Start the Docker containers:

    ```bash
    docker-compose up
    ```

2. Access the FastAPI application in your browser at [http://localhost:8000](http://localhost:8000).

### API Endpoints

- **POST /api/human-age**: Calculate the age of a human based on their name.

    - Request Body:

        ```json
        {
            "name": "John Doe"
        }
        ```

    - Response:

        ```json
        {
            "name": "John Doe",
            "age": 30,
            "date_of_birth": "1992-01-01"
        }
        ```

## Configuration

Environment variables can be configured in the `.env` file:

- `redis_host`: Hostname of the Redis server.
- `redis_port`: Port of the Redis server.
- `redis_username`: Username for authentication (if required).
- `redis_password`: Password for authentication (if required).
- `redis_db`: Database index to use in Redis.

## Project Structure

- **appsettings.py**: Configuration settings for the application.
- **main.py**: FastAPI application entry point.
- **human_age.py**: Implementation of the human age feature.
- **.env**: Environment variable configuration file.
- **Dockerfile**: Dockerfile for building the Docker image.
- **docker-compose.yml**: Docker Compose configuration file.
- **requirements.txt**: Python dependencies.

## Dependencies

- FastAPI: Web framework for building APIs with Python.
- Redis: In-memory data store for caching age data.
- Python-Dotenv: Library for loading environment variables from `.env` file.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
