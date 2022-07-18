                    # başlama aşaması

operation = 0

def commandIn():
    while True:
        command = input("İstasyondan gelen komut var mı? E/H")
        if command == "E":
            print("Komut gerçekleştiriliyor")
            continue
        elif command == "H":
            return False

