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


from pypdf import PdfReader, PdfWriter, Transformation

# 병합기 생성
merger = PdfWriter()

# 병합할 PDF 파일 목록
scale_factor=0.8
# 순서대로 추가
for pdf in pdf_files:
    reader = PdfReader(pdf)
    for page in reader.pages:
        # 스케일 변환 적용
        page.add_transformation(Transformation().scale(scale_factor))
        merger.add_page(page)

# 최종 병합 파일로 저장
merger.write("merged_output.pdf")
merger.close()

print("✅ merged_output.pdf 생성 완료!")
