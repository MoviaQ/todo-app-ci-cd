import unittest
from app import app, db, Todo

class TodoAppTestCase(unittest.TestCase):

    # Metoda setUp uruchamia się przed każdym testem
    def setUp(self):
        # Ustawienie aplikacji w tryb testowy
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    # Metoda tearDown uruchamia się po każdym teście
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Test sprawdzający, czy strona główna działa
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Test sprawdzający dodawanie zadania
    def test_add_task(self):
        response = self.app.post('/', data={'content': 'Test task'})
        self.assertEqual(response.status_code, 302)  # Przekierowanie po dodaniu
        # Sprawdź, czy zadanie zostało dodane do bazy danych
        task = Todo.query.first()
        self.assertIsNotNone(task)
        self.assertEqual(task.content, 'Test task')

if __name__ == '__main__':
    unittest.main()