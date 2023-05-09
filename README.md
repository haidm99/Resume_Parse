# File get_text
- Crop the image to the text area by model YOLOv8 with 8 labels box text area 
    ```
    (0: 'Địa chỉ hiện tại', 
    1: 'Ngày/tháng/năm sinh', 
    2: 'Giới tính', 
    3: 'Email', 
    4: 'Số điện thoại', 
    5: 'Họ và tên', 
    6: 'Text', 
    7: 'Vị trí mong muốn làm')
    ```
- Ocr the text area
- Return the text

# File extract_feature.py
- Extract the feature of the text area

# Run API
- Install requirement
```
pip install -r requirements.txt
```

- Run API
```
./run.sh
```

- Result will be saved in results.json with format:
```
{
    "image_path": "u_cv_1682554168.png",
    "info": {
        "Họ và tên": "VĂN THU HANH",
        "Vị trí mong muốn làm": "TƯ VẤN CHĂM SÓC KHÁCH HÀNG",
        "Số điện thoại": "0903268988",
        "Ngày/tháng/năm sinh": "24/02/1994",
        "Email": "hanh vietmedicare@gmail .com",
        "Giới tính": "",
        "Địa chỉ hiện tại": "Số 42\n31 ngõ 766 Đê La Thành; Hà Nội\nngách ",
        "Kinh nghiệm làm việc": "\nCông ty có\nVietmedicare\nVịtrí: Nhân viên telesales vê san\nphẩm dành cho phụ\nnữ sau sinh\nGọi điện, giới thiệu sản phẩm.\nCông ty cổ phần tập đoàn Giovani\nVịtrí: sale online\nChẳm sóc khách\nchỗt đon online, hỗ trợ store\nCông ty cố phần Lychee\nVị trí: sale online hổ trợ đào tạo\nchẳm sỏc khách hàng; chỗt đon online\nPhần\nhang",
        "Mục tiêu nghề nghiệp": "\nTrở thành một nhân viên telesales chuyên nghiệp; làm\nkhách hàng hài lòng và huớng đên hoàn thành\nmuc tiêu chung của\nNỗ lực trong việc học hỏi và bổ sung kiến thúc.\nnhững\ncông",
        "Trình độ học vấn": "\nTrung Cấp Quân Y /\nThòi gian: (2012\n2014)\nChuyên ngành: Điều dưõng đa khoa\nTổt nghiệp loai: Khả",
        "Kỹ năng": "",
        "Địa chỉ làm việc": "",
        "Giải thưởng": "",
        "Chứng chỉ": "",
        "Sở thích": "",
        "Người tham chiếu": "",
        "Hoạt động": "",
        "Dự án": "",
        "Thông tin bổ sung": ""
    }
}
```