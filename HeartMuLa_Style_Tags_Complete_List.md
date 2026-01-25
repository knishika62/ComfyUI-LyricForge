# HeartMuLa スタイルタグ カテゴリ別完全一覧

HeartMuLaの技術文書と公式ドキュメントに基づく、包括的なスタイルタグ一覧です。

## 目次

- [概要](#概要)
- [タグの基本ルール](#タグの基本ルール)
- [1. 構造タグ](#1-構造タグ-structural-tags)
- [2. ジャンルタグ](#2-ジャンルタグ-genre-tags)
- [3. ムード・雰囲気タグ](#3-ムード雰囲気タグ-mood--atmosphere-tags)
- [4. ボーカルタグ](#4-ボーカルタグ-vocal-tags)
- [5. 楽器・制作タグ](#5-楽器制作タグ-instrumentation--production-tags)
- [6. テンポタグ](#6-テンポタグ-tempo-tags)
- [使用例](#使用例)
- [タグ使用のコツ](#タグ使用のコツ)
- [参考資料](#参考資料)

## 概要

HeartMuLaは、歌詞とタグに基づいて音楽を生成する音楽基盤モデルファミリーです。このドキュメントでは、HeartMuLaでサポートされているすべてのスタイルタグをカテゴリ別に整理しています。

- **開発**: 北京大学（Peking University）他
- **論文**: [HeartMuLa: A Family of Open Sourced Music Foundation Models](https://arxiv.org/abs/2601.10547)
- **公式サイト**: https://heartmula.github.io/
- **GitHub**: https://github.com/HeartMuLa/heartlib
- **対応言語**: 英語、中国語、日本語、韓国語、スペイン語

## タグの基本ルール

1. **カンマ区切り、スペースなし**: タグは必ずカンマで区切り、スペースを入れません
   ```
   正: piano,happy,wedding,synthesizer,romantic
   誤: piano, happy, wedding, synthesizer, romantic
   ```

2. **アンダースコアの保持**: アンダースコアを含むタグはそのまま使用
   ```
   例: male_vocal, very_fast, electric_guitar
   ```

3. **複数カテゴリの組み合わせ可能**: ジャンル、ムード、楽器などを自由に組み合わせられます

4. **適度な数を推奨**: 一般的に5〜8個のタグが効果的です

5. **意味的整合**: HeartMuLaはHeartCLAPモデルによる意味的整合を重視しているため、自然言語での記述も理解可能

## 1. 構造タグ (Structural Tags)

楽曲の論理的な構成を制御するタグ。通常は歌詞内に配置します。

| タグ | 説明 | 推奨使用例 |
|------|------|-----------|
| `[Intro]` | イントロ、通常は楽器のみまたは最小限のボーカル | `[Intro: Piano]` |
| `[Verse]` | ヴァース、ストーリーを語る部分、落ち着いたリズム | `[Verse 1]`, `[Verse 2]` |
| `[Chorus]` | コーラス、曲のクライマックス、最も強いメロディ | `[Chorus: Powerful]` |
| `[Bridge]` | ブリッジ、コーラスとヴァースをつなぐ転換部分 | `[Bridge: Transition]` |
| `[Interlude]` | 間奏、純粋な楽器セクション | `[Interlude: Guitar Solo]` |
| `[Hook]` | フック、短くキャッチーなメロディ | コーラスの前後に配置 |
| `[Outro]` | アウトロ、曲の終わり、通常フェードアウト | `[Outro: Fade out]` |
| `[Solo]` | ソロパート、楽器の独奏 | `[Solo]` (Guitar solo) |

## 2. ジャンルタグ (Genre Tags)

HeartMuLaは主流ジャンルを幅広くサポートし、特に中国・日本・韓国（CJK）市場向けのポピュラースタイルを強化しています。

### ポップ系
- `pop` - ポップミュージック
- `Mandopop` - 中国ポップ
- `J-Pop` - 日本ポップ
- `K-Pop` - 韓国ポップ
- `Synthpop` - シンセポップ
- `City Pop` - シティポップ
- `ballad` - バラード

### ロック系
- `rock` - ロック
- `soft rock` - ソフトロック
- `punk` - パンク
- `alternative rock` - オルタナティブロック
- `heavy metal` - ヘヴィメタル

### ジャズ系
- `jazz` - ジャズ
- `traditional jazz` - トラディショナルジャズ
- `modern jazz` - モダンジャズ
- `fusion jazz` - フュージョンジャズ

### クラシック系
- `classical` - クラシック
- `baroque` - バロック
- `romanticism` - ロマン主義
- `orchestral` - オーケストラ

### エレクトロニック系
- `electronic` - エレクトロニック
- `EDM` - エレクトロニック・ダンス・ミュージック
- `house` - ハウス
- `techno` - テクノ
- `trance` - トランス
- `lo-fi` - ローファイ
- `ambient` - アンビエント

### フォーク系
- `folk` - フォーク
- `traditional folk` - トラディショナルフォーク
- `modern folk` - モダンフォーク
- `country folk` - カントリーフォーク

### ヒップホップ系
- `hip-hop` - ヒップホップ
- `rap` - ラップ
- `trap` - トラップ
- `r&b` / `R&B` - リズム・アンド・ブルース

### その他ジャンル
- `blues` - ブルース
  - `traditional blues` - トラディショナルブルース
  - `modern blues` - モダンブルース
- `reggae` - レゲエ
  - `traditional reggae` - トラディショナルレゲエ
  - `modern reggae` - モダンレゲエ
- `country` - カントリー
  - `traditional country` - トラディショナルカントリー
  - `modern country` - モダンカントリー

## 3. ムード・雰囲気タグ (Mood & Atmosphere Tags)

これらのタグは音楽の感情的なトーンを決定します（HeartCLAPの意味空間を通じて制御）。

### 感情系
- `happy` - 幸せ、ポジティブ（cheerful、joyful、excited）
- `sad` - 悲しい、ネガティブ（melancholy、sorrowful、painful）
- `romantic` - ロマンティック、温かく甘い（warm、sweet、affectionate）
- `energetic` - エネルギッシュ、ダイナミック（dynamic、passionate、powerful）
- `calm` - 穏やか、平和（peaceful、serene、relaxed）
- `melancholic` - 憂鬱、内省的（contemplative、nostalgic、sentimental）
- `angry` - 怒り、激しい（intense、irritable、rebellious）
- `hopeful` - 希望に満ちた、前向き（positive、upward、bright）
- `lonely` - 孤独、孤立（helpless、isolated）

### 雰囲気系
- `mysterious` - 神秘的（fantasy、unknown、eerie）
- `nostalgic` - ノスタルジック（recollection、retro、classic）
- `upbeat` - 陽気、活気（cheerful、lively、positive）
- `uplifting` - 高揚感、インスピレーション（inspiring、motivating、positive）
- `peaceful` - 平和、静か（tranquil、peaceful、calm）
- `depressing` - 憂鬱、暗い（gloomy、depressed、oppressive）
- `aggressive` - 攻撃的、激しい（intense、combative、aggressive）

### 空間・環境系
- `ambience` - アンビエンス、環境的（immersive、environmental、spatial）
- `spacey` - 宇宙的（cosmic、spatial、sci-fi）
- `dreamy` - 夢幻的（dreamy、hazy）
- `ethereal` - 超越的（ethereal、transcendental）
- `cinematic` - 映画的（epic、dramatic、emotionally rich）
- `cyberpunk` - サイバーパンク（futuristic、technological、dark）
- `dark` - ダーク（mysterious、oppressive、horror）
- `bright` - 明るい（cheerful、positive、sunny）

### シーン系
- `wedding` - 結婚式（romantic、warm、solemn）
- `healing` - ヒーリング（warm、soothing、comforting）
- `party` - パーティー（dynamic、lively、cheerful）
- `nature` - 自然（peaceful、fresh、harmonious）
- `urban` - 都会的（modern、bustling、fast-paced）
- `cafe` - カフェ

## 4. ボーカルタグ (Vocal Tags)

HeartMuLaの強力な多言語機能により、ボーカルコントロールは非常に精密です。

### 基本ボーカル
- `male vocal` - 男性ボーカル（deep、magnetic、powerful）
- `female vocal` - 女性ボーカル（high-pitched、sweet、gentle）
- `boy voice` / `girl voice` - 子供の声（innocent、pure、crisp）
- `duet` - デュエット
- `choir` - 合唱
- `instrumental` - インストゥルメンタル（ボーカルなし）

### ボーカルスタイル
- `whisper` - ささやき（soft、mysterious、intimate）
- `powerful` - パワフル（high-pitched、passionate、impressive）
- `airy` - 軽やか（ethereal、floating、fresh）
- `raspy` - かすれた（rough、weathered、textured）
- `smooth` - スムーズ（fluent、gentle、elegant）
- `energetic` - エネルギッシュ（dynamic、passionate、powerful）
- `emotional` - 感情的（affectionate、sincere、touching）
- `harmonic` - ハーモニック（harmonious、multi-layered、rich）
- `breathy` - 息づかい（soft、delicate）
- `sweet` - 甘い（gentle、cute、sweet）
- `husky` - ハスキー（deep、rough、magnetic）

### ボーカルテクニック
- `vibrato` - ビブラート（vibrato、fluctuation、expressive）
- `falsetto` - ファルセット（high-pitched、falsetto、ethereal）
- `syllabic` - シラビック（clear、accurate、powerful）
- `rap-singing` - ラップシンギング（rap、rhythm、fluent）

## 5. 楽器・制作タグ (Instrumentation & Production Tags)

特定の楽器をリード楽器として明示的に指定できます。

### 鍵盤楽器
- `piano` - ピアノ（classical piano、jazz piano、pop piano）
- `grand piano` - グランドピアノ（classical grand piano、concert piano）
- `electric piano` - エレクトリックピアノ（electronic piano、synthetic piano）
- `synthesizer` / `synth` - シンセサイザー（analog synthesizer、digital synthesizer）
- `keyboard` - キーボード

### 弦楽器
- `guitar` - ギター（acoustic guitar、electric guitar、classical guitar）
- `acoustic guitar` - アコースティックギター（folk guitar、classical guitar）
- `electric guitar` - エレクトリックギター（rock guitar、jazz guitar）
- `violin` - バイオリン（classical violin、electronic violin）
- `cello` - チェロ（classical cello、electronic cello）
- `bass` - ベース（electric bass、acoustic bass）
- `strings` - 弦楽器セクション

### パーカッション
- `drums` - ドラム（drum kit、electronic drums、percussion）
- `electronic drums` - エレクトロニックドラム（electronic drum kit、sampled drums）
- `drum machine` - ドラムマシン
- `percussion` - パーカッション（hand drums、shakers、tambourines）

### 管楽器
- `trumpet` - トランペット（jazz trumpet、classical trumpet）
- `saxophone` - サックス（jazz saxophone、pop saxophone）
- `flute` - フルート（classical flute、jazz flute）

### 制作・音質
- `high fidelity` - 高忠実度（high-quality、clear、detailed）
- `studio recording` - スタジオレコーディング（professional、clear、balanced）
- `reverb` - リバーブ（spatial、echo、atmospheric）
- `compressed` - 圧縮（compact、powerful、balanced）

## 6. テンポタグ (Tempo Tags)

音楽の速度とリズムを記述するタグ。

| タグ | 説明 | BPM目安 |
|------|------|---------|
| `fast` | 速い | 120-180 BPM |
| `slow` | 遅い | 60-90 BPM |
| `upbeat` | 陽気で活発 | 100-140 BPM |
| `relaxed` | リラックス | 70-100 BPM |
| `moderate` / `medium` | 中程度 | 90-120 BPM |
| `very_fast` | 非常に速い | 180+ BPM |
| `very_slow` | 非常に遅い | 60- BPM |

## 使用例

### 例1: ポップソング
```
female_vocal,pop,upbeat,happy,electronic,synthesizer,drums
```

### 例2: ロックソング
```
male_vocal,rock,energetic,fast,guitar,drums,bass
```

### 例3: アンビエント音楽
```
atmospheric,calm,electronic,synthesizer,slow,healing
```

### 例4: ジャズソング
```
jazz,smooth,romantic,saxophone,piano,moderate
```

### 例5: ウェディングソング
```
piano,happy,wedding,romantic,strings,female_vocal
```

### 例6: エレクトロニック・ダンス
```
EDM,energetic,fast,synthesizer,electronic_drums,party
```

### 例7: メランコリックなインディーロック
```
indie,rock,male_vocal,melancholic,slow,acoustic_guitar
```

### 例8: エナジェティックなロック
```
rock,electric_guitar,energetic,drums,powerful,driving
```

### 例9: ジャズ・インストゥルメンタル
```
jazz,piano,instrumental,calm,slow
```

### 例10: カフェでのアコースティック
```
warm,reflection,pop,cafe,acoustic_guitar,female_vocal
```

## タグ使用のコツ

1. **タグの組み合わせ**: 複数のタグを同時に使用して、音楽の特徴をより正確に記述できます

2. **優先順位**: 最も重要なタグを最初に配置します

3. **具体性**: 過度に広範なタグよりも、具体的なタグを使用します
   - 良い例: `jazz,saxophone,smooth`
   - 悪い例: `music,sound,audio`

4. **一貫性**: 同じ曲内でタグスタイルの一貫性を保ちます

5. **実験**: さまざまなタグの組み合わせを試して、新しい音楽スタイルを探求します

6. **適度な数**: 一般的に**5〜8個のタグ**が適切です。多すぎると効果が薄れる可能性があります

7. **矛盾を避ける**: 
   - 避けるべき組み合わせ: `fast,slow`
   - 避けるべき組み合わせ: `happy,sad`

8. **構造タグは歌詞内に**: `[Verse]`、`[Chorus]`などの構造タグは歌詞ファイル内に配置します

9. **スタイルタグは別ファイル**: 音楽スタイルを記述するタグは専用のタグファイル（tags.txt）に記載します

## 参考資料

### 公式リソース
- **論文**: Yang, D., et al. (2026). HeartMuLa: A Family of Open Sourced Music Foundation Models. arXiv:2601.10547
  - URL: https://arxiv.org/abs/2601.10547
  - HTML版: https://arxiv.org/html/2601.10547v1

- **公式ウェブサイト**: https://heartmula.github.io/

- **GitHubリポジトリ**: https://github.com/HeartMuLa/heartlib

- **Hugging Face**: 
  - モデル: https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B
  - デモ: https://huggingface.co/spaces/mrfakename/HeartMuLa

### コミュニティリソース
- **ComfyUIカスタムノード**: https://github.com/filliptm/ComfyUI_FL-HeartMuLa
- **MLXポート（Apple Silicon）**: https://github.com/Acelogic/heartlib-mlx

### 詳細ドキュメント
- **LM Downloader導入ガイド**: https://daiyl.com/lm-downloader-heartmula.html
  - タグシステムの詳細解説を含む

### 連絡先
- **Email**: heartmula.ai@gmail.com
- **Discord**: 公式リポジトリ参照

---

## ライセンス

HeartMuLaプロジェクトは**Apache 2.0ライセンス**の下で公開されています。

- 非商用の研究・教育目的での使用のみ
- 商用利用は厳格に禁止
- 生成されたコンテンツが第三者の著作権を侵害しないことを確認する責任はユーザーにあります

---

## 更新履歴

- **2026年1月23日**: HeartMuLa-RL-oss-3B-20260123リリース - 強化学習により、スタイルとタグのより精密な制御を実現
- **2026年1月14日**: HeartMuLa-oss-3B、HeartCodec-oss、HeartTranscriptor-oss 初回リリース
- **2026年1月**: Apache 2.0ライセンスに更新

---

## 貢献

このドキュメントは公式ドキュメント、技術論文、コミュニティリソースに基づいて作成されています。

誤りや追加情報がある場合は、GitHubのIssueまたはPull Requestでお知らせください。

---

**Last Updated**: 2026年1月25日
