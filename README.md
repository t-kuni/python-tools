# 画像・動画関連のスクリプト集

## 初期設定

```

```

## 動画の指定区間(秒)を切り抜き

```
python trim_video.py input.mp4 10 20 output.mp4
```

## 最初のフレームを画像として切り出し

```
python extract_first_frame.py input.mp4 output.png
```

## 動画のフレーム数削減

1/[第２引数の数値] 倍のフレーム数になるように間引く

```
python reduce_frames.py input_video.mp4 4
```

## 動画の高さ、幅調整

```
python clip_video.py input.mp4 50 100
```