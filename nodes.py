"""
LyricForge - AI Song Generator Node for ComfyUI
Generates style tags and lyrics from keywords using LLM API
Compatible with HeartMuLa and other music generation models
"""

import requests
import re
import json


class LyricForgeSongGenerator:
    """
    キーワードからHeartMuLa対応のタグと歌詞を生成するノード
    OpenAI API互換のエンドポイントに対応
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "keywords": ("STRING", {
                    "multiline": True,
                    "default": "j-pop 冬の歌 女性ボーカル 雪 カフェ"
                }),
                "api_endpoint": ("STRING", {
                    "default": "http://localhost:1234/v1/chat/completions"
                }),
                "api_key": ("STRING", {
                    "default": "lm-studio"
                }),
                "model": ("STRING", {
                    "default": "local-model"
                }),
            },
            "optional": {
                "language": (["Japanese", "English", "Chinese"], {
                    "default": "Japanese"
                }),
                "song_structure": (["Standard", "Short", "Extended"], {
                    "default": "Standard"
                }),
                "temperature": ("FLOAT", {
                    "default": 0.7,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("style_tags", "lyrics")
    FUNCTION = "generate"
    CATEGORY = "LyricForge"
    
    def generate(self, keywords, api_endpoint, api_key, model, 
                 language="Japanese", song_structure="Standard", temperature=0.7):
        """
        メイン生成関数
        """
        try:
            # エンドポイントの正規化（/v1/chat/completionsが含まれていない場合は追加）
            if not api_endpoint.endswith('/v1/chat/completions') and not api_endpoint.endswith('/chat/completions'):
                api_endpoint = api_endpoint.rstrip('/') + '/v1/chat/completions'
            
            # システムプロンプト構築
            system_prompt = self._build_system_prompt(language, song_structure)
            
            # API呼び出し
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"以下のキーワードから楽曲を生成してください：{keywords}"}
                ],
                "temperature": temperature
            }
            
            print(f"[LyricForge] Calling API: {api_endpoint}")
            print(f"[LyricForge] Keywords: {keywords}")
            
            response = requests.post(api_endpoint, headers=headers, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            
            # レスポンスパース
            content = result['choices'][0]['message']['content']
            print(f"[LyricForge] API Response received")
            
            style_tags, lyrics = self._parse_response(content)
            
            print(f"[LyricForge] Style Tags: {style_tags}")
            print(f"[LyricForge] Lyrics length: {len(lyrics)} characters")
            
            return (style_tags, lyrics)
            
        except Exception as e:
            error_msg = f"Error generating song: {str(e)}"
            print(f"[LyricForge] {error_msg}")
            return (f"Error: {str(e)}", f"Error: {str(e)}")
    
    def _build_system_prompt(self, language, structure):
        """HeartMuLa用のシステムプロンプト構築（v2.0 - 公式仕様準拠）"""
        
        structure_guide = {
            "Standard": "標準的な構成（Intro, Verse, Prechorus, Chorus, Verse, Prechorus, Chorus, Bridge, Chorus, Outro）",
            "Short": "短縮版（Intro, Verse, Chorus, Verse, Chorus, Outro）",
            "Extended": "拡張版（Intro, Verse, Prechorus, Chorus, Verse, Prechorus, Chorus, Bridge, Verse, Chorus, Outro）"
        }
        
        prompt = f"""あなたはHeartMuLa音楽生成モデル用の楽曲プランナーです。

## HeartMuLaタグ体系（公式論文 arXiv:2601.10547 準拠）

### 1. グローバルスタイルタグ（選択確率による優先度順）

HeartMuLaでは各カテゴリーに選択確率が設定されており、影響力の大きい順に：

**ジャンル (Genre) - 確率: 0.95 【最重要】**
- Pop, Rock, Hiphop, K-pop, Jazz, Blues, Electronic, Country, R&B, Metal, Folk, Reggae, Soul, Funk, Classical

**音色 (Timbre) - 確率: 0.50**
- Bright（明るい）, Dark（暗い）, Raspy（かすれた）, Smooth（滑らか）, Powerful（力強い）, Gentle（優しい）
- Rich（豊かな）, Thin（細い）, Warm（温かい）, Cold（冷たい）

**性別 (Gender) - 確率: 0.375**
- Male, Female

**ムード (Mood) - 確率: 0.325**
- Happy, Sad, Romantic, Joyful, Soft, Warm, Melancholic, Energetic, Calm
- Dreamy, Peaceful, Intense, Mysterious, Nostalgic, Hopeful, Tense

**楽器 (Instrument) - 確率: 0.25**
- Piano, Drum, Strings, Acoustic Guitar, Electric Guitar, Synthesizer, Bass, Violin
- Saxophone, Trumpet, Flute, Cello, Harmonica, Organ

**シーン (Scene) - 確率: 0.20**
- Dance, Workout, Wedding, Cafe, Drive, Relax, Party
- Study, Sleep, Meditation, Running, Cooking

**地域 (Region) - 確率: 0.125**
- Asian（アジア）, Western（西洋）, Latin（ラテン）, African（アフリカ）
- European, Middle Eastern, Caribbean

**テーマ (Topic) - 確率: 0.10 【最低優先度】**
- Love, Sweet, Freedom, Dream, Hope, Nostalgia, Nature
- Journey, Friendship, Loss, Victory, Peace

### 使用方式
**重要**: タグは必ずカンマ区切り、**スペースなし**、英語で出力してください。
正しい例: `Pop,Female,Romantic,Soft,Warm,Piano,Acoustic Guitar,Cafe`
誤った例: `Pop, Female, Romantic` （スペースあり - NG）

選択確率の高いカテゴリー（Genre, Timbre）を優先的に含めてください。

### 2. 構造タグ

楽曲の段落構造を示すタグ:
- **[Intro]** - イントロ/前奏
- **[Verse]** - Aメロ/主歌
- **[Prechorus]** - サビ前/導歌（Chorusへの橋渡し）
- **[Chorus]** - サビ/副歌（曲の最も印象的な部分）
- **[Bridge]** - ブリッジ（曲の転換部分）
- **[Outro]** - アウトロ/終奏

使用例: `[Chorus]` の後に歌詞を記述

## 出力フォーマット

**必ず以下の形式で正確に出力してください:**

STYLE_TAGS:
[カンマ区切り、スペースなしのグローバルスタイルタグリスト]

LYRICS:
[構造タグを含む完全な歌詞]

## 要件
1. STYLE_TAGSは必ず英語で、カンマ区切り、**スペースなし**で出力
2. 歌詞は{language}で出力
3. 楽曲構成：{structure_guide[structure]}
4. 構造タグ（[Intro], [Verse]等）のみ使用し、細粒度タグは付加しない
5. 歌詞は自然で音楽的な流れを重視
6. キーワードのテーマを歌詞に自然に組み込む
7. 選択確率の高いカテゴリー（Genre 0.95, Timbre 0.5）を優先的に含める

## 注意事項
- コードブロック（```）は使用しない
- 余計な説明文は含めない
- STYLE_TAGSとLYRICSのセクションのみ出力
- タグ内のスペースは絶対に入れない（例: "Acoustic Guitar"ではなく"Acoustic Guitar"は例外として許可）"""
        
        return prompt
    
    def _parse_response(self, content):
        """
        LLMレスポンスをタグと歌詞に分割
        """
        # コードブロック除去
        content = re.sub(r'```[a-zA-Z]*\n', '', content)
        content = content.replace('```', '')
        
        # STYLE_TAGSセクション抽出
        tags_match = re.search(r'STYLE_TAGS:\s*\n(.+?)(?=\n\nLYRICS:|\nLYRICS:|\Z)', content, re.DOTALL | re.IGNORECASE)
        if tags_match:
            style_tags = tags_match.group(1).strip()
            # 改行を削除してカンマ区切りに統一
            style_tags = ' '.join(style_tags.split())
        else:
            style_tags = "Pop,Female,Soft"  # デフォルト値
            print("[LyricForge] Warning: Could not parse STYLE_TAGS, using default")
        
        # LYRICSセクション抽出
        lyrics_match = re.search(r'LYRICS:\s*\n(.+)', content, re.DOTALL | re.IGNORECASE)
        if lyrics_match:
            lyrics = lyrics_match.group(1).strip()
        else:
            # STYLE_TAGSセクション以降を全て歌詞として扱う
            after_tags = re.split(r'STYLE_TAGS:.+?\n\n', content, flags=re.DOTALL | re.IGNORECASE)
            if len(after_tags) > 1:
                lyrics = after_tags[1].strip()
            else:
                lyrics = content.strip()
                print("[LyricForge] Warning: Could not parse LYRICS section clearly")
        
        # 余計な空行を整理
        lyrics = re.sub(r'\n{3,}', '\n\n', lyrics)

        # 細粒度スタイルタグを除去（構造タグの後の [xxx, yyy, zzz] 形式）
        lyrics = re.sub(r'(\[(?:Intro|Verse|Prechorus|Chorus|Bridge|Outro)\])\s*\[[^\]]+\]', r'\1', lyrics, flags=re.IGNORECASE)

        return style_tags, lyrics


# ノード登録
NODE_CLASS_MAPPINGS = {
    "LyricForgeSongGenerator": LyricForgeSongGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LyricForgeSongGenerator": "LyricForge Song Generator"
}
