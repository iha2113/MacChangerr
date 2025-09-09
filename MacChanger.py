import subprocess
import optparse
import time
import re



def control_new_mac(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface]).decode("utf-8")
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if new_mac:
         return new_mac.group(0)
    else:
        return None


def figlet():
    subprocess.call(["figlet", "Macchanger"])

def get_user_mac():
    usage = "Usage: %prog -i <interface> -s <islem_no> [-m <mac_adres>] [-t <time>]\n\n" \
            "Örnekler:\n" \
            "  python Tools.py -i eth0 -s 1 -t 5\n" \
            "      -> eth0 arayüzünde 5 saniyede bir random mac değiştirir.\n\n" \
            "  python Tools.py -i wlan0 -s 2 -m 12:34:56:78:9A:BC\n" \
            "      -> wlan0 arayüzünde MAC adresini manuel olarak değiştirir.\n\n" \
            "  python Tools.py -i wlan0 -s 3\n" \
            "      -> wlan0 arayüzünü orijinal MAC adresine döndürür.\n" \
            "  -----------------------------------------------------\n"


    mac_change = optparse.OptionParser(usage = usage)
    mac_change.add_option("-s","--islem_no",dest="islem_no",help="1 = random mac, 2 = manuel mac, 3 = orjinal mac")
    mac_change.add_option("-i","--interface", dest="interface", help="Ağ arayüzünüz")
    mac_change.add_option("-m","--mac_adress", dest="mac_adress", help="mac adresiniz")
    mac_change.add_option("-t","--time",dest="time",default=5,help="Kaç saniyede bir değişsin.")

    return mac_change.parse_args()

def mac(user_interface,user_mac_adress):
    old_mac = control_new_mac(user_interface)
    subprocess.call(["sudo","ifconfig",user_interface,"down"])
    subprocess.call(["sudo","ifconfig",user_interface,"hw","ether",user_mac_adress])
    subprocess.call(["sudo","ifconfig",user_interface,"up"])
    print("✅ Mac adresiniz manuel olarak değiştirildi:", user_mac_adress)
    new_mac = control_new_mac(user_interface)
    if old_mac == new_mac:
        print("MAC zaten aynıydı, döngü sonlandırılıyor.")
        exit()


def mac_random(user_interface):
    old_mac = control_new_mac(user_interface)
    subprocess.call(["sudo","ifconfig",user_interface,"down"])
    subprocess.call(["sudo","macchanger","-r",user_interface])
    subprocess.call(["sudo","ifconfig",user_interface,"up"])
    print("🎲 Mac adresiniz rastgele değiştirildi.")
    new_mac = control_new_mac(user_interface)
    print(f"🎲 Rastgele MAC değiştirildi: {old_mac} ➝ {new_mac}")

def mac_original(user_interface):
    old_mac = control_new_mac(user_interface)
    subprocess.call(["sudo","ifconfig",user_interface,"down"])
    subprocess.call(["sudo","macchanger","-p",user_interface])
    subprocess.call(["sudo","ifconfig",user_interface,"up"])
    print("🎲 Mac adresiniz orjinal hale döndürüldü.")
    new_mac = control_new_mac(user_interface)
    if old_mac == new_mac:
        print("Zaten orijinal MAC kullanılıyor, döngü sonlandırılıyor.")
        exit()

if __name__ == "__main__":
    figlet()
    (user_input, arguments) = get_user_mac()
    while True:


        if user_input.islem_no == "1":   # random
            mac_random(user_input.interface)
        elif user_input.islem_no == "2": # manuel
            mac(user_input.interface, user_input.mac_adress)
        elif user_input.islem_no == "3":
            mac_original(user_input.interface)
        else:
            print("⚠️ Lütfen işlem numarasını belirtin: 1 = random, 2 = manuel, 3 = orjinal")
        time.sleep(int(user_input.time))
