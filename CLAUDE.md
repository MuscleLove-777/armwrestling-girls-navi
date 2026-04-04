# アームレスリング女子ナビ - 更新ガイド

## サイト概要
- **サイト名**: アームレスリング女子ナビ
- **テーマ**: アームレスリング・腕相撲で活躍する女子選手の情報を日本語で毎日発信
- **運営**: MuscleLove
- **URL**: https://musclelove-777.github.io/armwrestling-girls-navi/
- **X**: @MuscleGirlLove7
- **Patreon**: https://www.patreon.com/MuscleLove

## 選手リスト（記事ネタ用）

### 日本選手
| 選手名 | 階級 | 主な実績 |
|--------|------|----------|
| 竹中 絢音 | 55kg級 | 2023 WAF世界選手権優勝、全日本男子の部優勝 |
| 芝岡 美津穂 | 50kg以下級 | 第31回JAWA全日本選手権優勝、アジア代表 |
| 北條 葵 | ジュニア | 全日本選手権出場の高校生選手、両親がアームレスラー |
| 市川 志津子 | 63kg級(マスターズ) | 2023年世界大会60歳以上63kg級右腕で世界王者 |
| 山田 よう子 | 50kg級 | 2005年WAF世界選手権で日本人女性初の世界王者 |

### 海外選手
| 選手名 | 国 | 主な実績 |
|--------|-----|----------|
| ガブリエラ・ヴァスコンセロス | ブラジル | WAFシニア28冠+ジュニア6冠=計34冠、「鉄の天使」 |
| バルボラ・バイチョヴァ | チェコ | EvW右腕ヘビー級世界タイトル、ヴァスコンセロスに勝利 |
| イリーナ・グラディシェワ | ロシア | WAF世界選手権複数回優勝 |
| サラ・バックマン | スウェーデン | 元世界王者、若くして複数タイトル獲得 |

## 記事カテゴリー
1. **選手紹介** - 国内外の女子アームレスリング選手のプロフィール・インタビュー
2. **大会情報** - JAWA全日本、WAF/IFA世界選手権、アジア大会等の速報・展望
3. **テクニック解説** - トップロール、フック、プレス等の技術解説
4. **トレーニング** - アームレスリングに必要な筋トレ・練習法
5. **コラム** - 女子アームレスリングの歴史、文化、魅力

## 記事テンプレート

### ファイル命名規則
`articles/YYYY-MM-DD-slug-name.html`

### 記事HTMLテンプレート
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【カテゴリ】タイトル | アームレスリング女子ナビ</title>
  <meta name="description" content="記事の要約（120文字以内）">
  <meta property="og:title" content="タイトル">
  <meta property="og:description" content="記事の要約">
  <meta property="og:image" content="https://images.unsplash.com/photo-XXXXX?w=1200&h=630&fit=crop">
  <link rel="canonical" href="https://musclelove-777.github.io/armwrestling-girls-navi/articles/YYYY-MM-DD-slug.html">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
  <!-- ダークテーマCSS（既存記事からコピー） -->
</head>
<body>
  <!-- header: ロゴ + ナビ -->
  <!-- article-hero: 背景画像 + 日付 + タイトル -->
  <!-- content: 本文（h2見出し + p段落） -->
  <!-- footer -->
</body>
</html>
```

### Unsplash画像の使い方
- フォーマット: `https://images.unsplash.com/photo-XXXXX?w=幅&h=高さ&fit=crop`
- サムネイル: w=600&h=300
- ヒーロー: w=1400&h=700
- OGP: w=1200&h=630
- 使える検索ワード: arm wrestling, strength, fitness, muscle, training, gym, competition, power

## 更新ルール

### 毎日の更新フロー
1. **WebSearchでリサーチ**: 「アームレスリング 女子」「arm wrestling women」等で最新ニュースを検索
2. **記事3本生成**: 選手紹介、大会情報、テクニック/トレーニングから各1本以上
3. **articles/ に保存**: 命名規則に従ってHTMLファイルを作成
4. **index.html更新**: 最新記事セクションの3記事を差し替え（古い記事リンクは残す）
5. **sitemap.xml更新**: 新しい記事URLを追加
6. **git commit & push**: 変更をコミットしてプッシュ

### コンテンツ品質ガイドライン
- 1記事あたり800〜1500文字（日本語）
- SEOを意識したタイトル（【カテゴリ】で始める）
- 必ずUnsplash画像をサムネイル・ヒーローに使用
- 選手名は漢字（ふりがな）で統一
- 海外選手はカタカナ表記
- 事実に基づいた情報のみ記載（推測は推測と明記）
- 大会結果は公式ソース（JAWA, WAF, IFA）を参照

### 関連リンク
- JAWA公式: https://jawa-armwrestling.org/
- AJAF公式: https://ajaf.jp/
- WAF公式: http://www.waf-armwrestling.com/
- IFA公式: https://armsportfederation.com/
- EvW Sports: https://evwsports.com/
