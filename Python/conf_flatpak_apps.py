import os
import subprocess
import time
import shutil
from plyer import notification


def alert(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Alerta do Sistema',
        timeout=15
    )


def limpa_tela():
    os.system("clear" if os.name == "posix" else "cls")


def verifica_flatpak():
    return shutil.which("flatpak") is not None


def instala_flatpak():
    alert("Instalação Flatpak", "Atualizando o sistema.")
    print("[INFO] -  Atualizando o sistema.")
    print("")
    time.sleep(2)
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

    limpa_tela()
    alert("Instalação Flatpak", "Instalando O Flatpak.")
    print("[INFO] - Instalando O Flatpak.")
    print("")
    time.sleep(2)
    subprocess.run(["sudo", "apt", "install", "-y", "flatpak"])
    limpa_tela()


def instala_aplicativos(apps):
    for app in apps:
        alert(f"Instalação Flatpak", "Instalando: {app}")
        print(f"[INFO] - Instalando: {app}")
        time.sleep(2)
        subprocess.run(["flatpak", "install", "-y", app])
        time.sleep(1)
        limpa_tela()


def main():
    limpa_tela()
    alert("Instalação Flatpak", "INICIANDO SCRIPT")
    time.sleep(2)
    limpa_tela()

    if not verifica_flatpak():
        alert("Instalação Flatpak", "Flatpak não está instalado.")
        print("[ALERT] - Flatpak não está instalado.")
        time.sleep(2)
        instala_flatpak()
    else:
        alert("Instalação Flatpak", "Flatpak já instalado.")
        print("[INFO] - Flatpak já instalado.")

    limpa_tela()
    alert("Instalação Flatpak", "Instalando os pacotes Flatpak.")
    print("[INFO] - Instalando os pacotes Flatpak.")
    time.sleep(3)
    limpa_tela()


    pacotes = [
        "com.discordapp.Discord",
        "org.telegram.desktop",
        "com.spotify.Client",
        "org.gimp.GIMP",
        "com.valvesoftware.Steam",
        "org.videolan.VLC",
        "com.visualstudio.code",
        "net.lutris.Lutris",
        "com.bitwarden.desktop",
        "org.mozilla.Thunderbird",
        "com.anydesk.Anydesk",
        "io.dbeaver.DBeaverCommunity",
        "org.raspberrypi.rpi-imager",
        "org.upscayl.Upscayl",
        "dev.deedles.Trayscale",
        "com.pokemmo.PokeMMO",
        "page.codeberg.libre_menu_editor.LibreMenuEditor",
        "io.github.flattool.Warehouse",
        "com.github.iwalton3.jellyfin-media-player",
        "io.github.shiftey.Desktop",
        "com.transmissionbt.Transmission",
        "org.vinegarhq.Sober",
        "com.mattjakeman.ExtensionManager",
        "net.davidotek.pupgui2",
        "com.github.ztefn.haguichi",
        "com.belmoussaoui.Authenticator",
        "io.github.realmazharhussain.GdmSettings",
        "br.gov.fazenda.receita.irpf2025"
    ]

    instala_aplicativos(pacotes)


main()