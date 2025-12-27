from fastapi.testclient import TestClient
from main import app

# 1. Tạo một client giả lập (tương tự app.test_client() bên Flask)
client = TestClient(app=app)


def test_root():
    # 2. Gửi request GET đến "/"
    response = client.get("/")

    # 3. Kiểm tra status code (giống hệt Flask)
    assert response.status_code == 200

    # 4. Kiểm tra nội dung trả về
    # Khác biệt: FastAPI thường trả về JSON, nên ta dùng .json() thay vì .data (bytes)
    assert response.json() == "hello world"
