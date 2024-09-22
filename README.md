# Concert Management 

#### This Python CLI application allows users to manage a database of bands, venues, and concerts. Users can see  schedule concerts, and track concert details, including band performances and venue information.

---

## Description

In this application:
- A **Band** can perform at many **Venues**.
- A **Venue** can host many **Bands**.
- The **Concert** model connects the **Band** and **Venue** in a many-to-many relationship, storing the concert details such as date and location.

The system uses **SQLAlchemy** for database migrations and querying, ensuring that data relationships are handled efficiently.



## Setup/Installation Requirements

To get started, you need the following:

- **Python 3.12** installed on your system.
- A **SQLite3** database for managing band, venue, and concert data.

### Setup Steps:

1. **Clone the Repository**:
   - Go to the repository URL:
   - Copy the SSH URL.
   - In your terminal, navigate to your preferred directory and run:
     ```bash
     git clone <SSH URL>
     ```

2. **Install Dependencies**:
   - Open the cloned repository:
     ```bash
     cd concert-challenge
     ```
   - Install required Python libraries using pip
     ```bash
     pip install
     ```

     Alternatively, use pipenv to manage dependencies:
     ```bash
     pipenv install
     pipenv shell
     ```

3. **Run the Application**:
   - Execute the  application:
     ```bash
     python debug.py
     ```

## Technologies Used

- **Python 3.12**: 
- **SQLAlchemy**: ORM used for database interactions 
- **SQLite3**: Database for storing band, venue, and concert information.
- **Alembic**: Tool used for database migrations.



