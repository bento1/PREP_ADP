pdf_files=["/Users/dongunyun/github.com/PREP_ADP/pdf/venv세팅법.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/1.EDA.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/2. 통계분석.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/7. 시계열분석.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/8. 텍스트마이닝.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출22.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출23.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출26.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출27.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출28.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출29.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출30.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기출31.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/확률분포.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/통계.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/statistics1.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/통계-회귀.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/베이지안.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/연관규칙.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/시계열분석.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/Statsmodel을_활용한_ARIMA_모델_.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/Linear_model.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/pandas_datebinnin.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/preprocessing.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/em.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/ensemble.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/factor_analyze.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/gmm.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/naive_bayse.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/optimization.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/pca.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/SNA.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/SNA_2.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/SOM.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/tf-idf.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/tree.pdf",
            "/Users/dongunyun/github.com/PREP_ADP/pdf/기타분석.pdf",
            ]

output_file = "merged_compact.pdf"
import fitz  # PyMuPDF
from pathlib import Path

def merge_pdfs_no_margin(
    folder="/Users/dongunyun/github.com/PREP_ADP/pdf",
    output="merged_tight_2x2.pdf",
    dpi=150
):
    pdf_files = sorted(Path(folder).glob("*.pdf"))
    A4_W, A4_H = fitz.paper_size("a4")  # portrait A4
    cols, rows = 1, 1                # 2x2 그리드

    # A4 가로, 세로 크기 그대로 사용 (여백 X)
    cell_w = A4_W / cols
    cell_h = A4_H / rows

    output_doc = fitz.open()
    pixmaps = []

    # 각 PDF 페이지를 이미지로 변환
    for file in pdf_files:
        doc = fitz.open(file)
        for page in doc:
            # PDF → pixmap (이미지)
            pix = page.get_pixmap(dpi=dpi,clip=page.cropbox,  alpha=False)
            pixmaps.append(pix)

    # 4개 단위로 묶어서 A4에 배치
    for i in range(0, len(pixmaps), cols * rows):
        new_page = output_doc.new_page(width=A4_W, height=A4_H)
        batch = pixmaps[i:i + cols * rows]

        for j, pix in enumerate(batch):
            c = j % cols
            r = j // cols
            # 좌표 계산 (여백 없이)
            x0 = c * cell_w
            y0 = r * cell_h
            rect = fitz.Rect(x0, y0, x0 + cell_w, y0 + cell_h)
            new_page.insert_image(rect, pixmap=pix, overlay=False)

    output_doc.save(output)
    output_doc.close()
    print(f"✅ {output} 생성 완료 — 여백 없이 2x2 배치")

# 사용 예시
merge_pdfs_no_margin("/Users/dongunyun/github.com/PREP_ADP/pdf", "merged_no_margin_1x1.pdf", dpi=300)