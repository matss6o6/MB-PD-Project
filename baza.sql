CREATE TABLE uzytkownicy ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
imie VARCHAR(255) NOT NULL, 
nazwisko VARCHAR(255) NOT NULL, 
numer_telefonu VARCHAR(255) NOT NULL, 
email VARCHAR(255) NOT NULL,
nazwa_uzytkownika VARCHAR(255) NOT NULL, 
haslo VARCHAR(255) NOT NULL,
verification_code VARCHAR(255) NOT NULL,
);


CREATE TABLE ksiazki (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tytul VARCHAR(255) NOT NULL,
  autor VARCHAR(255) NOT NULL,
  wydawnictwo VARCHAR(255) NOT NULL,
  seria VARCHAR(255) NOT NULL,
  oprawa VARCHAR(255) NOT NULL,
  rok_wydania INT NOT NULL,
  ilosc_stron INT NOT NULL,
  rzad INT NOT NULL,
  regal INT NOT NULL,
  polka INT NOT NULL
);

INSERT INTO ksiazki (id, tytul, autor, wydawnictwo, seria, oprawa, rok_wydania, ilosc_stron, rzad, regal, polka) VALUES
(1, 'Władca Pierścieni', 'J.R.R. Tolkien', 'Allen & Unwin', 'Władca Pierścieni', 'Miękka', 1954, 1178, 1, 1, 2),
(2, 'Harry Potter i Kamień Filozoficzny', 'J.K. Rowling', 'Bloomsbury', 'Harry Potter', 'Twarda', 1997, 223, 2, 3, 4),
(3, '1984', 'George Orwell', 'Secker & Warburg', 'Brak', 'Miękka', 1949, 328, 3, 2, 1),
(4, 'Duma i uprzedzenie', 'Jane Austen', 'Thomas Egerton', 'Brak', 'Twarda', 1813, 432, 1, 5, 3),
(5, 'Mistrz i Małgorzata', 'Michaił Bułhakow', 'Moskowskij Raboczij', 'Brak', 'Miękka', 1967, 512, 2, 2, 2),
(6, 'Zabić drozda', 'Harper Lee', 'J.B. Lippincott & Co.', 'Brak', 'Twarda', 1960, 281, 3, 4, 1),
(7, 'Harry Potter i Komnata Tajemnic', 'J.K. Rowling', 'Bloomsbury', 'Harry Potter', 'Miękka', 1998, 367, 1, 2, 3),
(8, 'Wiedźmin: Ostatnie życzenie', 'Andrzej Sapkowski', 'SuperNOWA', 'Saga o Wiedźminie', 'Twarda', 1993, 277, 2, 1, 1),
(9, 'Mroczne materie', 'Philip Pullman', 'Scholastic', 'Mroczne materie', 'Miękka', 1995, 399, 3, 3, 4),
(10, 'Człowiek z wysokiego zamku', 'Philip K. Dick', 'G.P. Putnam's Sons', 'Brak', 'Twarda', 1962, 259, 1, 4, 2),
(11, 'Zabójstwo w Orient Expressie', 'Agatha Christie', 'Agatha Christie', 'Hercule Poirot', 'Twarda', 1934, 256, 2, 5, 2),
(12, 'Zawód: Pisarz', 'John Doe, Jane Smith', 'J.B. Lippincott & Co.', 'Brak', 'Twarda', 2022, 400, 2, 3, 1);