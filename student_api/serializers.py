from rest_framework import serializers
from .models import Student,Path # models.py den tablolarımızı import ediyoruz.

# end point olarak dönüştüreceğimiz tabloyu yazıyoruz.
#bu kullanım yaygın olarak kullanılmayan yöntem.
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()

#       #create methodu
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#          #update methodu
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance


#piyasada yaygın kullanılan yöntem.
# modeli tanımlarız arka planda create ve update işlemlerini ve fielsları otomatik olarak tanımlar.
class StudentSerializer(serializers.ModelSerializer):
    born_year=serializers.SerializerMethodField() # born_year adında field ekledik. Sadece okunabilir.
    path = serializers.StringRelatedField() #path_name adında filed ekledik. Sadece okunabilir.
    #model kısmında str methodunda ne döndürürsek o ismi bize gösterir.
    path_id = serializers.IntegerField() #post metodunda kullanmak için tanımladım Çünkü modelde ForeingKey

    class Meta:
        model = Student # hangi modelimizde işlem yapacaksak tanımlıyoruz.
        # fields = '__all__' # frontend de göstereceğimiz bilgileri sunuyoruz. hepsini gösterir.
         # exclude= ["number"] number hariç hepsini gösterir.
        fields = (
            'id','first_name', 'last_name',
            'age', 'born_year', 'path', # model tablosunda path ile ilişkilendirdiğimiz için gözükür.
            'path_id',

        ) #istediğimiz bilgileri gösterebiliriz.

    # burada artı bir bilgi döndürebiliriz frontende bu bilgi database kayıtlı olmaz. Sadece okunabilir.
    def get_born_year(self,obj):
            import datetime
            current_time = datetime.datetime.now()
            return current_time.year - obj.age
            # bu fonksiyonda doğum yılını döndürdük.
  
class PathSerializer(serializers.ModelSerializer):
    students= StudentSerializer(many=True) #burda models.py dosyasında 2 tabloyu ilişkilendirdiğimiz için sadece path' kayıtlı öğrencileride görebiliriz.

    # students = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='detail'
    # ) # bu şelilde yaparsak tüm öğrencieri url adresi olarak görüntüleriz.
    class Meta:
        model = Path
        # fields = '__all__'
        fields = (
            'id',
            'path_name',
            'students'
        )