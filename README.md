Here’s an updated version of the README with the correct repository link:

---

# Late Show API

This is a Flask-based API for managing episodes, guests, and appearances on a late-night show. It allows you to perform CRUD operations on episodes, guests, and appearances, and links them together with a many-to-many relationship through appearances.

## Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Flask
- SQLAlchemy
- Flask-Migrate

### Clone the Repository

```bash
git clone https://github.com/KairuMaina/KairuMaina-Late-Show--Kairu-Maina.git
cd KairuMaina-Late-Show--Kairu-Maina
```

### Install Dependencies

Create a virtual environment (if not already created) and install the necessary dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt
```

### Set Up the Database

Before running the app, set up the database and apply migrations.

```bash
# Initialize the database (creates app.db file)
flask db init

# Create the migration scripts
flask db migrate -m "Initial migration"

# Apply the migrations to the database
flask db upgrade
```

### Seed the Database (Optional)

If you want to populate the database with some initial data, run the seeding script. Make sure you have the provided CSV file (`data.csv`) available or create your own sample data.

```bash
# Seed the database
flask db seed
```

## Running the App

To run the Flask application locally, use the following command:

```bash
flask run --port 5555
```

Your application will be accessible at `http://127.0.0.1:5555`.

## API Endpoints

### `GET /episodes`
- **Description**: Retrieves a list of all episodes.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "date": "1/11/99",
      "number": 1
    },
    {
      "id": 2,
      "date": "1/12/99",
      "number": 2
    }
  ]
  ```

### `GET /episodes/:id`
- **Description**: Retrieves a specific episode by ID, including its appearances and guests.
- **Response**:
  ```json
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1,
    "appearances": [
      {
        "episode_id": 1,
        "guest": {
          "id": 1,
          "name": "Michael J. Fox",
          "occupation": "actor"
        },
        "guest_id": 1,
        "id": 1,
        "rating": 4
      }
    ]
  }
  ```

### `GET /guests`
- **Description**: Retrieves a list of all guests.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Michael J. Fox",
      "occupation": "actor"
    },
    {
      "id": 2,
      "name": "Sandra Bernhard",
      "occupation": "Comedian"
    }
  ]
  ```

### `POST /appearances`
- **Description**: Creates a new appearance for a guest in a specific episode.
- **Request Body**:
  ```json
  {
    "rating": 5,
    "episode_id": 100,
    "guest_id": 123
  }
  ```
- **Response**:
  ```json
  {
    "id": 162,
    "rating": 5,
    "guest_id": 3,
    "episode_id": 2,
    "episode": {
      "date": "1/12/99",
      "id": 2,
      "number": 2
    },
    "guest": {
      "id": 3,
      "name": "Tracey Ullman",
      "occupation": "television actress"
    }
  }
  ```

## Testing with Postman

To test the API, import the provided Postman collection (`challenge-4-lateshow.postman_collection.json`) into Postman. It contains all the endpoints that you need to test, ensuring that your app works as expected.

### How to import the Postman collection:
1. Open Postman.
2. Click on the "Import" button.
3. Select the `Upload Files` option and navigate to the repository folder.
4. Select the `challenge-4-lateshow.postman_collection.json` file to import.
5. Run the tests in Postman to ensure your app is functioning correctly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

