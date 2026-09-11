# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**


**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Thứ tự phản hồi qua 4 lần khác nhau, cho thấy sự ngẫu nhiên của bước sinh từ. Model bị giới hạn bởi thời điểm dữ liệu huấn luyện, không tự động cập nhật sự kiện mới.


### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature khoảng 0.1–0.2 cho chatbot hỗ trợ khách hàng, vì mục tiêu chính là độ chính xác và nhất quán, không phải sự sáng tạo. Khách hàng cần nhận được thông tin đáng tin cậy về chính sách, sản phẩm.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> 16.666666666666668

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Persona "giáo viên tiểu học" dùng ví dụ đời thường (cuốn sổ, viên kẹo), ngôn ngữ đơn giản. Persona "chuyên gia tài chính" dùng thuật ngữ chuyên môn (distributed ledger, hàm băm), trình bày có cấu trúc kỹ thuật. System prompt ảnh hưởng mạnh đến từ vựng và độ phức tạp của câu trả lời, dù câu hỏi giống hệt nhau.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Với đoạn 97 từ: ước lượng cho 129 token, tiktoken thật cho 116 token — chênh lệch ~10%. Tiếng Việt tốn nhiều token hơn tiếng Anh vì tokenizer được huấn luyện chủ yếu trên tiếng Anh, còn dấu thanh và ký tự Unicode tiếng Việt thường bị tách thành nhiều token cho một từ.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất với chatbot tương tác trực tiếp và người dùng thấy chữ hiện dần ngay lập tức, cảm giác phản hồi nhanh dù model cần vài giây để sinh hết câu trả lời. Non-streaming phù hợp hơn khi xử lý hàng loạt/ngầm (batch job, gọi API để lưu vào database), vì lúc đó không có ai đang chờ xem trực tiếp, chỉ cần kết quả cuối cùng.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Nếu delay cố định, hàng nghìn client bị lỗi cùng lúc sẽ retry đồng loạt vào đúng 1 thời điểm (sau đúng 1 giây), làm server quá tải thêm lần nữa — gọi là "thundering herd problem". Exponential backoff trải đều thời điểm retry ra (delay tăng dần và khác nhau giữa các client), giảm áp lực dồn cục cho server.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Tôi chọn persona "trợ lý học tiếng Anh, chỉ trả lời bằng tiếng Việt, giải thích ngắn gọn không quá 3 câu". System prompt: "Bạn là trợ lý học tiếng Anh, chỉ trả lời bằng tiếng Việt, giải thích ngắn gọn không quá 3 câu." Tôi chỉ định "chỉ trả lời bằng tiếng Việt" vì người học tiếng Anh mới thường khó hiểu nếu phần giải thích cũng bằng tiếng Anh — cần ngôn ngữ mẹ đẻ để tiếp thu khái niệm nhanh hơn. Tôi thêm "không quá 3 câu" vì trợ lý học tập cần súc tích, tránh làm người học choáng ngợp với đoạn văn dài, dễ mất tập trung vào điểm chính.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất của trợ lý hiện tại là chỉ giữ 3 lượt hội thoại gần nhất (history = history[-6:]) và không có bộ nhớ giữa các lần chạy khác nhau — mỗi lần khởi động lại chương trình, trợ lý hoàn toàn quên hết cuộc trò chuyện trước đó. Cải thiện đề xuất: lưu history vào file JSON hoặc database nhẹ (SQLite) sau mỗi lượt hội thoại, và load lại khi khởi động chương trình — bằng cách thêm hàm save_history() gọi sau mỗi lượt, và load_history() gọi lúc bắt đầu run_assistant(), thay vì luôn khởi tạo history = [].

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
