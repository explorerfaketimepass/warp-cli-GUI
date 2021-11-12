
#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi


wget https://raw.githubusercontent.com/explorerfaketimepass/warp-cli-GUI/main/warp-switch.py -O warp-switch.pyl

wget https://raw.githubusercontent.com/explorerfaketimepass/warp-cli-GUI/main/warp.desktop -O warp.desktopl

chmod +x warp.desktopl
chmod +x warp-switch.pyl

mv warp.desktopl /usr/share/applications/warp.desktop
mv warp-switch.pyl /usr/bin/warp-switch.py

echo "REBOOT"
