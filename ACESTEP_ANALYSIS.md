# ACE-Step 1.5 仕様解析

ACE-Step 1.5音楽生成モデルの入力仕様を解析し、LyricForgeノードとの互換性を検証したドキュメント。

**参照元**: https://github.com/ace-step/ACE-Step-1.5

## モデル概要

| 項目 | 内容 |
|------|------|
| **モデル名** | ACE-Step 1.5 |
| **タイプ** | オープンソース音楽生成基盤モデル |
| **生成速度** | A100: 2秒以下、RTX 3090: 10秒以下 |
| **VRAM要件** | 4GB未満で動作可能 |
| **生成長さ** | 10秒〜600秒（10分） |
| **言語サポート** | 50以上の言語 |
| **楽器/スタイル** | 1000以上 |

## HeartMuLaとの比較

| 項目 | HeartMuLa | ACE-Step 1.5 |
|------|-----------|--------------|
| **スタイル指定** | カンマ区切りタグ | 自然言語キャプション |
| **BPM** | なし | 30-300 または Auto |
| **Key/Scale** | なし | 指定可能 |
| **Time Signature** | なし | 指定可能 |
| **構造タグ** | 基本6種 | 拡張セット |
| **参照オーディオ** | なし | 対応 |

## 入力形式

### 1. キャプション（Caption）

自然言語でスタイルを記述する形式。HeartMuLaのカンマ区切りタグとは異なる。

#### キャプション要素

| カテゴリ | 例 |
|---------|-----|
| **ジャンル** | pop, rock, jazz, electronic, hip-hop, R&B, folk, country, metal, classical, EDM, K-pop, J-pop |
| **雰囲気/ムード** | melancholic, uplifting, energetic, dreamy, romantic, sad, happy, peaceful, intense, nostalgic |
| **楽器** | acoustic guitar, piano, synth pads, 808 drums, strings, electric guitar, bass, violin, saxophone |
| **音質/テクスチャ** | warm, bright, crisp, airy, punchy, soft, rich, ethereal, gritty |
| **時代参照** | 80s synthwave, 90s grunge, modern trap, classic rock, retro disco |
| **ボーカル特性** | female vocal, male vocal, breathy, powerful, falsetto, soft, raspy, gentle |

#### キャプション例

```
upbeat pop rock with electric guitars, driving drums, and catchy synth hooks
```

```
soft piano ballad with female breathy vocal, warm melancholic atmosphere
```

```
energetic K-pop dance track with punchy synths and powerful female vocals
```

```
melancholic indie folk with acoustic guitar and gentle male vocals
```

### 2. BPM

| テンポ感 | BPM範囲 | 適用ジャンル例 |
|---------|---------|---------------|
| バラード・スロー | 60-80 | バラード、スローR&B |
| ミディアム | 80-110 | ポップ、ロック |
| アップテンポ | 110-140 | ダンスポップ、ファンク |
| ファスト・ダンス | 140-180 | EDM、ドラムンベース |

- 数値指定: 30-300の範囲
- 自動検出: "Auto"

### 3. Key/Scale

#### 形式

```
[音名][#/b (optional)] [Major/Minor]
```

#### 例

- `C Major` - ハ長調
- `A Minor` - イ短調
- `F# Minor` - 嬰ヘ短調
- `Bb Major` - 変ロ長調

#### Key/Scale選択ガイドライン

| 曲調 | 推奨Key/Scale |
|------|--------------|
| 明るい・ポジティブ | C Major, G Major, D Major |
| 暗い・悲しい | A Minor, D Minor, E Minor |
| EDM・ダンス | F Minor, A Minor, G Minor |
| ポップ | C Major, G Major, F Major |

### 4. Time Signature（拍子）

- `4/4` - 4分の4拍子（最も一般的）
- `3/4` - 4分の3拍子（ワルツ）
- `6/8` - 8分の6拍子

## 構造タグ

### 基本セクション

| タグ | 説明 | HeartMuLa対応 |
|-----|------|--------------|
| `[Intro]` | イントロ/前奏 | ○ |
| `[Verse 1]`, `[Verse 2]` | Aメロ（番号付き） | △（番号なし） |
| `[Pre-Chorus]` | サビ前/導歌 | ○ (Prechorus) |
| `[Chorus]` | サビ/副歌 | ○ |
| `[Bridge]` | ブリッジ | ○ |
| `[Outro]` | アウトロ/終奏 | ○ |

### ACE-Step独自セクション

| タグ | 説明 |
|-----|------|
| `[Build]` | エネルギー上昇部分 |
| `[Drop]` | エネルギー解放部分（EDM等） |
| `[Breakdown]` | 楽器削減部分 |
| `[Instrumental]` | 純粋な楽器パート |
| `[Guitar Solo]` | ギターソロ |
| `[Piano Interlude]` | ピアノ間奏 |

### 構造例

#### Standard構成

```
[Intro]

[Verse 1]
歌詞...

[Pre-Chorus]
歌詞...

[Chorus]
歌詞...

[Verse 2]
歌詞...

[Pre-Chorus]
歌詞...

[Chorus]
歌詞...

[Bridge]
歌詞...

[Chorus]
歌詞...

[Outro]
```

#### EDM構成例

```
[Intro]

[Build]

[Drop]

[Breakdown]

[Verse 1]
歌詞...

[Build]

[Drop]

[Outro]
```

## LyricForgeノード出力形式

`LyricForge ACE-Step Generator`ノードは以下の4出力を生成：

| 出力名 | 形式 | 例 |
|--------|------|-----|
| caption | 自然言語 | "soft piano ballad with female breathy vocal" |
| lyrics | 構造タグ付き | "[Verse 1]\n歌詞..." |
| bpm | 数値文字列 | "80" |
| key_scale | Key/Scale | "A Minor" |

## API/インターフェース

ACE-Step 1.5は以下のインターフェースを提供：

| インターフェース | エンドポイント/説明 |
|-----------------|-------------------|
| Gradio Web UI | ブラウザベースUI |
| REST API | `localhost:8001` |
| Python API | 推論用Pythonライブラリ |

※ ComfyUI公式連携は現時点でなし

## 参考リンク

- [ACE-Step 1.5 GitHub](https://github.com/ace-step/ACE-Step-1.5)
- [Gradio Guide](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GRADIO_GUIDE.md)
- [Tutorial](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/Tutorial.md)
- [Inference API](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INFERENCE.md)
