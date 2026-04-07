from image_api_sdk import ImageApiClient

print("import success")

# 서버 주소를 넣어서 클라이언트 생성
# 지금은 로컬에서 테스트하므로 localhost:8080 사용
client = ImageApiClient("http://localhost:8080")

# 서버 헬스체크
# /health를 호출해서 서버가 살아 있는지 확인
print(client.health())

# 실제 이미지 처리 요청
result = client.process_image(
    image_url="https://image.utoimage.com/preview/cp872722/2022/12/202212008462_500.jpg",
    operations=[
        # 1단계: 흑백 변환
        {"type": "grayscale"},

        # 2단계: 블러 적용
        {
            "type": "blur",
            "options": {
                "ksize": 9,
                "sigma": 2.0
            }
            
        },
    ],
    output_format="jpg",
)

# 서버가 알려준 결과 메타데이터 출력
print("mime_type =", result.mime_type)
print("width =", result.width)
print("height =", result.height)

# 결과 이미지를 파일로 저장
result.save("./temp/result.jpg")

# Pillow 이미지 객체로 바꾼 뒤 기본 이미지 뷰어로 띄워보기
img = result.to_pil()
img.show()