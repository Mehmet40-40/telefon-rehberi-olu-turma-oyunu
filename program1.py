# Kişi Rehberi oluşturmak için Python programı

class Contact:
    def __init__(self, name, phone, email):
        # Kişi nesnesi oluşturmak için başlangıç yöntemi
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        # Kişi nesnesini yazdırılabilir formatta döndüren yöntem
        return f"İsim: {self.name}, Telefon: {self.phone}, E-posta: {self.email}"

class ContactDirectory:
    def __init__(self):
        # Kişi rehberi oluşturmak için başlangıç yöntemi
        self.contacts = []

    def add_contact(self, name, phone, email):
        # Yeni bir kişi eklemek için yöntem
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Kişi {name} başarıyla eklendi!")

    def display_contacts(self):
        # Tüm kişileri görüntülemek için yöntem
        if not self.contacts:
            print("Kişi bulunamadı.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        # Belirli bir isme sahip kişiyi aramak için yöntem
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print(f"{name} isimli kişi bulunamadı.")

    def delete_contact(self, name):
        # Belirli bir isme sahip kişiyi silmek için yöntem
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            for contact in found_contacts:
                self.contacts.remove(contact)
            print(f"{name} isimli kişi(ler) başarıyla silindi!")
        else:
            print(f"{name} isimli kişi bulunamadı.")

def main():
    # Ana fonksiyon
    directory = ContactDirectory()
    while True:
        print("\nKişi Rehberi")
        print("1. Kişi Ekle")
        print("2. Tüm Kişileri Göster")
        print("3. İsimle Kişi Ara")
        print("4. İsimle Kişi Sil")
        print("5. Çıkış")
        choice = input("Seçiminizi girin (1-5): ")

        if choice == '1':
            # Kişi ekleme işlemi
            name = input("Kişinin ismini girin: ")
            phone = input("Kişinin telefon numarasını girin: ")
            email = input("Kişinin e-posta adresini girin: ")
            directory.add_contact(name, phone, email)
        elif choice == '2':
            # Tüm kişileri gösterme işlemi
            directory.display_contacts()
        elif choice == '3':
            # Belirli bir isme sahip kişiyi arama işlemi
            name = input("Aranacak ismi girin: ")
            directory.search_contact(name)
        elif choice == '4':
            # Belirli bir isme sahip kişiyi silme işlemi
            name = input("Silinecek ismi girin: ")
            directory.delete_contact(name)
        elif choice == '5':
            # Programdan çıkış işlemi
            print("Kişi Rehberinden çıkılıyor. Hoşça kalın!")
            break
        else:
            # Geçersiz seçim uyarısı
            print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir sayı girin.")

if __name__ == "__main__":
    main()
