from time import time
from rest_framework import serializers
from .models import *
from accounts.models import Survey
from accounts.serializers import UserSerializers
from perfumes.utils.exchange_rate import korean_won

EXCHANGE_RATE = 0; EXCHANGE_RATE_EXP = 0
print(f'환율 가져오기 전. 환율: {EXCHANGE_RATE}, 만료시간: {EXCHANGE_RATE_EXP}, 현재: {time()}')


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


kor_names = ['', '시트러스', '프루츠', '플로럴', '화이트 플로럴', '그린, 허브', '스파이시', '스위츠', '우디', '발삼', '머스크', '음료', '알데하이드']
class CategorySerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    value = serializers.IntegerField(source='id', read_only=True)
    label = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'
        include = ['value', 'label']
    
    def get_name(self, instance):
        name = kor_names[instance.id]
        return name

    def get_label(self, instance):
        label = kor_names[instance.id]
        return label


class PerfumeBriefSerializers(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')

    class Meta:
        model = Perfume
        fields = ['id', 'name', 'brand', 'thumbnail']


class PerfumeSerializers(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField(read_only=True)
    top_notes = NoteSerializers(many=True)
    heart_notes = NoteSerializers(many=True)
    base_notes = NoteSerializers(many=True)
    total_review = serializers.IntegerField(source='review_set.count', read_only=True)
    brand = BrandSerializers()
    price = serializers.SerializerMethodField(read_only=True)
    thumbnail = serializers.SerializerMethodField(read_only=True)
    categories = CategorySerializers(many=True)
    similar = serializers.SerializerMethodField()
    recommended = serializers.SerializerMethodField()

    class Meta:
        model = Perfume
        fields = '__all__'
        include = ['avg_rate', 'total_review']

    def get_avg_rate(self, instance):
        try:
            result = sum(instance.review_set.values_list('rate', flat=True))/instance.review_set.count()
        except:
            result = 0
        return result

    def get_price(self, instance):
        global EXCHANGE_RATE, EXCHANGE_RATE_EXP
        now = time()
        if EXCHANGE_RATE_EXP < now:
            EXCHANGE_RATE = korean_won()
            EXCHANGE_RATE_EXP = now + 24 * 3600
            print(f'환율 가져온 후. 환율: {EXCHANGE_RATE}, 만료시간: {EXCHANGE_RATE_EXP}, 현재: {now}')
        try:
            return instance.price * EXCHANGE_RATE
        except:
            return 0

    def get_thumbnail(self, instance):
        return f'http://i02b208.p.ssafy.io:8000/staticfiles/images/{instance.pk}.jpg'


    def get_similar(self, instance):
        if instance.similar:
            return instance.similar
        sim_p = Perfume.objects.exclude(similar='')
        if instance.categories.exists():
            sim_p = sim_p.filter(categories__in=instance.categories.all())[:10]\
                .values_list('id', flat=True)
            return str(list(sim_p))
        return sim_p[instance.id % 2694].similar


    def get_recommended(self, instance):
        if instance.recommended:
            return instance.recommended
        rec_p = Perfume.objects.exclude(recommended='')
        if instance.categories.exists():
            rec_p = rec_p.filter(categories__in=instance.categories.all())[:10]\
                .values_list('id', flat=True)
            return str(list(rec_p))
        return rec_p[instance.id % 2550].recommended


class PerfumeSurveySerializers(serializers.ModelSerializer):
    top_notes = NoteSerializers(read_only=True, many=True)
    heart_notes = NoteSerializers(read_only=True, many=True)
    base_notes = NoteSerializers(read_only=True, many=True)

    class Meta:
        model = Perfume
        fields = '__all__'
        exclude = ['price', 'similar', 'recommended']


class SurveySerializers(serializers.ModelSerializer):
    gender = UserSerializers(source='user.gender', read_only=True)
    age = UserSerializers(source='user.age',read_only=True)
    like_notes = NoteSerializers(many=True)
    like_category = CategorySerializers(many=True)

    class Meta:
        model = Survey
        fields = '__all__'
        include = ['age', 'gender']


class ReviewSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    perfume = serializers.IntegerField(source='perfume.pk', read_only=True)
    content = serializers.CharField()
    rate = serializers.IntegerField(min_value=0, max_value=10)
    created_at = serializers.DateTimeField(read_only=True)
    like_cnt = serializers.IntegerField(source='like_users.count',read_only=True)
    images = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.save()
        return instance

    def get_images(self, instance):
        return [f'http://i02b208.p.ssafy.io:8000/mediafiles/review/{image.pk}.webp' for image in instance.images.all()]


class PerfumeDetailSerializers(PerfumeSerializers):
    reviews = serializers.SerializerMethodField()
    recommended = serializers.SerializerMethodField()
    similar = serializers.SerializerMethodField()

    class Meta(PerfumeSerializers.Meta):
        exclude = None

    def get_reviews(self, instance):
        ordered = instance.review_set.order_by('-created_at')
        return ReviewSerializers(ordered, many=True).data

    def get_recommended(self, instance):
        recommended = instance.recommended
        if not recommended:
            recommended = Perfume.objects.exclude(recommended='')
            if instance.categories.exists():
                recom_p = recommended.filter(categories__in=instance.categories.all())[:10]
                return PerfumeBriefSerializers(recom_p, many=True).data
            else:
                recommended = recommended[instance.id % 2550].recommended
        recom = map(int, recommended[1:-1].split(', '))
        recom_p = [Perfume.objects.get(pk=perfume_pk) for perfume_pk in recom]
        return PerfumeBriefSerializers(recom_p, many=True).data

    def get_similar(self, instance):
        similar = instance.similar
        if not similar:
            similar = Perfume.objects.exclude(similar='')
            if instance.categories.exists():
                sim_p = similar.filter(categories__in=instance.categories.all())[:10]
                return PerfumeBriefSerializers(sim_p, many=True).data
            else:
                similar = similar[instance.id % 2694].similar
        sim = map(int, similar[1:-1].split(', '))
        sim_p = [Perfume.objects.get(pk=perfume_pk) for perfume_pk in sim]
        return PerfumeBriefSerializers(sim_p, many=True).data


class SearchQuerySerializers(serializers.Serializer):
    keywords = serializers.CharField(required=True)


class SurveyGETQuery(serializers.Serializer):
    category = serializers.CharField()


class SurveyPOSTQuery(serializers.Serializer):
    gender = serializers.CharField()
    season = serializers.CharField()
    category = serializers.CharField()
    notes = serializers.CharField()