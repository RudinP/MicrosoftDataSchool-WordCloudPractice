# Selenium, Kiwi, WordCloud를 이용한 워드클라우드 생성 실습
### Kiwi를 선택한 이유?
- Mecab의 설치가 힘든 점
- KoNLPy의 업데이트가 최근에 진행되지 않음
- 다른 패키지와 비교분석한 지표 존재
## 1. Selenium으로 테크데일리 주요 기사 크롤링해오기
- 주요 기사에 해당하는 기사들의 본문을 가져옴
## 2. Kiwi로 한글 형태소 분석하기
- 불용어 제외, 정규표현식을 이용한 명사 형태만 골라오기
## 3. WordCloud와 matplotlib로 워드클라우드 생성하기
- Frequency를 기반으로 한 워드클라우드 생성
- 
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/c36ef21a-9c2a-49d1-9d71-2bd3e1fc6e71" />
