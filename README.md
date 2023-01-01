# Django-Serializers
#Bu  çalışmada Django'nun rest_framework ile Backend tarafında oluşturulan complex veri setinin frontend'de kullanılacak olan JSON formatına serializers ile nasıl 
çevrildiği gösterilmiştir.

#Serializers bir çesit data conventer görevi görmektedir. 

#Djangonun Web API servevisi çalışması için  pip install djangorestframework komutu ile rest_framework yüklenir.

#Proje Klasörüne 'rest_framework' tanıtılır.(settings.py dosyasında "INSTALLED_APPS" kısmına)

#Daha sonra app içinde "serializers.py" dosyası oluşturuyoruz.

# Bu dosyaya from rest_framework import serializers import ediyoruz

# Sonra models.py 'de oluşturduğumuz modeli/modelleri import ediyoruz.

#serializers dosyamız

![image](https://user-images.githubusercontent.com/108414013/210173703-19e33663-6f3b-46c9-b7a1-28ee98f5fa39.png)

![image](https://user-images.githubusercontent.com/108414013/210173714-10af5ab7-60a8-4271-afc4-526a8514658e.png)

Bu uygulamayı ayağı kaldırmak için sırasıyla; 

python -m venv env

sonra .env dosyası oluşturup burada içine "SECRET_KEY" değişkeni oluşturup value olarak =065843865654654&/()%&/+^&^+())%+4  yazabilirsiniz

source env/Scripts/Activate (windows-bash için)

pip install -r requirements.txt (paketleri yüklemek için)

python manage.py createsuperuser

python manage.py runserver komutlarını çalıştırabilirsiniz.


