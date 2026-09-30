# kokone — ローカル文字PV（MV）作成ツール

歌詞を入れるだけで文字PV（リリックモーション）を自動で組み立て、MP4 に書き出せるツールです。
[JIZURA 字面](https://github.com/7MPra/JIZURA)（MIT ライセンス）のブラウザ版をベースに、ローカルで手軽に使って改造していくためのリポジトリです。

## 使い方

必要なもの：Python 3（追加のインストールは不要）、Chrome か Edge（MP4 書き出しに WebCodecs を使うため）

| OS | 起動方法 |
|---|---|
| Windows | `start.bat` をダブルクリック |
| macOS | `start.command` をダブルクリック（初回は右クリック →「開く」） |
| Linux / ターミナル | `./start.sh` または `python3 start.py` |

起動するとビルドが走り、ブラウザで `http://127.0.0.1:8000/` が開きます。終了はターミナルで `Ctrl+C`。

1. 左の欄に歌詞を入れる（1行 = 1フレーズ）
2. 曲（音声ファイル）を読み込むと拍を検出してカットを合わせる
3. 「おまかせで作る」（キー `R`）で演出を丸ごと入れ替え。気に入るまで押す
4. 書き出し → MP4

オプション：`python3 start.py --port 8080`（ポート変更）／`--no-open`（ブラウザを開かない）／`--no-build`（前回のビルドをそのまま使う）

## 改造するとき

| 場所 | 中身 |
|---|---|
| `src/` | エンジン本体（番号順に連結される）。`12_ui.js` が画面の動き、`11p_*.js` が演出部品のパック |
| `app/body.html` `app/style.css` | 画面の HTML と CSS |
| `docs/EXPRESSION_PACKS.md` | 演出部品を追加するためのガイド |
| `build.py` | `src/` `app/` `vendor/` を 1 ファイルの HTML にまとめる。`--local` で日本語版だけを `dist/index.html` に出力 |

ソースを編集したら `start.py` を起動し直せば反映されます（ビルドは毎回自動）。

## 取り込み元

- JIZURA: https://github.com/7MPra/JIZURA （commit `3fa77b2`、2026-09-29 時点）
- 取り込んだもの：ブラウザ版のソース（`src/` `app/` `vendor/` `docs/` `dev/` `tools/` `build.py`）。After Effects パネル（`ae/` `cep/`）とビルド済みファイルは含めていません
- 元の README は [README.upstream.md](README.upstream.md)、ライセンスは [LICENSE](LICENSE) と [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
