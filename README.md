# Crypto Market Price Fetcher

## Mô tả
Đây là một tập lệnh Python bất đồng bộ (`async`) sử dụng `aiohttp` để lấy giá của các loại tiền điện tử từ API công khai của CoinGecko. Người dùng có thể nhập danh sách các ký hiệu coin họ muốn truy xuất giá, và chương trình sẽ hiển thị giá hiện tại của các đồng tiền đó.

## Cách hoạt động
- Người dùng nhập danh sách các coin muốn lấy giá, cách nhau bởi dấu phẩy.
- Chương trình tạo URL động dựa trên danh sách coin đó.
- Gửi yêu cầu HTTP đến API của CoinGecko để lấy dữ liệu giá.
- Hiển thị giá trị USD của từng đồng coin trên màn hình.

## Yêu cầu hệ thống
- Python 3.10
- `aiohttp` (Cài đặt bằng `pip install aiohttp`)

## Cách sử dụng
1. **Clone hoặc tải xuống dự án**:
   ```sh
   git clone https://github.com/itustuna0702/TokenPrice.git
   cd crypto-price-fetcher
3. **Thư viện cần thiết**:
   ```sh
   pip install -r requirements.txt
4. **Chạy chương trình**:
   ```sh
   python demo.py
   
4. **Nhập tên coin muốn truy xuất giá**:
   ```sh
   Nhập các ký hiệu coin, cách nhau bởi dấu phẩy (ví dụ: bitcoin,ethereum): bitcoin, solana, dogecoin

5. **Kết quả**:
   ```sh
   Checking CoinGecko...
   BITCOIN: $43,200.50
   SOLANA: $125.30
   DOGECOIN: $0.095
