import streamlit as st
import datetime
import re

# ページ基本設定
st.set_page_config(
    page_title="人間関係とコミュニケーション b後半 練習問題70選",
    page_icon="📝",
    layout="centered"
)

# 明朝体および見やすい高コントラスト・アイコン保護用カスタムCSS
st.markdown("""
<style>
  /* 全体の背景と基本文字色を強制的に固定（ダークモード干渉を防止） */
  .stApp {
    background-color: #f8fafc !important; /* 明るい清潔な背景色 */
    color: #111827 !important; /* 極濃テキスト */
  }

  /* フォント指定：明朝体（※アイコンフォントやSVGタグは除外） */
  html, body, [data-testid="stAppViewContainer"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, label, input, textarea, select {
    font-family: "Hiragino Mincho ProN", "Yu Mincho", "MS Mincho", "Source Han Serif", serif !important;
  }

  /* Streamlitのシステムアイコン（アコーディオンの矢印「.arrow_right」等の文字化け・重複表示を完全に防止） */
  [data-testid*="Icon"],
  [data-testid*="icon"],
  [data-testid="stExpanderToggleIcon"],
  .material-symbols-rounded,
  .material-symbols-outlined,
  .material-icons,
  [class*="material-symbols"],
  [class*="material-icons"] {
    font-family: "Material Symbols Rounded", "Material Icons", sans-serif !important;
    font-style: normal !important;
    font-weight: normal !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    display: inline-block !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
  }

  /* expander ヘッダーのレイアウト崩れ・文字重なり防止 */
  summary[data-testid="stExpanderSummary"] {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
  }
  summary[data-testid="stExpanderSummary"] p {
    margin: 0 !important;
    font-weight: bold !important;
    color: #1e3a8a !important;
  }

  /* 一般テキスト、見出し、ラジオボタンの文字色をくっきり黒に固定 */
  h1, h2, h3, h4, p, span:not([data-testid*="Icon"]):not(.material-symbols-rounded), label, div {
    color: #0f172a !important;
  }

  /* ルビ（ふりがな）の視認性向上（濃紺・太字・少し拡大） */
  ruby {
    ruby-align: center;
    color: #000000 !important;
    font-weight: 500;
  }
  rt {
    font-size: 0.65em !important; /* 少し大きくして潰れを防止 */
    font-weight: bold !important;  /* 細くかすれないよう太字化 */
    color: #1e3a8a !important;    /* ふりがなを視認しやすい濃紺色に設定 */
    line-height: 1.2 !important;
  }

  /* 学生情報入力ボックス */
  .student-box {
    background-color: #ffffff !important;
    border: 2px solid #475569 !important;
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  /* ナビゲーションボックス */
  .nav-box {
    background-color: #ffffff !important;
    border: 2px solid #64748b !important;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 18px;
  }

  /* 単元タグバッジ */
  .tag {
    display: inline-block;
    background-color: #e2e8f0;
    color: #1e293b !important;
    font-size: 0.8rem;
    font-weight: bold;
    padding: 2px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
  }

  /* 問題カード：白背景にくっきりした濃色の枠線 */
  .q-card {
    background-color: #ffffff !important;
    border: 1.5px solid #64748b !important; /* 枠線を濃くして境界を明瞭化 */
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 16px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
  }

  /* 問題文タイトル：純黒・太字 */
  .q-title {
    font-size: 1.05rem !important;
    font-weight: bold !important;
    margin-bottom: 10px;
    color: #000000 !important;
    line-height: 1.7;
  }

  /* 選択肢テキスト：視認性の高い濃色 */
  .opt-item {
    margin-left: 18px;
    font-size: 0.96rem !important;
    margin-bottom: 6px;
    line-height: 1.6;
    color: #111827 !important;
    font-weight: 500;
  }

  /* 入力欄（テキスト入力・ラジオボタン）自体の文字色も強制黒化 */
  .stTextInput input {
    color: #000000 !important;
    background-color: #ffffff !important;
    border: 1.5px solid #64748b !important;
  }
  
  /* ラジオボタン選択肢の文字 */
  div[role="radiogroup"] label p {
    color: #000000 !important;
    font-size: 1rem !important;
    font-weight: bold !important;
  }

  /* 採点バナー */
  .score-badge {
    text-align: center;
    background-color: #e0f2fe !important;
    border: 2px solid #0284c7 !important;
    border-radius: 8px;
    padding: 18px;
    margin: 20px 0;
  }
</style>
""", unsafe_allow_html=True)

# アプリヘッダー
st.markdown("""
<h2 style='text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 8px; color: #1e3a8a;'>
<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>とコミュニケーション b<ruby>後<rt>こう</rt>半<rt>はん</rt></ruby>
</h2>
<p style='text-align: center; font-size: 0.92rem; color: #475569;'>
練習問題アプリ（全70問・全漢字ふりがな付き）｜テキストファイル提出＆コピーペースト対応
</p>
""", unsafe_allow_html=True)

# 1. 提出用 学生情報入力欄（最上部に設置）
st.markdown("<div class='student-box'>", unsafe_allow_html=True)
st.markdown("### 👤 学生情報の入力（提出必須）")
col1, col2, col3 = st.columns([1, 1.2, 1.5])
with col1:
    s_class = st.text_input("クラス名（組）", placeholder='例"25B"')
with col2:
    s_id = st.text_input("学籍番号", placeholder='例"9259999"')
with col3:
    s_name = st.text_input("名前（氏名）", placeholder='例"ヤグラ タロウ"')
st.markdown("</div>", unsafe_allow_html=True)

# ルビ除去用補助関数
def remove_ruby(text):
    if not text:
        return ""
    text_clean = re.sub(r'<rt>.*?</rt>', '', text)
    text_clean = re.sub(r'</?ruby>', '', text_clean)
    return text_clean

QUESTIONS = [
  {
    "id": 1,
    "section": "発達心理学からみた人間関係",
    "stem": "<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>の<ruby>一<rt>いち</rt></ruby><ruby>生<rt>せい</rt></ruby><ruby>涯<rt>がい</rt></ruby>にわたる<ruby>心<rt>しん</rt>身<rt>しん</rt></ruby>の<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>や<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>プロセスを<ruby>対<rt>たい</rt></ruby><ruby>象<rt>しょう</rt></ruby>とする<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>の<ruby>領<rt>りょう</rt></ruby><ruby>域<rt>いき</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>臨<rt>りん</rt></ruby><ruby>床<rt>しょう</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>",
      "<ruby>生<rt>せい</rt></ruby><ruby>涯<rt>がい</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>",
      "<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>生<rt>せい</rt></ruby><ruby>涯<rt>がい</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>生<rt>せい</rt></ruby><ruby>涯<rt>がい</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby>は、<ruby>受<rt>じゅ</rt>胎<rt>たい</rt></ruby>から<ruby>誕<rt>たん</rt>生<rt>じょう</rt></ruby>、<ruby>児<rt>じ</rt></ruby><ruby>童<rt>どう</rt></ruby><ruby>期<rt>き</rt></ruby>、<ruby>青<rt>せい</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>、<ruby>成<rt>せい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>期<rt>き</rt></ruby>、<ruby>老<rt>ろう</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>、そして<ruby>死<rt>し</rt></ruby>に<ruby>至<rt>いた</rt></ruby>るまでの<ruby>全<rt>ぜん</rt></ruby><ruby>生<rt>せい</rt></ruby><ruby>涯<rt>がい</rt></ruby>にわたる<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>過<rt>か</rt></ruby><ruby>程<rt>てい</rt></ruby>を<ruby>探<rt>たん</rt></ruby><ruby>究<rt>きゅう</rt></ruby>します。"
  },
  {
    "id": 2,
    "section": "発達心理学からみた人間関係",
    "stem": "エリクソンの<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby><ruby>説<rt>せつ</rt></ruby>において、<ruby>乳<rt>にゅう</rt></ruby><ruby>児<rt>じ</rt></ruby><ruby>期<rt>き</rt></ruby>（0〜1<ruby>歳<rt>さい</rt></ruby><ruby>頃<rt>ころ</rt></ruby>）に<ruby>獲<rt>かく</rt></ruby><ruby>得<rt>とく</rt></ruby>すべき<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>と<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>危<rt>き</rt></ruby><ruby>機<rt>き</rt></ruby>の<ruby>組<rt>ぐ</rt></ruby>み<ruby>合<rt>ごう</rt></ruby>わせとして、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>基<rt>き</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>頼<rt>らい</rt></ruby> <ruby>対<rt>たい</rt></ruby> <ruby>不<rt>ふ</rt></ruby><ruby>信<rt>しん</rt></ruby>",
      "<ruby>自<rt>じ</rt></ruby><ruby>律<rt>りつ</rt></ruby><ruby>性<rt>せい</rt></ruby> <ruby>対<rt>たい</rt></ruby> <ruby>恥<rt>はじ</rt></ruby>・<ruby>疑<rt>ぎ</rt></ruby><ruby>惑<rt>わく</rt></ruby>",
      "<ruby>勤<rt>きん</rt></ruby><ruby>勉<rt>べん</rt></ruby><ruby>性<rt>せい</rt></ruby> <ruby>対<rt>たい</rt></ruby> <ruby>劣<rt>れつ</rt></ruby><ruby>等<rt>とう</rt></ruby><ruby>感<rt>かん</rt></ruby>",
      "<ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>性<rt>せい</rt></ruby> <ruby>対<rt>たい</rt></ruby> <ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>拡<rt>かく</rt></ruby><ruby>散<rt>さん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>基<rt>き</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>頼<rt>らい</rt></ruby> <ruby>対<rt>たい</rt></ruby> <ruby>不<rt>ふ</rt></ruby><ruby>信<rt>しん</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>乳<rt>にゅう</rt></ruby><ruby>児<rt>じ</rt></ruby><ruby>期<rt>き</rt></ruby>に<ruby>養<rt>よう</rt></ruby><ruby>育<rt>いく</rt></ruby><ruby>者<rt>しゃ</rt></ruby>から<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なケアを<ruby>受<rt>う</rt></ruby>けることで「<ruby>基<rt>き</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>頼<rt>らい</rt></ruby>」が<ruby>育<rt>いく</rt></ruby>まれます。"
  },
  {
    "id": 3,
    "section": "発達心理学からみた人間関係",
    "stem": "エリクソンの<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby><ruby>説<rt>せつ</rt></ruby>において、<ruby>青<rt>せい</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>（12〜18<ruby>歳<rt>さい</rt></ruby><ruby>頃<rt>ころ</rt></ruby>）の<ruby>中<rt>ちゅう</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>基<rt>き</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>頼<rt>らい</rt></ruby>の<ruby>獲<rt>かく</rt></ruby><ruby>得<rt>とく</rt></ruby>",
      "<ruby>勤<rt>きん</rt></ruby><ruby>勉<rt>べん</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt></ruby><ruby>得<rt>とく</rt></ruby>",
      "アイデンティティ（<ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>性<rt>せい</rt></ruby>）の<ruby>確<rt>かく</rt></ruby><ruby>立<rt>りつ</rt></ruby>",
      "<ruby>せい<rt>せい</rt></ruby><ruby>しょく<rt>しょく</rt></ruby><ruby>せい<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt></ruby><ruby>得<rt>とく</rt></ruby>"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（アイデンティティ（<ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>性<rt>せい</rt></ruby>）の<ruby>確<rt>かく</rt></ruby><ruby>立<rt>りつ</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>青<rt>せい</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>は「<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>は<ruby>何<rt>なに</rt></ruby><ruby>者<rt>しゃ</rt></ruby>か」を<ruby>問<rt>と</rt></ruby>い、<ruby>自<rt>じ</rt></ruby><ruby>我<rt>が</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>確<rt>かく</rt></ruby><ruby>立<rt>りつ</rt></ruby>する<ruby>重<rt>じゅう</rt></ruby><ruby>要<rt>よう</rt></ruby>な<ruby>時<rt>じ</rt></ruby><ruby>期<rt>き</rt></ruby>です。"
  },
  {
    "id": 4,
    "section": "発達心理学からみた人間関係",
    "stem": "エリクソンの<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby><ruby>説<rt>せつ</rt></ruby>において、<ruby>老<rt>ろう</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>（65<ruby>歳<rt>さい</rt></ruby><ruby>以<rt>い</rt></ruby><ruby>上<rt>じょう</rt></ruby>）の<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>として、<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby>の<ruby>人<rt>じん</rt></ruby><ruby>生<rt>せい</rt></ruby>を<ruby>振<rt>ふ</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>り<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れることを<ruby>指<rt>さ</rt></ruby>す<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>自<rt>じ</rt></ruby><ruby>我<rt>が</rt></ruby>の<ruby>統<rt>とう</rt></ruby><ruby>合<rt>ごう</rt></ruby>（<ruby>統<rt>とう</rt></ruby><ruby>合<rt>ごう</rt></ruby><ruby>性<rt>せい</rt></ruby>）",
      "<ruby>しん<rt>しん</rt></ruby><ruby>みつ<rt>みつ</rt></ruby><ruby>せい<rt>せい</rt></ruby>の<ruby>確<rt>かく</rt></ruby><ruby>立<rt>りつ</rt></ruby>",
      "<ruby>自<rt>じ</rt></ruby><ruby>律<rt>りつ</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt></ruby><ruby>得<rt>とく</rt></ruby>",
      "<ruby>じ<rt>じ</rt></ruby><ruby>はつ<rt>はつ</rt></ruby><ruby>せい<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt></ruby><ruby>得<rt>とく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>自<rt>じ</rt></ruby><ruby>我<rt>が</rt></ruby>の<ruby>統<rt>とう</rt></ruby><ruby>合<rt>ごう</rt></ruby>（<ruby>統<rt>とう</rt></ruby><ruby>合<rt>ごう</rt></ruby><ruby>性<rt>せい</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>老<rt>ろう</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>にはこれまでの<ruby>人<rt>じん</rt></ruby><ruby>生<rt>せい</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れ<ruby>統<rt>とう</rt></ruby><ruby>合<rt>ごう</rt></ruby>することが<ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>であり、それができないと<ruby>絶<rt>ぜつ</rt></ruby><ruby>望<rt>ぼう</rt></ruby>に<ruby>陥<rt>おちい</rt></ruby>ります。"
  },
  {
    "id": 5,
    "section": "発達心理学からみた人間関係",
    "stem": "<ruby>乳<rt>にゅう</rt></ruby><ruby>幼<rt>よう</rt></ruby><ruby>児<rt>じ</rt></ruby><ruby>期<rt>き</rt></ruby>に<ruby>特<rt>とく</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>養<rt>よう</rt></ruby><ruby>育<rt>いく</rt></ruby><ruby>者<rt>しゃ</rt></ruby>との<ruby>間<rt>かん</rt></ruby>に<ruby>形<rt>けい</rt></ruby><ruby>成<rt>せい</rt></ruby>される<ruby>情<rt>じょう</rt></ruby><ruby>愛<rt>あい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>絆<rt>きずな</rt></ruby>であり、<ruby>子<rt>こ</rt></ruby>どもの<ruby>安<rt>あん</rt></ruby><ruby>心<rt>こころ</rt></ruby>の<ruby>基<rt>き</rt></ruby><ruby>地<rt>ち</rt></ruby>となる<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "アイデンティティ",
      "<ruby>愛<rt>あい</rt></ruby><ruby>着<rt>ちゃく</rt></ruby>（アタッチメント）",
      "ソーシャルスキル",
      "コンプライアンス"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>愛<rt>あい</rt></ruby><ruby>着<rt>ちゃく</rt></ruby>（アタッチメント））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ボウルビィが<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>した<ruby>愛<rt>あい</rt></ruby><ruby>着<rt>ちゃく</rt></ruby>は、<ruby>子<rt>こ</rt></ruby>どもの<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>安<rt>あん</rt></ruby><ruby>定<rt>てい</rt></ruby>と<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>の<ruby>土<rt>ど</rt></ruby><ruby>台<rt>だい</rt></ruby>となります。"
  },
  {
    "id": 6,
    "section": "発達心理学からみた人間関係",
    "stem": "<ruby>乳<rt>にゅう</rt></ruby><ruby>幼<rt>よう</rt></ruby><ruby>児<rt>じ</rt></ruby><ruby>期<rt>き</rt></ruby>の<ruby>愛<rt>あい</rt></ruby><ruby>着<rt>ちゃく</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>を<ruby>通<rt>つう</rt></ruby>じて<ruby>形<rt>けい</rt></ruby><ruby>成<rt>せい</rt></ruby>され、その<ruby>後<rt>こう</rt></ruby>の<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>のパターンや<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>への<ruby>期<rt>き</rt></ruby><ruby>待<rt>たい</rt></ruby>の<ruby>枠<rt>わく</rt></ruby><ruby>組<rt>ぐ</rt></ruby>みとなる<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>枠<rt>わく</rt></ruby><ruby>組<rt>ぐ</rt></ruby>みを<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>内<rt>ない</rt></ruby><ruby>的<rt>てき</rt></ruby>ワーキングモデル",
      "<ruby>外<rt>がい</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>機<rt>き</rt></ruby>づけ",
      "<ruby>防<rt>ぼう</rt></ruby><ruby>衛<rt>えい</rt></ruby><ruby>機<rt>き</rt></ruby><ruby>制<rt>せい</rt></ruby>",
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>規<rt>き</rt></ruby><ruby>範<rt>はん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>内<rt>ない</rt></ruby><ruby>的<rt>てき</rt></ruby>ワーキングモデル）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>幼<rt>よう</rt></ruby><ruby>少<rt>しょう</rt></ruby><ruby>期<rt>き</rt></ruby>に<ruby>築<rt>ちく</rt></ruby>かれた<ruby>愛<rt>あい</rt></ruby><ruby>着<rt>ちゃく</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>験<rt>けん</rt></ruby>は<ruby>内<rt>ない</rt></ruby><ruby>的<rt>てき</rt></ruby>ワーキングモデルとして<ruby>内<rt>ない</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>化<rt>か</rt></ruby>され、<ruby>成<rt>せい</rt></ruby><ruby>長<rt>ちょう</rt></ruby><ruby>後<rt>こう</rt></ruby>の<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>に<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>を<ruby>与<rt>よ</rt></ruby>えます。"
  },
  {
    "id": 7,
    "section": "発達心理学からみた人間関係",
    "stem": "トマスとチェスによる<ruby>乳<rt>にゅう</rt></ruby><ruby>幼<rt>よう</rt></ruby><ruby>児<rt>じ</rt></ruby>の<ruby>気<rt>き</rt></ruby><ruby>質<rt>しつ</rt></ruby><ruby>研<rt>けん</rt></ruby><ruby>究<rt>きゅう</rt></ruby>において、<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>リズムが<ruby>規<rt>き</rt></ruby><ruby>則<rt>そく</rt></ruby><ruby>的<rt>てき</rt></ruby>で<ruby>新<rt>しん</rt></ruby>しい<ruby>環<rt>かん</rt></ruby><ruby>境<rt>きょう</rt></ruby>にも<ruby>比<rt>ひ</rt></ruby><ruby>較<rt>かく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby>しやすいタイプの<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>扱<rt>あつか</rt></ruby>いやすい<ruby>子<rt>こ</rt></ruby>（<ruby>易<rt>やさ</rt></ruby>しい<ruby>気<rt>き</rt></ruby><ruby>質<rt>しつ</rt></ruby>）",
      "<ruby>扱<rt>あつか</rt></ruby>いにくい<ruby>子<rt>こ</rt></ruby>（<ruby>難<rt>むずか</rt></ruby>しい<ruby>気<rt>き</rt></ruby><ruby>質<rt>しつ</rt></ruby>）",
      "<ruby>順<rt>じゅん</rt></ruby><ruby>応<rt>おう</rt></ruby>の<ruby>遅<rt>おそ</rt></ruby>い<ruby>子<rt>こ</rt></ruby>（<ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がりの<ruby>遅<rt>おそ</rt></ruby>い<ruby>子<rt>こ</rt></ruby>）",
      "<ruby>無<rt>む</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>心<rt>しん</rt></ruby>な<ruby>子<rt>こ</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>扱<rt>あつか</rt></ruby>いやすい<ruby>子<rt>こ</rt></ruby>（<ruby>易<rt>やさ</rt></ruby>しい<ruby>気<rt>き</rt></ruby><ruby>質<rt>しつ</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>規<rt>き</rt></ruby><ruby>則<rt>そく</rt></ruby><ruby>的<rt>てき</rt></ruby>で<ruby>機<rt>き</rt></ruby><ruby>嫌<rt>けん</rt></ruby>がよく、<ruby>新<rt>しん</rt></ruby>しい<ruby>刺<rt>し</rt></ruby><ruby>激<rt>げき</rt></ruby>にも<ruby>前<rt>ぜん</rt></ruby><ruby>向<rt>こう</rt></ruby>きに<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby>しやすいタイプです。"
  },
  {
    "id": 8,
    "section": "発達心理学からみた人間関係",
    "stem": "<ruby>学<rt>がく</rt></ruby><ruby>童<rt>どう</rt></ruby><ruby>期<rt>き</rt></ruby><ruby>後<rt>こう</rt></ruby><ruby>半<rt>はん</rt></ruby>（<ruby>小<rt>しょう</rt></ruby><ruby>学<rt>がく</rt></ruby><ruby>校<rt>こう</rt></ruby><ruby>高<rt>こう</rt></ruby><ruby>学<rt>がく</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>頃<rt>ころ</rt></ruby>）にみられる、<ruby>同<rt>どう</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>齢<rt>れい</rt></ruby>の<ruby>同<rt>どう</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>士<rt>し</rt></ruby>で<ruby>強<rt>きょう</rt></ruby>い<ruby>結<rt>けつ</rt></ruby><ruby>束<rt>そく</rt></ruby>と<ruby>独<rt>どく</rt></ruby><ruby>自<rt>じ</rt></ruby>の<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby>・ルールを<ruby>持<rt>じ</rt></ruby>つ<ruby>徒<rt>と</rt></ruby><ruby>党<rt>とう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ギャンググループ（ギャングエイジ）",
      "ピアグループ",
      "チャムグループ",
      "ファミリーグループ"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ギャンググループ（ギャングエイジ））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>仲<rt>なか</rt>間<rt>ま</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>士<rt>し</rt></ruby>の<ruby>自<rt>じ</rt></ruby><ruby>律<rt>りつ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>活<rt>かつ</rt></ruby><ruby>動<rt>どう</rt></ruby>を<ruby>通<rt>つう</rt></ruby>じて、<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>協<rt>きょう</rt></ruby><ruby>調<rt>ちょう</rt></ruby><ruby>性<rt>せい</rt></ruby>やルール<ruby>遵<rt>じゅん</rt></ruby><ruby>守<rt>しゅ</rt></ruby>を<ruby>学<rt>がく</rt></ruby>びます。"
  },
  {
    "id": 9,
    "section": "発達心理学からみた人間関係",
    "stem": "<ruby>青<rt>せい</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>に<ruby>見<rt>み</rt></ruby>られる、<ruby>親<rt>しん</rt></ruby>しい<ruby>友<rt>ゆう</rt>人<rt>じん</rt></ruby>と<ruby>互<rt>ご</rt></ruby>いの<ruby>内<rt>ない</rt></ruby><ruby>面<rt>めん</rt></ruby>や<ruby>悩<rt>なや</rt></ruby>みを<ruby>深<rt>しん</rt></ruby>く<ruby>打<rt>う</rt></ruby>ち<ruby>明<rt>あ</rt></ruby>け<ruby>合<rt>あ</rt></ruby>い、<ruby>強<rt>きょう</rt></ruby>い<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>視<rt>し</rt></ruby>を<ruby>伴<rt>ともな</rt></ruby>う<ruby>友<rt>ゆう</rt>人<rt>じん</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "チャムグループ",
      "ギャンググループ",
      "<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>",
      "<ruby>作<rt>さく</rt></ruby><ruby>業<rt>ぎょう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（チャムグループ）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。サリヴァンが<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>した<ruby>親<rt>しん</rt></ruby><ruby>密<rt>みつ</rt></ruby>な<ruby>友<rt>ゆう</rt>人<rt>じん</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>で、<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>解<rt>かい</rt></ruby>と<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>解<rt>かい</rt></ruby>を<ruby>深<rt>しん</rt></ruby>める<ruby>契<rt>けい</rt></ruby><ruby>機<rt>き</rt></ruby>となります。"
  },
  {
    "id": 10,
    "section": "発達心理学からみた人間関係",
    "stem": "ハヴィガーストの<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>論<rt>ろん</rt></ruby>において、<ruby>青<rt>せい</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>期<rt>き</rt></ruby>の<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>として<ruby>挙<rt>きょ</rt></ruby>げられているものとして、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>歩<rt>ぽ</rt></ruby><ruby>行<rt>ぎょう</rt></ruby>の<ruby>学<rt>がく</rt></ruby><ruby>習<rt>しゅう</rt></ruby>",
      "<ruby>同<rt>どう</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>代<rt>だい</rt></ruby>の<ruby>男<rt>だん</rt></ruby><ruby>女<rt>じょ</rt></ruby>との<ruby>洗<rt>せん</rt></ruby><ruby>練<rt>れん</rt></ruby>された<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>の<ruby>構<rt>こう</rt></ruby><ruby>築<rt>ちく</rt></ruby>",
      "<ruby>配<rt>はい</rt></ruby><ruby>偶<rt>ぐう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>死<rt>し</rt></ruby>への<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby>",
      "<ruby>排<rt>はい</rt></ruby><ruby>泄<rt>せつ</rt></ruby>の<ruby>自<rt>じ</rt></ruby><ruby>立<rt>りつ</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>同<rt>どう</rt></ruby><ruby>年<rt>ねん</rt></ruby><ruby>代<rt>だい</rt></ruby>の<ruby>男<rt>だん</rt></ruby><ruby>女<rt>じょ</rt></ruby>との<ruby>洗<rt>せん</rt></ruby><ruby>練<rt>れん</rt></ruby>された<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>の<ruby>構<rt>こう</rt></ruby><ruby>築<rt>ちく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ハヴィガーストは<ruby>各<rt>かく</rt></ruby>ライフステージにおける<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>を<ruby>整<rt>せい</rt></ruby><ruby>理<rt>り</rt></ruby>しました。"
  },
  {
    "id": 11,
    "section": "発達心理学からみた人間関係",
    "stem": "<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>の<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>過<rt>か</rt></ruby><ruby>程<rt>てい</rt></ruby>における「<ruby>個<rt>こ</rt></ruby>の<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>」に<ruby>関<rt>かん</rt></ruby>する<ruby>記<rt>き</rt></ruby><ruby>述<rt>じゅつ</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "すべての<ruby>子<rt>こ</rt></ruby>どもは<ruby>同<rt>どう</rt></ruby>じ<ruby>年<rt>ねん</rt></ruby><ruby>齢<rt>れい</rt></ruby>であれば<ruby>同<rt>どう</rt></ruby>じ<ruby>速<rt>そく</rt></ruby><ruby>度<rt>ど</rt></ruby>で<ruby>画<rt>かく</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>すべきである",
      "<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>の<ruby>速<rt>そく</rt></ruby><ruby>度<rt>ど</rt></ruby>や<ruby>個<rt>こ</rt></ruby><ruby>性<rt>せい</rt></ruby>には<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>差<rt>さ</rt></ruby>があり、その<ruby>人<rt>じん</rt></ruby><ruby>固<rt>こ</rt></ruby><ruby>有<rt>ゆう</rt></ruby>の<ruby>歩<rt>あゆ</rt></ruby>みを<ruby>認<rt>にん</rt></ruby>め<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>することが<ruby>重<rt>じゅう</rt></ruby><ruby>要<rt>よう</rt></ruby>である",
      "<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>の<ruby>遅<rt>ち</rt></ruby>れがある<ruby>場<rt>じょう</rt></ruby><ruby>合<rt>ごう</rt></ruby>は<ruby>標<rt>ひょう</rt></ruby><ruby>準<rt>じゅん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>型<rt>がた</rt></ruby>に<ruby>無<rt>む</rt></ruby><ruby>理<rt>り</rt></ruby>やり<ruby>合<rt>ごう</rt></ruby>わせることが<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby>の<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>である",
      "<ruby>本<rt>ほん</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>欲<rt>よく</rt></ruby>や<ruby>環<rt>かん</rt></ruby><ruby>境<rt>きょう</rt></ruby><ruby>要<rt>よう</rt></ruby><ruby>因<rt>いん</rt></ruby>は<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>の<ruby>様<rt>よう</rt></ruby><ruby>相<rt>そう</rt></ruby>にまったく<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>を<ruby>与<rt>よ</rt></ruby>えない"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>の<ruby>速<rt>そく</rt></ruby><ruby>度<rt>ど</rt></ruby>や<ruby>個<rt>こ</rt></ruby><ruby>性<rt>せい</rt></ruby>には<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>差<rt>さ</rt></ruby>があり、その<ruby>人<rt>じん</rt></ruby><ruby>固<rt>こ</rt></ruby><ruby>有<rt>ゆう</rt></ruby>の<ruby>歩<rt>あゆ</rt></ruby>みを<ruby>認<rt>にん</rt></ruby>め<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>することが<ruby>重<rt>じゅう</rt></ruby><ruby>要<rt>よう</rt></ruby>である）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby>には<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>性<rt>せい</rt></ruby>と<ruby>多<rt>た</rt></ruby><ruby>様<rt>よう</rt></ruby><ruby>性<rt>せい</rt></ruby>があります。"
  },
  {
    "id": 12,
    "section": "発達心理学からみた人間関係",
    "stem": "ピアジェの<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>論<rt>ろん</rt></ruby>において、<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>の<ruby>視<rt>し</rt></ruby><ruby>点<rt>てん</rt></ruby>と<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>の<ruby>視<rt>し</rt></ruby><ruby>点<rt>てん</rt></ruby>を<ruby>区<rt>く</rt></ruby><ruby>別<rt>べつ</rt></ruby>できず、<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>も<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>と<ruby>同<rt>どう</rt></ruby>じように<ruby>見<rt>み</rt></ruby>えていると<ruby>捉<rt>とら</rt></ruby>える<ruby>幼<rt>よう</rt></ruby><ruby>児<rt>じ</rt></ruby><ruby>期<rt>き</rt></ruby>の<ruby>特<rt>とく</rt></ruby><ruby>徴<rt>ちょう</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>中<rt>ちゅう</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>性<rt>せい</rt></ruby>",
      "アニミズム",
      "<ruby>対<rt>たい</rt></ruby><ruby>象<rt>しょう</rt></ruby>の<ruby>永<rt>えい</rt></ruby><ruby>続<rt>ぞく</rt></ruby><ruby>性<rt>せい</rt></ruby>",
      "<ruby>保<rt>ほ</rt></ruby><ruby>存<rt>ぞん</rt></ruby>の<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>中<rt>ちゅう</rt></ruby><ruby>心<rt>しん</rt></ruby><ruby>性<rt>せい</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>前<rt>ぜん</rt></ruby><ruby>操<rt>そう</rt></ruby><ruby>作<rt>さ</rt></ruby><ruby>期<rt>き</rt></ruby>（2〜7<ruby>歳<rt>さい</rt></ruby><ruby>頃<rt>ころ</rt></ruby>）の<ruby>幼<rt>よう</rt></ruby><ruby>児<rt>じ</rt></ruby>に<ruby>見<rt>み</rt></ruby>られる<ruby>特<rt>とく</rt></ruby><ruby>徴<rt>ちょう</rt></ruby>で、<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>の<ruby>視<rt>し</rt></ruby><ruby>点<rt>てん</rt></ruby>に<ruby>立<rt>りつ</rt></ruby>って<ruby>考<rt>かんが</rt></ruby>えることがまだ<ruby>難<rt>むずか</rt></ruby>しい<ruby>状<rt>じょう</rt></ruby><ruby>態<rt>たい</rt></ruby>を<ruby>指<rt>し</rt></ruby>します。"
  },
  {
    "id": 13,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>の<ruby>表<rt>ひょう</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>服<rt>ふく</rt></ruby><ruby>装<rt>そう</rt></ruby>、<ruby>肩<rt>かた</rt></ruby><ruby>書<rt>しょ</rt></ruby>などの<ruby>限<rt>げん</rt></ruby>られた<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>から、その<ruby>人<rt>じん</rt></ruby>の<ruby>性<rt>せい</rt></ruby><ruby>格<rt>かく</rt></ruby>や<ruby>内<rt>ない</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>人<rt>じん</rt></ruby><ruby>柄<rt>がら</rt></ruby>を<ruby>推<rt>すい</rt></ruby><ruby>測<rt>そく</rt></ruby>して<ruby>把<rt>は</rt></ruby><ruby>握<rt>あく</rt></ruby>する<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>プロセスを<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>",
      "<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>移<rt>い</rt></ruby><ruby>入<rt>にゅう</rt></ruby>",
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>凝<rt>ぎょう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>性<rt>せい</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>は<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>容<rt>よう</rt></ruby><ruby>姿<rt>し</rt></ruby>、<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>、<ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>・<ruby>非<rt>ひ</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>をもとにその<ruby>人<rt>じん</rt></ruby><ruby>物<rt>ぶつ</rt></ruby><ruby>像<rt>ぞう</rt></ruby>を<ruby>推<rt>すい</rt></ruby><ruby>測<rt>そく</rt></ruby>・<ruby>構<rt>こう</rt></ruby><ruby>成<rt>せい</rt></ruby>する<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>活<rt>かつ</rt></ruby><ruby>動<rt>どう</rt></ruby>です。"
  },
  {
    "id": 14,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>最<rt>さい</rt></ruby><ruby>初<rt>しょ</rt></ruby>に<ruby>与<rt>よ</rt></ruby>えられた<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>や<ruby>第<rt>だい</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>印<rt>いん</rt></ruby><ruby>象<rt>しょう</rt></ruby>が、その<ruby>後<rt>こう</rt></ruby>の<ruby>全<rt>ぜん</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>や<ruby>印<rt>いん</rt></ruby><ruby>象<rt>しょう</rt></ruby><ruby>形<rt>けい</rt></ruby><ruby>成<rt>せい</rt></ruby>に<ruby>強<rt>きょう</rt></ruby>く<ruby>長<rt>ちょう</rt></ruby>く<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>を<ruby>及<rt>およ</rt></ruby>ぼす<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>初<rt>しょ</rt></ruby><ruby>あたま<rt>あたま</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "<ruby>親<rt>しん</rt></ruby><ruby>近<rt>きん</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "ピグマリオン<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "プラセボ<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>初<rt>しょ</rt></ruby><ruby>あたま<rt>あたま</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。アッシュの<ruby>実<rt>じっ</rt></ruby><ruby>験<rt>けん</rt></ruby><ruby>等<rt>とう</rt></ruby>で<ruby>知<rt>ち</rt></ruby>られ、<ruby>最<rt>さい</rt></ruby><ruby>初<rt>しょ</rt></ruby>に<ruby>提<rt>てい</rt></ruby><ruby>示<rt>じ</rt></ruby>された<ruby>特<rt>とく</rt></ruby><ruby>性<rt>せい</rt></ruby>が<ruby>全<rt>ぜん</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>解<rt>かい</rt></ruby><ruby>釈<rt>しゃく</rt></ruby>の<ruby>枠<rt>わく</rt></ruby><ruby>組<rt>ぐ</rt></ruby>みを<ruby>形<rt>けい</rt></ruby><ruby>成<rt>せい</rt></ruby>します。"
  },
  {
    "id": 15,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>最<rt>さい</rt></ruby><ruby>後<rt>こう</rt></ruby>に<ruby>提<rt>てい</rt></ruby><ruby>示<rt>じ</rt></ruby>された<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>や<ruby>直<rt>ちょく</rt></ruby><ruby>近<rt>きん</rt></ruby>の<ruby>出<rt>で</rt></ruby><ruby>来<rt>き</rt></ruby><ruby>事<rt>ごと</rt></ruby>が<ruby>記<rt>き</rt></ruby><ruby>憶<rt>おく</rt></ruby>に<ruby>強<rt>きょう</rt></ruby>く<ruby>残<rt>ざん</rt></ruby>り、<ruby>直<rt>ちょく</rt></ruby><ruby>後<rt>こう</rt></ruby>の<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>や<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>に<ruby>大<rt>たい</rt></ruby>きな<ruby>影<rt>えい</rt></ruby><ruby>響<rt>きょう</rt></ruby>を<ruby>与<rt>よ</rt></ruby>える<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>親<rt>しん</rt></ruby><ruby>近<rt>きん</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>（<ruby>新<rt>しん</rt></ruby><ruby>近<rt>きん</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>）",
      "<ruby>初<rt>しょ</rt></ruby><ruby>あたま<rt>あたま</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "ハロー<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "ブーメラン<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>親<rt>しん</rt></ruby><ruby>近<rt>きん</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>（<ruby>新<rt>しん</rt></ruby><ruby>近<rt>きん</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>時<rt>じ</rt></ruby><ruby>間<rt>かん</rt></ruby><ruby>差<rt>さ</rt></ruby>がある<ruby>場<rt>じょう</rt></ruby><ruby>合<rt>ごう</rt></ruby>や<ruby>直<rt>ちょく</rt></ruby><ruby>近<rt>きん</rt></ruby>の<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>が<ruby>重<rt>じゅう</rt></ruby><ruby>視<rt>し</rt></ruby>される<ruby>場<rt>じょう</rt></ruby><ruby>面<rt>めん</rt></ruby>で<ruby>強<rt>きょう</rt></ruby>く<ruby>発<rt>はつ</rt></ruby><ruby>現<rt>げん</rt></ruby>します。"
  },
  {
    "id": 16,
    "section": "社会心理学からみた人間関係",
    "stem": "ある<ruby>人<rt>じん</rt></ruby>が<ruby>際<rt>きわ</rt></ruby><ruby>立<rt>だ</rt></ruby>って<ruby>優<rt>ゆう</rt></ruby>れた<ruby>特<rt>とく</rt></ruby><ruby>徴<rt>ちょう</rt></ruby>や<ruby>目<rt>め</rt></ruby><ruby>立<rt>だ</rt></ruby>つ<ruby>側<rt>そく</rt></ruby><ruby>面<rt>めん</rt></ruby>を<ruby>持<rt>じ</rt></ruby>つとき、その<ruby>人<rt>じん</rt></ruby><ruby>全<rt>ぜん</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>他<rt>た</rt></ruby>の<ruby>側<rt>そく</rt></ruby><ruby>面<rt>めん</rt></ruby>まで<ruby>実<rt>じっ</rt></ruby><ruby>際<rt>さい</rt></ruby><ruby>以<rt>い</rt></ruby><ruby>上<rt>じょう</rt></ruby>に<ruby>高<rt>こう</rt></ruby>く<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>してしまう<ruby>歪<rt>ゆが</rt></ruby>みを<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ハロー<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>（<ruby>光<rt>こう</rt></ruby><ruby>背<rt>はい</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>）",
      "ステレオタイプ",
      "<ruby>内<rt>ない</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>バイアス",
      "<ruby>根<rt>こん</rt></ruby><ruby>本<rt>ぽん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>帰<rt>き</rt></ruby><ruby>属<rt>ぞく</rt></ruby>の<ruby>誤<rt>あやま</rt></ruby>り"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ハロー<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>（<ruby>光<rt>こう</rt></ruby><ruby>背<rt>はい</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>外<rt>がい</rt></ruby><ruby>見<rt>けん</rt></ruby>や<ruby>学<rt>がく</rt></ruby><ruby>歴<rt>れき</rt></ruby>などの<ruby>一<rt>いち</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>が、<ruby>人<rt>じん</rt></ruby><ruby>物<rt>ぶつ</rt></ruby><ruby>全<rt>ぜん</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>印<rt>いん</rt></ruby><ruby>象<rt>しょう</rt></ruby>を<ruby>歪<rt>ゆが</rt></ruby>めてしまう<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>です。"
  },
  {
    "id": 17,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>特<rt>とく</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>やカテゴリーの<ruby>構<rt>こう</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>員<rt>いん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して、<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>考<rt>こう</rt></ruby><ruby>慮<rt>りょ</rt></ruby>せず<ruby>固<rt>こ</rt></ruby><ruby>定<rt>てい</rt></ruby><ruby>化<rt>か</rt></ruby>された<ruby>画<rt>かく</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>的<rt>てき</rt></ruby>なイメージや<ruby>固<rt>こ</rt></ruby><ruby>定<rt>てい</rt></ruby><ruby>観<rt>かん</rt></ruby><ruby>念<rt>ねん</rt></ruby>を<ruby>抱<rt>いだ</rt></ruby>くことを<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ステレオタイプ",
      "ラポール",
      "アサーション",
      "アタッチメント"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ステレオタイプ）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。「<ruby>高<rt>こう</rt></ruby><ruby>齢<rt>れい</rt></ruby><ruby>者<rt>しゃ</rt></ruby>は<ruby>頑<rt>がん</rt></ruby><ruby>固<rt>こ</rt></ruby>である」「<ruby>若<rt>わか</rt></ruby><ruby>者<rt>しゃ</rt></ruby>は<ruby>忍<rt>にん</rt></ruby><ruby>耐<rt>たい</rt></ruby><ruby>力<rt>りょく</rt></ruby>がない」などの<ruby>単<rt>たん</rt></ruby><ruby>純<rt>じゅん</rt></ruby><ruby>化<rt>か</rt></ruby>された<ruby>先<rt>せん</rt></ruby><ruby>入<rt>にゅう</rt></ruby><ruby>観<rt>かん</rt></ruby>がこれに<ruby>該<rt>がい</rt></ruby><ruby>当<rt>あて</rt></ruby>します。"
  },
  {
    "id": 18,
    "section": "社会心理学からみた人間関係",
    "stem": "クーリーが<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>した、<ruby>家<rt>か</rt></ruby><ruby>族<rt>ぞく</rt></ruby>や<ruby>親<rt>しん</rt></ruby><ruby>密<rt>みつ</rt></ruby>な<ruby>遊<rt>ゆう</rt></ruby>び<ruby>仲<rt>なか</rt>間<rt>ま</rt></ruby>のように<ruby>対<rt>たい</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>的<rt>てき</rt></ruby>で<ruby>親<rt>しん</rt></ruby><ruby>密<rt>みつ</rt></ruby>な<ruby>愛<rt>あい</rt></ruby><ruby>情<rt>じょう</rt></ruby>・<ruby>結<rt>けつ</rt></ruby>びつきを<ruby>持<rt>じ</rt></ruby>つ<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>第<rt>だい</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>（<ruby>初<rt>しょ</rt></ruby><ruby>あたま<rt>あたま</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>）",
      "<ruby>第<rt>だい</rt></ruby><ruby>二<rt>に</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>",
      "<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>",
      "<ruby>形<rt>けい</rt></ruby><ruby>式<rt>しき</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>第<rt>だい</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>（<ruby>初<rt>しょ</rt></ruby><ruby>あたま<rt>あたま</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>家<rt>か</rt></ruby><ruby>族<rt>ぞく</rt></ruby>や<ruby>地<rt>ち</rt></ruby><ruby>域<rt>いき</rt></ruby><ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby>の<ruby>親<rt>しん</rt></ruby><ruby>密<rt>みつ</rt></ruby>な<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>で、<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>形<rt>けい</rt></ruby><ruby>成<rt>せい</rt></ruby>の<ruby>基<rt>き</rt></ruby><ruby>盤<rt>ばん</rt></ruby>となります。"
  },
  {
    "id": 19,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>特<rt>とく</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>や<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby>（<ruby>仕<rt>し</rt></ruby><ruby>事<rt>ごと</rt></ruby>、<ruby>学<rt>がく</rt></ruby><ruby>習<rt>しゅう</rt></ruby>、<ruby>利<rt>り</rt></ruby><ruby>益<rt>えき</rt></ruby>など）を<ruby>果<rt>か</rt></ruby>たすために<ruby>人<rt>じん</rt></ruby><ruby>為<rt>い</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>結<rt>けつ</rt></ruby><ruby>成<rt>せい</rt></ruby>された<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>（<ruby>第<rt>だい</rt></ruby><ruby>二<rt>に</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>）",
      "<ruby>基<rt>き</rt></ruby><ruby>礎<rt>そ</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>",
      "<ruby>血<rt>けつ</rt></ruby><ruby>縁<rt>えん</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>",
      "<ruby>自<rt>じ</rt></ruby><ruby>然<rt>ぜん</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>（<ruby>第<rt>だい</rt></ruby><ruby>二<rt>に</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>企<rt>き</rt></ruby><ruby>業<rt>ぎょう</rt></ruby>、<ruby>病<rt>びょう</rt></ruby><ruby>院<rt>いん</rt></ruby>、<ruby>福<rt>ふく</rt></ruby><ruby>祉<rt>し</rt></ruby><ruby>施<rt>し</rt></ruby><ruby>設<rt>せつ</rt></ruby>、<ruby>学<rt>がく</rt></ruby><ruby>校<rt>こう</rt></ruby>などの<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>型<rt>がた</rt></ruby><ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby>が<ruby>該<rt>がい</rt></ruby><ruby>当<rt>あて</rt></ruby>します。"
  },
  {
    "id": 20,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>の<ruby>発<rt>はつ</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>過<rt>か</rt></ruby><ruby>程<rt>てい</rt></ruby>における5<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>モデル（タックマンモデル）において、メンバー<ruby>間<rt>かん</rt></ruby>の<ruby>対<rt>たい</rt></ruby><ruby>立<rt>りつ</rt></ruby>や<ruby>衝<rt>しょう</rt></ruby><ruby>突<rt>とつ</rt></ruby>が<ruby>生<rt>しょう</rt></ruby>じる<ruby>第<rt>だい</rt></ruby>2<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>の<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>嵐<rt>あらし</rt></ruby>の<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>（<ruby>動<rt>どう</rt></ruby><ruby>乱<rt>らん</rt></ruby><ruby>期<rt>き</rt></ruby>・ストーミング）",
      "<ruby>形<rt>けい</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>期<rt>き</rt></ruby>（フォーミング）",
      "<ruby>規<rt>き</rt></ruby><ruby>範<rt>はん</rt></ruby><ruby>期<rt>き</rt></ruby>（ノーミング）",
      "<ruby>達<rt>たつ</rt></ruby><ruby>成<rt>せい</rt></ruby><ruby>期<rt>き</rt></ruby>（パフォーミング）"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>嵐<rt>あらし</rt></ruby>の<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>（<ruby>動<rt>どう</rt></ruby><ruby>乱<rt>らん</rt></ruby><ruby>期<rt>き</rt></ruby>・ストーミング））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>本<rt>ほん</rt></ruby><ruby>音<rt>ね</rt></ruby>や<ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>の<ruby>食<rt>く</rt></ruby>い<ruby>違<rt>ちが</rt></ruby>いが<ruby>表<rt>ひょう</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>化<rt>か</rt></ruby>し、これを<ruby>乗<rt>の</rt></ruby>り<ruby>越<rt>こ</rt></ruby>えることで<ruby>真<rt>しん</rt></ruby>のチームが<ruby>育<rt>そだ</rt></ruby>ちます。"
  },
  {
    "id": 21,
    "section": "社会心理学からみた人間関係",
    "stem": "アッシュ（Asch）の<ruby>直<rt>ちょく</rt></ruby><ruby>線<rt>せん</rt></ruby><ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby><ruby>実<rt>じっ</rt></ruby><ruby>験<rt>けん</rt></ruby>により<ruby>実<rt>じっ</rt></ruby><ruby>証<rt>しょう</rt></ruby>された、<ruby>明<rt>めい</rt></ruby>らかに<ruby>間<rt>かん</rt></ruby><ruby>違<rt>い</rt></ruby>っている<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>い</rt></ruby>の<ruby>多<rt>た</rt></ruby><ruby>数<rt>すう</rt></ruby><ruby>派<rt>は</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>に<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>を<ruby>合<rt>ごう</rt></ruby>わせて<ruby>同<rt>どう</rt></ruby><ruby>調<rt>ちょう</rt></ruby>させてしまう<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>同<rt>どう</rt></ruby><ruby>調<rt>ちょう</rt></ruby><ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>怠<rt>たい</rt></ruby><ruby>惰<rt>だ</rt></ruby>",
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>浅<rt>せん</rt></ruby><ruby>慮<rt>りょ</rt></ruby>",
      "<ruby>防<rt>ぼう</rt></ruby><ruby>衛<rt>えい</rt></ruby><ruby>機<rt>き</rt></ruby><ruby>制<rt>せい</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>同<rt>どう</rt></ruby><ruby>調<rt>ちょう</rt></ruby><ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>圧<rt>あつ</rt></ruby><ruby>力<rt>りょく</rt></ruby>を<ruby>受<rt>う</rt></ruby>け、<ruby>孤<rt>こ</rt></ruby><ruby>立<rt>りつ</rt></ruby>を<ruby>恐<rt>おそ</rt></ruby>れて<ruby>多<rt>た</rt></ruby><ruby>数<rt>すう</rt></ruby><ruby>派<rt>は</rt></ruby>に<ruby>合<rt>ごう</rt></ruby>わせてしまう<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>傾<rt>けい</rt></ruby><ruby>向<rt>こう</rt></ruby>です。"
  },
  {
    "id": 22,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>が<ruby>所<rt>しょ</rt></ruby><ruby>属<rt>ぞく</rt></ruby>している<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>（<ruby>内<rt>ない</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>）のメンバーを<ruby>過<rt>か</rt></ruby><ruby>大<rt>たい</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>して<ruby>優<rt>ゆう</rt></ruby><ruby>遇<rt>ぐう</rt></ruby>し、<ruby>所<rt>しょ</rt></ruby><ruby>属<rt>ぞく</rt></ruby>していない<ruby>外<rt>がい</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>のメンバーを<ruby>低<rt>てい</rt></ruby>く<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>・<ruby>排<rt>はい</rt></ruby><ruby>斥<rt>せき</rt></ruby>しがちになる<ruby>偏<rt>へん</rt></ruby>りを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>内<rt>ない</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>バイアス",
      "ハロー<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "<ruby>初<rt>しょ</rt></ruby><ruby>あたま<rt>あたま</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>奉<rt>ほう</rt></ruby><ruby>仕<rt>し</rt></ruby>バイアス"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>内<rt>ない</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>バイアス）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。「<ruby>身<rt>み</rt></ruby><ruby>内<rt>うち</rt></ruby>びいき」の<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby>であり、<ruby>部<rt>ぶ</rt></ruby><ruby>署<rt>しょ</rt></ruby><ruby>間<rt>かん</rt></ruby>やチーム<ruby>間<rt>かん</rt></ruby>の<ruby>対<rt>たい</rt></ruby><ruby>立<rt>りつ</rt></ruby>や<ruby>偏<rt>へん</rt></ruby><ruby>見<rt>けん</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>因<rt>いん</rt></ruby>となります。"
  },
  {
    "id": 23,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>で<ruby>共<rt>きょう</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby><ruby>業<rt>ぎょう</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>う<ruby>際<rt>さい</rt></ruby>、1<ruby>人<rt>ひとり</rt></ruby>あたりの<ruby>努<rt>ど</rt></ruby><ruby>力<rt>りょく</rt></ruby>やパフォーマンスが<ruby>単<rt>たん</rt></ruby><ruby>独<rt>どく</rt></ruby>で<ruby>行<rt>おこな</rt></ruby>う<ruby>時<rt>じ</rt></ruby>よりも<ruby>低<rt>てい</rt></ruby><ruby>下<rt>か</rt></ruby>してしまう<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>怠<rt>たい</rt></ruby><ruby>惰<rt>だ</rt></ruby>（<ruby>手<rt>て</rt></ruby><ruby>抜<rt>ぬ</rt></ruby>き<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>）",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>",
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>極<rt>きょく</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>化<rt>か</rt></ruby>",
      "リスキーシフト"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>怠<rt>たい</rt></ruby><ruby>惰<rt>だ</rt></ruby>（<ruby>手<rt>て</rt></ruby><ruby>抜<rt>ぬ</rt></ruby>き<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>責<rt>せき</rt></ruby><ruby>任<rt>にん</rt></ruby>の<ruby>所<rt>しょ</rt></ruby><ruby>在<rt>ざい</rt></ruby>が<ruby>曖<rt>あい</rt></ruby><ruby>昧<rt>まい</rt></ruby>になることで、<ruby>無<rt>む</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>に<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>努<rt>ど</rt></ruby><ruby>力<rt>りょく</rt></ruby>が<ruby>減<rt>げん</rt></ruby><ruby>少<rt>しょう</rt></ruby>する<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>です。"
  },
  {
    "id": 24,
    "section": "社会心理学からみた人間関係",
    "stem": "<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>の<ruby>存<rt>そん</rt></ruby><ruby>在<rt>ざい</rt></ruby>や<ruby>観<rt>かん</rt></ruby><ruby>察<rt>さつ</rt></ruby>されている<ruby>状<rt>じょう</rt></ruby><ruby>況<rt>きょう</rt></ruby>によって、<ruby>簡<rt>かん</rt></ruby><ruby>単<rt>たん</rt></ruby>な<ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>や<ruby>得<rt>とく</rt></ruby><ruby>意<rt>い</rt></ruby>な<ruby>作<rt>さく</rt></ruby><ruby>業<rt>ぎょう</rt></ruby>の<ruby>成<rt>せい</rt></ruby><ruby>績<rt>せき</rt></ruby>が<ruby>向<rt>こう</rt></ruby><ruby>上<rt>じょう</rt></ruby>する<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>抑<rt>よく</rt></ruby><ruby>制<rt>せい</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>怠<rt>たい</rt></ruby><ruby>惰<rt>だ</rt></ruby>",
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>浅<rt>せん</rt></ruby><ruby>慮<rt>りょ</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>の<ruby>視<rt>し</rt></ruby><ruby>線<rt>せん</rt></ruby>や<ruby>励<rt>はげ</rt></ruby>ましが<ruby>適<rt>てき</rt></ruby><ruby>度<rt>ど</rt></ruby>な<ruby>緊<rt>きん</rt></ruby><ruby>張<rt>ちょう</rt></ruby><ruby>感<rt>かん</rt></ruby>とモチベーションを<ruby>生<rt>せい</rt></ruby>み、<ruby>作<rt>さく</rt></ruby><ruby>業<rt>ぎょう</rt></ruby><ruby>効<rt>こう</rt></ruby><ruby>率<rt>りつ</rt></ruby>が<ruby>上<rt>じょう</rt></ruby>がります。"
  },
  {
    "id": 25,
    "section": "人間関係とストレス・コーピング",
    "stem": "ストレスを<ruby>引<rt>ひ</rt></ruby>き<ruby>起<rt>お</rt></ruby>こす<ruby>外<rt>がい</rt></ruby><ruby>部<rt>ぶ</rt></ruby>からの<ruby>刺<rt>し</rt></ruby><ruby>激<rt>げき</rt></ruby>（<ruby>騒<rt>そう</rt></ruby><ruby>音<rt>おん</rt></ruby>、<ruby>病<rt>びょう</rt></ruby><ruby>気<rt>き</rt></ruby>、<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>のトラブルなど）を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ストレッサー",
      "ストレス<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>",
      "コーピング",
      "レジリエンス"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ストレッサー）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ストレッサーは<ruby>心<rt>しん</rt>身<rt>しん</rt></ruby>に<ruby>負<rt>ふ</rt></ruby><ruby>荷<rt>か</rt></ruby>を<ruby>与<rt>よ</rt></ruby>える<ruby>刺<rt>し</rt></ruby><ruby>激<rt>げき</rt></ruby><ruby>要<rt>よう</rt></ruby><ruby>因<rt>いん</rt></ruby>そのものを<ruby>指<rt>し</rt></ruby>します。"
  },
  {
    "id": 26,
    "section": "人間関係とストレス・コーピング",
    "stem": "ストレッサーによって<ruby>引<rt>ひ</rt></ruby>き<ruby>起<rt>お</rt></ruby>こされる、<ruby><ruby>あたま<rt>あたま</rt></ruby><rt>ず</rt></ruby><ruby>痛<rt>つう</rt></ruby>・<ruby>胃<rt>い</rt></ruby><ruby>痛<rt>つう</rt></ruby>・<ruby>不<rt>ふ</rt></ruby><ruby>眠<rt>みん</rt></ruby>などの<ruby>身<rt>しん</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>や、<ruby>不<rt>ふ</rt></ruby><ruby>安<rt>あん</rt></ruby>・<ruby>抑<rt>よく</rt></ruby>うつなどの<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ストレス<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>",
      "ストレッサー",
      "<ruby>防<rt>ぼう</rt></ruby><ruby>衛<rt>えい</rt></ruby><ruby>機<rt>き</rt></ruby><ruby>制<rt>せい</rt></ruby>",
      "<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ストレス<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ストレッサーに<ruby>対<rt>たい</rt></ruby>して<ruby>心<rt>しん</rt>身<rt>しん</rt></ruby>が<ruby>生<rt>しょう</rt></ruby>じる<ruby>様<rt>よう</rt></ruby>々な<ruby>生<rt>せい</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>です。"
  },
  {
    "id": 27,
    "section": "人間関係とストレス・コーピング",
    "stem": "ラザルスらのストレス<ruby>理<rt>り</rt></ruby><ruby>論<rt>ろん</rt></ruby>において、<ruby>直<rt>ちょく</rt></ruby><ruby>面<rt>めん</rt></ruby>した<ruby>状<rt>じょう</rt></ruby><ruby>況<rt>きょう</rt></ruby>が「<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>にとって<ruby>脅<rt>きょう</rt></ruby><ruby>威<rt>い</rt></ruby>・<ruby>有<rt>ゆう</rt></ruby><ruby>害<rt>がい</rt></ruby>・<ruby>挑<rt>ちょう</rt></ruby><ruby>戦<rt>せん</rt></ruby><ruby>的<rt>てき</rt></ruby>か」を<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>・<ruby>知<rt>ち</rt></ruby><ruby>覚<rt>かく</rt></ruby>する<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>の<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>一<rt>いち</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>二<rt>に</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>再<rt>さい</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>結<rt>けつ</rt></ruby><ruby>果<rt>か</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>一<rt>いち</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>出<rt>で</rt></ruby><ruby>来<rt>き</rt></ruby><ruby>事<rt>ごと</rt></ruby>が<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>にとってどのような<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby>を<ruby>持<rt>じ</rt></ruby>つかを<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>する<ruby>最<rt>さい</rt></ruby><ruby>初<rt>しょ</rt></ruby>のステップです。"
  },
  {
    "id": 28,
    "section": "人間関係とストレス・コーピング",
    "stem": "ラザルスの<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>論<rt>ろん</rt></ruby>において、「<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>はその<ruby>事<rt>ごと</rt></ruby><ruby>態<rt>たい</rt></ruby>に<ruby>対<rt>たい</rt></ruby><ruby>処<rt>しょ</rt></ruby>できる<ruby>資<rt>し</rt></ruby><ruby>源<rt>げん</rt></ruby>や<ruby>能<rt>のう</rt></ruby><ruby>力<rt>りょく</rt></ruby>を<ruby>持<rt>じ</rt></ruby>っているか」を<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>する<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>の<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>二<rt>に</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>一<rt>いち</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>直<rt>ちょく</rt></ruby><ruby>感<rt>かん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>感<rt>かん</rt></ruby><ruby>覚<rt>かく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>二<rt>に</rt></ruby><ruby>次<rt>じ</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>可<rt>か</rt></ruby><ruby>能<rt>のう</rt></ruby>なコーピング<ruby>資<rt>し</rt></ruby><ruby>源<rt>げん</rt></ruby>（<ruby>知<rt>ち</rt></ruby><ruby>識<rt>しき</rt></ruby>、<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>い</rt></ruby>の<ruby>支<rt>し</rt></ruby><ruby>援<rt>えん</rt></ruby>、<ruby>時<rt>じ</rt></ruby><ruby>間<rt>かん</rt></ruby>など）を<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>する<ruby>段<rt>だん</rt></ruby><ruby>階<rt>かい</rt></ruby>です。"
  },
  {
    "id": 29,
    "section": "人間関係とストレス・コーピング",
    "stem": "フリードマンとローゼンマンが<ruby>心<rt>しん</rt></ruby><ruby>臓<rt>ぞう</rt></ruby><ruby>疾<rt>しっ</rt></ruby><ruby>患<rt>かん</rt></ruby>の<ruby>危<rt>き</rt></ruby><ruby>険<rt>けん</rt></ruby><ruby>因<rt>いん</rt></ruby><ruby>子<rt>こ</rt></ruby>として<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>した、<ruby>強<rt>きょう</rt></ruby>い<ruby>競<rt>きょう</rt></ruby><ruby>争<rt>そう</rt></ruby><ruby>心<rt>しん</rt></ruby>・<ruby>時<rt>じ</rt></ruby><ruby>間<rt>かん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>切<rt>せつ</rt></ruby><ruby>迫<rt>はく</rt></ruby><ruby>感<rt>かん</rt></ruby>・<ruby>攻<rt>こう</rt></ruby><ruby>撃<rt>げき</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>持<rt>じ</rt></ruby>つ<ruby>性<rt>せい</rt></ruby><ruby>格<rt>かく</rt></ruby>・<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>特<rt>とく</rt></ruby><ruby>性<rt>せい</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "タイプA<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン",
      "タイプB<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン",
      "タイプC<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン",
      "タイプD<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（タイプA<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>常<rt>じょう</rt></ruby>に<ruby>時<rt>じ</rt></ruby><ruby>間<rt>かん</rt></ruby>に<ruby>追<rt>お</rt></ruby>われ、<ruby>攻<rt>こう</rt></ruby><ruby>撃<rt>げき</rt></ruby><ruby>的<rt>てき</rt></ruby>で<ruby>精<rt>せい</rt></ruby><ruby>力<rt>りょく</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>活<rt>かつ</rt></ruby><ruby>動<rt>どう</rt></ruby>する<ruby>傾<rt>けい</rt></ruby><ruby>向<rt>こう</rt></ruby>があり、<ruby>循<rt>じゅん</rt></ruby><ruby>環<rt>かん</rt></ruby><ruby>器<rt>き</rt></ruby><ruby>疾<rt>しっ</rt></ruby><ruby>患<rt>かん</rt></ruby>リスクが<ruby>高<rt>こう</rt></ruby>いとされます。"
  },
  {
    "id": 30,
    "section": "人間関係とストレス・コーピング",
    "stem": "<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>過<rt>か</rt></ruby><ruby>度<rt>ど</rt></ruby>に<ruby>よく<rt>よく</rt></ruby><ruby>圧<rt>あつ</rt></ruby>し、<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>犠<rt>ぎ</rt></ruby><ruby>牲<rt>せい</rt></ruby><ruby>的<rt>てき</rt></ruby>で<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>い</rt></ruby>に<ruby>過<rt>か</rt></ruby><ruby>剰<rt>じょう</rt></ruby>に<ruby>同<rt>どう</rt></ruby><ruby>調<rt>ちょう</rt></ruby>・<ruby>じゅう<rt>じゅう</rt></ruby><ruby>属<rt>ぞく</rt></ruby>しやすい、がんの<ruby>り<rt>り</rt></ruby><ruby>患<rt>かん</rt></ruby>との<ruby>関<rt>かん</rt></ruby><ruby>連<rt>れん</rt></ruby>が<ruby>研<rt>けん</rt></ruby><ruby>究<rt>きゅう</rt></ruby>されている<ruby>性<rt>せい</rt></ruby><ruby>格<rt>かく</rt></ruby><ruby>傾<rt>けい</rt></ruby><ruby>向<rt>こう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "タイプC<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン",
      "タイプA<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン",
      "タイプB<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン",
      "<ruby>外<rt>がい</rt></ruby><ruby>向<rt>こう</rt></ruby><ruby>型<rt>がた</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>格<rt>かく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（タイプC<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>パターン）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>怒<rt>いか</rt></ruby>りや<ruby>不<rt>ふ</rt></ruby><ruby>安<rt>あん</rt></ruby>を<ruby>外<rt>がい</rt></ruby>に<ruby>出<rt>しゅつ</rt></ruby>さず、<ruby>極<rt>きょく</rt></ruby><ruby>端<rt>たん</rt></ruby>に<ruby>我<rt>が</rt></ruby><ruby>慢<rt>まん</rt></ruby><ruby>強<rt>づよ</rt></ruby>く<ruby>じゅう<rt>じゅう</rt></ruby><ruby>順<rt>じゅん</rt></ruby>な<ruby>特<rt>とく</rt></ruby><ruby>徴<rt>ちょう</rt></ruby>を<ruby>持<rt>じ</rt></ruby>ちます。"
  },
  {
    "id": 31,
    "section": "人間関係とストレス・コーピング",
    "stem": "ストレスの<ruby>原<rt>げん</rt></ruby><ruby>因<rt>いん</rt></ruby>となっている<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby>そのものを<ruby>直<rt>ちょく</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>解<rt>かい</rt></ruby><ruby>決<rt>けつ</rt></ruby>・<ruby>改<rt>かい</rt></ruby><ruby>善<rt>ぜん</rt></ruby>しようとする<ruby>対<rt>たい</rt></ruby><ruby>処<rt>しょ</rt></ruby><ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>（コーピング）として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby><ruby>焦<rt>しょう</rt></ruby><ruby>点<rt>てん</rt></ruby><ruby>型<rt>がた</rt></ruby>コーピング",
      "<ruby>情<rt>じょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>焦<rt>しょう</rt></ruby><ruby>点<rt>てん</rt></ruby><ruby>型<rt>がた</rt></ruby>コーピング",
      "<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>回<rt>かい</rt></ruby><ruby>避<rt>ひ</rt></ruby>",
      "<ruby>防<rt>ぼう</rt></ruby><ruby>衛<rt>えい</rt></ruby><ruby>機<rt>き</rt></ruby><ruby>制<rt>せい</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby><ruby>焦<rt>しょう</rt></ruby><ruby>点<rt>てん</rt></ruby><ruby>型<rt>がた</rt></ruby>コーピング）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby><ruby>収<rt>しゅう</rt></ruby><ruby>集<rt>しゅう</rt></ruby>、<ruby>計<rt>けい</rt></ruby><ruby>画<rt>かく</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>対<rt>たい</rt></ruby><ruby>策<rt>さく</rt></ruby>の<ruby>実<rt>じっ</rt></ruby><ruby>行<rt>ぎょう</rt></ruby>、<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>要<rt>よう</rt></ruby><ruby>請<rt>せい</rt></ruby>など<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>解<rt>かい</rt></ruby><ruby>消<rt>しょう</rt></ruby>を<ruby>図<rt>と</rt></ruby>る<ruby>対<rt>たい</rt></ruby><ruby>処<rt>しょ</rt></ruby><ruby>法<rt>ほう</rt></ruby>です。"
  },
  {
    "id": 32,
    "section": "人間関係とストレス・コーピング",
    "stem": "<ruby>運<rt>うん</rt></ruby><ruby>動<rt>どう</rt></ruby>、カラオケ、<ruby>深<rt>しん</rt></ruby><ruby>呼<rt>こ</rt></ruby><ruby>吸<rt>きゅう</rt></ruby>、<ruby>愚<rt>ぐ</rt></ruby><ruby>痴<rt>ち</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いてもらうなど、<ruby>生<rt>しょう</rt></ruby>じた<ruby>不<rt>ふ</rt></ruby><ruby>快<rt>かい</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>興<rt>きょう</rt></ruby><ruby>奮<rt>ふん</rt></ruby>を<ruby>鎮<rt>しず</rt></ruby>めたり<ruby>発<rt>はつ</rt></ruby><ruby>散<rt>さん</rt></ruby>したりすることを<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>とする<ruby>対<rt>たい</rt></ruby><ruby>処<rt>しょ</rt></ruby><ruby>法<rt>ほう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>情<rt>じょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>焦<rt>しょう</rt></ruby><ruby>点<rt>てん</rt></ruby><ruby>型<rt>がた</rt></ruby>コーピング",
      "<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby><ruby>焦<rt>しょう</rt></ruby><ruby>点<rt>てん</rt></ruby><ruby>型<rt>がた</rt></ruby>コーピング",
      "<ruby>環<rt>かん</rt></ruby><ruby>境<rt>きょう</rt></ruby><ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby>",
      "<ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby><ruby>解<rt>かい</rt></ruby><ruby>決<rt>けつ</rt></ruby><ruby>訓<rt>くん</rt></ruby><ruby>練<rt>れん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>情<rt>じょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>焦<rt>しょう</rt></ruby><ruby>点<rt>てん</rt></ruby><ruby>型<rt>がた</rt></ruby>コーピング）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ストレス<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>そのものを<ruby>緩<rt>かん</rt></ruby><ruby>和<rt>わ</rt></ruby>し、<ruby>気<rt>き</rt></ruby><ruby>持<rt>も</rt></ruby>ちの<ruby>切<rt>せつ</rt></ruby>り<ruby>替<rt>か</rt></ruby>えを<ruby>図<rt>と</rt></ruby>るアプローチです。"
  },
  {
    "id": 33,
    "section": "人間関係とストレス・コーピング",
    "stem": "つらい<ruby>出<rt>で</rt></ruby><ruby>来<rt>き</rt></ruby><ruby>事<rt>ごと</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して「これは<ruby>成<rt>せい</rt></ruby><ruby>長<rt>ちょう</rt></ruby>の<ruby>機<rt>き</rt></ruby><ruby>会<rt>かい</rt></ruby>である」「<ruby>良<rt>よ</rt></ruby>い<ruby>教<rt>きょう</rt></ruby><ruby>訓<rt>くん</rt></ruby>になった」と<ruby>捉<rt>とら</rt></ruby>え<ruby>方<rt>ほう</rt></ruby>や<ruby>解<rt>かい</rt></ruby><ruby>釈<rt>しゃく</rt></ruby>を<ruby>変<rt>へん</rt></ruby>える<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>対<rt>たい</rt></ruby><ruby>処<rt>しょ</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>再<rt>さい</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>",
      "<ruby>ごう<rt>ごう</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>化<rt>か</rt></ruby>",
      "<ruby>よく<rt>よく</rt></ruby><ruby>圧<rt>あつ</rt></ruby>",
      "<ruby>ひ<rt>ひ</rt></ruby><ruby>認<rt>にん</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>再<rt>さい</rt></ruby><ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>物<rt>ぶつ</rt></ruby><ruby>事<rt>ごと</rt></ruby>の<ruby>認<rt>にん</rt></ruby><ruby>知<rt>ち</rt></ruby>（<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>め<ruby>方<rt>ほう</rt></ruby>）を<ruby>変<rt>へん</rt></ruby>えることで、<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>ストレス<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>を<ruby>根<rt>こん</rt></ruby><ruby>本<rt>ほん</rt></ruby>から<ruby>軽<rt>けい</rt></ruby><ruby>減<rt>げん</rt></ruby>させます。"
  },
  {
    "id": 34,
    "section": "人間関係とストレス・コーピング",
    "stem": "<ruby>周<rt>しゅう</rt></ruby><ruby>囲<rt>い</rt></ruby>の<ruby>人<rt>じん</rt></ruby>々から<ruby>提<rt>てい</rt></ruby><ruby>供<rt>きょう</rt></ruby>される<ruby>支<rt>し</rt></ruby><ruby>援<rt>えん</rt></ruby>（ソーシャルサポート）のうち、<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>、<ruby>傾<rt>けい</rt></ruby><ruby>聴<rt>ちょう</rt></ruby>、<ruby>励<rt>はげ</rt></ruby>まし、<ruby>愛<rt>あい</rt></ruby><ruby>情<rt>じょう</rt></ruby>など<ruby>精<rt>せい</rt></ruby><ruby>神<rt>しん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>安<rt>あん</rt></ruby>らぎを<ruby>与<rt>よ</rt></ruby>える<ruby>支<rt>し</rt></ruby><ruby>援<rt>えん</rt></ruby>の<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート",
      "<ruby>道<rt>どう</rt></ruby><ruby>具<rt>ぐ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート",
      "<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート",
      "<ruby>評<rt>ひょう</rt></ruby><ruby>価<rt>か</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby><ruby>話<rt>はなし</rt></ruby><rt>はなし</rt></ruby>を<ruby>聴<rt>き</rt></ruby>いて<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>し<ruby>寄<rt>よ</rt></ruby>り<ruby>添<rt>そ</rt></ruby>う<ruby>精<rt>せい</rt></ruby><ruby>神<rt>しん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>支<rt>ささ</rt></ruby>えを<ruby>指<rt>し</rt></ruby>します。"
  },
  {
    "id": 35,
    "section": "人間関係とストレス・コーピング",
    "stem": "ソーシャルサポートのうち、<ruby>資<rt>し</rt></ruby><ruby>金<rt>きん</rt></ruby><ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby>、<ruby>介<rt>かい</rt></ruby><ruby>助<rt>じょ</rt></ruby>の<ruby>手<rt>て</rt></ruby><ruby>助<rt>だす</rt></ruby>け、<ruby>物<rt>ぶつ</rt></ruby><ruby>品<rt>ひん</rt></ruby>の<ruby>提<rt>てい</rt></ruby><ruby>供<rt>きょう</rt></ruby>など、<ruby>実<rt>じっ</rt></ruby><ruby>質<rt>しつ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>物<rt>ぶつ</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>金<rt>きん</rt></ruby><ruby>銭<rt>せん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>道<rt>どう</rt></ruby><ruby>具<rt>ぐ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート",
      "<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート",
      "<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート",
      "<ruby>自<rt>じ</rt></ruby><ruby>律<rt>りつ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>道<rt>どう</rt></ruby><ruby>具<rt>ぐ</rt></ruby><ruby>的<rt>てき</rt></ruby>サポート）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>直<rt>ちょく</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>物<rt>ぶつ</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>物<rt>ぶつ</rt></ruby><ruby>質<rt>しつ</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>手<rt>て</rt></ruby><ruby>助<rt>だす</rt></ruby>けやサービスの<ruby>提<rt>てい</rt></ruby><ruby>供<rt>きょう</rt></ruby>を<ruby>指<rt>し</rt></ruby>します。"
  },
  {
    "id": 36,
    "section": "人間関係とストレス・コーピング",
    "stem": "<ruby>困<rt>こん</rt></ruby><ruby>難<rt>なん</rt></ruby>や<ruby>逆<rt>ぎゃく</rt></ruby><ruby>境<rt>きょう</rt></ruby>に<ruby>直<rt>ちょく</rt></ruby><ruby>面<rt>めん</rt></ruby>した<ruby>際<rt>さい</rt></ruby>に、それに<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby>し<ruby>回<rt>かい</rt></ruby><ruby>復<rt>ふく</rt></ruby>・<ruby>克<rt>こく</rt></ruby><ruby>服<rt>ふく</rt></ruby>していく<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>精<rt>せい</rt></ruby><ruby>神<rt>しん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>回<rt>かい</rt></ruby><ruby>復<rt>ふく</rt></ruby><ruby>力<rt>りょく</rt></ruby>・<ruby>弾<rt>だん</rt></ruby><ruby>力<rt>りょく</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "レジリエンス",
      "バーンアウト",
      "コンプライアンス",
      "アドボカシー"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（レジリエンス）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ストレスや<ruby>困<rt>こん</rt></ruby><ruby>難<rt>なん</rt></ruby>を<ruby>柔<rt>じゅう</rt></ruby><ruby>軟<rt>なん</rt></ruby>に<ruby>乗<rt>の</rt></ruby>り<ruby>越<rt>こ</rt></ruby>える<ruby>回<rt>かい</rt></ruby><ruby>復<rt>ふく</rt></ruby><ruby>力<rt>りょく</rt></ruby>・<ruby>復<rt>ふく</rt></ruby><ruby>元<rt>げん</rt></ruby><ruby>力<rt>りょく</rt></ruby>を<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby>します。"
  },
  {
    "id": 37,
    "section": "対人関係におけるコミュニケーション",
    "stem": "コミュニケーション（communication）の<ruby>語<rt>ご</rt></ruby><ruby>源<rt>げん</rt></ruby>となったラテン<ruby>語<rt>ご</rt></ruby>「communis」の<ruby>本<rt>ほん</rt></ruby><ruby>来<rt>らい</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "「<ruby>共<rt>きょう</rt></ruby><ruby>有<rt>ゆう</rt></ruby>する」「<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby><ruby>項<rt>こう</rt></ruby>をつくる」",
      "「<ruby>命<rt>めい</rt></ruby><ruby>令<rt>れい</rt></ruby>する」「<ruby>支<rt>し</rt></ruby><ruby>配<rt>はい</rt></ruby>する」",
      "「<ruby>救<rt>きゅう</rt></ruby><ruby>済<rt>さい</rt></ruby>する」「<ruby>治<rt>ち</rt></ruby><ruby>療<rt>りょう</rt></ruby>する」",
      "「<ruby>論<rt>ろん</rt></ruby><ruby>破<rt>は</rt></ruby>する」「<ruby>納<rt>のう</rt></ruby><ruby>得<rt>とく</rt></ruby>させる」"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（「<ruby>共<rt>きょう</rt></ruby><ruby>有<rt>ゆう</rt></ruby>する」「<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby><ruby>項<rt>こう</rt></ruby>をつくる」）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>を<ruby>一<rt>いち</rt></ruby><ruby>方<rt>ほう</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>伝<rt>でん</rt></ruby>えるだけでなく、<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby>や<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>分<rt>わ</rt></ruby>かち<ruby>合<rt>あ</rt></ruby>い<ruby>共<rt>きょう</rt></ruby><ruby>有<rt>ゆう</rt></ruby>することが<ruby>本<rt>ほん</rt></ruby><ruby>質<rt>しつ</rt></ruby>です。"
  },
  {
    "id": 38,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby>発<rt>はつ</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby><ruby>あたま<rt>あたま</rt></ruby><rt>あたま</rt></ruby>の<ruby>中<rt>なか</rt></ruby>の<ruby>思<rt>おも</rt></ruby><ruby>考<rt>こう</rt></ruby>や<ruby>意<rt>い</rt></ruby><ruby>図<rt>と</rt></ruby>を、<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>や<ruby>身<rt>み</rt></ruby><ruby>振<rt>ぶ</rt></ruby>りなどの<ruby>具<rt>ぐ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>なサインに<ruby>変<rt>へん</rt></ruby><ruby>換<rt>かん</rt></ruby>して<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>に<ruby>届<rt>とど</rt></ruby>けるプロセスを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>き<rt>き</rt></ruby><ruby>号<rt>ごう</rt></ruby><ruby>化<rt>か</rt></ruby>（<ruby>ふ<rt>ふ</rt></ruby><ruby>号<rt>ごう</rt></ruby><ruby>化<rt>か</rt></ruby>・エンコード）",
      "<ruby>かい<rt>かい</rt></ruby><ruby>読<rt>どく</rt></ruby>（デコード）",
      "フィードバック",
      "ノイズ"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>き<rt>き</rt></ruby><ruby>号<rt>ごう</rt></ruby><ruby>化<rt>か</rt></ruby>（<ruby>ふ<rt>ふ</rt></ruby><ruby>号<rt>ごう</rt></ruby><ruby>化<rt>か</rt></ruby>・エンコード））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>受<rt>じゅ</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>がそれを<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>って<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby>を<ruby>読<rt>どく</rt></ruby>み<ruby>解<rt>かい</rt></ruby>く<ruby>行<rt>ぎょう</rt></ruby><ruby>為<rt>い</rt></ruby>を「<ruby>かい<rt>かい</rt></ruby><ruby>読<rt>どく</rt></ruby>（デコード）」と<ruby>呼<rt>こ</rt></ruby>びます。"
  },
  {
    "id": 39,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby>受<rt>じゅ</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>ったメッセージを<ruby>理<rt>り</rt></ruby><ruby>解<rt>かい</rt></ruby>し、それに<ruby>対<rt>たい</rt></ruby>する<ruby>返<rt>へん</rt></ruby><ruby>事<rt>ごと</rt></ruby>や<ruby>反<rt>はん</rt></ruby><ruby>応<rt>おう</rt></ruby>を<ruby>発<rt>はつ</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>へと<ruby>送<rt>そう</rt></ruby>り<ruby>返<rt>へん</rt></ruby>すプロセスとして、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "フィードバック",
      "チャネル",
      "エンコード",
      "インターアクション"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（フィードバック）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。フィードバックによって<ruby>発<rt>はつ</rt></ruby><ruby>信<rt>しん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>は<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>図<rt>と</rt></ruby>が<ruby>正<rt>ただ</rt></ruby>しく<ruby>伝<rt>でん</rt></ruby>わったかを<ruby>確<rt>かく</rt></ruby><ruby>認<rt>にん</rt></ruby>・<ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby>できます。"
  },
  {
    "id": 40,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション（バーバル・コミュニケーション）の<ruby>主<rt>しゅ</rt></ruby>な<ruby>特<rt>とく</rt></ruby><ruby>徴<rt>ちょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>論<rt>ろん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>客<rt>きゃっ</rt></ruby><ruby>観<rt>かん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>事<rt>ごと</rt></ruby><ruby>実<rt>じっ</rt></ruby>や<ruby>抽<rt>ちゅう</rt></ruby><ruby>象<rt>しょう</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>を<ruby>正<rt>せい</rt></ruby><ruby>確<rt>かく</rt></ruby>に<ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>するのに<ruby>適<rt>てき</rt></ruby>している",
      "<ruby>無<rt>む</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>好<rt>こう</rt></ruby><ruby>意<rt>い</rt></ruby>を<ruby>偽<rt>ぎ</rt></ruby>りなく<ruby>直<rt>ちょく</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>伝<rt>でん</rt></ruby>えるのが<ruby>得<rt>とく</rt></ruby><ruby>意<rt>い</rt></ruby>である",
      "<ruby>動<rt>どう</rt></ruby><ruby>物<rt>ぶつ</rt></ruby>と<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>始<rt>し</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby><ruby>手<rt>て</rt></ruby><ruby>段<rt>だん</rt></ruby>である",
      "<ruby><ruby>声<rt>こえ</rt></ruby><rt>こえ</rt></ruby>のトーンや<ruby><ruby>話<rt>はなし</rt></ruby><rt>はな</rt></ruby>す<ruby>速<rt>そく</rt></ruby><ruby>度<rt>ど</rt></ruby>そのものを<ruby>指<rt>さ</rt></ruby>す"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>論<rt>ろん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>客<rt>きゃっ</rt></ruby><ruby>観<rt>かん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>事<rt>ごと</rt></ruby><ruby>実<rt>じっ</rt></ruby>や<ruby>抽<rt>ちゅう</rt></ruby><ruby>象<rt>しょう</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>を<ruby>正<rt>せい</rt></ruby><ruby>確<rt>かく</rt></ruby>に<ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>するのに<ruby>適<rt>てき</rt></ruby>している）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>は<ruby>思<rt>おも</rt></ruby><ruby>考<rt>こう</rt></ruby>や<ruby>事<rt>ごと</rt></ruby><ruby>実<rt>じっ</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>の<ruby>正<rt>せい</rt></ruby><ruby>確<rt>かく</rt></ruby>な<ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>に<ruby>優<rt>ゆう</rt></ruby>れています。"
  },
  {
    "id": 41,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby><ruby>声<rt>こえ</rt></ruby><rt>こえ</rt></ruby>の<ruby>大<rt>たい</rt></ruby>きさ、<ruby>高<rt>こう</rt></ruby><ruby>低<rt>てい</rt></ruby>、<ruby><ruby>話<rt>はなし</rt></ruby><rt>はな</rt></ruby>す<ruby>速<rt>そく</rt></ruby><ruby>度<rt>ど</rt></ruby>、リズム、<ruby>口<rt>くち</rt></ruby><ruby>調<rt>ちょう</rt></ruby>など、<ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>の<ruby>内<rt>ない</rt></ruby><ruby>容<rt>よう</rt></ruby>そのものではなく「<ruby><ruby>話<rt>はなし</rt></ruby><rt>はな</rt></ruby>し<ruby>方<rt>かた</rt></ruby>の<ruby>音<rt>おん</rt></ruby><ruby>声<rt>こえ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>特<rt>とく</rt></ruby><ruby>徴<rt>ちょう</rt></ruby>」を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>準<rt>じゅん</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>（<ruby>周<rt>しゅう</rt></ruby><ruby>辺<rt>へん</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>・パラ<ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>）",
      "<ruby>しん<rt>しん</rt></ruby><ruby>たい<rt>たい</rt></ruby><ruby>げん<rt>げん</rt></ruby><ruby>ご<rt>ご</rt></ruby>（キネシクス）",
      "<ruby>しょう<rt>しょう</rt></ruby><ruby>ちょう<rt>ちょう</rt></ruby><ruby>き<rt>き</rt></ruby><ruby>ごう<rt>ごう</rt></ruby>",
      "<ruby>じん<rt>じん</rt></ruby><ruby>こう<rt>こう</rt></ruby><ruby>ぶつ<rt>ぶつ</rt></ruby><ruby>げん<rt>げん</rt></ruby><ruby>ご<rt>ご</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>準<rt>じゅん</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>（<ruby>周<rt>しゅう</rt></ruby><ruby>辺<rt>へん</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>・パラ<ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby><ruby>以<rt>い</rt></ruby><ruby>上<rt>じょう</rt></ruby>に、<ruby><ruby>話<rt>はなし</rt></ruby><rt>はな</rt></ruby>し<ruby>手<rt>て</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>を<ruby>強<rt>きょう</rt></ruby>く<ruby>伝<rt>でん</rt></ruby>える<ruby>要<rt>よう</rt></ruby><ruby>素<rt>そ</rt></ruby>です。"
  },
  {
    "id": 42,
    "section": "対人関係におけるコミュニケーション",
    "stem": "エドワード・ホールによる<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>の<ruby>分<rt>ぶん</rt></ruby><ruby>類<rt>るい</rt></ruby>において、<ruby>家<rt>か</rt></ruby><ruby>族<rt>ぞく</rt></ruby>や<ruby>恋<rt>こい</rt></ruby><ruby>人<rt>じん</rt></ruby>など<ruby>極<rt>きょく</rt></ruby>めて<ruby>親<rt>しん</rt></ruby><ruby>密<rt>みつ</rt></ruby>な<ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>で<ruby>許<rt>きょ</rt></ruby>される<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（0〜50cm<ruby>未<rt>み</rt></ruby><ruby>満<rt>まん</rt></ruby>）の<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>密<rt>みつ</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>個<rt>こ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>）",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>公<rt>こう</rt></ruby><ruby>衆<rt>しゅう</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>密<rt>みつ</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>身<rt>しん</rt></ruby><ruby>体<rt>たい</rt></ruby>が<ruby>容<rt>よう</rt></ruby><ruby>易<rt>い</rt></ruby>に<ruby>触<rt>ふ</rt></ruby>れ<ruby>合<rt>あ</rt></ruby>う<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>であり、<ruby>親<rt>しん</rt></ruby><ruby>密<rt>みつ</rt></ruby>な<ruby>間<rt>あいだがら</rt></ruby><ruby>以<rt>い</rt></ruby><ruby>外<rt>がい</rt></ruby>が<ruby>侵<rt>しん</rt></ruby><ruby>入<rt>にゅう</rt></ruby>すると<ruby>強<rt>きょう</rt></ruby>い<ruby>不<rt>ふ</rt></ruby><ruby>快<rt>かい</rt></ruby><ruby>感<rt>かん</rt></ruby>や<ruby>警<rt>けい</rt></ruby><ruby>戒<rt>かい</rt></ruby><ruby>感<rt>かん</rt></ruby>を<ruby>抱<rt>いだ</rt></ruby>きます。"
  },
  {
    "id": 43,
    "section": "対人関係におけるコミュニケーション",
    "stem": "ホールの<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>において、<ruby>友<rt>ゆう</rt>人<rt>じん</rt></ruby>や<ruby>知<rt>ち</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>士<rt>し</rt></ruby>が<ruby>日<rt>にち</rt></ruby><ruby>常<rt>じょう</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はなし</rt></ruby>や<ruby>歓<rt>かん</rt></ruby><ruby>談<rt>だん</rt></ruby>をするのに<ruby>適<rt>てき</rt></ruby>した<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（<ruby>約<rt>やく</rt></ruby>50cm〜1.2m）の<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>個<rt>こ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>・パーソナルディスタンス）",
      "<ruby>密<rt>みつ</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>公<rt>こう</rt></ruby><ruby>衆<rt>しゅう</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>個<rt>こ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>・パーソナルディスタンス））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>手<rt>て</rt></ruby>を<ruby>伸<rt>の</rt></ruby>ばせば<ruby>触<rt>ふ</rt></ruby>れられるが、<ruby>互<rt>ご</rt></ruby>いの<ruby>私<rt>し</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>領<rt>りょう</rt></ruby><ruby>域<rt>いき</rt></ruby>を<ruby>守<rt>しゅ</rt></ruby>れる<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>です。"
  },
  {
    "id": 44,
    "section": "対人関係におけるコミュニケーション",
    "stem": "ホールの<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>において、<ruby>仕<rt>し</rt></ruby><ruby>事<rt>ごと</rt></ruby><ruby>上<rt>じょう</rt></ruby>の<ruby>商<rt>しょう</rt></ruby><ruby>談<rt>だん</rt></ruby>や<ruby>公<rt>こう</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>事<rt>ごと</rt></ruby><ruby>務<rt>む</rt></ruby><ruby>手<rt>て</rt></ruby><ruby>続<rt>ぞく</rt></ruby>き、あまり<ruby>親<rt>しん</rt></ruby>しくない<ruby>人<rt>じん</rt></ruby>との<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>対<rt>たい</rt></ruby><ruby><ruby>話<rt>はなし</rt></ruby><rt>はなし</rt></ruby>に<ruby>適<rt>てき</rt></ruby>した<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（<ruby>約<rt>やく</rt></ruby>1.2m〜3.6m）の<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>密<rt>みつ</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>個<rt>こ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>公<rt>こう</rt></ruby><ruby>衆<rt>しゅう</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>身<rt>しん</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>接<rt>せつ</rt></ruby><ruby>触<rt>しょく</rt></ruby>はなく、<ruby>公<rt>こう</rt></ruby><ruby>式<rt>しき</rt></ruby>なやり<ruby>取<rt>と</rt></ruby>りに<ruby>適<rt>てき</rt></ruby>した<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby><ruby>感<rt>かん</rt></ruby>です。"
  },
  {
    "id": 45,
    "section": "対人関係におけるコミュニケーション",
    "stem": "ホールの<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>において、<ruby>講<rt>こう</rt></ruby><ruby>演<rt>えん</rt></ruby><ruby>会<rt>かい</rt></ruby>や<ruby>講<rt>こう</rt></ruby><ruby>義<rt>ぎ</rt></ruby>、<ruby>演<rt>えん</rt></ruby><ruby>説<rt>せつ</rt></ruby>など、<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>対<rt>たい</rt></ruby><ruby>話<rt>はなし</rt></ruby>ではなく<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>に<ruby>向<rt>こう</rt></ruby>けて<ruby><ruby>話<rt>はなし</rt></ruby><rt>はな</rt></ruby>しかける<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>（<ruby>約<rt>やく</rt></ruby>3.6m<ruby>以<rt>い</rt></ruby><ruby>上<rt>じょう</rt></ruby>）の<ruby>名<rt>めい</rt></ruby><ruby>称<rt>しょう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>公<rt>こう</rt></ruby><ruby>衆<rt>しゅう</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>個<rt>こ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>",
      "<ruby>密<rt>みつ</rt></ruby><ruby>接<rt>せつ</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>公<rt>こう</rt></ruby><ruby>衆<rt>しゅう</rt></ruby><ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>公<rt>こう</rt></ruby>の<ruby>場<rt>じょう</rt></ruby>で<ruby>不<rt>ふ</rt></ruby><ruby>特<rt>とく</rt></ruby><ruby>定<rt>てい</rt></ruby><ruby>多<rt>た</rt></ruby><ruby>数<rt>すう</rt></ruby>と<ruby>接<rt>せつ</rt></ruby>する<ruby>際<rt>さい</rt></ruby>に<ruby>設<rt>せつ</rt></ruby><ruby>定<rt>てい</rt></ruby>される<ruby>距<rt>きょ</rt></ruby><ruby>離<rt>り</rt></ruby>です。"
  },
  {
    "id": 46,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby>非<rt>ひ</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>のうち、<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>の<ruby>内<rt>ない</rt></ruby><ruby>容<rt>よう</rt></ruby>を<ruby>視<rt>し</rt></ruby><ruby>覚<rt>かく</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>強<rt>きょう</rt></ruby><ruby>調<rt>ちょう</rt></ruby>・<ruby>補<rt>ほ</rt></ruby><ruby>足<rt>そく</rt></ruby>するために<ruby>手<rt>て</rt></ruby>の<ruby>動<rt>どう</rt></ruby>きなどで<ruby>形<rt>けい</rt></ruby>や<ruby>方<rt>ほう</rt></ruby><ruby>向<rt>こう</rt></ruby>を<ruby>指<rt>さ</rt></ruby>し<ruby>示<rt>しめ</rt></ruby>すジェスチャーを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>例<rt>れい</rt></ruby><ruby>示<rt>じ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（イラストレーター）",
      "<ruby>表<rt>ひょう</rt></ruby><ruby>象<rt>しょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（エンブレム）",
      "<ruby>かん<rt>かん</rt></ruby><ruby>じょう<rt>じょう</rt></ruby><ruby>ひょう<rt>ひょう</rt></ruby><ruby>しゅつ<rt>しゅつ</rt></ruby><ruby>どう<rt>どう</rt></ruby><ruby>さ<rt>さ</rt></ruby>",
      "<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（アダプター）"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>例<rt>れい</rt></ruby><ruby>示<rt>じ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（イラストレーター））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。「これくらいの<ruby>大<rt>たい</rt></ruby>きさ」「<ruby>右<rt>う</rt></ruby>へ<ruby>曲<rt>ま</rt></ruby>がって」など<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>を<ruby>補<rt>ほ</rt></ruby><ruby>強<rt>きょう</rt></ruby>する<ruby>身<rt>み</rt></ruby><ruby>振<rt>ぶ</rt></ruby>りです。"
  },
  {
    "id": 47,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby>対<rt>たい</rt></ruby><ruby>話<rt>はなし</rt></ruby>の<ruby>進<rt>しん</rt></ruby><ruby>行<rt>ぎょう</rt></ruby>を<ruby>円<rt>えん</rt></ruby><ruby>滑<rt>かつ</rt></ruby>にするために<ruby>行<rt>おこな</rt></ruby>われる、うなずきや<ruby>相<rt>あい</rt></ruby>づち、<ruby>視<rt>し</rt></ruby><ruby>線<rt>せん</rt></ruby>の<ruby>移<rt>い</rt></ruby><ruby>動<rt>どう</rt></ruby>など、<ruby>会<rt>かい</rt></ruby><ruby>話<rt>はなし</rt></ruby>の<ruby>順<rt>じゅん</rt></ruby><ruby>番<rt>ばん</rt></ruby>や<ruby>流<rt>なが</rt></ruby>れを<ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby>する<ruby>非<rt>ひ</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby><ruby>的<rt>てき</rt></ruby>サインを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（レギュレーター）",
      "<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（アダプター）",
      "<ruby>表<rt>ひょう</rt></ruby><ruby>象<rt>しょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（エンブレム）",
      "<ruby>ほ<rt>ほ</rt></ruby><ruby>かん<rt>かん</rt></ruby><ruby>どう<rt>どう</rt></ruby><ruby>さ<rt>さ</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（レギュレーター））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby><ruby>話<rt>はなし</rt></ruby><rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いている<ruby>合<rt>ごう</rt></ruby><ruby>図<rt>と</rt></ruby>や、<ruby>発<rt>はつ</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>交<rt>こう</rt></ruby><ruby>代<rt>だい</rt></ruby>のサインとして<ruby>機<rt>き</rt></ruby><ruby>能<rt>のう</rt></ruby>します。"
  },
  {
    "id": 48,
    "section": "対人関係におけるコミュニケーション",
    "stem": "<ruby>緊<rt>きん</rt></ruby><ruby>張<rt>ちょう</rt></ruby>や<ruby>不<rt>ふ</rt></ruby><ruby>安<rt>あん</rt></ruby>、<ruby>退<rt>たい</rt></ruby><ruby>屈<rt>くつ</rt></ruby>を<ruby>感<rt>かん</rt></ruby>じたときに、<ruby>無<rt>む</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>に<ruby>髪<rt>かみ</rt></ruby>を<ruby>触<rt>さわ</rt></ruby>ったり<ruby>爪<rt>つめ</rt></ruby>を<ruby>か<rt>か</rt></ruby>んだり<ruby>貧<rt>びん</rt></ruby><ruby>乏<rt>ぼう</rt></ruby>ゆすりをしたりする<ruby>身<rt>しん</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（アダプター）",
      "<ruby>調<rt>ちょう</rt></ruby><ruby>整<rt>せい</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（レギュレーター）",
      "<ruby>例<rt>れい</rt></ruby><ruby>示<rt>じ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（イラストレーター）",
      "<ruby>表<rt>ひょう</rt></ruby><ruby>象<rt>しょう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（エンブレム）"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>（アダプター））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>内<rt>ない</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>緊<rt>きん</rt></ruby><ruby>張<rt>ちょう</rt></ruby>やストレスを<ruby>解<rt>かい</rt></ruby><ruby>消<rt>しょう</rt></ruby>・<ruby>適<rt>てき</rt></ruby><ruby>応<rt>おう</rt></ruby>させようとする<ruby>無<rt>む</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>識<rt>しき</rt></ruby>の<ruby>動<rt>どう</rt></ruby><ruby>作<rt>さく</rt></ruby>です。"
  },
  {
    "id": 49,
    "section": "対人援助関係とバイステックの原則",
    "stem": "<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>や<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>率<rt>りつ</rt></ruby><ruby>直<rt>ちょく</rt></ruby>・<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>に<ruby>伝<rt>でん</rt></ruby>えると<ruby>同<rt>どう</rt></ruby><ruby>時<rt>じ</rt></ruby>に、<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>立<rt>りつ</rt></ruby><ruby>場<rt>じょう</rt></ruby>や<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>も<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>し<ruby>対<rt>たい</rt></ruby><ruby>等<rt>とう</rt></ruby>な<ruby>対<rt>たい</rt></ruby><ruby><ruby>話<rt>はなし</rt></ruby><rt>はなし</rt></ruby>をめざすコミュニケーション<ruby>姿<rt>し</rt></ruby><ruby>勢<rt>せい</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "アサーティブ・コミュニケーション",
      "アグレッシブ（<ruby>攻<rt>こう</rt></ruby><ruby>撃<rt>げき</rt></ruby><ruby>的<rt>てき</rt></ruby>）・コミュニケーション",
      "ノンアサーティブ（<ruby>非<rt>ひ</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>張<rt>ちょう</rt></ruby><ruby>的<rt>てき</rt></ruby>）・コミュニケーション",
      "パターナリズム（<ruby>父<rt>ふ</rt></ruby><ruby>権<rt>けん</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>義<rt>ぎ</rt></ruby>）"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（アサーティブ・コミュニケーション）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>自<rt>じ</rt></ruby><ruby>他<rt>た</rt></ruby>を<ruby>共<rt>きょう</rt></ruby>に<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>する<ruby>さわ<rt>さわ</rt></ruby>やかな<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>張<rt>ちょう</rt></ruby>のあり<ruby>方<rt>ほう</rt></ruby>です。"
  },
  {
    "id": 50,
    "section": "対人援助関係とバイステックの原則",
    "stem": "<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>にノーと<ruby>言<rt>げん</rt></ruby>えず、<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>我<rt>が</rt></ruby><ruby>慢<rt>まん</rt></ruby>して<ruby>押<rt>お</rt></ruby>し<ruby>黙<rt>だま</rt></ruby>り、<ruby>結<rt>けつ</rt></ruby><ruby>果<rt>か</rt></ruby>として<ruby>不<rt>ふ</rt></ruby><ruby>満<rt>まん</rt></ruby>やストレスを<ruby>抱<rt>かか</rt></ruby>え<ruby>込<rt>こ</rt></ruby>んでしまうコミュニケーション<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ノンアサーティブ（<ruby>非<rt>ひ</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>張<rt>ちょう</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>受<rt>じゅ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>的<rt>てき</rt></ruby>）<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>",
      "アサーティブ<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>",
      "アグレッシブ<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>",
      "<ruby>作<rt>さく</rt></ruby><ruby>為<rt>い</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ノンアサーティブ（<ruby>非<rt>ひ</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>張<rt>ちょう</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>受<rt>じゅ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>的<rt>てき</rt></ruby>）<ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>を<ruby>優<rt>ゆう</rt></ruby><ruby>先<rt>せん</rt></ruby>しすぎて<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>を<ruby>粗<rt>そ</rt></ruby><ruby>末<rt>まつ</rt></ruby>にしてしまう<ruby>状<rt>じょう</rt></ruby><ruby>態<rt>たい</rt></ruby>です。"
  },
  {
    "id": 51,
    "section": "対人援助関係とバイステックの原則",
    "stem": "<ruby>対<rt>たい</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby>における「<ruby>受<rt>じゅ</rt></ruby><ruby>容<rt>よう</rt></ruby>」の<ruby>正<rt>ただ</rt></ruby>しい<ruby>意<rt>い</rt></ruby><ruby>味<rt>み</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>のどのような<ruby>違<rt>い</rt></ruby><ruby>法<rt>ほう</rt></ruby><ruby>行<rt>ぎょう</rt></ruby><ruby>為<rt>い</rt></ruby>や<ruby>暴<rt>ぼう</rt></ruby><ruby>言<rt>げん</rt></ruby>もすべて<ruby>正<rt>ただ</rt></ruby>しいと<ruby>肯<rt>こう</rt></ruby><ruby>定<rt>てい</rt></ruby>・<ruby>推<rt>すい</rt></ruby><ruby>奨<rt>しょう</rt></ruby>すること",
      "<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>価<rt>か</rt></ruby><ruby>値<rt>ち</rt></ruby><ruby>観<rt>かん</rt></ruby>や<ruby>道<rt>どう</rt></ruby><ruby>徳<rt>とく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>基<rt>き</rt></ruby><ruby>準<rt>じゅん</rt></ruby>で<ruby>善<rt>ぜん</rt></ruby><ruby>悪<rt>あく</rt></ruby>を<ruby>裁<rt>さい</rt></ruby>かず、その<ruby>人<rt>じん</rt></ruby>のありのままの<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>存<rt>そん</rt></ruby><ruby>在<rt>ざい</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>めること",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>抱<rt>だ</rt></ruby>える<ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>や<ruby>生<rt>せい</rt></ruby><ruby>活<rt>かつ</rt></ruby>のすべてを<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>肩<rt>かた</rt></ruby><ruby>代<rt>が</rt></ruby>わりして<ruby>代<rt>だい</rt></ruby><ruby>行<rt>ぎょう</rt></ruby>すること",
      "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby><ruby>話<rt>はなし</rt></ruby><rt>はなし</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>表<rt>ひょう</rt></ruby><ruby>面<rt>めん</rt></ruby><ruby>的<rt>てき</rt></ruby>なお<ruby>世<rt>せ</rt></ruby><ruby>辞<rt>じ</rt></ruby>を<ruby>言<rt>げん</rt></ruby>ってその<ruby>場<rt>じょう</rt></ruby>を<ruby>取<rt>と</rt></ruby>り<ruby>繕<rt>つくろ</rt></ruby>うこと"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>価<rt>か</rt></ruby><ruby>値<rt>ち</rt></ruby><ruby>観<rt>かん</rt></ruby>や<ruby>道<rt>どう</rt></ruby><ruby>徳<rt>とく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>基<rt>き</rt></ruby><ruby>準<rt>じゅん</rt></ruby>で<ruby>善<rt>ぜん</rt></ruby><ruby>悪<rt>あく</rt></ruby>を<ruby>裁<rt>さい</rt></ruby>かず、その<ruby>人<rt>じん</rt></ruby>のありのままの<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>や<ruby>存<rt>そん</rt></ruby><ruby>在<rt>ざい</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>めること）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>行<rt>ぎょう</rt></ruby><ruby>為<rt>い</rt></ruby>の<ruby>是<rt>ぜ</rt></ruby><ruby>非<rt>ひ</rt></ruby>と<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>の<ruby>尊<rt>そん</rt></ruby><ruby>厳<rt>げん</rt></ruby>を<ruby>しゅん<rt>しゅん</rt></ruby><ruby>別<rt>べつ</rt></ruby>し、<ruby>丸<rt>まる</rt></ruby>ごと<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れます。"
  },
  {
    "id": 52,
    "section": "対人援助関係とバイステックの原則",
    "stem": "<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>における「<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>」と「<ruby>同<rt>どう</rt></ruby><ruby>情<rt>じょう</rt></ruby>」の<ruby>違<rt>ちが</rt></ruby>いに<ruby>関<rt>かん</rt></ruby>する<ruby>記<rt>き</rt></ruby><ruby>述<rt>じゅつ</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>同<rt>どう</rt></ruby><ruby>情<rt>じょう</rt></ruby>は<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>の<ruby>主<rt>しゅ</rt></ruby><ruby>観<rt>かん</rt></ruby>でかわいそうと<ruby>上<rt>じょう</rt></ruby>から<ruby>あわ<rt>あわ</rt></ruby>れむ<ruby>傾<rt>けい</rt></ruby><ruby>向<rt>こう</rt></ruby>があり、<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>は<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>立<rt>りつ</rt></ruby><ruby>場<rt>じょう</rt></ruby>に<ruby>立<rt>た</rt></ruby>ちつつも<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>巻<rt>ま</rt></ruby>き<ruby>込<rt>こ</rt></ruby>まれず<ruby>客<rt>きゃっ</rt></ruby><ruby>観<rt>かん</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>保<rt>ほ</rt></ruby>つ<ruby>姿<rt>し</rt></ruby><ruby>勢<rt>せい</rt></ruby>である",
      "<ruby>同<rt>どう</rt></ruby><ruby>情<rt>じょう</rt></ruby>と<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>は<ruby>心<rt>しん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>学<rt>がく</rt></ruby><ruby>的<rt>てき</rt></ruby>にまったく<ruby>同<rt>どう</rt></ruby><ruby>一<rt>いち</rt></ruby>の<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>である",
      "<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>とは<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>と<ruby>全<rt>ぜん</rt></ruby>く<ruby>同<rt>どう</rt></ruby>じ<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>に<ruby>飲<rt>の</rt></ruby>み<ruby>込<rt>こ</rt></ruby>まれて<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>が<ruby>冷<rt>れい</rt></ruby><ruby>静<rt>せい</rt></ruby>さを<ruby>失<rt>しっ</rt></ruby>うことである",
      "<ruby>専<rt>せん</rt></ruby><ruby>門<rt>もん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby>においては<ruby>同<rt>どう</rt></ruby><ruby>情<rt>じょう</rt></ruby>のみを<ruby>重<rt>じゅう</rt></ruby><ruby>視<rt>し</rt></ruby>し、<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>は<ruby>排<rt>はい</rt></ruby><ruby>除<rt>じょ</rt></ruby>すべきである"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>同<rt>どう</rt></ruby><ruby>情<rt>じょう</rt></ruby>は<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>の<ruby>主<rt>しゅ</rt></ruby><ruby>観<rt>かん</rt></ruby>でかわいそうと<ruby>上<rt>じょう</rt></ruby>から<ruby>あわ<rt>あわ</rt></ruby>れむ<ruby>傾<rt>けい</rt></ruby><ruby>向<rt>こう</rt></ruby>があり、<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>は<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>立<rt>りつ</rt></ruby><ruby>場<rt>じょう</rt></ruby>に<ruby>立<rt>た</rt></ruby>ちつつも<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>巻<rt>ま</rt></ruby>き<ruby>込<rt>こ</rt></ruby>まれず<ruby>客<rt>きゃっ</rt></ruby><ruby>観<rt>かん</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>保<rt>ほ</rt></ruby>つ<ruby>姿<rt>し</rt></ruby><ruby>勢<rt>せい</rt></ruby>である）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。"
  },
  {
    "id": 53,
    "section": "対人援助関係とバイステックの原則",
    "stem": "バイステックの7<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>において、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>を<ruby>画<rt>かく</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>扱<rt>あつか</rt></ruby>わず、その<ruby>人<rt>じん</rt></ruby><ruby>固<rt>こ</rt></ruby><ruby>有<rt>ゆう</rt></ruby>の<ruby>生<rt>お</rt></ruby>い<ruby>立<rt>た</rt></ruby>ちや<ruby>特<rt>とく</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>持<rt>じ</rt></ruby>ったかけがえのない1<ruby>人<rt>ひとり</rt></ruby>の<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>として<ruby>捉<rt>とら</rt></ruby>える<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>意<rt>い</rt></ruby><ruby>図<rt>と</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>表<rt>ひょう</rt></ruby><ruby>出<rt>しゅつ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>統<rt>とう</rt></ruby><ruby>制<rt>せい</rt></ruby>された<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>与<rt>よ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>受<rt>じゅ</rt></ruby><ruby>用<rt>よう</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>性<rt>せい</rt></ruby>や<ruby>独<rt>どく</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>深<rt>しん</rt></ruby>く<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>する<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>です。"
  },
  {
    "id": 54,
    "section": "対人援助関係とバイステックの原則",
    "stem": "バイステックの7<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>において、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>怒<rt>いか</rt></ruby>りや<ruby>悲<rt>かな</rt></ruby>しみなどの<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>も<ruby>含<rt>ふく</rt></ruby>めて、<ruby>よく<rt>よく</rt></ruby><ruby>圧<rt>あつ</rt></ruby>することなく<ruby>自<rt>じ</rt></ruby><ruby>由<rt>ゆう</rt></ruby>に<ruby>表<rt>ひょう</rt></ruby><ruby>現<rt>げん</rt></ruby>できるように<ruby>支<rt>し</rt></ruby><ruby>援<rt>えん</rt></ruby>する<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>意<rt>い</rt></ruby><ruby>図<rt>と</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>表<rt>ひょう</rt></ruby><ruby>出<rt>しゅつ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>非<rt>ひ</rt></ruby><ruby>審<rt>しん</rt></ruby><ruby>判<rt>ぱん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>決<rt>けっ</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby><ruby>保<rt>ほ</rt></ruby><ruby>持<rt>じ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>意<rt>い</rt></ruby><ruby>図<rt>と</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>表<rt>ひょう</rt></ruby><ruby>出<rt>しゅつ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>耳<rt>みみ</rt></ruby>を<ruby>傾<rt>かたむ</rt></ruby>け、<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>安<rt>あん</rt></ruby><ruby>心<rt>しん</rt></ruby>して<ruby>表<rt>ひょう</rt></ruby><ruby>出<rt>しゅつ</rt></ruby>できる<ruby>受<rt>じゅ</rt></ruby><ruby>容<rt>よう</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>場<rt>じょう</rt></ruby>をつくります。"
  },
  {
    "id": 55,
    "section": "対人援助関係とバイステックの原則",
    "stem": "バイステックの7<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>において、<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>は<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>に<ruby>巻<rt>ま</rt></ruby>き<ruby>込<rt>こ</rt></ruby>まれて<ruby>動<rt>どう</rt></ruby><ruby>揺<rt>ゆ</rt></ruby>するのではなく、<ruby>みずか<rt>みずか</rt></ruby>らの<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby>を<ruby>専<rt>せん</rt></ruby><ruby>門<rt>もん</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>自<rt>じ</rt></ruby><ruby>覚<rt>かく</rt></ruby>・<ruby>統<rt>とう</rt></ruby><ruby>制<rt>せい</rt></ruby>して<ruby>関<rt>かか</rt></ruby>わる<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>統<rt>とう</rt></ruby><ruby>制<rt>せい</rt></ruby>された<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>与<rt>よ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>受<rt>じゅ</rt></ruby><ruby>用<rt>よう</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>非<rt>ひ</rt></ruby><ruby>審<rt>しん</rt></ruby><ruby>判<rt>ぱん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>統<rt>とう</rt></ruby><ruby>制<rt>せい</rt></ruby>された<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>与<rt>よ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>共<rt>きょう</rt></ruby><ruby>感<rt>かん</rt></ruby>しつつも<ruby>専<rt>せん</rt></ruby><ruby>門<rt>もん</rt></ruby><ruby>職<rt>しょく</rt></ruby>としての<ruby>境<rt>きょう</rt></ruby><ruby>界<rt>かい</rt></ruby><ruby>線<rt>せん</rt></ruby>と<ruby>冷<rt>れい</rt></ruby><ruby>静<rt>せい</rt></ruby>さを<ruby>保<rt>ほ</rt></ruby>ちます。"
  },
  {
    "id": 56,
    "section": "対人援助関係とバイステックの原則",
    "stem": "バイステックの7<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>において、<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>みずか<rt>みずか</rt></ruby>らの<ruby>道<rt>どう</rt></ruby><ruby>徳<rt>とく</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>基<rt>き</rt></ruby><ruby>準<rt>じゅん</rt></ruby>や<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>価<rt>か</rt></ruby><ruby>値<rt>ち</rt></ruby><ruby>観<rt>かん</rt></ruby>によって、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>えや<ruby>過<rt>か</rt></ruby><ruby>去<rt>こ</rt></ruby>の<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>を<ruby>一<rt>いち</rt></ruby><ruby>方<rt>ほう</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>裁<rt>さい</rt></ruby>き<ruby>批<rt>ひ</rt></ruby><ruby>判<rt>はん</rt></ruby>してはならないとする<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>非<rt>ひ</rt></ruby><ruby>審<rt>しん</rt></ruby><ruby>判<rt>ぱん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>決<rt>けっ</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby><ruby>保<rt>ほ</rt></ruby><ruby>持<rt>じ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>受<rt>じゅ</rt></ruby><ruby>用<rt>よう</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>非<rt>ひ</rt></ruby><ruby>審<rt>しん</rt></ruby><ruby>判<rt>ぱん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>は<ruby>裁<rt>さい</rt></ruby><ruby>判<rt>はん</rt></ruby><ruby>官<rt>かん</rt></ruby>ではなく、<ruby>非<rt>ひ</rt></ruby><ruby>難<rt>なん</rt></ruby>せずに<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby>の<ruby>背<rt>はい</rt></ruby><ruby>景<rt>けい</rt></ruby>を<ruby>共<rt>きょう</rt></ruby>に<ruby>探<rt>たん</rt></ruby><ruby>求<rt>きゅう</rt></ruby>します。"
  },
  {
    "id": 57,
    "section": "対人援助関係とバイステックの原則",
    "stem": "バイステックの7<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>において、<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>方<rt>ほう</rt></ruby><ruby>針<rt>しん</rt></ruby>や<ruby>人<rt>じん</rt></ruby><ruby>生<rt>せい</rt></ruby>の<ruby>選<rt>せん</rt></ruby><ruby>択<rt>たく</rt></ruby>において、<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が<ruby>命<rt>めい</rt></ruby><ruby>令<rt>れい</rt></ruby>や<ruby>押<rt>お</rt></ruby>しつけをするのではなく、<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>が<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>し<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>する<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby>を<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>する<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>決<rt>けっ</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>意<rt>い</rt></ruby><ruby>図<rt>と</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>表<rt>ひょう</rt></ruby><ruby>出<rt>しゅつ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>統<rt>とう</rt></ruby><ruby>制<rt>せい</rt></ruby>された<ruby>情<rt>じょう</rt></ruby><ruby>緒<rt>ちょ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>与<rt>よ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>決<rt>けっ</rt></ruby><ruby>定<rt>てい</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>主<rt>しゅ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>性<rt>せい</rt></ruby>を<ruby>最<rt>さい</rt></ruby><ruby>大<rt>たい</rt></ruby><ruby>限<rt>げん</rt></ruby>に<ruby>尊<rt>そん</rt></ruby><ruby>重<rt>じゅう</rt></ruby>し、<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>できるよう<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby><ruby>提<rt>てい</rt></ruby><ruby>供<rt>きょう</rt></ruby>と<ruby>支<rt>し</rt></ruby><ruby>援<rt>えん</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>います。"
  },
  {
    "id": 58,
    "section": "対人援助関係とバイステックの原則",
    "stem": "バイステックの7<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>において、<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>活<rt>かつ</rt></ruby><ruby>動<rt>どう</rt></ruby>の<ruby>中<rt>ちゅう</rt></ruby>で<ruby>知<rt>し</rt></ruby>り<ruby>得<rt>え</rt></ruby>た<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby><ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>や<ruby>私<rt>し</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby>を、<ruby>正<rt>せい</rt></ruby><ruby>当<rt>あて</rt></ruby>な<ruby>理<rt>り</rt></ruby><ruby>由<rt>ゆう</rt></ruby>なく<ruby>第<rt>だい</rt></ruby><ruby>三<rt>さん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>漏<rt>も</rt></ruby>らしてはならないとする<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby><ruby>保<rt>ほ</rt></ruby><ruby>持<rt>じ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>非<rt>ひ</rt></ruby><ruby>審<rt>しん</rt></ruby><ruby>判<rt>ぱん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>態<rt>たい</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>受<rt>じゅ</rt></ruby><ruby>用<rt>よう</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>",
      "<ruby>個<rt>こ</rt></ruby><ruby>別<rt>べつ</rt></ruby><ruby>化<rt>か</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>秘<rt>ひ</rt></ruby><ruby>密<rt>みつ</rt></ruby><ruby>保<rt>ほ</rt></ruby><ruby>持<rt>じ</rt></ruby>の<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>信<rt>しん</rt></ruby><ruby>頼<rt>らい</rt></ruby><ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby>の<ruby>土<rt>ど</rt></ruby><ruby>台<rt>だい</rt></ruby>であり、<ruby>専<rt>せん</rt></ruby><ruby>門<rt>もん</rt></ruby><ruby>職<rt>しょく</rt></ruby>としての<ruby>法<rt>ほう</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>倫<rt>りん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>義<rt>ぎ</rt></ruby><ruby>務<rt>む</rt></ruby>です。"
  },
  {
    "id": 59,
    "section": "対人援助関係とバイステックの原則",
    "stem": "<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>そのものだけでなく、<ruby><ruby>声<rt>こえ</rt></ruby><rt>こえ</rt></ruby>のトーンや<ruby>沈<rt>ちん</rt></ruby><ruby>黙<rt>もく</rt></ruby>、<ruby>表<rt>ひょう</rt></ruby><ruby>情<rt>じょう</rt></ruby>、しぐさなどの<ruby>非<rt>ひ</rt></ruby><ruby>言<rt>げん</rt></ruby><ruby>語<rt>ご</rt></ruby><ruby>的<rt>てき</rt></ruby>なメッセージや「<ruby><ruby>声<rt>こえ</rt></ruby><rt>こえ</rt></ruby>なき<ruby><ruby>声<rt>こえ</rt></ruby><rt>こえ</rt></ruby>」にも<ruby>心<rt>しん</rt></ruby>を<ruby>配<rt>はい</rt></ruby>り<ruby>深<rt>しん</rt></ruby>く<ruby>耳<rt>みみ</rt></ruby>を<ruby>傾<rt>かたむ</rt></ruby>ける<ruby>聴<rt>き</rt></ruby>き<ruby>方<rt>かた</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>傾<rt>けい</rt></ruby><ruby>聴<rt>ちょう</rt></ruby>（アクティブ・リスニング）",
      "<ruby>指<rt>し</rt></ruby><ruby>示<rt>じ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>対<rt>たい</rt></ruby><ruby>話<rt>はなし</rt></ruby>",
      "<ruby>論<rt>ろん</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>分<rt>ぶん</rt></ruby><ruby>析<rt>せき</rt></ruby>",
      "<ruby>批<rt>ひ</rt></ruby><ruby>判<rt>はん</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>検<rt>けん</rt></ruby><ruby>討<rt>とう</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>傾<rt>けい</rt></ruby><ruby>聴<rt>ちょう</rt></ruby>（アクティブ・リスニング））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>心<rt>こころ</rt></ruby>の<ruby>世<rt>せ</rt></ruby><ruby>界<rt>かい</rt></ruby>に<ruby>寄<rt>よ</rt></ruby>り<ruby>添<rt>そ</rt></ruby>い、<ruby>真<rt>しん</rt></ruby><ruby>摯<rt>し</rt></ruby>に<ruby>受<rt>う</rt></ruby>け<ruby>止<rt>と</rt></ruby>めながら<ruby>聴<rt>き</rt></ruby>く<ruby>技<rt>ぎ</rt></ruby><ruby>法<rt>ほう</rt></ruby>です。"
  },
  {
    "id": 60,
    "section": "対人援助関係とバイステックの原則",
    "stem": "<ruby>援<rt>えん</rt></ruby><ruby>助<rt>じょ</rt></ruby><ruby>者<rt>しゃ</rt></ruby>が「<ruby>良<rt>よ</rt></ruby>かれと<ruby>思<rt>おも</rt></ruby>って」<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>を<ruby>無<rt>む</rt></ruby><ruby>視<rt>し</rt></ruby>し、<ruby>親<rt>しん</rt></ruby>が<ruby>子<rt>こ</rt></ruby>どもに<ruby>対<rt>たい</rt></ruby>するように<ruby>一<rt>いち</rt></ruby><ruby>方<rt>ほう</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>指<rt>し</rt></ruby><ruby>示<rt>じ</rt></ruby>・<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>してしまう<ruby>過<rt>か</rt></ruby><ruby>度<rt>ど</rt></ruby>の<ruby>保<rt>ほ</rt></ruby><ruby>護<rt>ご</rt></ruby>・<ruby>干<rt>かん</rt></ruby><ruby>渉<rt>しょう</rt></ruby><ruby>姿<rt>し</rt></ruby><ruby>勢<rt>せい</rt></ruby>を<ruby>指<rt>さ</rt></ruby>す<ruby>用<rt>よう</rt></ruby><ruby>語<rt>ご</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "パターナリズム（<ruby>父<rt>ふ</rt></ruby><ruby>権<rt>けん</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>義<rt>ぎ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>介<rt>かい</rt></ruby><ruby>入<rt>にゅう</rt></ruby>）",
      "アドボカシー（<ruby>権<rt>けん</rt></ruby><ruby>利<rt>り</rt></ruby><ruby>擁<rt>よう</rt></ruby><ruby>護<rt>ご</rt></ruby>）",
      "エンパワメント",
      "ノーマライゼーション"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（パターナリズム（<ruby>父<rt>ふ</rt></ruby><ruby>権<rt>けん</rt></ruby><ruby>主<rt>しゅ</rt></ruby><ruby>義<rt>ぎ</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>介<rt>かい</rt></ruby><ruby>入<rt>にゅう</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>尊<rt>そん</rt></ruby><ruby>厳<rt>げん</rt></ruby>や<ruby>自<rt>じ</rt></ruby><ruby>立<rt>りつ</rt></ruby>を<ruby>阻<rt>そ</rt></ruby><ruby>害<rt>がい</rt></ruby>する<ruby>危<rt>き</rt></ruby><ruby>険<rt>けん</rt></ruby><ruby>性<rt>せい</rt></ruby>があり、<ruby>戒<rt>かい</rt></ruby>められる<ruby>姿<rt>し</rt></ruby><ruby>勢<rt>せい</rt></ruby>です。"
  },
  {
    "id": 61,
    "section": "組織におけるコミュニケーション",
    "stem": "バーナードによる<ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby>の<ruby>成<rt>せい</rt></ruby><ruby>立<rt>りつ</rt></ruby><ruby>要<rt>よう</rt></ruby><ruby>件<rt>けん</rt></ruby>（3<ruby>要<rt>よう</rt></ruby><ruby>素<rt>そ</rt></ruby>）に<ruby>含<rt>ふく</rt></ruby>まれないものとして、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby>の<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>（<ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby><ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>）",
      "<ruby>貢<rt>こう</rt></ruby><ruby>献<rt>けん</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>欲<rt>よく</rt></ruby>（<ruby>協<rt>きょう</rt></ruby><ruby>働<rt>どう</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>思<rt>おも</rt></ruby>）",
      "<ruby>意<rt>い</rt></ruby><ruby>思<rt>おも</rt></ruby><ruby>疎<rt>そ</rt></ruby><ruby>通<rt>つう</rt></ruby>（コミュニケーション）",
      "<ruby>画<rt>かく</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>思<rt>おも</rt></ruby><ruby>想<rt>そう</rt></ruby>（<ruby>個<rt>こ</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>）"
    ],
    "answer": 4,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 4（<ruby>画<rt>かく</rt></ruby><ruby>一<rt>いち</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>思<rt>おも</rt></ruby><ruby>想<rt>そう</rt></ruby>（<ruby>個<rt>こ</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。バーナードの<ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby>の3<ruby>要<rt>よう</rt></ruby><ruby>素<rt>そ</rt></ruby>は「<ruby>共<rt>きょう</rt></ruby><ruby>通<rt>つう</rt></ruby>の<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>」「<ruby>貢<rt>こう</rt></ruby><ruby>献<rt>けん</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>欲<rt>よく</rt></ruby>」「<ruby>意<rt>い</rt></ruby><ruby>思<rt>おも</rt></ruby><ruby>疎<rt>そ</rt></ruby><ruby>通<rt>つう</rt></ruby>」です。"
  },
  {
    "id": 62,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby>におけるタテの<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>のうち、<ruby>経<rt>けい</rt></ruby><ruby>営<rt>えい</rt></ruby><ruby>陣<rt>じん</rt></ruby>や<ruby>上<rt>じょう</rt></ruby><ruby>司<rt>し</rt></ruby>から<ruby>部<rt>ぶ</rt></ruby><ruby>下<rt>か</rt></ruby>や<ruby>現<rt>げん</rt></ruby><ruby>場<rt>じょう</rt></ruby>スタッフへ<ruby>向<rt>こう</rt></ruby>けて<ruby>方<rt>ほう</rt></ruby><ruby>針<rt>しん</rt></ruby>や<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby><ruby>指<rt>し</rt></ruby><ruby>示<rt>じ</rt></ruby>を<ruby>伝<rt>でん</rt></ruby>える<ruby>流<rt>なが</rt></ruby>れを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "トップダウン・コミュニケーション（<ruby>下<rt>か</rt></ruby><ruby>降<rt>こう</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>）",
      "ボトムアップ・コミュニケーション（<ruby>上<rt>じょう</rt></ruby><ruby>昇<rt>しょう</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>）",
      "<ruby>水<rt>すい</rt></ruby><ruby>平<rt>へい</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション",
      "<ruby>対<rt>たい</rt></ruby><ruby>角<rt>かく</rt></ruby><ruby>線<rt>せん</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（トップダウン・コミュニケーション（<ruby>下<rt>か</rt></ruby><ruby>降<rt>こう</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>方<rt>ほう</rt></ruby><ruby>針<rt>しん</rt></ruby>やマニュアルの<ruby>徹<rt>てつ</rt></ruby><ruby>底<rt>てい</rt></ruby>を<ruby>目<rt>もく</rt></ruby><ruby>的<rt>てき</rt></ruby>とします。"
  },
  {
    "id": 63,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>現<rt>げん</rt></ruby><ruby>場<rt>じょう</rt></ruby>のスタッフが<ruby>日<rt>にち</rt></ruby><ruby>常<rt>じょう</rt></ruby><ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby>の<ruby>中<rt>ちゅう</rt></ruby>で<ruby>気<rt>き</rt></ruby>づいた<ruby>利<rt>り</rt></ruby><ruby>用<rt>よう</rt></ruby><ruby>者<rt>しゃ</rt></ruby>の<ruby>変<rt>へん</rt></ruby><ruby>化<rt>か</rt></ruby>、<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby>の<ruby>課<rt>か</rt></ruby><ruby>題<rt>だい</rt></ruby>、<ruby>改<rt>かい</rt></ruby><ruby>善<rt>ぜん</rt></ruby><ruby>提<rt>てい</rt></ruby><ruby>案<rt>あん</rt></ruby>などを<ruby>上<rt>じょう</rt></ruby><ruby>層<rt>そう</rt></ruby><ruby>部<rt>ぶ</rt></ruby>へと<ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>する<ruby>流<rt>なが</rt></ruby>れを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ボトムアップ・コミュニケーション（<ruby>上<rt>じょう</rt></ruby><ruby>昇<rt>しょう</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>）",
      "トップダウン・コミュニケーション",
      "<ruby>水<rt>すい</rt></ruby><ruby>平<rt>へい</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション",
      "インフォーマル・コミュニケーション"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ボトムアップ・コミュニケーション（<ruby>上<rt>じょう</rt></ruby><ruby>昇<rt>しょう</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>現<rt>げん</rt></ruby><ruby>場<rt>じょう</rt></ruby>の<ruby><ruby>声<rt>こえ</rt></ruby><rt>こえ</rt></ruby>を<ruby>吸<rt>す</rt></ruby>い<ruby>上<rt>あ</rt></ruby>げ、<ruby>組<rt>ぐ</rt></ruby><ruby>織<rt>しき</rt></ruby>の<ruby>質<rt>しつ</rt></ruby>の<ruby>向<rt>こう</rt></ruby><ruby>上<rt>じょう</rt></ruby>やリスク<ruby>回<rt>かい</rt></ruby><ruby>避<rt>ひ</rt></ruby>につなげます。"
  },
  {
    "id": 64,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>同<rt>どう</rt></ruby><ruby>僚<rt>りょう</rt></ruby><ruby>同<rt>どう</rt></ruby><ruby>士<rt>し</rt></ruby>や<ruby>他<rt>た</rt></ruby><ruby>職<rt>しょく</rt></ruby><ruby>種<rt>しゅ</rt></ruby>（<ruby>介<rt>かい</rt></ruby><ruby>護<rt>ご</rt></ruby><ruby>職<rt>しょく</rt></ruby>、<ruby>看<rt>かん</rt></ruby><ruby>護<rt>ご</rt></ruby><ruby>職<rt>しょく</rt></ruby>、<ruby>相<rt>そう</rt></ruby><ruby>談<rt>だん</rt></ruby><ruby>員<rt>いん</rt></ruby>、リハビリ<ruby>職<rt>しょく</rt></ruby>など）の<ruby>間<rt>かん</rt></ruby>で、<ruby>対<rt>たい</rt></ruby><ruby>等<rt>とう</rt></ruby>な<ruby>立<rt>りつ</rt></ruby><ruby>場<rt>じょう</rt></ruby>で<ruby>情<rt>じょう</rt></ruby><ruby>報<rt>ほう</rt></ruby>を<ruby>交<rt>こう</rt></ruby><ruby>換<rt>かん</rt></ruby>し<ruby>連<rt>れん</rt></ruby><ruby>携<rt>けい</rt></ruby>を<ruby>図<rt>と</rt></ruby>るコミュニケーションを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>水<rt>すい</rt></ruby><ruby>平<rt>へい</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション（ヨコのコミュニケーション）",
      "<ruby>下<rt>か</rt></ruby><ruby>降<rt>こう</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション",
      "<ruby>権<rt>けん</rt></ruby><ruby>威<rt>い</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション",
      "<ruby>閉<rt>へい</rt></ruby><ruby>鎖<rt>さ</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>水<rt>すい</rt></ruby><ruby>平<rt>へい</rt></ruby><ruby>的<rt>てき</rt></ruby>コミュニケーション（ヨコのコミュニケーション））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。チームケアや<ruby>多<rt>た</rt></ruby><ruby>職<rt>しょく</rt></ruby><ruby>種<rt>しゅ</rt></ruby><ruby>連<rt>れん</rt></ruby><ruby>携<rt>けい</rt></ruby>を<ruby>円<rt>えん</rt></ruby><ruby>滑<rt>かつ</rt></ruby>にする<ruby>要<rt>よう</rt></ruby>です。"
  },
  {
    "id": 65,
    "section": "組織におけるコミュニケーション",
    "stem": "ビジネスや<ruby>福<rt>ふく</rt></ruby><ruby>祉<rt>し</rt></ruby><ruby>現<rt>げん</rt></ruby><ruby>場<rt>じょう</rt></ruby>で<ruby>基<rt>き</rt></ruby><ruby>本<rt>ほん</rt></ruby>とされる「<ruby>報<rt>ほう</rt></ruby>・<ruby>連<rt>れん</rt></ruby>・<ruby>相<rt>そう</rt></ruby>（ほうれんそう）」の「<ruby>相<rt>そう</rt></ruby>」にあたる<ruby>行<rt>ぎょう</rt></ruby><ruby>為<rt>い</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>相<rt>そう</rt></ruby><ruby>談<rt>だん</rt></ruby>（<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>に<ruby>迷<rt>まよ</rt></ruby>った<ruby>時<rt>とき</rt></ruby>や<ruby>困<rt>こま</rt></ruby>った<ruby>時<rt>とき</rt></ruby>に<ruby>上<rt>じょう</rt></ruby><ruby>司<rt>し</rt></ruby>や<ruby>同<rt>どう</rt></ruby><ruby>僚<rt>りょう</rt></ruby>に<ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>を<ruby>求<rt>もと</rt></ruby>め<ruby>知<rt>ち</rt></ruby><ruby>恵<rt>けい</rt></ruby>を<ruby>借<rt>か</rt></ruby>りること）",
      "<ruby>報<rt>ほう</rt></ruby><ruby>告<rt>こく</rt></ruby>（<ruby>頼<rt>たの</rt></ruby>まれた<ruby>仕<rt>し</rt></ruby><ruby>事<rt>ごと</rt></ruby>の<ruby>進<rt>しん</rt></ruby><ruby>捗<rt>ちょく</rt></ruby>や<ruby>結<rt>けつ</rt></ruby><ruby>果<rt>か</rt></ruby>を<ruby>知<rt>し</rt></ruby>らせること）",
      "<ruby>連<rt>れん</rt></ruby><ruby>絡<rt>らく</rt></ruby>（<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby><ruby>上<rt>じょう</rt></ruby>の<ruby>事<rt>ごと</rt></ruby><ruby>実<rt>じっ</rt></ruby>や<ruby>予<rt>よ</rt></ruby><ruby>定<rt>てい</rt></ruby>を<ruby>関<rt>かん</rt></ruby><ruby>係<rt>けい</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>漏<rt>も</rt></ruby>れなく<ruby>伝<rt>でん</rt></ruby>えること）",
      "<ruby>相<rt>あい</rt></ruby><ruby>槌<rt>づち</rt></ruby>（<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby><ruby>話<rt>はなし</rt></ruby><rt>はなし</rt></ruby>を<ruby>黙<rt>もく</rt></ruby>って<ruby>聞<rt>き</rt></ruby>くこと）"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>相<rt>そう</rt></ruby><ruby>談<rt>だん</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>自<rt>じ</rt></ruby><ruby>己<rt>こ</rt></ruby><ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>で<ruby>問<rt>もん</rt></ruby><ruby>題<rt>だい</rt></ruby>を<ruby>抱<rt>かか</rt></ruby>え<ruby>込<rt>こ</rt></ruby>まず、<ruby>事<rt>ごと</rt></ruby><ruby>前<rt>ぜん</rt></ruby>に<ruby>相<rt>そう</rt></ruby><ruby>談<rt>だん</rt></ruby>することでミスや<ruby>事<rt>ごと</rt></ruby><ruby>故<rt>こ</rt></ruby>を<ruby>防<rt>ぼう</rt></ruby>ぎます。"
  },
  {
    "id": 66,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>での<ruby>討<rt>とう</rt></ruby><ruby>議<rt>ぎ</rt></ruby>を<ruby>経<rt>けい</rt></ruby>ることで、<ruby>個<rt>こ</rt></ruby><ruby>人<rt>じん</rt></ruby>の<ruby>当<rt>あて</rt></ruby><ruby>初<rt>しょ</rt></ruby>の<ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>よりも<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>全<rt>ぜん</rt></ruby><ruby>体<rt>たい</rt></ruby>の<ruby>決<rt>けつ</rt></ruby><ruby>定<rt>てい</rt></ruby>がより<ruby>極<rt>きょく</rt></ruby><ruby>端<rt>たん</rt></ruby>な<ruby>方<rt>ほう</rt></ruby><ruby>向<rt>こう</rt></ruby>（リスクの<ruby>高<rt>こう</rt></ruby>い<ruby>方<rt>ほう</rt></ruby><ruby>向<rt>こう</rt></ruby>、または<ruby>過<rt>か</rt></ruby><ruby>度<rt>ど</rt></ruby>に<ruby>安<rt>あん</rt></ruby><ruby>全<rt>ぜん</rt></ruby>な<ruby>方<rt>ほう</rt></ruby><ruby>向<rt>こう</rt></ruby>）へ<ruby>偏<rt>へん</rt></ruby>ってしまう<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>極<rt>きょく</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>化<rt>か</rt></ruby>（<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>分<rt>ぶん</rt></ruby><ruby>極<rt>きょく</rt></ruby><ruby>化<rt>か</rt></ruby>・ポラリゼーション）",
      "ハロー<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby>",
      "<ruby>社<rt>しゃ</rt></ruby><ruby>会<rt>かい</rt></ruby><ruby>的<rt>てき</rt></ruby><ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>",
      "ステレオタイプ"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>極<rt>きょく</rt></ruby><ruby>性<rt>せい</rt></ruby><ruby>化<rt>か</rt></ruby>（<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>分<rt>ぶん</rt></ruby><ruby>極<rt>きょく</rt></ruby><ruby>化<rt>か</rt></ruby>・ポラリゼーション））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。リスキーシフトやコーシャスシフトを<ruby>含<rt>ふく</rt></ruby>みます。"
  },
  {
    "id": 67,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>凝<rt>ぎょう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>性<rt>せい</rt></ruby>の<ruby>高<rt>こう</rt></ruby>い<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby>において、<ruby>反<rt>はん</rt></ruby><ruby>対<rt>たい</rt></ruby><ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>を<ruby>排<rt>はい</rt></ruby><ruby>除<rt>じょ</rt></ruby>し、メンバー<ruby>同<rt>どう</rt></ruby><ruby>士<rt>し</rt></ruby>の<ruby>結<rt>けつ</rt></ruby><ruby>束<rt>そく</rt></ruby>や<ruby>満<rt>まん</rt></ruby><ruby>場<rt>じょう</rt></ruby><ruby>一<rt>いっ</rt></ruby><ruby>致<rt>ち</rt></ruby>を<ruby>優<rt>ゆう</rt></ruby><ruby>先<rt>せん</rt></ruby>するあまり、<ruby>客<rt>きゃっ</rt></ruby><ruby>観<rt>かん</rt></ruby><ruby>的<rt>てき</rt></ruby>・<ruby>合<rt>ごう</rt></ruby><ruby>理<rt>り</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>判<rt>はん</rt></ruby><ruby>断<rt>だん</rt></ruby>が<ruby>損<rt>そん</rt></ruby>なわれて<ruby>致<rt>ち</rt></ruby><ruby>命<rt>めい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>失<rt>しっ</rt></ruby><ruby>敗<rt>はい</rt></ruby>を<ruby>招<rt>まね</rt></ruby>く<ruby>現<rt>げん</rt></ruby><ruby>象<rt>しょう</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>こ</rt></ruby>ぶか、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>浅<rt>せん</rt></ruby><ruby>慮<rt>りょ</rt></ruby>（グループシンク）",
      "<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>凝<rt>ぎょう</rt></ruby><ruby>集<rt>しゅう</rt></ruby><ruby>性<rt>せい</rt></ruby>",
      "ブレインストーミング",
      "アサーション"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>集<rt>しゅう</rt></ruby><ruby>団<rt>だん</rt></ruby><ruby>浅<rt>せん</rt></ruby><ruby>慮<rt>りょ</rt></ruby>（グループシンク））が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ジャニスが<ruby>提<rt>てい</rt></ruby><ruby>唱<rt>しょう</rt></ruby>した<ruby>概<rt>がい</rt></ruby><ruby>念<rt>ねん</rt></ruby>で、<ruby>批<rt>ひ</rt></ruby><ruby>判<rt>はん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>意<rt>い</rt></ruby><ruby>見<rt>けん</rt></ruby>を<ruby>言<rt>げん</rt></ruby>いにくい<ruby>同<rt>どう</rt></ruby><ruby>調<rt>ちょう</rt></ruby><ruby>圧<rt>あつ</rt></ruby><ruby>力<rt>りょく</rt></ruby>が<ruby>原<rt>げん</rt></ruby><ruby>因<rt>いん</rt></ruby>となります。"
  },
  {
    "id": 68,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>自<rt>じ</rt></ruby><ruby>由<rt>ゆう</rt></ruby>なアイデア<ruby>発<rt>はつ</rt></ruby><ruby>想<rt>そう</rt></ruby>を<ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>するブレインストーミングの4<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>に<ruby>含<rt>ふく</rt></ruby>まれないものとして、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "<ruby>批<rt>ひ</rt></ruby><ruby>判<rt>はん</rt></ruby>の<ruby>厳<rt>げん</rt></ruby><ruby>禁<rt>きん</rt></ruby>（<ruby>出<rt>しゅつ</rt></ruby>されたアイデアをその<ruby>場<rt>じょう</rt></ruby>で<ruby>批<rt>ひ</rt></ruby><ruby>判<rt>はん</rt></ruby>・<ruby>否<rt>ひ</rt></ruby><ruby>定<rt>てい</rt></ruby>しない）",
      "<ruby>自<rt>じ</rt></ruby><ruby>由<rt>ゆう</rt></ruby><ruby>奔<rt>ほん</rt></ruby><ruby>放<rt>ぽう</rt></ruby>（<ruby>奇<rt>き</rt></ruby><ruby>抜<rt>ばつ</rt></ruby>で<ruby>斬<rt>ざん</rt></ruby><ruby>新<rt>しん</rt></ruby>なアイデアを<ruby>歓<rt>かん</rt></ruby><ruby>迎<rt>げい</rt></ruby>する）",
      "<ruby>質<rt>しつ</rt></ruby>の<ruby>重<rt>じゅう</rt></ruby><ruby>視<rt>し</rt></ruby>（<ruby>最<rt>さい</rt></ruby><ruby>初<rt>しょ</rt></ruby>から<ruby>完<rt>かん</rt></ruby><ruby>璧<rt>ぺき</rt></ruby>で<ruby>実<rt>じっ</rt></ruby><ruby>現<rt>げん</rt></ruby><ruby>可<rt>か</rt></ruby><ruby>能<rt>のう</rt></ruby>な<ruby>案<rt>あん</rt></ruby>だけに<ruby>絞<rt>しぼ</rt></ruby>る）",
      "<ruby>結<rt>けつ</rt></ruby><ruby>合<rt>ごう</rt></ruby>・<ruby>便<rt>びん</rt></ruby><ruby>乗<rt>じょう</rt></ruby><ruby>発<rt>はっ</rt></ruby><ruby>展<rt>てん</rt></ruby>（<ruby>他<rt>た</rt>人<rt>にん</rt></ruby>のアイデアを<ruby>組<rt>ぐ</rt></ruby>み<ruby>合<rt>ごう</rt></ruby>わせ<ruby>発<rt>はつ</rt></ruby><ruby>展<rt>てん</rt></ruby>させる）"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（<ruby>質<rt>しつ</rt></ruby>の<ruby>重<rt>じゅう</rt></ruby><ruby>視<rt>し</rt></ruby>）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。ブレインストーミングの4<ruby>原<rt>げん</rt></ruby><ruby>則<rt>そく</rt></ruby>は「<ruby>批<rt>ひ</rt></ruby><ruby>判<rt>はん</rt></ruby><ruby>厳<rt>げん</rt></ruby><ruby>禁<rt>きん</rt></ruby>」「<ruby>自<rt>じ</rt></ruby><ruby>由<rt>ゆう</rt></ruby><ruby>奔<rt>ほん</rt></ruby><ruby>放<rt>ぽう</rt></ruby>」「<ruby>質<rt>しつ</rt></ruby>より<ruby>量<rt>りょう</rt></ruby>の<ruby>重<rt>じゅう</rt></ruby><ruby>視<rt>し</rt></ruby>」「<ruby>結<rt>けつ</rt></ruby><ruby>合<rt>ごう</rt></ruby><ruby>発<rt>はつ</rt></ruby><ruby>展<rt>てん</rt></ruby>」です。"
  },
  {
    "id": 69,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>職<rt>しょく</rt></ruby><ruby>場<rt>じょう</rt></ruby><ruby>内<rt>ない</rt></ruby><ruby>訓<rt>くん</rt></ruby><ruby>練<rt>れん</rt></ruby>（OJT）において、<ruby>先<rt>せん</rt></ruby><ruby>輩<rt>ぱい</rt></ruby>が<ruby>後<rt>こう</rt></ruby><ruby>輩<rt>ぱい</rt></ruby>に<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby>の<ruby>手<rt>て</rt></ruby><ruby>順<rt>じゅん</rt></ruby>や<ruby>必<rt>ひつ</rt></ruby><ruby>要<rt>よう</rt></ruby>な<ruby>知<rt>ち</rt></ruby><ruby>識<rt>しき</rt></ruby>・<ruby>技<rt>ぎ</rt></ruby><ruby>術<rt>じゅつ</rt></ruby>を<ruby>具<rt>ぐ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>に<ruby>示<rt>しめ</rt></ruby>しながら「<ruby>教<rt>おし</rt></ruby>えて<ruby>習<rt>しゅう</rt></ruby><ruby>得<rt>とく</rt></ruby>させる」<ruby>手<rt>て</rt></ruby><ruby>法<rt>ほう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "ティーチング",
      "コーチング",
      "カウンセリング",
      "アセスメント"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ティーチング）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>新<rt>しん</rt></ruby><ruby>任<rt>にん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>や<ruby>未<rt>み</rt></ruby><ruby>経<rt>けい</rt></ruby><ruby>験<rt>けん</rt></ruby><ruby>者<rt>しゃ</rt></ruby>に<ruby>基<rt>き</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>業<rt>ぎょう</rt></ruby><ruby>務<rt>む</rt></ruby>やルールを<ruby>的<rt>てき</rt></ruby><ruby>確<rt>かく</rt></ruby>に<ruby>伝<rt>でん</rt></ruby><ruby>達<rt>たつ</rt></ruby>・<ruby>教<rt>きょう</rt></ruby><ruby>育<rt>いく</rt></ruby>する<ruby>際<rt>さい</rt></ruby>に<ruby>効<rt>こう</rt></ruby><ruby>果<rt>か</rt></ruby><ruby>的<rt>てき</rt></ruby>です。"
  },
  {
    "id": 70,
    "section": "組織におけるコミュニケーション",
    "stem": "<ruby>指<rt>し</rt></ruby><ruby>示<rt>じ</rt></ruby><ruby>命<rt>めい</rt></ruby><ruby>令<rt>れい</rt></ruby>ではなく、<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>に<ruby>質<rt>しつ</rt></ruby><ruby>問<rt>もん</rt></ruby>を<ruby>投<rt>な</rt></ruby>げかけたり<ruby>傾<rt>けい</rt></ruby><ruby>聴<rt>ちょう</rt></ruby>したりすることで、<ruby>相<rt>あい</rt>手<rt>て</rt></ruby><ruby>自<rt>じ</rt></ruby><ruby>身<rt>しん</rt></ruby>が<ruby>持<rt>じ</rt></ruby>つ<ruby>潜<rt>せん</rt></ruby><ruby>在<rt>ざい</rt></ruby><ruby>能<rt>のう</rt></ruby><ruby>力<rt>りょく</rt></ruby>やアイデアを<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>だ</rt></ruby>し、<ruby>じ<rt>じ</rt></ruby><ruby>はつ<rt>はつ</rt></ruby><ruby>てき<rt>てき</rt></ruby>な<ruby>行<rt>ぎょう</rt></ruby><ruby>動<rt>どう</rt></ruby>を<ruby>促<rt>そく</rt></ruby><ruby>進<rt>しん</rt></ruby>する<ruby>指<rt>し</rt></ruby><ruby>導<rt>どう</rt></ruby><ruby>手<rt>て</rt></ruby><ruby>法<rt>ほう</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "コーチング",
      "ティーチング",
      "パターナリズム",
      "トップダウン"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（コーチング）が<ruby>正<rt>せい</rt>解<rt>かい</rt></ruby>です。<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>主<rt>しゅ</rt></ruby><ruby>体<rt>たい</rt></ruby><ruby>的<rt>てき</rt></ruby>な<ruby>気<rt>き</rt></ruby>づきや<ruby>成<rt>せい</rt></ruby><ruby>長<rt>ちょう</rt></ruby>を<ruby>支<rt>し</rt></ruby><ruby>援<rt>えん</rt></ruby>するコミュニケーション<ruby>技<rt>ぎ</rt></ruby><ruby>法<rt>ほう</rt></ruby>です。"
  }
]

# 単元定義
SECTIONS = {
    "all": "全70問を一括表示（模擬試験モード）",
    "sec1": "第1単元: 発達心理学からみた人間関係（問1〜12）",
    "sec2": "第2単元: 社会心理学からみた人間関係（問13〜24）",
    "sec3": "第3単元: ストレスとコーピング（問25〜36）",
    "sec4": "第4単元: 対人関係におけるコミュニケーション（問37〜48）",
    "sec5": "第5単元: 対人援助関係とバイステックの原則（問49〜60）",
    "sec6": "第6単元: 組織におけるコミュニケーション（問61〜70）"
}

# 提出ファイル名・レポート用識別記号マッピング
TAG_MAP = {
    "all": "[ALL_全70問]",
    "sec1": "[B1_問01-12]",
    "sec2": "[B2_問13-24]",
    "sec3": "[B3_問25-36]",
    "sec4": "[B4_問37-48]",
    "sec5": "[B5_問49-60]",
    "sec6": "[B6_問61-70]"
}

# 2. 出題ナビゲーション
st.markdown("<div class='nav-box'>", unsafe_allow_html=True)
st.markdown("### 🎯 出題モードの選択")
c_nav1, c_nav2 = st.columns([2.5, 1.5])
with c_nav1:
    view_mode = st.selectbox(
        "取り組み方を選択してください（切り替えても回答内容は保持されます）:",
        options=list(SECTIONS.keys()),
        format_func=lambda x: SECTIONS[x]
    )
with c_nav2:
    show_ruby = st.checkbox("ふりがな（ルビ）を表示する", value=True)
st.markdown("</div>", unsafe_allow_html=True)

# 表示対象の問題をフィルタリング
if view_mode == "all":
    display_questions = QUESTIONS
elif view_mode == "sec1":
    display_questions = QUESTIONS[0:12]
elif view_mode == "sec2":
    display_questions = QUESTIONS[12:24]
elif view_mode == "sec3":
    display_questions = QUESTIONS[24:36]
elif view_mode == "sec4":
    display_questions = QUESTIONS[36:48]
elif view_mode == "sec5":
    display_questions = QUESTIONS[48:60]
else:
    display_questions = QUESTIONS[60:70]

# セッション状態での回答管理
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 解答進捗状況の表示
answered_count = len([k for k, v in st.session_state.answers.items() if v is not None])
progress_pct = int((answered_count / 70) * 100)
st.progress(answered_count / 70)
st.caption(f"現在の全体の解答状況: **{answered_count} / 70 問 解答済み** ({progress_pct}%)")

st.markdown(f"### ✍️ 問題一覧（{SECTIONS[view_mode]}：{len(display_questions)} 問）")

# 問題のレンダリング
for q in display_questions:
    q_id = q["id"]
    stem_txt = q["stem"] if show_ruby else remove_ruby(q["stem"])
    
    st.markdown("<div class='q-card'>", unsafe_allow_html=True)
    st.markdown(f"<span class='tag'>{q['section']}</span>", unsafe_allow_html=True)
    st.markdown(f"<div class='q-title'>問 {q_id}. {stem_txt}</div>", unsafe_allow_html=True)
    
    for opt_idx, opt in enumerate(q["options"]):
        opt_txt = opt if show_ruby else remove_ruby(opt)
        st.markdown(f"<div class='opt-item'>{opt_idx + 1}. {opt_txt}</div>", unsafe_allow_html=True)
        
    current_val = st.session_state.answers.get(q_id, None)
    selected = st.radio(
        label=f"問 {q_id} の解答を選択:",
        options=[1, 2, 3, 4],
        index=None if current_val is None else current_val - 1,
        horizontal=True,
        key=f"radio_q_{q_id}"
    )
    if selected is not None:
        st.session_state.answers[q_id] = selected
    st.markdown("</div>", unsafe_allow_html=True)

# 採点と提出
st.markdown("---")
current_tag = TAG_MAP[view_mode]
current_range_title = SECTIONS[view_mode]

button_label = "📊 全70問を採点して提出用テキストを作成する" if view_mode == "all" else f"📊 {current_range_title}（{len(display_questions)}問）を採点して提出用テキストを作成する"

if st.button(button_label, type="primary", use_container_width=True):
    if not s_class.strip() or not s_id.strip() or not s_name.strip():
        st.error("⚠️ 最上部の「クラス名」「学籍番号」「名前」をすべて入力してください。")
    else:
        # 現在の対象範囲に対する採点
        score = 0
        unanswered = 0
        detail_lines = []
        
        target_scope = QUESTIONS if view_mode == "all" else display_questions
        
        for q in target_scope:
            q_id = q["id"]
            u_ans = st.session_state.answers.get(q_id, None)
            is_correct = (u_ans == q["answer"])
            
            if u_ans is None:
                unanswered += 1
                status_str = "未回答 ×"
                ans_str = "未"
            elif is_correct:
                score += 1
                status_str = "正解 ○"
                ans_str = str(u_ans)
            else:
                status_str = "不正解 ×"
                ans_str = str(u_ans)
                
            detail_lines.append(f"問{q_id:02d} [{q['section']}]: あなたの回答 [{ans_str}] / 正解 [{q['answer']}] -> {status_str}")
            
        total_q = len(target_scope)
        pct = round((score / total_q) * 100)
        
        st.markdown(f"""
        <div class='score-badge'>
          <h3 style='margin:0 0 8px 0; color:#1e3a8a;'>採点結果（{current_range_title}）</h3>
          <div style='font-size: 2.2rem; font-weight: bold; color: #1e3a8a;'>{score} / {total_q} 点</div>
          <div style='font-size: 1.1rem; color: #475569;'>正答率: <strong>{pct}%</strong> （全体進捗: {answered_count} / 70問 完了）</div>
        </div>
        """, unsafe_allow_html=True)
        
        if unanswered > 0:
            st.warning(f"※ 対象範囲内に未回答の問題が {unanswered} 問あります。")
            
        # 解説アコーディオン（arrow_rightの文字化け・重なりをCSSで完全防止）
        with st.expander("📖 各問題の解説を確認する"):
            for q in target_scope:
                st.markdown(f"**問 {q['id']}. [{q['section']}]**")
                exp_txt = q['exp'] if show_ruby else remove_ruby(q['exp'])
                st.markdown(f"・{exp_txt}", unsafe_allow_html=True)
                st.markdown("---")
                
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y年%m月%d日 %H:%M:%S")
        auth_raw = f"{s_class}_{s_id}_{s_name}_{score}_{total_q}_{current_tag}_{timestamp}"
        auth_code = f"VER-B70-{current_tag}-{abs(hash(auth_raw)):X}-{now.strftime('%f')}"
        
        details_block = "\n".join(detail_lines)
        report_text = (
            "==================================================\n"
            "【課題提出用 成績レポート】\n"
            "教科・単元　：人間関係とコミュニケーション b後半\n"
            f"実施範囲　　：{current_range_title} 【識別記号: {current_tag}】\n"
            f"クラス名（組）：{s_class.strip()}\n"
            f"学籍番号　　：{s_id.strip()}\n"
            f"名前（氏名）：{s_name.strip()}\n"
            f"実施日時　　：{timestamp}\n"
            f"得点　　　　：{score} / {total_q} 点（正答率 {pct}%）\n"
            f"全体進捗　　：{answered_count} / 70 問 解答済み\n"
            f"改ざん防止用認証コード：{auth_code}\n"
            "==================================================\n"
            f"【{current_tag} 解答記録】\n"
            f"{details_block}\n"
            "==================================================\n"
            "以上を提出内容として記録しました。\n"
        )
        
        st.markdown("### 📥 課題の提出方法（2通りの方法が使えます）")
        st.info(f"""
**【提出方法A：テキストファイルをダウンロードして提出】**
1. すぐ下の **「📥 提出用テキストファイル（.txt）をダウンロード」** ボタンを押してファイルを端末に保存します。
2. Google Classroom の該当課題ページで **「ファイルの添付」** から保存したテキストファイルを提出してください。
※ファイル名に選択した範囲の識別記号 **{current_tag}** が自動付与されています。

**【提出方法B：テキストをコピー＆ペーストして提出】**
1. さらに下にある **「📋 コピーペースト用提出テキスト」** の枠内をクリックし、すべて選択（Ctrl+A / ⌘+A）してコピーします。
2. Google Classroom の回答欄・コメント欄にそのまま貼り付けて提出してください。
""")
        
        file_name = f"提出用_人間関係とコミュニケーションb後半_{current_tag}_{s_class.strip()}_{s_id.strip()}_{s_name.strip()}.txt"
        st.download_button(
            label="📥 提出用テキストファイル（.txt）をダウンロード",
            data=report_text,
            file_name=file_name,
            mime="text/plain",
            use_container_width=True
        )
        
        st.markdown("<div style='margin-top:14px;'></div>", unsafe_allow_html=True)
        
        st.text_area(
            label="📋 コピーペースト用提出テキスト（枠内をすべて選択・コピーしてGoogle Classroomに貼り付け）:",
            value=report_text,
            height=280
        )
        
        st.markdown("[Google Classroom を開く ↗](https://classroom.google.com)", unsafe_allow_html=True)
