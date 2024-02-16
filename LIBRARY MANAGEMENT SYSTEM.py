###############################
## LIBRARY MANAGEMENT SYSTEM ##
###############################

# 1.BOLUM

# "Library" adında bir sınıf oluştur
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+") # "a+" modu ile books.txt dosyasını aç
        print("Kütüphane oluşturuldu. books.txt dosyası açıldı.")
    def __del__(self):
        # Nesne yok edildiğinde dosyayı kapat
        if hasattr(self, 'file') and self.file: 
            # Yukarıdaki ifade, bir nesnenin belirli bir özelliğe sahip olup olmadığını kontrol eder. 
            # self nesnesinin içinde "file" adında bir özellik (attribute) var mı diye bakar.
            # Eğer bu özellik varsa (dosya önceden açılmışsa), ifade True değerini döndürür. 
            # Eğer özellik yoksa veya self nesnesi genelde tanımlanmamışsa, False değerini döndürür.
            self.file.close()
            print("Kütüphane kapatıldı. books.txt dosyası kapatıldı.")


# 2.BOLUM
            
# Kitapları listeleme:
    def list_books(self):
        self.file.seek(0) # Dosyanın başına git
        book_lines = self.file.read().splitlines() 
        # İlk başta dosyanın tamamını okudu ve bir string olarak aldı.
        # splitlines() metodu ile de satırları ayırdı. Yani satır sonu karakterlern üzerinden bölünmüş bir list oluşturdu

        for line in book_lines:
            book_info = line.split(",") # girilen inputların arasına virgül ekler
            print (f"Kitabın Başlığı: {book_info[0]}, Kitabın Yazarı: {book_info[1]}")

# Kitap ekleme:
    def add_book(self):
        title = input("Kitabın Başlığı: ").title()
        author = input("Kitabın Yazarı: ").split()
        if len(author) > 1:
            isimler = [isim.capitalize() for isim in author[:-1]]
            soyad = author[-1][0].upper() + author[-1][1:].lower()
            isimler.append(soyad)
            author = " ".join(isimler)
        else:
            author = author[0].title()
        release_year = input("Kitabın İlk Yayım Yılı: ")
        if release_year.isnumeric() == False:
            print("Lütfen sayısal bir değer giriniz.")
            release_year = input("Kitabın İlk Yayım Yılı: ")
        language = input ("Kitabı Orijinal Dili: ")
        publisher = input("Sizde Olan Kitabın Yayınevi: ")
        number_pages = input("Kitabın Sayfa Sayısı: ")
        if number_pages.isnumeric() == False:
            print("Lütfen sayısal bir değer giriniz.")
            number_pages = input("Kitabın Sayfa Sayısı: ")

        new_book = f"{title}, {author}, {release_year}, {language}, {publisher}, {number_pages} \n"
        self.file.write(new_book)

# Kitap çıkartma:
    def remove_book(self, title_to_remove):
        self.file.seek(0) # Dosyanın başından itibaren okuma yapılmasını sağlar 
        book_lines = self.file.read().splitlines()

        updated_books = [line for line in book_lines if title_to_remove not in line]
        # silinmek istenilen kitabı filtreleyerek yeni bir liste oluştur

        self.file.seek(0)  

        self.file.truncate() 
        # yukarıdaki ifade, dosyanın boyutunu 0 byte'a düşürür. 
        # Bu, dosyanın içeriğini temizlemek için kullanılır.

        self.file.writelines("\n".join(updated_books) + "\n") # Güncellenmiş kitap listesini dosyaya yazarak dosyayı günceller. 


# 3.BOLUM

# Library sınıından nesne oluşturma:
lib = Library()


# 4.BOLUM

# "lib" nesnesi ile etkileşim için bir menü oluştur
while True:
    print("\n")
    print("### MENU ###")
    print("1) Kitapları Listele ")
    print("2) Kitap Ekle ")
    print("3) Kitap Sil")
    print("4) Çıkış ")

    choice = input("Seçiminizi yapın (1-4): ")
    print("\n")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        title_to_remove = input("Silmek istediğiniz kitabın başlığını giriniz: ")
        lib.remove_book(title_to_remove)
    elif choice == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir sayı girmelisiniz. Eğer çıkmak istiyorsanız 4'e basınız.")
