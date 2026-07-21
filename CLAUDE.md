# アームレスリング女子ナビ - 更新ガイド

## サイト概要
- **サイト名**: アームレスリング女子ナビ
- **テーマ**: アームレスリング・腕相撲で活躍する女子選手の情報を日本語で毎日発信
- **運営**: MuscleLove
- **URL**: https://musclelove-777.github.io/armwrestling-girls-navi/
- **X**: @MuscleGirlLove7
- **Patreon**: https://www.patreon.com/MuscleLove

## 掲載対象（ロスター）
記事対象の選手リストは必ず `references/roster.md` を読んで参照すること。リストの追加・更新もそのファイルに対して行う。

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
<!-- ML_PROMO_CARD_START -->
<section style="max-width:800px;margin:32px auto;padding:0 20px;">
  <div style="background:#111827;border:1px solid rgba(255,255,255,0.14);border-radius:10px;padding:24px;text-align:center;">
    <p style="margin:0 0 6px;color:#f0f0f5;font-weight:800;">MuscleLove 公式</p>
    <p style="margin:0 0 14px;color:#9ca3af;font-size:0.9rem;">最新情報・限定コンテンツはこちら</p>
    <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;">
      <a href="https://x.com/MuscleGirlLove7" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#1d9bf0;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">X @MuscleGirlLove7</a>
      <a href="https://www.patreon.com/MuscleLove" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#ff424d;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">Patreon 限定コンテンツ</a>
      <a href="https://musclelove-games.vercel.app/?utm_source=blog&amp;utm_medium=promo_card&amp;utm_campaign=armwrestling-girls-navi" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#22c55e;color:#0b1220;border-radius:6px;font-weight:800;text-decoration:none;">🎮 無料ゲーム95本</a>
    </div>
  </div>
</section>
<!-- ML_PROMO_CARD_END -->

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

## 広告カード必須ルール
- 全記事とindex.htmlのフッター直前に MuscleLove広告カード（ML_PROMO_CARDマーカー）を必ず含める（テンプレのカードHTML参照）。広告カードにはX / Patreon / ゲームポータルの3導線を必ず入れる。
