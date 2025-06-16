import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="이민복 자기소개서",
    page_icon="👨 🚒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 스타일링
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; margin-bottom: 2rem;">
        <h1 style="color: #7c3aed; font-size: 1.5rem; margin-bottom: 0.5rem;">👨 🚒 이민복</h1>
        <p style="color: #6b7280; font-size: 0.9rem; margin: 0;">소방안전 전문가 지망생</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 네비게이션 메뉴 (5개로 확장)
    page = st.radio(
        "",
        ["🌟 소개 & 가치관", "🌿 성격 & 강점", "🛠️ 기술 & 프로젝트", "🎨 취미 & 관심사", "🚀 포부 & 연락처"],
        key="navigation"
    )

# 메인 컨텐츠 영역 스타일링
st.markdown("""
<style>
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1200px;
    }
    .stRadio > div {
        gap: 1rem;
    }
    .stRadio > div > label {
        background: white;
        padding: 0.8rem 1rem;
        border-radius: 8px;
        border: 2px solid #f3f4f6;
        transition: all 0.3s ease;
        cursor: pointer;
        font-weight: 500;
    }
    .stRadio > div > label:hover {
        border-color: #7c3aed;
        background: #f8fafc;
    }
    .stRadio > div > label[data-checked="true"] {
        border-color: #7c3aed;
        background: #7c3aed;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# HTML 템플릿 함수 (개선된 버전)
def render_enhanced_html(content, height=600):
    html_template = f"""
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
        <style>
            body {{
                font-family: 'Noto Sans KR', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 1rem;
                margin: 0;
                min-height: 100vh;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                padding: 0;
            }}
            .card {{
                background: white;
                padding: 2.5rem;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                margin-bottom: 1.5rem;
                position: relative;
                overflow: hidden;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            .card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            }}
            .card::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 4px;
                background: linear-gradient(90deg, #7c3aed, #3b82f6, #06d6a0);
            }}
            .card h2 {{
                font-size: 2rem;
                font-weight: 700;
                background: linear-gradient(135deg, #7c3aed, #3b82f6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 1.5rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            .card h3 {{
                font-size: 1.3rem;
                font-weight: 600;
                color: #374151;
                margin: 1.5rem 0 1rem 0;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid #f3f4f6;
            }}
            .card p {{
                font-size: 1.1rem;
                line-height: 1.8;
                color: #4b5563;
                margin-bottom: 1.2rem;
            }}
            .skill-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1rem;
                margin: 1.5rem 0;
            }}
            .skill-item {{
                background: #f8fafc;
                padding: 1rem;
                border-radius: 10px;
                border-left: 4px solid #7c3aed;
                transition: all 0.3s ease;
            }}
            .skill-item:hover {{
                background: #f1f5f9;
                transform: translateX(5px);
            }}
            .hobby-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
                margin: 1.5rem 0;
            }}
            .hobby-card {{
                background: linear-gradient(135deg, #fef3c7, #fed7d7);
                padding: 1.5rem;
                border-radius: 15px;
                border: 2px solid #f59e0b;
                transition: all 0.3s ease;
            }}
            .hobby-card:hover {{
                transform: scale(1.05);
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            }}
            .hobby-card.blue {{
                background: linear-gradient(135deg, #dbeafe, #bfdbfe);
                border-color: #3b82f6;
            }}
            .hobby-card.green {{
                background: linear-gradient(135deg, #d1fae5, #a7f3d0);
                border-color: #10b981;
            }}
            .hobby-card.purple {{
                background: linear-gradient(135deg, #ede9fe, #ddd6fe);
                border-color: #8b5cf6;
            }}
            .contact-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin: 1.5rem 0;
            }}
            .contact-item {{
                background: linear-gradient(135deg, #7c3aed, #3b82f6);
                color: white;
                padding: 1.5rem;
                border-radius: 12px;
                text-align: center;
                transition: transform 0.3s ease;
            }}
            .contact-item:hover {{
                transform: scale(1.05);
            }}
            .contact-item i {{
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
                display: block;
            }}
            .highlight-box {{
                background: linear-gradient(135deg, #fef3c7, #fde68a);
                padding: 1.5rem;
                border-radius: 12px;
                border-left: 4px solid #f59e0b;
                margin: 1.5rem 0;
            }}
            .strength-list {{
                list-style: none;
                padding: 0;
            }}
            .strength-list li {{
                background: #f8fafc;
                margin: 0.8rem 0;
                padding: 1rem;
                border-radius: 8px;
                border-left: 4px solid #06d6a0;
                font-size: 1.1rem;
                transition: all 0.3s ease;
            }}
            .strength-list li:hover {{
                background: #f1f5f9;
                transform: translateX(8px);
            }}
            .strength-list li::before {{
                content: '✓';
                color: #06d6a0;
                font-weight: bold;
                margin-right: 0.5rem;
            }}
            .icon-large {{
                font-size: 2.5rem;
                margin-bottom: 1rem;
                display: block;
                text-align: center;
            }}
            @keyframes fadeInUp {{
                from {{
                    opacity: 0;
                    transform: translateY(30px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            .card {{
                animation: fadeInUp 0.6s ease-out;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {content}
        </div>
    </body>
    </html>
    """
    components.html(html_template, height=height, scrolling=True)

# 각 페이지 내용
if page == "🌟 소개 & 가치관":
    content = """
    <div class="card">
        <h2><i class="fas fa-star"></i> 소개 & 가치관</h2>
        
        <div class="highlight-box">
            <h3>💫 나의 꿈의 시작</h3>
            <p>어릴 적부터 위급 상황에서 누군가를 돕고 싶다는 꿈을 키워왔습니다. 
            화재 대피 훈련에서 침착하게 대처하던 선생님의 모습은 저의 롤모델이 되었고, 
            결국 소방 분야의 전문가로 성장하고자 건양대학교 재난안전소방학과에 진학했습니다.</p>
        </div>
        
        <h3>🎯 핵심 가치관</h3>
        <div class="skill-grid">
            <div class="skill-item">
                <h4 style="color: #7c3aed; margin-bottom: 0.5rem;">🛡️ 안전 수호</h4>
                <p style="margin: 0; font-size: 1rem;">사람들의 안전을 지키며 세상을 더 나은 방향으로 바꾸는 것</p>
            </div>
            <div class="skill-item">
                <h4 style="color: #7c3aed; margin-bottom: 0.5rem;">📈 지속적 성장</h4>
                <p style="margin: 0; font-size: 1rem;">배우고 도전하며 끊임없이 성장하는 것</p>
            </div>
        </div>
        
        <p style="text-align: center; font-style: italic; color: #6b7280; font-size: 1.2rem; margin-top: 2rem;">
            "작은 관심과 준비가 큰 생명을 구할 수 있다는 믿음으로 살아가고 있습니다"
        </p>
    </div>
    """
    render_enhanced_html(content, height=650)

elif page == "🌿 성격 & 강점":
    content = """
    <div class="card">
        <h2><i class="fas fa-leaf"></i> 성격 & 강점</h2>
        
        <h3>🌟 나의 성격</h3>
        <p>저는 밝고 긍정적인 태도로 팀에 좋은 에너지를 주려고 노력하며, 
        책임감 있게 맡은 업무를 끝까지 완수하는 성격입니다. 
        계획적으로 업무를 처리하며, 위기 상황에서도 침착하게 문제를 해결해왔습니다.</p>
        
        <h3>💪 핵심 강점</h3>
        <ul class="strength-list">
            <li><strong>긍정적 에너지:</strong> 팀에 활력을 불어넣는 밝은 성격</li>
            <li><strong>강한 책임감:</strong> 맡은 업무를 끝까지 완수하는 신뢰성</li>
            <li><strong>계획적 사고:</strong> 체계적이고 논리적인 업무 처리</li>
            <li><strong>위기 대응력:</strong> 긴급 상황에서의 침착한 판단력</li>
            <li><strong>소통 능력:</strong> 팀원들과의 원활한 커뮤니케이션</li>
        </ul>
        
        <div class="highlight-box">
            <h3>🔄 지속적인 개선</h3>
            <p>완벽을 추구하다 가끔은 결정이 늦어질 때도 있지만, 
            이를 보완하기 위해 소통과 피드백을 중시하며 개선해 나가고 있습니다. 
            약점을 인정하고 개선하려는 자세가 저의 또 다른 강점이라고 생각합니다.</p>
        </div>
    </div>
    """
    render_enhanced_html(content, height=700)

elif page == "🛠️ 기술 & 프로젝트":
    content = """
    <div class="card">
        <h2><i class="fas fa-tools"></i> 기술 & 프로젝트 경험</h2>
        
        <h3>🚒 소방 전문 기술</h3>
        <div class="skill-grid">
            <div class="skill-item">
                <h4 style="color: #dc2626;">🔥 소방설비 전문</h4>
                <p style="margin: 0;">소화설비, 경보설비 점검 및 유지보수</p>
            </div>
            <div class="skill-item">
                <h4 style="color: #dc2626;">📜 전문 자격증</h4>
                <p style="margin: 0;">소방설비기사(전기) 자격증 보유</p>
            </div>
        </div>
        
        <h3>💻 기술 스킬</h3>
        <div class="skill-grid">
            <div class="skill-item">
                <h4 style="color: #3b82f6;">🐍 Python</h4>
                <p style="margin: 0;">데이터 분석 및 자동화 스크립트 작성</p>
            </div>
            <div class="skill-item">
                <h4 style="color: #3b82f6;">🌐 웹 기술</h4>
                <p style="margin: 0;">HTML/CSS, Tailwind CSS, JavaScript</p>
            </div>
        </div>
        
        <h3>🎯 주요 프로젝트</h3>
        <ul class="strength-list">
            <li><strong>소방설비 점검 시뮬레이션:</strong> 실무 능력 향상을 위한 가상 환경 구축</li>
            <li><strong>재난안전 교육 콘텐츠:</strong> 초등학생 대상 교육 자료 및 영상 제작</li>
            <li><strong>안전 교육 시스템:</strong> 효과적인 안전 교육을 위한 디지털 솔루션 개발</li>
        </ul>
        
        <div class="highlight-box">
            <h3>📈 성과와 배움</h3>
            <p>이러한 프로젝트들을 통해 현장 이해도와 커뮤니케이션 능력을 크게 강화했으며, 
            이론과 실무를 연결하는 능력을 기를 수 있었습니다. 
            특히 교육 콘텐츠 제작 경험은 복잡한 내용을 쉽게 전달하는 능력을 키워주었습니다.</p>
        </div>
    </div>
    """
    render_enhanced_html(content, height=750)

elif page == "🎨 취미 & 관심사":
    content = """
    <div class="card">
        <h2><i class="fas fa-palette"></i> 취미 & 관심사</h2>
        
        <p style="text-align: center; font-size: 1.2rem; color: #4b5563; margin-bottom: 2rem;">
            "일과 삶의 균형을 통해 더 나은 전문가가 되고자 합니다"
        </p>
        
        <h3>🎯 주요 취미 활동</h3>
        <div class="hobby-grid">
            <div class="hobby-card">
                <i class="fas fa-code icon-large" style="color: #f59e0b;"></i>
                <h4 style="color: #92400e; margin-bottom: 0.8rem; font-size: 1.2rem;">💻 프로그래밍</h4>
                <p style="margin: 0; color: #78350f;">
                    Python과 웹 개발을 통해 창의적인 솔루션을 만드는 것을 즐깁니다. 
                    특히 소방 분야에 적용할 수 있는 기술적 아이디어를 구현하는 데 관심이 많습니다.
                </p>
            </div>
            
            <div class="hobby-card blue">
                <i class="fas fa-book-open icon-large" style="color: #3b82f6;"></i>
                <h4 style="color: #1e40af; margin-bottom: 0.8rem; font-size: 1.2rem;">📚 독서 & 학습</h4>
                <p style="margin: 0; color: #1e3a8a;">
                    소방안전 관련 전문서적과 기술 트렌드 관련 도서를 꾸준히 읽으며, 
                    온라인 강의를 통해 새로운 지식을 습득하는 것을 좋아합니다.
                </p>
            </div>
            
            <div class="hobby-card green">
                <i class="fas fa-running icon-large" style="color: #10b981;"></i>
                <h4 style="color: #047857; margin-bottom: 0.8rem; font-size: 1.2rem;">🏃 ♂️ 운동 & 건강관리</h4>
                <p style="margin: 0; color: #064e3b;">
                    체력이 중요한 소방 분야 특성상 꾸준한 운동을 하고 있습니다. 
                    주로 러닝과 웨이트 트레이닝을 통해 체력과 정신력을 기르고 있습니다.
                </p>
            </div>
            
            <div class="hobby-card purple">
                <i class="fas fa-users icon-large" style="color: #8b5cf6;"></i>
                <h4 style="color: #6b21a8; margin-bottom: 0.8rem; font-size: 1.2rem;">👥 봉사활동</h4>
                <p style="margin: 0; color: #581c87;">
                    지역 안전 교육 봉사와 응급처치 교육 지원 활동을 통해 
                    배운 지식을 사회에 환원하고 실무 경험을 쌓고 있습니다.
                </p>
            </div>
        </div>
        
        <h3>🌟 특별한 관심사</h3>
        <ul class="strength-list">
            <li><strong>스마트 안전기술:</strong> IoT와 AI를 활용한 화재 예방 시스템에 대한 깊은 관심</li>
            <li><strong>교육 콘텐츠 제작:</strong> 복잡한 안전 지식을 쉽게 전달하는 방법 연구</li>
            <li><strong>팀워크 스포츠:</strong> 협력과 소통의 중요성을 배우는 단체 운동 활동</li>
            <li><strong>재난 대응 시뮬레이션:</strong> 다양한 재난 시나리오 분석과 대응 방안 연구</li>
        </ul>
        
        <div class="highlight-box">
            <h3>💡 취미를 통한 성장</h3>
            <p>이러한 취미 활동들은 단순한 여가가 아닌 전문성 향상의 도구가 되고 있습니다. 
            프로그래밍은 업무 효율성을, 운동은 체력과 정신력을, 봉사활동은 실무 경험과 사회적 책임감을 키워주고 있습니다. 
            앞으로도 이런 다양한 활동을 통해 균형 잡힌 전문가로 성장해 나가겠습니다.</p>
        </div>
    </div>
    """
    render_enhanced_html(content, height=900)

elif page == "🚀 포부 & 연락처":
    content = """
    <div class="card">
        <h2><i class="fas fa-rocket"></i> 입사 후 포부</h2>
        
        <div class="highlight-box">
            <h3>🎯 단기 목표 (1년 내)</h3>
            <p>배움의 자세를 가지고 맡은 일에 책임감을 다하며, 
            현장에서의 경험을 통해 실질적인 문제 해결 능력을 쌓겠습니다.</p>
        </div>
        
        <h3>🌟 장기 비전</h3>
        <ul class="strength-list">
            <li><strong>전문성 강화:</strong> 소방안전 분야의 전문가로 성장</li>
            <li><strong>팀워크 향상:</strong> 팀원과의 협력을 통해 시너지 창출</li>
            <li><strong>사회 기여:</strong> 안전한 사회 구현에 실질적 기여</li>
            <li><strong>혁신 추진:</strong> 새로운 기술과 아이디어로 업무 효율성 개선</li>
        </ul>
        
        <div style="text-align: center; margin: 2rem 0;">
            <p style="font-size: 1.3rem; font-weight: 600; color: #7c3aed;">
                "함께 성장하며 더 안전한 세상을 만들어가겠습니다"
            </p>
        </div>
    </div>
    
    <div class="card">
        <h2><i class="fas fa-envelope"></i> 연락처</h2>
        
        <div class="contact-grid">
            <div class="contact-item">
                <i class="fas fa-envelope"></i>
                <h4 style="margin: 0.5rem 0; font-size: 1rem;">이메일</h4>
                <p style="margin: 0; font-size: 0.9rem;">alsqhr1230@naver.com</p>
            </div>
            <div class="contact-item">
                <i class="fas fa-phone"></i>
                <h4 style="margin: 0.5rem 0; font-size: 1rem;">연락처</h4>
                <p style="margin: 0; font-size: 0.9rem;">010-5932-0281</p>
            </div>
            <div class="contact-item">
                <i class="fas fa-map-marker-alt"></i>
                <h4 style="margin: 0.5rem 0; font-size: 1rem;">위치</h4>
                <p style="margin: 0; font-size: 0.9rem;">충청남도 논산시</p>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: #f8fafc; border-radius: 8px;">
            <p style="margin: 0; color: #6b7280; font-size: 0.9rem;">
                언제든지 연락 주시면 성실히 답변드리겠습니다! 🤝
            </p>
        </div>
    </div>
    """
    render_enhanced_html(content, height=800)

# 푸터
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #6b7280; font-size: 0.9rem;">
    <p>Made with ❤️ by 이민복 | 소방안전 전문가를 꿈꾸며</p>
</div>
""", unsafe_allow_html=True)