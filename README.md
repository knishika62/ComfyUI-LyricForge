# ComfyUI-LyricForge

AI音楽生成モデル（HeartMuLa等）用のスタイルタグと歌詞を、キーワードから自動生成するComfyUI Custom Nodeです。

**[HeartMuLa_ComfyUI](https://github.com/benjiyaya/HeartMuLa_ComfyUI)** と組み合わせて使用することを前提としています。

**v2.1.0**: 歌詞出力を簡略化し、構造タグ（`[Chorus]`等）のみを出力するように変更しました。

## 機能

- **キーワード入力**: 自然言語のキーワードを入力
- **自動タグ生成**: HeartMuLa等に対応したスタイルタグを自動生成（選択確率準拠）
- **歌詞生成**: 構造タグを含む完全な歌詞を生成
- **LLM API対応**: OpenAI API互換のエンドポイント対応（OpenAI, Claude, ローカルLLM等）
- **多言語対応**: 日本語、英語、中国語、韓国語、スペイン語の歌詞生成

## インストール

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-LyricForge.git
cd ComfyUI-LyricForge
pip install -r requirements.txt
```

ComfyUIを再起動してください。

## 使用方法

### 1. ノードの配置

ComfyUIのノードメニューから`LyricForge > LyricForge Song Generator`を選択して配置します。

### 2. 入力パラメータの設定

#### 必須パラメータ

- **keywords**: 楽曲のキーワード（例: "j-pop 冬の歌 女性ボーカル 雪 カフェ"）
- **api_endpoint**: LLM APIのエンドポイントURL
  - OpenAI: `https://api.openai.com/v1/chat/completions`
  - Claude: `https://api.anthropic.com/v1/messages`
  - ローカルLLM (Ollama): `http://localhost:11434/v1/chat/completions`
- **api_key**: APIキー
- **model**: 使用するモデル名（例: `gpt-4`, `claude-3-5-sonnet-20241022`, `llama3.1`）

#### オプションパラメータ

- **language**: 歌詞の言語（Japanese / English / Chinese）
- **song_structure**: 楽曲構成
  - Standard: 標準的な構成
  - Short: 短縮版
  - Extended: 拡張版
- **temperature**: 生成の創造性（0.0-2.0、デフォルト: 0.7）

### 3. 出力

ノードは2つの出力を提供します：

- **style_tags**: 音楽生成モデル用のグローバルスタイルタグ（カンマ区切り）
  - 例: `Pop,Female,Soft,Warm,Piano,Acoustic Guitar,Cafe,Romantic`
- **lyrics**: 構造タグを含む完全な歌詞

### 4. ワークフロー例

```
LyricForge Song Generator
    ↓ style_tags
Music Generator Node (style_tags入力)
    ↓ lyrics
Music Generator Node (lyrics入力)
    ↓
Preview Node / Save Audio
```

## 対応タグ体系について（HeartMuLa公式仕様準拠 v2.0）

### グローバルスタイルタグ（選択確率順）

HeartMuLa公式論文（arXiv:2601.10547）に基づく8つのカテゴリー。
各カテゴリーには選択確率が設定されており、影響力の大きい順に：

1. **ジャンル (Genre)** - **確率: 0.95** 【最重要】
   - Pop, Rock, Hiphop, K-pop, Jazz, Blues, Electronic, Country, R&B, Metal, Folk
   
2. **音色 (Timbre)** - **確率: 0.50**
   - Bright (明るい), Dark (暗い), Raspy (かすれた), Smooth (滑らか), Powerful (力強い), Gentle (優しい)
   
3. **性別 (Gender)** - **確率: 0.375**
   - Male, Female
   
4. **ムード (Mood)** - **確率: 0.325**
   - Happy, Sad, Romantic, Joyful, Soft, Warm, Melancholic, Energetic, Calm, Dreamy
   
5. **楽器 (Instrument)** - **確率: 0.25**
   - Piano, Drum, Strings, Acoustic Guitar, Electric Guitar, Synthesizer, Bass, Violin
   
6. **シーン (Scene)** - **確率: 0.20**
   - Dance, Workout, Wedding, Cafe, Drive, Relax, Party, Study
   
7. **地域 (Region)** - **確率: 0.125**
   - Asian (アジア), Western (西洋), Latin (ラテン), African (アフリカ)
   
8. **テーマ (Topic)** - **確率: 0.10** 【最低優先度】
   - Love, Sweet, Freedom, Dream, Hope, Nostalgia, Nature

**重要**: タグはカンマ区切り、**スペースなし**で出力されます。  
例: `Pop,Female,Romantic,Soft,Warm,Piano,Acoustic Guitar,Cafe`

### 構造タグ

- `[Intro]` - イントロ
- `[Verse]` - Aメロ
- `[Prechorus]` - サビ前
- `[Chorus]` - サビ
- `[Bridge]` - ブリッジ
- `[Outro]` - アウトロ

## API設定例

### LM Studio（推奨・デフォルト設定）

LM Studioを起動し、"Local Server"タブでサーバーを開始してください。

```
api_endpoint: http://192.168.11.20:1234
api_key: lm-studio (任意の文字列でOK)
model: (選択したモデル名、または "local-model")
```

**注意**: エンドポイントには `/v1/chat/completions` を含めなくても自動的に追加されます。  
以下のいずれの形式でも動作します：
- `http://192.168.11.20:1234`
- `http://192.168.11.20:1234/v1/chat/completions`

### OpenAI

```
api_endpoint: https://api.openai.com/v1/chat/completions
api_key: sk-...
model: gpt-4
```

### Claude (Anthropic)

Claude APIは現在標準的なOpenAI互換フォーマットではないため、プロキシまたはラッパーの使用を推奨します。

### ローカルLLM (Ollama)

```bash
# Ollamaのインストールと起動
ollama serve

# モデルのダウンロード
ollama pull llama3.1
```

```
api_endpoint: http://localhost:11434
api_key: dummy
model: llama3.1
```

**注意**: Ollamaの場合もエンドポイントは自動的に `/v1/chat/completions` が追加されます。

## 使用例

### 例1: 冬のカフェソング

**入力キーワード:**
```
j-pop 冬の歌 女性ボーカル 雪 カフェ
```

**生成されるタグ例:**
```
Pop,Female,Soft,Warm,Piano,Acoustic Guitar,Cafe,Romantic
```

**生成される歌詞例:**
```
[Intro]

[Verse]
窓の外 舞い落ちる雪
カフェの香り 優しく包む
...
```

### 例2: 元気なダンスポップ

**入力キーワード:**
```
k-pop ダンス 女性グループ エネルギッシュ シンセサイザー
```

**生成されるタグ例:**
```
K-pop,Female,Energetic,Dance,Synthesizer,Electronic,Party
```

## トラブルシューティング

### API接続エラー

- APIキーが正しいか確認
- エンドポイントURLが正確か確認
- ネットワーク接続を確認
- APIの利用制限を確認

### 生成結果が期待と異なる

- キーワードをより具体的に記述
- temperatureパラメータを調整（低い値で安定、高い値で創造的）
- 使用するLLMモデルを変更（GPT-4の方が高精度）

### ノードが表示されない

- ComfyUIを完全に再起動
- `requirements.txt`の依存関係を再インストール
- ComfyUIのコンソールでエラーログを確認

## ライセンス

MIT License

## 貢献

プルリクエストやイシューの報告を歓迎します。

## 関連リンク

- [HeartMuLa_ComfyUI](https://github.com/benjiyaya/HeartMuLa_ComfyUI) - 連携先カスタムノード（必須）
- [HeartMuLa GitHub](https://github.com/HeartMuLa/heartlib) - 対応音楽生成モデル
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 更新履歴

### v2.1.0 (2025-01-24)
- 🎯 歌詞出力から細粒度スタイルタグを削除（構造タグのみに簡略化）
- 📝 `[Chorus]` のような構造タグのみを出力するように変更

### v2.0.0 (2025-01-22)
- 🎉 HeartMuLa公式論文（arXiv:2601.10547）の仕様に完全準拠
- ✨ 選択確率による優先度を明示化（Genre 0.95が最重要）
- 📝 Timbre（音色）カテゴリーに具体例を追加（Bright, Dark, Raspy等）
- 🌍 Region（地域）カテゴリーに具体例を追加（Asian, Western等）
- 📚 システムプロンプトを大幅強化（より正確なタグ生成）
- 📖 公式論文との対照分析ドキュメント（HEARTMULA_ANALYSIS.md）を追加

### v1.0.0 (2025-01-22)
- 初回リリース
- キーワードからのタグ・歌詞自動生成機能
- OpenAI API互換エンドポイント対応
- 多言語対応（日本語、英語、中国語）
- HeartMuLaタグ体系に対応
