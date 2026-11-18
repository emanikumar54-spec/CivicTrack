
from database import initialize_database, get_all_complaints


def main():
    initialize_database()

    print("Database initialized successfully!")

    complaints = get_all_complaints()

    print("Existing complaints:", complaints)


if __name__ == "__main__":
    main()
