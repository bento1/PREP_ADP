from weasyprint import HTML,CSS
from pathlib import Path

# HTML 폴더 지정
# input_dir = Path("~/.")
output_pdf = Path("merged_output2.pdf")

# 모든 HTML 파일 정렬해서 읽기
# html_files = sorted(input_dir.glob("*.html"))

css_font = CSS(string='''
@font-face {
  font-family: "AppleSDGothicNeo";
  src: url("/System/Library/Fonts/AppleSDGothicNeo.ttc");
}
body {
  font-family: "AppleSDGothicNeo", sans-serif;
  font-size: 13px;
  line-height: 1.5;
}
''')
# if not html_files:
    # raise FileNotFoundError("❌ HTML 파일이 없습니다. (html_pages/*.html)")
html_files=["/Users/dongunyun/github.com/PREP_ADP/venv세팅법.html",
            "/Users/dongunyun/github.com/PREP_ADP/1.EDA.html",
            # "/Users/dongunyun/github.com/PREP_ADP/2. 통계분석.html",
            # "/Users/dongunyun/github.com/PREP_ADP/7. 시계열분석.html",
            # "/Users/dongunyun/github.com/PREP_ADP/8. 텍스트마이닝.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출22.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출23.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출26.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출27.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출28.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출29.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출30.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기출31.html",
            # "/Users/dongunyun/github.com/PREP_ADP/확률분포.html",
            # "/Users/dongunyun/github.com/PREP_ADP/통계.html",
            # "/Users/dongunyun/github.com/PREP_ADP/statistics1.html",
            # "/Users/dongunyun/github.com/PREP_ADP/통계-회귀.html",
            # "/Users/dongunyun/github.com/PREP_ADP/베이지안.html",
            # "/Users/dongunyun/github.com/PREP_ADP/연관규칙.html",
            # "/Users/dongunyun/github.com/PREP_ADP/시계열분석.html",
            # "/Users/dongunyun/github.com/PREP_ADP/Statsmodel을_활용한_ARIMA_모델_.html",
            # "/Users/dongunyun/github.com/PREP_ADP/Linear_model.html",
            # "/Users/dongunyun/github.com/PREP_ADP/pandas_datebinnin.html",
            # "/Users/dongunyun/github.com/PREP_ADP/preprocessing.html",
            # "/Users/dongunyun/github.com/PREP_ADP/em.html",
            # "/Users/dongunyun/github.com/PREP_ADP/ensemble.html",
            # "/Users/dongunyun/github.com/PREP_ADP/factor_analyze.html",
            # "/Users/dongunyun/github.com/PREP_ADP/gmm.html",
            # "/Users/dongunyun/github.com/PREP_ADP/naive_bayse.html",
            # "/Users/dongunyun/github.com/PREP_ADP/optimization.html",
            # "/Users/dongunyun/github.com/PREP_ADP/pca.html",
            # "/Users/dongunyun/github.com/PREP_ADP/SNA.html",
            # "/Users/dongunyun/github.com/PREP_ADP/SNA_2.html",
            # "/Users/dongunyun/github.com/PREP_ADP/SOM.html",
            # "/Users/dongunyun/github.com/PREP_ADP/tf-idf.html",
            # "/Users/dongunyun/github.com/PREP_ADP/tree.html",
            # "/Users/dongunyun/github.com/PREP_ADP/기타분석.html",
            ]
# 각 HTML을 PDF 페이지로 렌더링
rendered_docs = [HTML(filename=f, encoding="utf-8").render() for f in html_files]

# 첫 번째 문서를 기준으로 병합
combined_pdf = rendered_docs[0]
for doc in rendered_docs[1:]:
    combined_pdf.pages.extend(doc.pages)

# 최종 PDF 저장
combined_pdf.write_pdf(output_pdf, stylesheets=[css_font])

print(f"✅ {len(html_files)}개의 HTML이 '{output_pdf}' 로 병합되었습니다.")
