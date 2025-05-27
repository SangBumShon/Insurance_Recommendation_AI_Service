# Talk2Sell

## 📌 개요
본 시스템은 고객과 상담사의 대화 내용을 바탕으로 고객의 요구를 파악하고, 그에 적합한 보험 상품을 실시간으로 추천하는 대화 기반 추천 시스템입니다. 사용자의 음성을 입력으로 받아 대화 내용을 분석하고, 고객의 목적과 상황에 맞는 상품을 자연스럽게 제안하는 것을 목표로 합니다.


---

- **STT (Speech-to-Text)**: 상담사와 고객의 음성을 실시간으로 텍스트로 변환하고, 화자 분리 수행  
- **Conversation Pattern Analyzer (NLU)**: 텍스트 기반으로 사용자의 의도와 목적, 관심사를 분석  
- **Conversation Predictor**: 고객 정보와 대화 패턴을 바탕으로 적절한 보험 상품 후보를 예측  
- **RAG**: 예측된 상품 후보를 기반으로 벡터 DB에서 관련 정보를 검색하여 LLM 입력에 활용  
- **추천 멘트 생성**: LLM이 검색 결과를 바탕으로 자연스러운 보험 상품 추천 멘트를 생성

---

## 💡 기술 스택

| 컴포넌트 | 사용 기술                           |
|------|---------------------------------|
| STT  | Whisper                         |
| 서버   | FastAPI, Uvicorn                |
| DB   | RDS(Mysql), Pinecone(Vector DB) |
| 인프라  | Docker, AWS EC2, Git Actions    |

---

## 🧾 워크플로우

![워크플로우](/images/workflow1.png)

---

## 📸 서비스 화면 예시

![캡쳐화면](/images/image1.png)
![캡쳐화면](/images/image2.png)
![캡쳐화면](/images/image3.png)
![캡쳐화면](/images/image4.png)

