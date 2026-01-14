import os
import subprocess
import sys

def run_command(command):
    """Sistem komutlarını çalıştırır ve çıktıyı yönetir."""
    try:
        print(f"Çalıştırılıyor: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Hata oluştu: {e.stderr}")
        return False

def main():
    print("--- aaa Projesi Yapılandırma Yardımcısı ---")
    print("Hedef Depo: https://github.com/kerilov1138/den.git")
    
    # Python sürüm kontrolü
    print(f"Python Sürümü: {sys.version}")

    # Flutter kontrolü
    print("Flutter SDK kontrol ediliyor...")
    if not run_command("flutter --version"):
        print("Hata: Flutter SDK kurulu değil veya PATH üzerinde bulunamadı.")
        return

    # Bağımlılıkların yüklenmesi
    print("Proje bağımlılıkları (pub get) yükleniyor...")
    run_command("flutter pub get")

    # Yerel APK testi
    answer = input("Yerel bir APK derlemek istiyor musunuz? (e/h): ")
    if answer.lower() == 'e':
        print("APK derleme işlemi başlatılıyor...")
        if run_command("flutter build apk --release"):
            print("Derleme Başarılı: build/app/outputs/flutter-apk/app-release.apk")
        else:
            print("Derleme başarısız oldu.")
    
    print("Kurulum tamamlandı. GitHub Actions yapılandırması '.github/workflows/main.yml' dosyasına kaydedilmelidir.")

if __name__ == '__main__':
    main()
