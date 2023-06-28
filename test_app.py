import unittest, mysql.connector
from markupsafe import escape
from app import app, validate_name, validate_phone_number, validate_email, validate_password, validate_book_year, validate_positive_number, validate

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="biblioteka"
        )
        cursor = db.cursor()
        cursor.execute("DELETE FROM uzytkownicy WHERE nazwa_uzytkownika = 'johnsmith'")
        db.commit()
        cursor.close()
        db.close()

    def test_validate_name(self):
        valid_name = "John"
        self.assertTrue(validate_name(valid_name))

        invalid_name = "John123"
        self.assertFalse(validate_name(invalid_name))

    def test_validate_phone_number(self):
        valid_number = "123456789"
        self.assertTrue(validate_phone_number(valid_number))

        invalid_number = "1234"
        self.assertFalse(validate_phone_number(invalid_number))

    def test_validate_email(self):
        valid_email = "test@example.com"
        self.assertTrue(validate_email(valid_email))

        invalid_email = "testexample.com"
        self.assertFalse(validate_email(invalid_email))

    def test_validate_password(self):
        valid_password = "Passw0rd"
        self.assertTrue(validate_password(valid_password))

        invalid_password = "password"
        self.assertFalse(validate_password(invalid_password))

    def test_validate_book_year(self):
        valid_year = "2021"
        self.assertTrue(validate_book_year(valid_year))

        invalid_year = "abcd"
        self.assertFalse(validate_book_year(invalid_year))

    def test_validate_positive_number(self):
        valid_number = "10"
        self.assertTrue(validate_positive_number(valid_number))

        invalid_number = "-5"
        self.assertFalse(validate_positive_number(invalid_number))

    def test_validate(self):
        valid_text = "John Doe"
        self.assertTrue(validate(valid_text))

        invalid_text = "John Doe 123"
        self.assertFalse(validate(invalid_text))
    
    def test_app(self):
        self.assertEqual(self.app.get("/").status_code, 200)

    def test_profil(self):
        self.assertEqual(self.app.get("/profil").status_code, 302)
    
    def test_change_password_ok(self):
        old = "pasW0rdd"
        new = "pasW0rd1"

        data = {"stare_haslo": old, "nowe_haslo": new}
        response = self.app.post("/zmien_haslo", data=data)

        self.assertEqual(response.status_code, 302, response.data)

    def test_register_wrong_passwd(self):
        name = "John"
        surname = "Smith"
        tel_no = "668753201"
        email = "dummy.mail@mail.com"
        passwd = "passwordo"
        username = "johnsmith"

        data = {"imie": name, "nazwisko": surname, "numer_telefonu": tel_no, "email": email, "haslo": passwd, "nazwa_uzytkownika": username}
        response = self.app.post("/register", data=data)

        self.assertEqual(response.status_code, 400, response.data)

    def test_strona_glowna_logged_in(self):
        with self.app.session_transaction() as session:
            session['logged_in'] = True
            session['nazwa_uzytkownika'] = 'example_user'

        response = self.app.get("/strona_glowna")
        self.assertEqual(response.status_code, 200)

    def test_strona_glowna_not_logged_in(self):
        response = self.app.get("/strona_glowna", follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_wyszukaj_ksiazke(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['logged_in'] = True

            response = client.post('/wyszukaj_ksiazke', data={
                'tytul': 'Harry Potter',
                'autor': 'J.K. Rowling',
                'wydawnictwo': 'ABC',
                'seria': 'Magical Series',
                'oprawa': 'Twarda',
                'rok_wydania': '2005',
                'ilosc_stron': '500',
                'rzad': '3',
                'regal': '2',
                'polka': '2'
            })
            self.assertEqual(response.status_code, 200)


    def test_wyloguj(self):
        with self.app as client:
            response = client.get('/wyloguj', follow_redirects=True)

            self.assertEqual(response.status_code, 200)

            with client.session_transaction() as sess:
                self.assertFalse(sess.get('logged_in'))
                self.assertIsNone(sess.get('nazwa_uzytkownika'))

    def test_edytuj_ksiazke_with_errors(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['logged_in'] = True

            response = client.post('/edytuj_ksiazke/1', data={
                'tytul': 'Nowy tytuł',
                'autor': 'Nowy autor',
                'wydawnictwo': 'Nowe wydawnictwo',
                'seria': 'Nowa seria',
                'oprawa': 'Nieprawidłowa oprawa',
                'rok_wydania': '2022',
                'ilosc_stron': 'abc',
                'rzad': '-1',
                'regal': 'B',
                'polka': '1'
            }, follow_redirects=True)

            self.assertIn(response.status_code, [400, 422])

            self.assertEqual(response.request.path, '/edytuj_ksiazke/1')

if __name__ == '__main__':
    unittest.main()
