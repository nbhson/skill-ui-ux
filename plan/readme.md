# Plan — skill-ui-ux

> Kế hoạch nâng cấp chuẩn enterprise — cập nhật: 28/10/2026

## Tổng quan

Skill bộ 12 design styles (Minimalism → Glassmorphism) cho OpenCode: mỗi style
có SKILL.md đầy đủ 8 sections + `data.json` machine-readable + validator CI.

## Đánh giá

| Hạng mục | Kết quả |
|----------|---------|
| 12 SKILL.md — đủ 8 sections chuẩn | ✅ Pass |
| data.json hợp lệ, 12 styles | ✅ |
| Anti-patterns khớp giữa JSON ↔ MD | ✅ |
| 91 palette hex hợp lệ | ✅ |
| Ma trận combination đối xứng | ✅ |
| Figma URLs well-formed | ✅ |
| `scripts/validate_skills.py` CI check | ✅ Có sẵn, pass toàn bộ |

## Vấn đề phát hiện & đã sửa

1. **[BUG-DOCS] Schema data.json bị mô tả sai trong README.md + root SKILL.md**
   - Docs hứa: `{ "styles": [{ "id", "palette", "combinations", "antiPatterns" }] }`
   - Thực tế: các field nằm trong `styles[].sections.*`
   - Hậu quả: AI agent đọc theo spec sẽ nhận `undefined` → fail silently
   - **Fix:** cập nhật JSON snippet trong `README.md` + `SKILL.md` phản ánh đúng schema `sections: { palette, combinations, antiPatterns }`

## Kiểm chứng

```
python3 scripts/validate_skills.py  →  All checks passed ✓
```

## Backlog đề xuất

- [ ] GitHub Actions workflow chạy `validate_skills.py` tự động
- [ ] Thêm ví dụ CSS tokens khởi động cho từng style vào `assets/`
- [ ] Kiểm tra tương thích phiên bản: thêm section "Version" vào root SKILL.md
