
import yagmail

yag = yagmail.SMTP('mostafa.khalifa.2000.mk@gmail.com', 'snzg ztfd ovcn owiz')

yag.send(to='mostafa.mohsen.khalifaa@gmail.com', subject='just say hi', contents='hi from master email my name is mostafa')

print("Email sent")