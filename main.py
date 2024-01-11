from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/")
def get_answer(query: Query):
    # Bạn có thể thêm logic xử lý câu hỏi ở đây.
    # Hiện tại, chúng tôi chỉ đơn giản trả về câu trả lời cố định.
    if query.question:
        return {"answer": "Đây là câu trả lời cho câu hỏi của bạn."}
    else:
        raise HTTPException(status_code=400, detail="No question provided")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
