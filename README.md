# 🛠️ MacChanger - Python ile MAC Adresi Değiştirici

Bu proje, ağ arayüzünüzün MAC adresini **rastgele, manuel veya orijinal** hale getirmek için geliştirilmiş bir Python aracıdır.  
Aracın amacı, özellikle siber güvenlik testlerinde ve ağ gizliliği sağlamak isteyen kullanıcılar için pratik bir MAC değiştirme yöntemi sunmaktır.  

---

## 🚀 Özellikler
- ✅ Manuel MAC adresi değiştirme
- 🎲 Rastgele MAC adresi oluşturma
- 🔄 Orijinal MAC adresine dönme
- ⏱️ Belirlenen süre aralıklarında otomatik MAC değiştirme
- 🖥️ Kullanıcı dostu **komut satırı arayüzü**

---

## 📦 Kurulum

```bash
# Kali Linux veya benzeri sistemlerde
sudo apt update
sudo apt install macchanger net-tools figlet -y

git clone https://github.com/<kullanici-adi>/<repo-adi>.git
cd <repo-adi>

python Tools.py -h


# eth0 arayüzünde 5 saniyede bir random MAC adresi değiştir
python Tools.py -i eth0 -s 1 -t 5

# wlan0 arayüzünde manuel MAC adresi belirle
python Tools.py -i wlan0 -s 2 -m 12:34:56:78:9A:BC

# wlan0 arayüzünü orijinal MAC adresine döndür
python Tools.py -i wlan0 -s 3


⚠️ Not

Komutlar root yetkisi ile çalıştırılmalıdır (sudo kullanın).

Yanlış kullanım internet bağlantınızın kesilmesine neden olabilir.

Sadece yasal testler ve öğrenme amaçlı kullanılmalıdır.
