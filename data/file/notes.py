represent_notes = [
    "Muguet", "Bergamot", "Rose", "Jasmine", "Orange Flower", "Cotton", "Patchouli", "Cedarwood", "Musk", "Amber",
    "Tangerine", "Bubble Soap", "Tea", "White Flowers", "White Iris", "Cherry Blossom Petals", "Vetiver", "Sandalwood", 
    "Vanilla", "Grapefruit", "Mandarine", "Ginger", "Neroli", "Red Apple", "Eucalyptus", "Peony", "Pink Rose", 
    "Velvet", "Leafy Green", "Woody"
]


explains = [
    "자생하는 진달래(목련)의 꽃향", "시트러스 과일인 베르가못의 상큼한 향", "로즈(장미)의 우아하고 달콤한 향", "매혹적인 자스민 향기", "오렌지꽃의 향기", 
    "포근하고 부드러운 면 옷의 향", "마취제로 유명한 향기의 쌉싸름한 향", "향긋한 임 목재의 향", "섬세하고 성형할 수 있는 밀감 향", "따뜻하고 달콤한 아몬드의 향",
    "상큼한 감귤류인 탄저린의 향", "아기들을 위한 거품 목욕비누의 향", "편안한 차를 마실 때 느껴지는 향", "맑은 하늘 아래서 피는 백합의 향", 
    "차분하고 우아한 화이트 아이리스의 향", "벚꽃잎의 상쾌한 향", "톡 쏘는 향기의 베티버향", "부드럽고 따뜻한 샌달우드의 향",
    "달콤하고 부드러운 바닐라 향", "새콤한 과일인 자몽의 향", "상큼한 감귤류인 만다린의 향", "생기 넘치는 생강의 향", 
    "자연에서 추출한 오렌지꽃의 향", "맛있는 붉은 사과의 향", "상쾌한 유향의 향", "매혹적인 피오니 향", 
    "달콤하고 로맨틱한 핑크 장미의 향", "부드럽고 고급스러운 벨벳의 향", "신선하고 상큼한 잎의 향", "숲속에서 느껴지는 우디의 향"
]



represents = {
    {
            'category': [1,2],
            'notes' : {
            'Muguet': '자생하는 진달래(목련)의 꽃향',
            'Bergamot': '시트러스 과일인 베르가못의 상큼한 향',
            'Rose': '로즈(장미)의 우아하고 달콤한 향',
            'Jasmine': '매혹적인 자스민 향기',
            'Orange Flower': '오렌지꽃의 향기',
            'Cotton': '포근하고 부드러운 면 옷의 향',
            'Patchouli': '마취제로 유명한 향기의 쌉싸름한 향',
            'White Flowers': '맑은 하늘 아래서 피는 백합의 향',
            'White Iris': '차분하고 우아한 화이트 아이리스의 향',
            'Cherry Blossom Pethals': '벚꽃잎의 상쾌한 향',
            'Vetiver': '톡 쏘는 향기의 베티버향',
            'Vanilla': '달콤하고 부드러운 바닐라 향',
            'Neroli': '자연에서 추출한 오렌지꽃의 향',
            'Peony': '매혹적인 피오니 향',
            'Pink Rose': '달콤하고 로맨틱한 핑크 장미의 향',
            }
        },
        {
            'category': [2],
            'notes' : {
            'Cedarwood': '향긋한 임 목재의 향',
            'Amber': '따뜻하고 달콤한 아몬드의 향',
            'Sandal Wood': '부드럽고 따뜻한 샌달우드의 향',
            'Eucalyptus': '상쾌한 유향의 향',
            'Cedar Wood': '신선하고 상큼한 잎의 향',
            'Woody': '숲속에서 느껴지는 우디의 향',
            }
        },
        {
            'category': [3],
            'notes' : {
            'Tangerine': '상큼한 감귤류인 탄저린의 향',
            'Grapefruit': '새콤한 과일인 자몽의 향',
            'Mandarine': '상큼한 감귤류인 만다린의 향',
            'Red Apple': '맛있는 붉은 사과의 향',
            }
        },
        {
            'category': [4],
            'notes': {
            'Musk': '섬세하고 성형할 수 있는 밀감 향',
            'Bubble Soap': '아기들을 위한 거품 목욕비누의 향',
            'Tea': '편안한 차를 마실 때 느껴지는 향',
            'Ginger': '생기 넘치는 생강의 향',
            'Velvet': '부드럽고 고급스러운 벨벳의 향',
            'Leafy Green': '신선하고 상큼한 잎의 향',
            }
        },
    }
represents = {}

for i in range(len(represent_notes)):
    if i >= 0 and i < 4:
        represents['category'] = 1
        represents['category'][represent_notes[i]] = explains[i]
    elif i >= 4 and i <

for j in range(len(represents))
print(represents)

represents = {
    {
            'category': [1,2],
            'notes' : {
            'Muguet': '자생하는 진달래(목련)의 꽃향',
            'Bergamot': '시트러스 과일인 베르가못의 상큼한 향',
            'Rose': '로즈(장미)의 우아하고 달콤한 향',
            'Jasmine': '매혹적인 자스민 향기',
            'Orange Flower': '오렌지꽃의 향기',
            'Cotton': '포근하고 부드러운 면 옷의 향',
            'Patchouli': '마취제로 유명한 향기의 쌉싸름한 향',
            'White Flowers': '맑은 하늘 아래서 피는 백합의 향',
            'White Iris': '차분하고 우아한 화이트 아이리스의 향',
            'Cherry Blossom Pethals': '벚꽃잎의 상쾌한 향',
            'Vetiver': '톡 쏘는 향기의 베티버향',
            'Vanilla': '달콤하고 부드러운 바닐라 향',
            'Neroli': '자연에서 추출한 오렌지꽃의 향',
            'Peony': '매혹적인 피오니 향',
            'Pink Rose': '달콤하고 로맨틱한 핑크 장미의 향',
            }
        },
        {
            'category': [2],
            'notes' : {
            'Cedarwood': '향긋한 임 목재의 향',
            'Amber': '따뜻하고 달콤한 아몬드의 향',
            'Sandal Wood': '부드럽고 따뜻한 샌달우드의 향',
            'Eucalyptus': '상쾌한 유향의 향',
            'Cedar Wood': '신선하고 상큼한 잎의 향',
            'Woody': '숲속에서 느껴지는 우디의 향',
            }
        },
        {
            'category': [3],
            'notes' : {
            'Tangerine': '상큼한 감귤류인 탄저린의 향',
            'Grapefruit': '새콤한 과일인 자몽의 향',
            'Mandarine': '상큼한 감귤류인 만다린의 향',
            'Red Apple': '맛있는 붉은 사과의 향',
            }
        },
        {
            'category': [4],
            'notes': {
            'Musk': '섬세하고 성형할 수 있는 밀감 향',
            'Bubble Soap': '아기들을 위한 거품 목욕비누의 향',
            'Tea': '편안한 차를 마실 때 느껴지는 향',
            'Ginger': '생기 넘치는 생강의 향',
            'Velvet': '부드럽고 고급스러운 벨벳의 향',
            'Leafy Green': '신선하고 상큼한 잎의 향',
            }
        },
    }
