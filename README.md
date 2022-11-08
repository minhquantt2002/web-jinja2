# WEB BLOG - FASTAPI AND MYSQL

- Báo cáo công việc đã làm lần 2:
  - 

- Guide: 
  - Cần cài các thư sử dụng trong project. Chạy lệnh: pip install -r requirements.txt
  - Tạo database local là blog. Trong database.py fixed cứng url: 'mysql+pymysql://root:@localhost/blog'
  - migrate dữ liệu từ các bảng trong file model. Trước tiên phải thay đổi host tại mỗi máy khác nhau trong file alembic.ini (sqlachemy.url) 
  và chạy câu lệnh migrate: alembic upgrade head
  - Run server (chạy project), tại dir fa-3_7 chạy lệnh: uvicorn server.main:app - lên trình duyệt truy cập localhost:8000


- Báo cáo ngày 08/11/2022
  - phía admin tạo được giao diện thêm sửa xóa một article, 1 video
  - phía user xem các article, video
  - thêm tính năng phân quyền authz cho admin portal (TODO)

- Complete BTL: ngày 08/11/2022